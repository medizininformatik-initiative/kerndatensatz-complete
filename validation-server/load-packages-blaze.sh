#!/bin/bash
# Load all MII KDS packages into Blaze FHIR server (Ballot-Stand 2027.0.0)
# Usage: ./load-packages-blaze.sh [BLAZE_URL]

BLAZE_URL="${1:-http://localhost:8082/fhir}"

echo "Loading MII KDS packages into Blaze at $BLAZE_URL"

PACKAGES=(
  "de.medizininformatikinitiative.kerndatensatz.base/2027.0.0-ballot.rc1"
  "de.medizininformatikinitiative.kerndatensatz.meta/2027.0.0-ballot.rc3"
  "de.medizininformatikinitiative.kerndatensatz.medikation/2026.0.1"
  "de.medizininformatikinitiative.kerndatensatz.laborbefund/2026.0.3"
  "de.medizininformatikinitiative.kerndatensatz.biobank/2027.0.0-ballot.rc1"
  "de.medizininformatikinitiative.kerndatensatz.icu/2027.0.0"
  "de.medizininformatikinitiative.kerndatensatz.mikrobiologie/2027.0.0-alpha.5"
  "de.medizininformatikinitiative.kerndatensatz.molgen/2026.0.4"
  "de.medizininformatikinitiative.kerndatensatz.patho/2026.0.2"
  "de.medizininformatikinitiative.kerndatensatz.studie/2027.0.0-ballot.rc1"
  "de.medizininformatikinitiative.kerndatensatz.bildgebung/2027.0.0-ballot.rc2"
  "de.medizininformatikinitiative.kerndatensatz.dokument/2027.0.0-ballot.rc1"
  "de.medizininformatikinitiative.kerndatensatz.onkologie/2026.0.3"
  "de.medizininformatikinitiative.kerndatensatz.seltene/2026.0.1"
  "de.medizininformatikinitiative.kerndatensatz.mtb/2026.0.1"
  "de.medizininformatikinitiative.kerndatensatz.pros/2026.7.0"
  "de.medizininformatikinitiative.kerndatensatz.consent/2026.0.1-rc-4"
  "de.basisprofil.r4/1.6.0"
  "de.einwilligungsmanagement/2.0.3"
)

# Reihenfolge entspricht der BOM (package.json / sushi-config.yaml).
# Ballot-Stand 2027.0.0: base und meta liegen auf der Ballot-Linie, die uebrigen
# Module deklarieren teilweise noch die 2026er Versionen -- siehe mii-kds-complete-d3d.

TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

for pkg in "${PACKAGES[@]}"; do
  NAME="${pkg%/*}"
  VERSION="${pkg#*/}"
  SHORT="${NAME##*.}"

  echo -n "  $SHORT $VERSION ... "

  # Download and extract package
  curl -sL "https://packages.fhir.org/${NAME}/${VERSION}" -o "$TMPDIR/pkg.tgz"
  mkdir -p "$TMPDIR/pkg"
  tar -xzf "$TMPDIR/pkg.tgz" -C "$TMPDIR/pkg"

  # Upload conformance resources (StructureDefinition, ValueSet, CodeSystem, etc.)
  COUNT=0
  for f in "$TMPDIR/pkg/package/"*.json; do
    [ -f "$f" ] || continue
    RESOURCE_TYPE=$(jq -r '.resourceType // empty' "$f" 2>/dev/null)
    case "$RESOURCE_TYPE" in
      StructureDefinition|ValueSet|CodeSystem|NamingSystem|ConceptMap|SearchParameter|OperationDefinition|CapabilityStatement)
        HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" -X PUT \
          -H "Content-Type: application/fhir+json" \
          -d @"$f" \
          "$BLAZE_URL/${RESOURCE_TYPE}/$(jq -r '.id' "$f")")
        if [ "$HTTP_CODE" -ge 200 ] && [ "$HTTP_CODE" -lt 300 ]; then
          COUNT=$((COUNT + 1))
        fi
        ;;
    esac
  done

  echo "$COUNT resources"
  rm -rf "$TMPDIR/pkg"
done

echo ""
echo "Done. Loaded all MII KDS conformance resources into Blaze."
