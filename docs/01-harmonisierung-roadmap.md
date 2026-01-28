# MII KDS Module - Harmonisierungs-Roadmap

**Stand:** 2025-01-08
**Basierend auf:** Analyse von 21 KDS-Repositories

---

## Executive Summary

Die Analyse der 21 MII Kerndatensatz-Module zeigt erhebliche Heterogenität in Struktur, Konfiguration und Implementierung. Dieses Dokument definiert konkrete Harmonisierungsmaßnahmen.

---

## 1. Kritische Lücken

| Bereich | Problem | Betroffene Module |
|---------|---------|-------------------|
| CI/CD | Keine GitHub Actions | kardiologie, consent |
| Logical Models | Fehlen komplett | kardiologie, meta, consent |
| Mappings | LM vorhanden aber keine Mappings | icu, mikrobiologie, patho, studie |
| Translations | Keine Element-Translations | kardiologie, meta, consent, icu, mikrobiologie |
| IG-Sprache | Kein `language:` gesetzt | 13 von 21 Modulen |
| EN-Version | Keine englische IG-Version | 18 von 21 Modulen |

---

## 2. Harmonisierungsmaßnahmen

### 2.1 Aliases standardisieren

**Ziel:** Einheitliche Alias-Namen über alle Module

**Standard-Aliases (aliases.fsh):**
```fsh
// Terminologien - OHNE Version (für ValueSet-Bindings)
Alias: $SCT = http://snomed.info/sct
Alias: $LNC = http://loinc.org
Alias: $UCUM = http://unitsofmeasure.org

// Terminologien - MIT Version (für Coding in Beispielen)
Alias: $SCT-2025 = http://snomed.info/sct|http://snomed.info/sct/900000000000207008/version/20250701

// Deutsche Terminologien
Alias: $ICD10GM = http://fhir.de/CodeSystem/bfarm/icd-10-gm
Alias: $OPS = http://fhir.de/CodeSystem/bfarm/ops
Alias: $ATC = http://fhir.de/CodeSystem/bfarm/atc
Alias: $ALPHA-ID = http://fhir.de/CodeSystem/bfarm/alpha-id

// ICD-O-3
Alias: $ICDO3 = http://terminology.hl7.org/CodeSystem/icd-o-3

// FHIR Core
Alias: $ObsCat = http://terminology.hl7.org/CodeSystem/observation-category
Alias: $CondCat = http://terminology.hl7.org/CodeSystem/condition-category
Alias: $CondVerStatus = http://terminology.hl7.org/CodeSystem/condition-ver-status
```

**Migration:**
| Alt | Neu |
|-----|-----|
| `$sct`, `$sct-no-ver` | `$SCT` |
| `$loinc`, `$LOINC` | `$LNC` |
| `$icd-10-gm`, `$icd10-gm`, `$CS_icd10-gm` | `$ICD10GM` |
| `$ops`, `$cs-ops` | `$OPS` |
| `$atc`, `$cs-atc`, `$ATC_DE` | `$ATC` |

---

### 2.2 SNOMED CT Version vereinheitlichen

**Ziel:** Alle Module nutzen dieselbe SNOMED-Version

**Aktuelle Situation:**
- `20250701`: basis, bildgebung, kardiologie, labor, medikation
- `20240701`: lungenfunktion, prozedur
- Ohne Version: 11 Module

**Standard:**
```fsh
// Für ValueSet-Bindings (versionsneutral)
Alias: $SCT = http://snomed.info/sct

// Für Beispiele (mit Version)
Alias: $SCT-2025 = http://snomed.info/sct|http://snomed.info/sct/900000000000207008/version/20250701
```

---

### 2.3 Rulesets standardisieren

**Kern-Rulesets (verpflichtend):**

```
input/fsh/rulesets/
├── version.fsh          # Versionierung
├── publisher.fsh        # MII Publisher-Metadaten
├── license-terms.fsh    # Lizenzierung
├── translation.fsh      # Translation-Extension Helper
└── meta-profile.fsh     # Meta.profile setzen
```

**version.fsh:**
```fsh
RuleSet: PR_CS_VS_Version
* ^version = "2025.0.0"
* ^date = "2025-01-08"
* ^status = #active
```

**translation.fsh:**
```fsh
RuleSet: Translation(element, lang, text)
* {element}.extension[+].url = "http://hl7.org/fhir/StructureDefinition/translation"
* {element}.extension[=].extension[+].url = "lang"
* {element}.extension[=].extension[=].valueCode = #{lang}
* {element}.extension[=].extension[+].url = "content"
* {element}.extension[=].extension[=].valueString = "{text}"
```

**Fehlend in:**
- consent: ALLE Rulesets
- kardiologie: license-terms, translation
- icu: translation
- mikrobiologie: translation

---

### 2.4 Language-Setting

**Ziel:** Alle Module setzen `language: de-DE`

**sushi-config.yaml:**
```yaml
language: de-DE
```

**Fehlend in:** basis, bildgebung, lungenfunktion, meta, biobank, consent, icu, labor, medikation, mikrobiologie, prozedur, studie

---

### 2.5 Translation-Elemente

**Standard:** Alle Profile übersetzen mindestens:
- `^title` (Profile-Titel)
- `^description` (Profile-Beschreibung)
- `^short` (Element-Kurztext)
- `^definition` (Element-Definition)

**Beispiel:**
```fsh
Profile: MII_PR_Person_Patient
* insert Translation(^title, de-DE, MII PR Person Patient)
* insert Translation(^description, de-DE, Dieses Profil beschreibt eine Person in der Medizininformatik-Initiative.)
* name ^short = "Name"
* insert Translation(name ^short, en-US, Name)
* name ^definition = "Der vollständige Name der Person"
* insert Translation(name ^definition, en-US, The complete name of the person)
```

**Aktueller Stand:**
| Modul | ^short | ^definition | ^title | ^description |
|-------|--------|-------------|--------|--------------|
| mtb | 442 | 342 | 0 | 0 |
| bildgebung | 248 | 248 | 42 | 42 |
| onkologie | 168 | 167 | 2 | 1 |

---

### 2.6 Logical Models & Mappings

**Ziel:** Jedes Modul hat:
1. Logical Model(s)
2. Mapping: LM → FHIR Profile
3. Mapping: Profile → LM (optional, für Rückwärtskompatibilität)

**Fehlend:**

| Modul | Logical Model | LM→Profile | Profile→LM |
|-------|---------------|------------|------------|
| kardiologie | ❌ | ❌ | ❌ |
| consent | ❌ | ❌ | ❌ |
| meta | ❌ | ❌ | ❌ |
| icu | ✅ | ❌ | ❌ |
| mikrobiologie | ✅ | ❌ | ❌ |
| patho | ✅ | ❌ | ❌ |
| studie | ✅ | ❌ | ❌ |

---

### 2.7 CI/CD Standardisierung

**Standard-Workflow (main.yml):**
```yaml
name: CI (FHIR Validation)

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
      - name: Install SUSHI
        run: npm install -g fsh-sushi
      - name: Run SUSHI
        run: sushi .
      - name: Validate
        run: # HAPI Validator oder IG Publisher
```

**Fehlend in:** kardiologie, consent

---

### 2.8 Englische IG-Version

**Ziel:** Alle Module haben DE + EN IG-Version

**Aktuell mit EN:**
- onkologie (2025.x-EN)
- PathologieBefund (2026.0.x-EN)
- prozedur (2024.x-EN)

**Struktur:**
```
implementation-guides/
├── ImplementationGuide-2025.x-DE/
│   └── MIIIGModul{Name}/
└── ImplementationGuide-2025.x-EN/
    └── MIIIGModul{Name}/
```

---

## 3. Priorisierung

### Phase 1: Quick Wins (1-2 Wochen)
- [ ] `language: de-DE` in allen sushi-config.yaml setzen
- [ ] Fehlende CI/CD Actions hinzufügen (kardiologie, consent)
- [ ] Standard-Aliases als shared Ruleset erstellen

### Phase 2: Struktur (2-4 Wochen)
- [ ] Aliases in allen Modulen migrieren
- [ ] SNOMED-Versionen vereinheitlichen
- [ ] Kern-Rulesets in allen Modulen etablieren

### Phase 3: Inhalt (4-8 Wochen)
- [ ] Fehlende Logical Models erstellen
- [ ] Fehlende Mappings ergänzen
- [ ] Translation-Lücken füllen

### Phase 4: Internationalisierung (8-12 Wochen)
- [ ] EN IG-Versionen für alle Module
- [ ] Translation-Review und Qualitätssicherung

---

## 4. Governance

### Shared Resources Repository

Empfehlung: Zentrales Repo für gemeinsame Ressourcen:

```
mii-kds-shared/
├── rulesets/
│   ├── version.fsh
│   ├── publisher.fsh
│   ├── license-terms.fsh
│   ├── translation.fsh
│   └── meta-profile.fsh
├── aliases/
│   └── standard-aliases.fsh
├── templates/
│   └── github-actions/
│       └── main.yml
└── scripts/
    └── harmonization-check.py
```

Module importieren via git submodule oder npm package.

---

## 5. Metriken

| Metrik | Aktuell | Ziel |
|--------|---------|------|
| Module mit CI/CD | 19/21 (90%) | 21/21 (100%) |
| Module mit `language:` | 8/21 (38%) | 21/21 (100%) |
| Module mit Logical Model | 17/21 (81%) | 21/21 (100%) |
| Module mit Mappings | 13/21 (62%) | 21/21 (100%) |
| Module mit EN-IG | 3/21 (14%) | 21/21 (100%) |
| Einheitliche Aliases | 0/21 (0%) | 21/21 (100%) |

---

## Anhang: Modul-Übersicht

| Modul | Profile | MS | CI/CD | LM | Map | Trans | Lang | EN-IG |
|-------|---------|-----|-------|-----|-----|-------|------|-------|
| basis | 7 | 24 | ✅+ | ✅4 | ✅ | ✅427 | ❌ | ❌ |
| bildgebung | 12 | 12 | ✅ | ✅1 | ✅ | ✅610 | ❌ | ❌ |
| biobank | 11 | 9 | ✅ | ✅1 | ⚠️ | ✅207 | ❌ | ❌ |
| consent | 0 | 0 | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| dokument | 1 | 16 | ✅+ | ✅1 | ⚠️ | ⚠️5 | ✅ | ❌ |
| GenetischeTests | 16 | 27 | ✅ | ✅1 | ✅ | ✅476 | ⚠️ | ❌ |
| icu | 80 | 29 | ✅ | ✅1 | ❌ | ❌ | ❌ | ❌ |
| kardiologie | 21 | 12 | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| labor | 3 | 1 | ✅ | ✅1 | ✅ | ✅188 | ❌ | ❌ |
| lungenfunktion | 2 | 4 | ✅ | ✅1 | ✅ | ✅124 | ❌ | ❌ |
| medikation | 5 | 18 | ✅ | ✅1 | ✅ | ✅326 | ❌ | ❌ |
| mikrobiologie | 13 | 25 | ✅ | ✅1 | ❌ | ❌ | ❌ | ❌ |
| mtb | 50 | 103 | ✅+ | ✅1 | ✅ | ✅784 | ✅ | ❌ |
| onkologie | 75 | 65 | ✅+ | ✅3 | ✅ | ✅338 | ✅ | ✅ |
| patho | 17 | 14 | ✅ | ✅1 | ❌ | ✅468 | ✅ | ✅ |
| proms | 20 | 13 | ✅ | ✅1 | ✅ | ⚠️ | ✅ | ❌ |
| prozedur | 1 | 3 | ✅ | ✅1 | ✅ | ✅52 | ❌ | ✅ |
| seltene | 18 | 32 | ✅ | ✅1 | ✅ | ⚠️1 | ✅ | ❌ |
| studie | 7 | 7 | ✅ | ✅1 | ❌ | ✅144 | ❌ | ❌ |

---

*Dokument erstellt: 2025-01-08*
