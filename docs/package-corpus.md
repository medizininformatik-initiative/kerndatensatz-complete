# Paket-Korpus

Lokale Rohdatenbasis für Analysen über den KDS-Ballot-Stand. Liegt unter
`package-corpus/` und ist **nicht eingecheckt** (`.gitignore`).

```bash
./scripts/build-package-corpus.py              # aufbauen (wiederaufnehmbar)
./scripts/corpus-query.py overview             # auswerten
```

## Auswahlregel

Je Modul **eine** Version: die höchste 2027er, sonst die höchste überhaupt verfügbare.

Bewusst *nicht* „höchste `ballot.*`": ICU ist vom Ballot bereits zum finalen `2027.0.0`
weitergezogen. Der Korpus soll den Stand abbilden, den die BOM pinnt und den Standorte
tatsächlich bekommen — also final vor RC, wenn beides existiert.

## Inhalt

21 Pakete, 1419 Conformance-Ressourcen, 102 MB.

| Herkunft | Module |
|---|---|
| 2027er Ballot-RC | base, meta, laborbefund, biobank, bildgebung, dokument, studie, kardiologie, lungenfunktion, soziodemographie |
| 2027 final | icu |
| 2027 alpha | mikrobiologie |
| höchste 2026er | medikation, molgen, patho, onkologie, seltene, mtb, pros, consent |
| älter | symptom (2024.0.0-ballot) |

| Ressourcentyp | Anzahl |
|---|---|
| StructureDefinition | 531 |
| ValueSet | 390 |
| SearchParameter | 234 |
| CodeSystem | 113 |
| ObservationDefinition | 47 |
| ConceptMap | 45 |
| Questionnaire | 32 |
| CapabilityStatement | 20 |
| ImplementationGuide | 6 |

**Soziodemographie** stammt nicht aus der Registry — das Package ist dort nicht
publiziert. Es wurde aus dem GitHub-Repo mit SUSHI gebaut und aus dem lokalen
FHIR-Cache übernommen. Provenienz steht in `manifest.json`.

## Auswertung

```bash
./scripts/corpus-query.py overview                     # Umfang je Modul
./scripts/corpus-query.py resources                    # Ressourcentypen
./scripts/corpus-query.py canonicals --duplicates      # URL-Kollisionen
./scripts/corpus-query.py deps --module icu            # Abhängigkeiten
./scripts/corpus-query.py profiles --module base -v    # Profile je Version
./scripts/corpus-query.py grep 'snomed.info/sct'       # Volltextsuche
```

Für Analysen über die Zeit statt nur des Ballot-Stands: `--all-versions` lädt die
komplette Historie (292 Paketversionen).

## Was der Korpus schon gezeigt hat

`canonicals --duplicates` findet die ICU-Kollision aus der Ballot-Analyse: zwei
verschiedene ValueSets unter derselben canonical URL
(`mii-vs-icu-code-observation-extrakorporale-verfahren-loinc`) — siehe
`docs/validation-2027.0.0-ballot.1.md`.

## Struktur

```
package-corpus/
  manifest.json                             Provenienz, Kennzahlen, Dependencies je Paket
  <package-id>#<version>/package/*.json     entpackter Paketinhalt
```
