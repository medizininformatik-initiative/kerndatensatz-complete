#!/usr/bin/env bash
# release-gate.sh
# Vorbedingungen fuer ein BOM-Release. Buendelt die Checks, die sonst einzeln
# laufen, und bricht bei harten Fehlern ab.
#
#   ./scripts/release-gate.sh          # alles ausser der HAPI-Validierung
#   ./scripts/release-gate.sh --full   # zusaetzlich Validation-Server bauen und pruefen
#   ./scripts/release-gate.sh --quick  # nur Konsistenz, ohne Netz
#
# Exit 0 = release-faehig, 1 = harter Fehler, 2 = nur Hinweise.

set -uo pipefail
cd "$(dirname "$0")/.."

MODE="${1:-normal}"
FAIL=0
WARN=0
QA_SKILL="$HOME/.claude/skills/mii-qa-reports/scripts/fetch_qa.py"

step()  { printf "\n\033[1m▸ %s\033[0m\n" "$1"; }
ok()    { printf "  ✓ %s\n" "$1"; }
warn()  { printf "  ! %s\n" "$1"; WARN=$((WARN+1)); }
fail()  { printf "  ✗ %s\n" "$1"; FAIL=$((FAIL+1)); }

VERSION=$(node -p "require('./package.json').version")
printf "\033[1mBOM Release-Gate — Version %s\033[0m\n" "$VERSION"

# ── 1. Konsistenz über alle Quellen ───────────────────────────────────────────
step "Konsistenz der Versionsangaben (6 Quellen)"
if ./scripts/check-module-versions.py --offline > /tmp/gate-consistency.txt 2>&1; then
  ok "package.json, sushi-config, HAPI, Blaze, Dockerfile und index.md stimmen überein"
else
  fail "Quellen weichen voneinander ab:"
  grep -E "^FEHLER" /tmp/gate-consistency.txt | sed 's/^/      /'
fi

[[ "$MODE" == "--quick" ]] && { printf "\n%d Fehler, %d Hinweise (quick)\n" "$FAIL" "$WARN"; exit $((FAIL>0?1:0)); }

# ── 2. Registry: existieren alle Pins, gibt es Neueres? ───────────────────────
step "Abgleich gegen die Registry"
if ./scripts/check-module-versions.py > /tmp/gate-registry.txt 2>&1; then
  ok "alle gepinnten Versionen sind auflösbar"
else
  if grep -q "gepinnte Version existiert nicht\|nicht aufloesbar" /tmp/gate-registry.txt; then
    fail "gepinnte Version nicht auflösbar:"
    grep -E "existiert nicht|nicht aufloesbar" /tmp/gate-registry.txt | sed 's/^/      /'
  else
    warn "Abgleich meldete Abweichungen — siehe /tmp/gate-registry.txt"
  fi
fi
NEWER=$(grep -c "^hinweis" /tmp/gate-registry.txt || true)
[[ "$NEWER" -gt 0 ]] && warn "$NEWER Paket(e) haben eine neuere Version als gepinnt"

# ── 3. QA-Reports der Module ──────────────────────────────────────────────────
step "QA-Reports der Module"
if [[ -x "$QA_SKILL" ]]; then
  "$QA_SKILL" --pin-file package.json --no-branch-check > /tmp/gate-qa.txt 2>&1 || true
  ERRSUM=$(awk '$0 ~ /^[a-z-]+ / {for(i=1;i<=NF;i++) if($i ~ /^[0-9]+$/) {print $i; break}}' /tmp/gate-qa.txt \
           | awk '{s+=$1} END {print s+0}')
  ok "Reports abgerufen (Summe gemeldeter Errors: ${ERRSUM:-?})"
  if grep -q "Report beschreibt eine andere Version" /tmp/gate-qa.txt; then
    warn "QA-Report bezieht sich bei mindestens einem Modul auf eine andere Version als gepinnt"
  fi
else
  warn "Skill mii-qa-reports nicht gefunden — QA-Reports übersprungen"
fi

# ── 4. Paket bauen ────────────────────────────────────────────────────────────
step "BOM-Paket bauen"
if ./scripts/build-bom-package.sh > /tmp/gate-build.txt 2>&1; then
  COLL=$(grep -oE "[0-9]+ Kollisionen" /tmp/gate-build.txt | grep -oE "^[0-9]+" || echo 0)
  RES=$(grep -oE "Resources:\s+[0-9]+" /tmp/gate-build.txt | grep -oE "[0-9]+" || echo "?")
  if [[ "$COLL" -gt 0 ]]; then
    fail "$COLL Dateinamen-Kollision(en) beim Zusammenbauen"
    grep "Kollision:" /tmp/gate-build.txt | sed 's/^/      /'
  else
    ok "$RES Ressourcen, keine Kollisionen"
  fi
else
  fail "Build fehlgeschlagen — siehe /tmp/gate-build.txt"
fi

# ── 5. Doppelte Canonicals im gebauten Paket ──────────────────────────────────
step "Canonical-Kollisionen im Paket"
DUP=$(python3 - <<'PY'
import json, os, collections
d=".bake/package"; byurl=collections.defaultdict(set)
if os.path.isdir(d):
    for f in os.listdir(d):
        if not f.endswith(".json") or f in ("package.json",".index.json") or f.startswith("._"): continue
        try: r=json.load(open(os.path.join(d,f)))
        except Exception: continue
        if r.get("url"): byurl[r["url"]].add(r.get("id"))
print(sum(1 for u,i in byurl.items() if len(i)>1))
PY
)
if [[ "$DUP" -eq 0 ]]; then ok "keine doppelt belegten canonical URLs"
else warn "$DUP canonical URL(s) von mehreren Ressourcen belegt (Modulfehler, kein Blocker fürs Paket)"; fi

# ── 6. Validation-Server (nur --full) ─────────────────────────────────────────
if [[ "$MODE" == "--full" ]]; then
  step "Validation-Server (HAPI)"
  if (cd validation-server && docker compose build hapi-fhir > /tmp/gate-hapi-build.txt 2>&1); then
    ok "Image gebaut"
    docker rm -f gate-hapi >/dev/null 2>&1
    docker run -d --name gate-hapi --network none \
      -e SPRING_DATASOURCE_URL="jdbc:h2:mem:hapi" \
      -e SPRING_DATASOURCE_DRIVERCLASSNAME=org.h2.Driver \
      validation-server-hapi-fhir >/dev/null 2>&1
    for _ in $(seq 1 24); do
      docker logs gate-hapi 2>&1 | grep -q "Started Application" && break
      [[ "$(docker inspect -f '{{.State.Status}}' gate-hapi 2>/dev/null)" == "exited" ]] && break
      sleep 10
    done
    if docker logs gate-hapi 2>&1 | grep -q "Started Application"; then
      IDX=$(docker logs gate-hapi 2>&1 | grep -c Indexing)
      ok "startet offline durch, $IDX Ressourcen indiziert"
    else
      fail "Validation-Server startet nicht — docker logs gate-hapi"
    fi
    docker rm -f gate-hapi >/dev/null 2>&1
  else
    fail "Image-Build fehlgeschlagen — siehe /tmp/gate-hapi-build.txt"
  fi
fi

# ── Fazit ─────────────────────────────────────────────────────────────────────
printf "\n"
if [[ "$FAIL" -gt 0 ]]; then
  printf "\033[1;31m%d harte(r) Fehler, %d Hinweis(e) — nicht release-fähig.\033[0m\n" "$FAIL" "$WARN"
  exit 1
elif [[ "$WARN" -gt 0 ]]; then
  printf "\033[1;33mKeine harten Fehler, %d Hinweis(e) — release-fähig nach Sichtung.\033[0m\n" "$WARN"
  exit 2
else
  printf "\033[1;32mAlle Checks bestanden — release-fähig.\033[0m\n"
  exit 0
fi
