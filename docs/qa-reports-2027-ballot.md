# QA-Reports der KDS-Module — Auswertung

Stand: 2026-09-03 · IG Publisher v2.3.3 · reproduzierbar mit dem Skill `mii-qa-reports`:

```bash
~/.claude/skills/mii-qa-reports/scripts/fetch_qa.py --pin-file package.json --details
```

> **Korrektur gegenüber der ersten Fassung.** Die erste Auswertung suchte nur an der
> gh-pages-Wurzel, auf build.fhir.org und am Canonical und fand deshalb nur 5 Reports.
> Während Ballotierung und Template-Migration liegt der aktuelle Build aber meist unter
> `gh-pages/branches/<branch>/`. Mit dieser Quelle sind es **18 von 39** Repos — und
> mehrere Zahlen unten ändern sich drastisch.

## Verfügbarkeit: 18 von 39

Achtzehn Repos publizieren einen auswertbaren QA-Report, verteilt über build.fhir.org, die gh-pages-Wurzel und vor allem `gh-pages/branches/<branch>/`. Es gibt keinen einheitlichen Ort und keine einheitliche Branch-Konvention.

### Die auffälligsten Reports

| Repo | Branch | Version | Errors | Warnings |
|---|---|---|---|---|
| kerndatensatzmodul-onkologie | dev | 2026.0.3 | **6872** | 3961 |
| kerndatensatzmodul-studie | tech-test-2026-07-23 | 2026.0.1 | **783** | 662 |
| kerndatensatzmodul-seltene-erkrankungen | dev | v2 | **681** | 387 |
| kerndatensatz-meta | 2027.0.0-ballot.rc3 | 2027.0.0-ballot.rc3 | **386** | 957 |
| kerndatensatzmodul-proms | dev | 2026.7.0 | **302** | 1004 |
| kerndatensatzmodul-labor | flatten-category-v2 | 2027.0.0-ballot.rc3 | **37** | 41 |
| kds-fdpg-layer | Wurzel | 2026.0.0 | 26 | 7389 |
| kerndatensatz-basis | develop | 2027.0.0-ballot.rc1 | 22 | 635 |
| kerndatensatz-dokument | dev | 2027.0.0-ballot.rc1 | 8 | 120 |
| kerndatensatz-soziodemographie | 1.0.0 | 2027.0.0-ballot.rc1 | 8 | 216 |

### Von welchem Branch stammt der Report?

Ein frisches Build-Datum heißt nicht, dass der Branch aktuell ist. Sechs der achtzehn
Reports stammen von einem Branch, der nicht den aktuellen Stand trägt:

| Repo | Branch | Stand |
|---|---|---|
| lungenfunktion | tech-test-2026-07-23 | 42 Commits hinter `main` |
| studie | tech-test-2026-07-23 | 40 Commits hinter `master` |
| molgen | tech-test-2026-07-23 | 32 Commits hinter `main` |
| meta | 2027.0.0-ballot.rc3 | 3 Commits hinter `main` |
| soziodemographie | 1.0.0 | 2 Commits hinter `main` |
| laborbefund | flatten-category-v2 | **Branch existiert nicht mehr** |

Die `tech-test-2026-07-23`-Builds sind vom Juli und wirken durch das Datum aktuell,
beschreiben aber einen Stand von vor der Migration. Für Studie heißt das: die 783 Errors
beziehen sich auf 2026.0.1, nicht auf die gepinnte `2027.0.0-ballot.rc1` — zu dieser
Version gibt es **keinen** Report.

Bei Labor ist der Befund trotzdem belastbar: `master`, der Tag `v2027.0.0-ballot.rc3`
und der gelöschte Branch liefern identische Zahlen (37 Errors, 41 Warnings).

Verlässlich sind die Reports von **onkologie, proms, seltene** (jeweils Default-Branch)
sowie **basis und dokument** (identisch mit dem Default).

**Meta ist der wichtigste Fund.** An der zuerst gefundenen Stelle stand ein Report über
2026.0.0 mit 3 Errors. Der Branch-Build zur tatsächlich gepinnten Ballot-Version
2027.0.0-ballot.rc3 hat **386 Errors** — zwei Größenordnungen mehr. Meta ist das
Fundament, auf dem alle anderen Module aufsetzen.

**Labor 2027.0.0-ballot.rc3 hat 37 Errors** und war vorher gar nicht sichtbar, weil das
Modul keinen Report an der gh-pages-Wurzel ablegt.

**Mikrobiologie baut bereits 2027.0.0-alpha.6**, publiziert ist aber nur alpha.5 — der
Pin der BOM ist also korrekt, alpha.6 steht bevor.

**Auf einem Labor-Branch (`restrict-interpretation-vs`) läuft eine Paket-Umbenennung**
von `kerndatensatz.laborbefund` nach `kerndatensatz.labor`. Falls das so kommt, bricht es
jede BOM, die auf den alten Namen pinnt.

### Erste Auswertung (nur Wurzel-/CI-Quellen) — hier zum Vergleich:

| Modul | QA-Report über | BOM pinnt | Errors | Warnings | Hints | Quelle |
|---|---|---|---|---|---|---|
| base | 2027.0.0-ballot.rc1 | 2027.0.0-ballot.rc1 | **22** | 635 | 2915 | github.io |
| dokument | 2027.0.0-ballot.rc1 | 2027.0.0-ballot.rc1 | **8** | 120 | 16 | build.fhir.org |
| meta | 2026.0.0 | 2027.0.0-ballot.rc3 | 3 | 260 | 524 | build.fhir.org — **veralteter Stand** |
| pros | 2026.7.0 | 2026.7.0 | **302** | 1004 | 1044 | build.fhir.org |
| soziodemographie | 2027.0.0-ballot.rc1 | nicht gepinnt | **8** | 216 | 74 | github.io |

Ohne Report: bildgebung, biobank, consent, icu, kardiologie, laborbefund, lungenfunktion, medikation, mikrobiologie, molgen, mtb, onkologie, patho, seltene, studie.

> **Falle bei der Suche:** `www.medizininformatik-initiative.de` liefert für *jeden* Pfad HTTP 200 mit einer HTML-Seite zurück, auch für nicht existierende Dateien. Ein 200 beweist dort nichts. Labor und Medikation sahen deshalb zunächst wie Treffer aus — beides waren HTML-Platzhalter. Das Skript parst deshalb den Inhalt statt auf den Statuscode zu vertrauen.

## Befunde

### PROs 2026.7.0 — 302 Errors

Mit Abstand der auffälligste Report, und es ist die Version, die die BOM pinnt.

| Anzah| Befund |
|---|---|
| 151 | `Wrong Display Name` — Display-Texte weichen von der Terminologie ab |
| **45** | **`Validation_VAL_Profile_NotAllowed` — Element durch das Profil nicht erlaubt** |
| 42 | `HTML_IMG_SRC_CHECK_FAILED` — Bildquellen im IG nicht auflösbar |
| 17 | `CONCEPTMAP_GROUP_SOURCE_CODE_INVALID` — Quell-Code im ConceptMap ungültig |
| 15 | `TYPE_SPECIFIC_CHECKS_DT_CANONICAL_RESOLVE` — Canonical nicht auflösbar |
| 12 | Links nicht auflösbar · 12 Referenzen nicht auffindbar |
| 9 | `Validation_VAL_Profile_Minimum` — Pflichtelement fehlt |

Die 45 Profilverletzungen konzentrieren sich vollständig auf **einen** Fragebogen: `mii-qst-pro-eortc-qlq-c30`. Betroffen sind die *contained* Ressourcen — 13 Meldungen allein auf `contained[0]` (CodeSystem `eortc-qlq-c30-cs`), dazu jede einzelne `concept[n]`, `caseSensitive` und `content`. Dazu fehlen `Questionnaire.extension:capabilities` und `Questionnaire.code`.

Das Profil erlaubt die eingebetteten CodeSystem/ValueSet-Ressourcen nicht, die der Fragebogen mitbringt. Entweder muss das Profil `contained` zulassen oder der Fragebogen die Terminologie auslagern.

### base 2027.0.0-ballot.rc1 — 22 Errors

Fast ausschließlich Terminologie-Pflege, und zwar echte Fehler:

- **13x** SNOMED-Codes, die in der referenzierten SNOMED-Version (`20250701`) nicht gültig sind — z.B. `363676003`, `261004008`, `264931009`, `255231005`. Vermutlich zurückgezogene oder ersetzte Konzepte.
- **6x** Codes in einem CodeSystem-Supplement, die im Basis-CodeSystem SNOMED gar nicht deklariert sind (`41847000`, `263659003`, `255398004`, `713153009`) — ein Supplement kann nur Konzepte ergänzen, die es gibt.
- 3x falscher Display-Name für `urn:iso:std:iso:3166#DE`.

### dokument 2027.0.0-ballot.rc1 — 8 Errors

- **1x FHIR-Versionskonflikt**: „This IG is for FHIR version 4.0.1, while the package `hl7.fhir.uv.subscriptions-backport.r4#1.1.0` is for FHIR version 4.0.0". Das Paket kommt transitiv über ISiK 6.0.0 herein — deckt sich mit der Abhängigkeitsanalyse der BOM.
- 6x ValueSet-Filter auf eine Property eines CodeSystems, dessen Definition nicht auflösbar ist.
- 1x Dependency-URL zeigt nicht direkt auf die ImplementationGuide-Ressource (`de.ihe-d.terminology`).

### soziodemographie 2027.0.0-ballot.rc1 — 8 Errors laut qa.json, 38 im HTML

- 28x nicht auflösbare interne Links (`HTML_LINK_CHECK_FAILED`) — Navigationsziele im IG.
- 4x `UNABLE_TO_INFER_CODESYSTEM` plus 4 Folgefehler: IG-Parameter wie `ImplementationGuide-mii-ig-soziodemographie.md` und `translationinfo.md` stehen nicht im ValueSet `ig-parameters`. Tooling-Konfiguration, keine inhaltliche Modellierung.

### meta — Report veraltet

Der publizierte Report beschreibt **2026.0.0**, die BOM pinnt **2027.0.0-ballot.rc3**. Die 3 Errors (fehlende Suppressed-Messages-Datei, Canonical-Mismatch bei `CodeSystem-mii-cs-meta-diz-standorte`) beziehen sich auf einen Stand, der nicht mehr aktuell ist. Für die Ballot-Version gibt es keine Aussage.

## Einordnung gegen die eigene Validierung

Die QA-Reports und die HAPI-Validierung (`docs/validation-2027.0.0-ballot.1.md`) sehen **unterschiedliche Dinge**, sie ersetzen einander nicht:

- Der IG Publisher prüft den Guide als Ganzes — Links, Bilder, Terminologie-Displays, IG-Metadaten. Das findet HAPI nicht.
- HAPI prüft Instanzen gegen Profile mit dem tatsächlich gepinnten Paketstand. Der Slicing-Fehler in Lungenfunktion und die 66 ins Leere zeigenden Profil-Referenzen tauchen in keinem QA-Report auf — schon weil 15 Module gar keinen publizieren.

Für die Ballot-Bewertung sind beide nötig.
