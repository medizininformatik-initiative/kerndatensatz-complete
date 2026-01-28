# FDPG Obligations & Translation Layer

**Konzept-Dokument**
**Stand:** 2025-01-08

---

## Motivation

Die MII KDS-Module werden von verschiedenen Arbeitsgruppen gepflegt. Eine zentrale Harmonisierung der Translations und FDPG-spezifischer Anforderungen direkt in den Modulen ist:
- Organisatorisch aufwändig (21 Repos, verschiedene Maintainer)
- Versionierungstechnisch komplex
- Schwer konsistent zu halten

**Lösung:** Ein separates "Overlay-Repository" das:
1. Alle KDS-Module als Dependencies importiert
2. FDPG-spezifische **Obligations** definiert
3. Zentral gepflegte **Translations** bereitstellt
4. Keine Änderungen an den Original-Modulen erfordert

---

## Architektur

```
┌─────────────────────────────────────────────────────────────┐
│                    FDPG Data Consumer                        │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              fdpg-kds-obligations                            │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │ Obligations │  │Translations │  │ ActorDefinitions    │  │
│  │ (SHOULD,    │  │ (DE, EN)    │  │ - DataProvider      │  │
│  │  SHALL)     │  │             │  │ - DataConsumer      │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐
│  KDS Person     │ │  KDS Diagnose   │ │  KDS Labor      │
│  (Original)     │ │  (Original)     │ │  (Original)     │
└─────────────────┘ └─────────────────┘ └─────────────────┘
```

---

## FHIR Obligations

### Was sind Obligations?

[FHIR Obligations](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-obligation.html) sind Extensions die Anforderungen an Implementierungen definieren, ohne die Profile selbst zu ändern.

**Obligation Codes:**
- `SHALL:populate` - MUSS befüllt werden
- `SHOULD:populate` - SOLLTE befüllt werden
- `SHALL:handle` - MUSS verarbeitet werden können
- `SHOULD:display` - SOLLTE angezeigt werden
- `SHALL:persist` - MUSS persistiert werden

### Actors

```fsh
Instance: fdpg-actor-data-provider
InstanceOf: ActorDefinition
Usage: #definition
* name = "FDPGDataProvider"
* title = "FDPG Datenlieferant"
* status = #active
* type = #system
* description = "Systeme die Daten an das FDPG liefern (DIZ, Standorte)"

Instance: fdpg-actor-data-consumer
InstanceOf: ActorDefinition
Usage: #definition
* name = "FDPGDataConsumer"
* title = "FDPG Datenkonsument"
* status = #active
* type = #system
* description = "Systeme die Daten vom FDPG abrufen (Forschungsprojekte)"
```

---

## Repository-Struktur

```
fdpg-kds-obligations/
├── sushi-config.yaml
├── package.json
├── input/
│   ├── fsh/
│   │   ├── actors/
│   │   │   ├── fdpg-actor-data-provider.fsh
│   │   │   └── fdpg-actor-data-consumer.fsh
│   │   │
│   │   ├── obligations/
│   │   │   ├── person/
│   │   │   │   └── fdpg-ob-person-patient.fsh
│   │   │   ├── diagnose/
│   │   │   │   └── fdpg-ob-diagnose-condition.fsh
│   │   │   ├── labor/
│   │   │   │   └── fdpg-ob-labor-observation.fsh
│   │   │   └── ... (pro Modul)
│   │   │
│   │   ├── translations/
│   │   │   ├── de-DE/
│   │   │   │   ├── person-translations.fsh
│   │   │   │   ├── diagnose-translations.fsh
│   │   │   │   └── ...
│   │   │   └── en-US/
│   │   │       ├── person-translations.fsh
│   │   │       ├── diagnose-translations.fsh
│   │   │       └── ...
│   │   │
│   │   └── rulesets/
│   │       ├── obligation-patterns.fsh
│   │       └── translation-patterns.fsh
│   │
│   └── pagecontent/
│       ├── index.md
│       ├── obligations.md
│       └── translations.md
│
└── implementation-guides/
    ├── fdpg-obligations-de/
    └── fdpg-obligations-en/
```

---

## sushi-config.yaml

```yaml
id: fdpg-kds-obligations
canonical: https://forschen-fuer-gesundheit.de/fhir/fdpg-obligations
name: FDPGKDSObligations
title: FDPG KDS Obligations & Translations
status: active
version: 2025.0.0
fhirVersion: 4.0.1
language: de-DE

publisher:
  name: FDPG / Medizininformatik-Initiative
  url: https://forschen-fuer-gesundheit.de

dependencies:
  # MII Kerndatensatz Core
  de.medizininformatikinitiative.kerndatensatz.person: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.diagnose: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.prozedur: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.laborbefund: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.medikation: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.fall: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.consent: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.biobank: 2025.0.x

  # MII Kerndatensatz Specialized
  de.medizininformatikinitiative.kerndatensatz.onkologie: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.icu: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.molgen: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.patho: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.bildgebung: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.mikrobiologie: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.studie: 2025.0.x
  de.medizininformatikinitiative.kerndatensatz.seltene: 2026.0.x

  # FHIR Extensions
  hl7.fhir.uv.extensions.r4: 5.1.x

parameters:
  show-inherited-invariants: false
  apply-jurisdiction: true
  apply-publisher: true
```

---

## Beispiel: Obligations für Person/Patient

```fsh
// input/fsh/obligations/person/fdpg-ob-person-patient.fsh

Instance: fdpg-ob-person-patient
InstanceOf: StructureDefinition
Usage: #definition
* url = "https://forschen-fuer-gesundheit.de/fhir/fdpg-obligations/StructureDefinition/fdpg-ob-person-patient"
* name = "FDPG_OB_Person_Patient"
* title = "FDPG Obligations für MII Person Patient"
* status = #active
* kind = #resource
* abstract = false
* type = "Patient"
* baseDefinition = "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/Patient"
* derivation = #constraint

// Obligations für Data Provider
* differential.element[+].id = "Patient.identifier"
* differential.element[=].path = "Patient.identifier"
* differential.element[=].extension[+].url = "http://hl7.org/fhir/StructureDefinition/obligation"
* differential.element[=].extension[=].extension[+].url = "code"
* differential.element[=].extension[=].extension[=].valueCode = #SHALL:populate
* differential.element[=].extension[=].extension[+].url = "actor"
* differential.element[=].extension[=].extension[=].valueCanonical = "https://forschen-fuer-gesundheit.de/fhir/fdpg-obligations/ActorDefinition/fdpg-actor-data-provider"

* differential.element[+].id = "Patient.name"
* differential.element[=].path = "Patient.name"
* differential.element[=].extension[+].url = "http://hl7.org/fhir/StructureDefinition/obligation"
* differential.element[=].extension[=].extension[+].url = "code"
* differential.element[=].extension[=].extension[=].valueCode = #SHOULD:populate
* differential.element[=].extension[=].extension[+].url = "actor"
* differential.element[=].extension[=].extension[=].valueCanonical = "https://forschen-fuer-gesundheit.de/fhir/fdpg-obligations/ActorDefinition/fdpg-actor-data-provider"
* differential.element[=].extension[=].extension[+].url = "documentation"
* differential.element[=].extension[=].extension[=].valueMarkdown = "Name sollte geliefert werden, wenn nicht durch Datenschutz-Constraints ausgeschlossen"

// Obligations für Data Consumer
* differential.element[+].id = "Patient.birthDate"
* differential.element[=].path = "Patient.birthDate"
* differential.element[=].extension[+].url = "http://hl7.org/fhir/StructureDefinition/obligation"
* differential.element[=].extension[=].extension[+].url = "code"
* differential.element[=].extension[=].extension[=].valueCode = #SHALL:handle
* differential.element[=].extension[=].extension[+].url = "actor"
* differential.element[=].extension[=].extension[=].valueCanonical = "https://forschen-fuer-gesundheit.de/fhir/fdpg-obligations/ActorDefinition/fdpg-actor-data-consumer"
```

---

## Beispiel: Translations

```fsh
// input/fsh/translations/de-DE/person-translations.fsh

RuleSet: PersonPatientTranslations_DE
// Profile-Level
* ^title.extension[+].url = "http://hl7.org/fhir/StructureDefinition/translation"
* ^title.extension[=].extension[+].url = "lang"
* ^title.extension[=].extension[=].valueCode = #de-DE
* ^title.extension[=].extension[+].url = "content"
* ^title.extension[=].extension[=].valueString = "MII Profil Person Patient"

// Element-Level
* identifier ^short.extension[+].url = "http://hl7.org/fhir/StructureDefinition/translation"
* identifier ^short.extension[=].extension[+].url = "lang"
* identifier ^short.extension[=].extension[=].valueCode = #de-DE
* identifier ^short.extension[=].extension[+].url = "content"
* identifier ^short.extension[=].extension[=].valueString = "Identifikatoren des Patienten"

* identifier ^definition.extension[+].url = "http://hl7.org/fhir/StructureDefinition/translation"
* identifier ^definition.extension[=].extension[+].url = "lang"
* identifier ^definition.extension[=].extension[=].valueCode = #de-DE
* identifier ^definition.extension[=].extension[+].url = "content"
* identifier ^definition.extension[=].extension[=].valueString = "Eindeutige Identifikatoren zur Identifikation des Patienten, z.B. Krankenversichertennummer, interne Patienten-ID"

* name ^short.extension[+].url = "http://hl7.org/fhir/StructureDefinition/translation"
* name ^short.extension[=].extension[+].url = "lang"
* name ^short.extension[=].extension[=].valueCode = #de-DE
* name ^short.extension[=].extension[+].url = "content"
* name ^short.extension[=].extension[=].valueString = "Name des Patienten"
```

```fsh
// input/fsh/translations/en-US/person-translations.fsh

RuleSet: PersonPatientTranslations_EN
* ^title.extension[+].url = "http://hl7.org/fhir/StructureDefinition/translation"
* ^title.extension[=].extension[+].url = "lang"
* ^title.extension[=].extension[=].valueCode = #en-US
* ^title.extension[=].extension[+].url = "content"
* ^title.extension[=].extension[=].valueString = "MII Profile Person Patient"

* identifier ^short.extension[+].url = "http://hl7.org/fhir/StructureDefinition/translation"
* identifier ^short.extension[=].extension[+].url = "lang"
* identifier ^short.extension[=].extension[=].valueCode = #en-US
* identifier ^short.extension[=].extension[+].url = "content"
* identifier ^short.extension[=].extension[=].valueString = "Patient identifiers"

* identifier ^definition.extension[+].url = "http://hl7.org/fhir/StructureDefinition/translation"
* identifier ^definition.extension[=].extension[+].url = "lang"
* identifier ^definition.extension[=].extension[=].valueCode = #en-US
* identifier ^definition.extension[=].extension[+].url = "content"
* identifier ^definition.extension[=].extension[=].valueString = "Unique identifiers for patient identification, e.g., health insurance number, internal patient ID"
```

---

## Alternativer Ansatz: Requirements Resource

Statt Obligations auf StructureDefinition-Ebene kann auch die **Requirements**-Resource (R5) verwendet werden:

```fsh
Instance: fdpg-req-person
InstanceOf: Requirements
Usage: #definition
* url = "https://forschen-fuer-gesundheit.de/fhir/fdpg-obligations/Requirements/fdpg-req-person"
* name = "FDPG_REQ_Person"
* title = "FDPG Anforderungen für Person-Modul"
* status = #active
* derivedFrom = "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/Patient"

* statement[+].key = "fdpg-person-1"
* statement[=].label = "Identifikator-Pflicht"
* statement[=].conformance = #SHALL
* statement[=].requirement = "Mindestens ein Identifikator MUSS vorhanden sein"
* statement[=].source.display = "FDPG Datenqualitäts-AG"

* statement[+].key = "fdpg-person-2"
* statement[=].label = "Geburtsdatum-Genauigkeit"
* statement[=].conformance = #SHOULD
* statement[=].requirement = "Geburtsdatum SOLLTE mindestens auf Monat genau sein"
```

---

## Aufwandsschätzung

| Task | Aufwand |
|------|---------|
| Repository-Setup | 1 Tag |
| ActorDefinitions | 1 Tag |
| Obligations für ~450 Profile (Basis-Set) | 5-7 Tage |
| Translations DE für MS-Elemente (~414) | 3-5 Tage |
| Translations EN für MS-Elemente (~414) | 5-7 Tage |
| IG-Dokumentation | 2-3 Tage |
| Review & Testing | 3-5 Tage |
| **Gesamt** | **~4-5 Wochen** |

---

## Vorteile

| Aspekt | Vorteil |
|--------|---------|
| **Unabhängigkeit** | Keine Änderungen an KDS-Modulen nötig |
| **Zentrale Pflege** | Translations und Obligations an einem Ort |
| **Versionierung** | Unabhängig von Modul-Releases |
| **Konsistenz** | Einheitliche Terminologie über alle Module |
| **Erweiterbarkeit** | Weitere Actors/Obligations einfach ergänzbar |
| **Mehrsprachigkeit** | DE/EN zentral gepflegt |

---

## Nachteile / Risiken

| Aspekt | Risiko | Mitigation |
|--------|--------|------------|
| **Sync-Aufwand** | Bei KDS-Updates müssen Obligations angepasst werden | CI/CD mit Dependency-Check |
| **Tooling** | Nicht alle Tools unterstützen Obligations | Fallback auf Requirements |
| **Komplexität** | Zusätzliche Indirektionsebene | Klare Dokumentation |
| **Adoption** | Nutzer müssen beide Packages einbinden | NPM meta-package |

---

## Nächste Schritte

1. [ ] Proof-of-Concept mit Person-Modul
2. [ ] Tooling-Evaluation (IG Publisher Obligations-Support)
3. [ ] Abstimmung mit FDPG-AG
4. [ ] Entscheidung: Obligations vs. Requirements
5. [ ] Repository-Setup
6. [ ] Pilotierung mit 3-5 Modulen

---

## Referenzen

- [FHIR Obligations Extension](http://hl7.org/fhir/extensions/5.1.0/StructureDefinition-obligation.html)
- [FHIR Translation Extension](https://build.fhir.org/languages.html)
- [FHIR Requirements Resource (R5)](https://build.fhir.org/requirements.html)
- [HL7 EU Obligations IG](https://www.hl7.eu/obligations/)

---

*Konzept-Dokument erstellt: 2025-01-08*
