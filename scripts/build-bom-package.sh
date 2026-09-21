#!/bin/bash
# build-bom-package.sh
# Builds the MII KDS Complete BOM package by downloading all module packages
# from the FHIR registry and assembling their resources into a single package.
#
# No SUSHI or Firely Bake required - this is a pure assembly step.
#
# Usage: ./scripts/build-bom-package.sh [--skip-download] [--output-dir DIR]

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# --- Configuration ---
REGISTRY="https://packages.simplifier.net"
FHIR_CACHE="${HOME}/.fhir/packages"
BUILD_DIR="${PROJECT_DIR}/.bake"
PACKAGE_DIR="${BUILD_DIR}/package"
SKIP_DOWNLOAD=false
OUTPUT_DIR=""

# --- Parse arguments ---
while [[ $# -gt 0 ]]; do
  case "$1" in
    --skip-download) SKIP_DOWNLOAD=true; shift ;;
    --output-dir) OUTPUT_DIR="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

# --- Read package metadata ---
PACKAGE_NAME=$(node -p "require('${PROJECT_DIR}/package.json').name")
VERSION=$(node -p "require('${PROJECT_DIR}/package.json').version")
TARBALL_NAME="${PACKAGE_NAME}-${VERSION}.tgz"

if [[ -n "$OUTPUT_DIR" ]]; then
  TARBALL_PATH="${OUTPUT_DIR}/${TARBALL_NAME}"
else
  TARBALL_PATH="${PROJECT_DIR}/${TARBALL_NAME}"
fi

echo "╭──────────────────────────────────────────────────╮"
echo "│  MII KDS Complete - BOM Package Builder          │"
echo "╰──────────────────────────────────────────────────╯"
echo ""
echo "  Package:  ${PACKAGE_NAME}"
echo "  Version:  ${VERSION}"
echo ""

# --- Extract MII KDS dependencies (skip hl7.fhir.r4.core and de.basisprofil.r4) ---
DEPS=$(node -p "
  const deps = require('${PROJECT_DIR}/package.json').dependencies;
  Object.entries(deps)
    .filter(([k]) => k.startsWith('de.medizininformatikinitiative.kerndatensatz.'))
    .map(([k,v]) => k + '@' + v)
    .join('\n')
")

echo "  Modules:  $(echo "$DEPS" | wc -l | tr -d ' ')"
echo ""

# --- Phase 1: Download packages ---
if [[ "$SKIP_DOWNLOAD" == "false" ]]; then
  echo "▸ Phase 1: Downloading packages..."
  TMPDIR=$(mktemp -d)
  trap "rm -rf $TMPDIR" EXIT

  while IFS= read -r dep; do
    NAME="${dep%@*}"
    VER="${dep#*@}"
    SHORT="${NAME##*.}"
    CACHE_DIR="${FHIR_CACHE}/${NAME}#${VER}"

    if [[ -d "$CACHE_DIR" ]]; then
      echo "  ✓ ${SHORT}@${VER} (cached)"
      continue
    fi

    echo -n "  ↓ ${SHORT}@${VER} ... "
    HTTP_CODE=$(curl -sL -o "$TMPDIR/pkg.tgz" -w "%{http_code}" "${REGISTRY}/${NAME}/${VER}")

    if [[ "$HTTP_CODE" -ne 200 ]]; then
      echo "FAILED (HTTP ${HTTP_CODE})"
      echo "    Could not download from ${REGISTRY}/${NAME}/${VER}"
      exit 1
    fi

    mkdir -p "$CACHE_DIR"
    tar -xzf "$TMPDIR/pkg.tgz" -C "$CACHE_DIR"
    rm -f "$TMPDIR/pkg.tgz"
    echo "OK"
  done <<< "$DEPS"
  echo ""
else
  echo "▸ Phase 1: Skipped (--skip-download)"
  echo ""
fi

# --- Phase 2: Assemble package ---
echo "▸ Phase 2: Assembling resources..."
rm -rf "$PACKAGE_DIR"
mkdir -p "$PACKAGE_DIR/examples"

TOTAL_RESOURCES=0
TOTAL_EXAMPLES=0
COLLISIONS=0

while IFS= read -r dep; do
  NAME="${dep%@*}"
  VER="${dep#*@}"
  SHORT="${NAME##*.}"
  CACHE_DIR="${FHIR_CACHE}/${NAME}#${VER}"

  if [[ ! -d "$CACHE_DIR/package" ]]; then
    echo "  ✗ ${SHORT}@${VER} - not in cache!"
    exit 1
  fi

  PKG_RESOURCES=0
  PKG_EXAMPLES=0

  # Copy conformance resources (StructureDefinition, ValueSet, CodeSystem, etc.)
  for f in "$CACHE_DIR/package/"*.json; do
    [[ -f "$f" ]] || continue
    BASENAME=$(basename "$f")

    # Skip package metadata files
    [[ "$BASENAME" == "package.json" ]] && continue
    [[ "$BASENAME" == ".index.json" ]] && continue

    # Skip macOS AppleDouble resource forks (._package.json etc.), die in
    # einigen publizierten Modul-Tarballs stecken und zwischen Modulen
    # kollidieren -- siehe mii-kds-complete Issue zu Dokument/Seltene
    [[ "$BASENAME" == ._* ]] && continue

    # Kollisionen sichtbar machen, statt still zu ueberschreiben
    if [[ -e "$PACKAGE_DIR/${BASENAME}" ]]; then
      echo "    ! Kollision: ${BASENAME} wird von ${SHORT} ueberschrieben"
      COLLISIONS=$((COLLISIONS + 1))
    fi

    cp "$f" "$PACKAGE_DIR/${BASENAME}"
    PKG_RESOURCES=$((PKG_RESOURCES + 1))
  done

  # Copy examples if present
  if [[ -d "$CACHE_DIR/package/examples" ]]; then
    for f in "$CACHE_DIR/package/examples/"*.json; do
      [[ -f "$f" ]] || continue
      cp "$f" "$PACKAGE_DIR/examples/"
      PKG_EXAMPLES=$((PKG_EXAMPLES + 1))
    done
  fi

  TOTAL_RESOURCES=$((TOTAL_RESOURCES + PKG_RESOURCES))
  TOTAL_EXAMPLES=$((TOTAL_EXAMPLES + PKG_EXAMPLES))
  echo "  ✓ ${SHORT}@${VER}: ${PKG_RESOURCES} resources, ${PKG_EXAMPLES} examples"

done <<< "$DEPS"

echo ""
echo "  Total: ${TOTAL_RESOURCES} resources, ${TOTAL_EXAMPLES} examples, ${COLLISIONS} Kollisionen"
echo ""

# --- Phase 3: Write package.json ---
echo "▸ Phase 3: Writing package metadata..."
cp "$PROJECT_DIR/package.json" "$PACKAGE_DIR/package.json"

# --- Phase 4: Generate .index.json ---
echo "▸ Phase 4: Generating .index.json..."

node -e "
const fs = require('fs');
const path = require('path');

const pkgDir = '${PACKAGE_DIR}';
const files = [];

// Scan root for resources
for (const f of fs.readdirSync(pkgDir)) {
  if (!f.endsWith('.json') || f === 'package.json' || f === '.index.json') continue;
  try {
    const res = JSON.parse(fs.readFileSync(path.join(pkgDir, f), 'utf8'));
    if (res.resourceType) {
      const entry = { filename: f, resourceType: res.resourceType };
      if (res.id) entry.id = res.id;
      if (res.url) entry.url = res.url;
      if (res.version) entry.version = res.version;
      if (res.kind) entry.kind = res.kind;
      if (res.type) entry.type = res.type;
      files.push(entry);
    }
  } catch(e) {}
}

// Scan examples
const exDir = path.join(pkgDir, 'examples');
if (fs.existsSync(exDir)) {
  for (const f of fs.readdirSync(exDir)) {
    if (!f.endsWith('.json')) continue;
    try {
      const res = JSON.parse(fs.readFileSync(path.join(exDir, f), 'utf8'));
      if (res.resourceType) {
        const entry = { filename: 'examples/' + f, resourceType: res.resourceType };
        if (res.id) entry.id = res.id;
        files.push(entry);
      }
    } catch(e) {}
  }
}

const index = { 'index-version': 2, files };
fs.writeFileSync(path.join(pkgDir, '.index.json'), JSON.stringify(index, null, 2));
console.log('  ✓ Indexed ' + files.length + ' entries');
"

echo ""

# --- Phase 5: Create tarball ---
echo "▸ Phase 5: Creating tarball..."
cd "$BUILD_DIR"
COPYFILE_DISABLE=1 tar -czf "$TARBALL_PATH" package/
cd "$PROJECT_DIR"

TARBALL_SIZE=$(ls -lh "$TARBALL_PATH" | awk '{print $5}')
FILE_COUNT=$(tar -tzf "$TARBALL_PATH" | wc -l | tr -d ' ')

echo "  ✓ ${TARBALL_NAME} (${TARBALL_SIZE}, ${FILE_COUNT} files)"
echo ""

# --- Summary ---
echo "╭──────────────────────────────────────────────────╮"
echo "│  Build Complete                                  │"
echo "╰──────────────────────────────────────────────────╯"
echo ""
echo "  Package:    ${PACKAGE_NAME}"
echo "  Version:    ${VERSION}"
echo "  Tarball:    ${TARBALL_PATH}"
echo "  Size:       ${TARBALL_SIZE}"
echo "  Files:      ${FILE_COUNT}"
echo "  Resources:  ${TOTAL_RESOURCES}"
echo "  Examples:   ${TOTAL_EXAMPLES}"
echo ""
echo "  Install locally:"
echo "    fhir install ${TARBALL_PATH}"
echo ""
echo "  Inspect:"
echo "    tar -tzf ${TARBALL_PATH} | head -30"
