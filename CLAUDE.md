# MII Kerndatensatz Complete

Bill of Materials (BOM) aller MII KDS-Module mit kompatiblen Versionen. Enthält keine eigenen FSH-Profile — nur Dependency-Deklarationen und Dokumentation.

## Projektstruktur

- `package.json` / `sushi-config.yaml` — Modulliste mit Versionen (source of truth)
- `validation-server/` — HAPI + Blaze Konfiguration für lokale Validierung
- `scripts/` — Build- und Hilfsskripte
- `input/pagecontent/index.md` — IG-Dokumentation mit Modultabellen
- `docs/` — Zusätzliche Doku (Mermaid-Graphen, historisch)

## Abhängigkeitsgraph

Der Abhängigkeitsgraph wird als Graphviz DOT-Datei gepflegt und daraus als PNG/SVG gerendert:

```bash
# Quelle bearbeiten (aktuell: Ballot-Linie 2027)
dep-graph-2027.dot

# Rendern
dot -Tpng dep-graph-2027.dot -o input/images/dep-graph-2027.png
dot -Tsvg dep-graph-2027.dot -o input/images/dep-graph-2027.svg
```

Zusätzlich gibt es `dep-graph-2027-extern.dot` für die externen Abhängigkeiten:

```bash
dot -Tpng dep-graph-2027-extern.dot -o input/images/dep-graph-2027-extern.png
dot -Tsvg dep-graph-2027-extern.dot -o input/images/dep-graph-2027-extern.svg
```

`dep-graph-2026.dot` bleibt als Historie des 2026er Stands liegen.

### Farbschema

| Farbe | Hex | Bedeutung |
|-------|-----|-----------|
| Grün | `#d4edda` | Finale Version (normative / STU-abgeschlossen) |
| Gelb | `#fff3cd` | Ballot / RC / Alpha |
| Grau | `#e2e3e5` | In Entwicklung / nicht publiziert |

Kanten: grau = deklarierte Dependency passt zur BOM; rot gestrichelt (`#c0392b`) = das Modul
deklariert noch die 2026er Version des Ziels, während die BOM auf die 2027er Ballot-Linie pinnt.

## Package bauen

Dieses Projekt ist ein reines BOM-Package — kein SUSHI/Bake nötig:

```bash
./scripts/build-bom-package.sh
```

Das Script lädt alle Module-Packages von Simplifier, sammelt Conformance-Ressourcen + Examples ein und erstellt einen Tarball.

## Versionierung

Beim Hinzufügen oder Aktualisieren eines Moduls müssen diese Dateien angepasst werden:

1. `package.json` — Dependency-Version
2. `sushi-config.yaml` — Dependency-Version + ggf. Paketversion/releaseLabel
3. `validation-server/application.yaml` — HAPI-Konfiguration
4. `validation-server/load-packages-blaze.sh` — Blaze-Loader
5. `validation-server/Dockerfile` — **eigene Paketliste** für den Pre-Cache des HAPI-Images
6. `input/pagecontent/index.md` — Modultabelle
7. `dep-graph-2027.dot` — Abhängigkeitsgraph (danach neu rendern)
8. `dep-graph-2027-extern.dot` — bei geänderten externen Abhängigkeiten (danach neu rendern)

Danach prüfen, ob alle Quellen übereinstimmen:

```bash
./scripts/check-module-versions.py            # Konsistenz + Registry-Abgleich
./scripts/check-module-versions.py --offline  # nur Konsistenz, ohne Netz
```

## QA-Reports der Module

Dafür gibt es den Skill **`mii-qa-reports`** (global unter `~/.claude/skills/`), weil
er für alle MII-KDS-Repos gilt, nicht nur für dieses Projekt:

```bash
~/.claude/skills/mii-qa-reports/scripts/fetch_qa.py --pin-file package.json --details
```

Er entdeckt die Repos aus der GitHub-Org und sucht die QA-Reports auch unter
`gh-pages/branches/<branch>/` — dort liegen während Ballotierung und
Template-Migration die aktuellen Builds. Auswertung in `docs/qa-reports-2027-ballot.md`.

**Zwei Fallen:** `www.medizininformatik-initiative.de` antwortet auf *jeden* Pfad mit
HTTP 200 und einer HTML-Seite (Statuscode-Check erzeugt dort Fehlalarme), und ein
Report beschreibt nicht zwingend die Version, die die BOM pinnt — immer `ig-ver`
gegenhalten.

Das Skript kennt die bewussten Ausnahmen (Consent fehlt in HAPI wegen HAPI-1821,
`hl7.fhir.r4.core` steht nicht unter `implementationguides`) und meldet neuere
verfügbare Versionen als Hinweis, nicht als Fehler.

### Pinning-Regel für externe Pakete

Die BOM pinnt externe Pakete (Terminology, Extensions, ISiK, EU-Profile, MIABIS, Clinical
Genomics) auf **die höchste Version, die ein MII-Modul transitiv tatsächlich anfordert** —
nicht auf die neueste verfügbare. Eine Version, gegen die kein Modul gebaut wurde, gehört
nicht in eine BOM. Deshalb steht z.B. `eu.miabis.r4` auf 0.2.0, obwohl MIABIS bei 1.3.0 ist.

Die transitive Hülle lässt sich so ermitteln: `https://packages.simplifier.net/<pkg>` liefert
JSON mit allen Versionen, `https://packages.simplifier.net/<pkg>/<version>` dagegen das
gzip-Tarball — die deklarierten Dependencies stehen darin in `package/package.json`.


<!-- BEGIN BEADS INTEGRATION v:1 profile:minimal hash:ca08a54f -->
## Beads Issue Tracker

This project uses **bd (beads)** for issue tracking. Run `bd prime` to see full workflow context and commands.

### Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --claim  # Claim work
bd close <id>         # Complete work
```

### Rules

- Use `bd` for ALL task tracking — do NOT use TodoWrite, TaskCreate, or markdown TODO lists
- Run `bd prime` for detailed command reference and session close protocol
- Use `bd remember` for persistent knowledge — do NOT use MEMORY.md files

## Session Completion

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd dolt push
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
<!-- END BEADS INTEGRATION -->
