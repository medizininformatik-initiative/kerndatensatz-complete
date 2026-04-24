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
# Quelle bearbeiten
dep-graph-2026.dot

# Rendern
dot -Tpng dep-graph-2026.dot -o input/images/dep-graph-2026.png
dot -Tsvg dep-graph-2026.dot -o input/images/dep-graph-2026.svg
```

### Farbschema

| Farbe | Hex | Bedeutung |
|-------|-----|-----------|
| Grün | `#d4edda` | Finale Version (normative / STU-abgeschlossen) |
| Gelb | `#fff3cd` | STU / Trial Use / Alpha |
| Grau | `#e2e3e5` | In Entwicklung / nicht publiziert |

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
5. `input/pagecontent/index.md` — Modultabelle
6. `dep-graph-2026.dot` — Abhängigkeitsgraph (danach neu rendern)
