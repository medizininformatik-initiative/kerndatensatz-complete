# MII Kerndatensatz Complete

Dieses Paket ist die **Bill of Materials (BOM)** des MII Kerndatensatzes — eine kuratierte Zusammenstellung aller KDS-Module mit ihren kompatiblen Versionen. Es enthält keine eigenen Profile, sondern definiert, welche Modulversionen zusammen getestet und freigegeben wurden.

### Warum eine BOM?

Die Module des Kerndatensatzes werden von verschiedenen Teams eigenständig weiterentwickelt und versioniert. Änderungen an einem Modul können Auswirkungen auf abhängige Module haben und müssen konsistent nach unten propagiert werden. Die BOM löst drei zentrale Herausforderungen:

1. **Konsistenz**: Sie stellt sicher, dass alle Modulversionen zueinander kompatibel sind und Änderungen in Abhängigkeiten berücksichtigt wurden.
2. **Verbindlichkeit**: Standorte und Projekte können sich auf einen definierten, geprüften Versionsstand des gesamten Kerndatensatzes beziehen.
3. **Flexibilität**: Modulteams können unabhängig weiterentwickeln und neue Versionen veröffentlichen. Standorte können bei Bedarf einzelne Module in neueren Versionen nutzen — etwa für projektspezifische Anforderungen — ohne auf ein neues BOM-Release warten zu müssen.

Während das [Meta-Modul](https://github.com/medizininformatik-initiative/kerndatensatz-meta) (`de.medizininformatikinitiative.kerndatensatz.meta`) modulübergreifende Ressourcen bereitstellt, die von den einzelnen KDS-Modulen als Grundlage genutzt werden (Extensions, CodeSystems, Naming-Conventions), dient dieses Complete-Paket als gebündelter Output: Eine einzelne Abhängigkeit, die alle Module des Kerndatensatzes in ein Projekt einbindet.

## Abhängigkeitsgraph

<img src="dep-graph-2026.png" alt="MII KDS 2026 Abhängigkeitsgraph" width="100%"/>

## Module

> Die Einteilung in Basis- und Erweiterungsmodule folgt der bisherigen Konvention des Kerndatensatzes. Diese Kategorisierung spiegelt jedoch nicht den aktuellen Reifegrad, die Verbreitung oder den Innovationscharakter der einzelnen Module wider. Wir arbeiten derzeit an einer differenzierteren Klassifikation, die den dynamischen Entwicklungen im MII-Ökosystem besser gerecht wird.

### Basismodule

| Modul | Package | Version | GitHub | Release |
|-------|---------|---------|--------|---------|
| Base (Person, Fall, Diagnose, Prozedur, Consent) | `de.medizininformatikinitiative.kerndatensatz.base` | 2026.0.0 | [kerndatensatz-basis](https://github.com/medizininformatik-initiative/kerndatensatz-basis) | [v2026.0.0](https://github.com/medizininformatik-initiative/kerndatensatz-basis/releases/tag/v2026.0.0) (2025-12-13) |
| Meta | `de.medizininformatikinitiative.kerndatensatz.meta` | 2026.0.0 | [kerndatensatz-meta](https://github.com/medizininformatik-initiative/kerndatensatz-meta) | [v2026.0.0](https://github.com/medizininformatik-initiative/kerndatensatz-meta/releases/tag/v2026.0.0) (2025-11-24) |
| Medikation | `de.medizininformatikinitiative.kerndatensatz.medikation` | 2026.0.1 | [kerndatensatzmodul-medikation](https://github.com/medizininformatik-initiative/kerndatensatzmodul-medikation) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-medikation/releases/tag/v2026.0.1) (2026-02-13) |
| Laborbefund | `de.medizininformatikinitiative.kerndatensatz.laborbefund` | 2026.0.1 | [kerndatensatzmodul-labor](https://github.com/medizininformatik-initiative/kerndatensatzmodul-labor) | [2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-labor/releases/tag/2026.0.1) |

### Erweiterungsmodule

| Modul | Package | Version | GitHub | Release |
|-------|---------|---------|--------|---------|
| Biobank | `de.medizininformatikinitiative.kerndatensatz.biobank` | 2026.0.1 | [kerndatensatzmodul-biobank](https://github.com/medizininformatik-initiative/kerndatensatzmodul-biobank) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-biobank/releases/tag/v2026.0.1) (2026-02-11) |
| ICU | `de.medizininformatikinitiative.kerndatensatz.icu` | 2026.0.2 | [kerndatensatzmodul-intensivmedizin](https://github.com/medizininformatik-initiative/kerndatensatzmodul-intensivmedizin) | [v2026.0.2](https://github.com/medizininformatik-initiative/kerndatensatzmodul-intensivmedizin/releases/tag/v2026.0.2) (2026-03-18) |
| Mikrobiologie | `de.medizininformatikinitiative.kerndatensatz.mikrobiologie` | 2025.0.1 | [kerndatensatzmodul-mikrobiologie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-mikrobiologie) | - |
| Molekulargenetik | `de.medizininformatikinitiative.kerndatensatz.molgen` | 2026.0.4 | [kerndatensatzmodul-GenetischeTests](https://github.com/medizininformatik-initiative/kerndatensatzmodul-GenetischeTests) | [v2026.0.4](https://github.com/medizininformatik-initiative/kerndatensatzmodul-GenetischeTests/releases/tag/v2026.0.4) (2026-01-02) |
| Pathologie | `de.medizininformatikinitiative.kerndatensatz.patho` | 2026.0.1 | [kerndatensatzmodul-PathologieBefund](https://github.com/medizininformatik-initiative/kerndatensatzmodul-PathologieBefund) | - |
| Studie | `de.medizininformatikinitiative.kerndatensatz.studie` | 2026.0.2 | [kerndatensatzmodul-studie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-studie) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-studie/releases/tag/v2026.0.1) (2026-01-09) |
| Bildgebung | `de.medizininformatikinitiative.kerndatensatz.bildgebung` | 2026.0.0 | [kerndatensatz-bildgebung](https://github.com/medizininformatik-initiative/kerndatensatz-bildgebung) | [v2026.0.0](https://github.com/medizininformatik-initiative/kerndatensatz-bildgebung/releases/tag/v2026.0.0) (2025-12-19) |
| Dokument | `de.medizininformatikinitiative.kerndatensatz.dokument` | 2026.0.1 | [kerndatensatz-dokument](https://github.com/medizininformatik-initiative/kerndatensatz-dokument) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatz-dokument/releases/tag/v2026.0.1) |
| Onkologie | `de.medizininformatikinitiative.kerndatensatz.onkologie` | 2026.0.3 | [kerndatensatzmodul-onkologie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-onkologie) | [v2026.0.3](https://github.com/medizininformatik-initiative/kerndatensatzmodul-onkologie/releases/tag/v2026.0.3) (2026-03-29) |
| Seltene Erkrankungen | `de.medizininformatikinitiative.kerndatensatz.seltene` | 2026.0.1 | [kerndatensatzmodul-seltene-erkrankungen](https://github.com/medizininformatik-initiative/kerndatensatzmodul-seltene-erkrankungen) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-seltene-erkrankungen/releases/tag/v2026.0.1) |
| Molekulares Tumorboard | `de.medizininformatikinitiative.kerndatensatz.mtb` | 2026.0.1 | [kerndatensatzmodul-molekulares-tumorboard](https://github.com/medizininformatik-initiative/kerndatensatzmodul-molekulares-tumorboard) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-molekulares-tumorboard/releases/tag/v2026.0.1) (2026-03-30) |
| PROs | `de.medizininformatikinitiative.kerndatensatz.pros` | 2026.2.0 | [kerndatensatzmodul-proms](https://github.com/medizininformatik-initiative/kerndatensatzmodul-proms) | [v2026.2.0](https://github.com/medizininformatik-initiative/kerndatensatzmodul-proms/releases/tag/v2026.2.0) |
| Consent | `de.medizininformatikinitiative.kerndatensatz.consent` | 2026.0.0 | [kerndatensatzmodul-consent](https://github.com/medizininformatik-initiative/kerndatensatzmodul-consent) | [v2026.0.0](https://github.com/medizininformatik-initiative/kerndatensatzmodul-consent/releases/tag/2026.0.0) |

### Nationale Abhängigkeiten

| Paket | Version | Verwendet von |
|-------|---------|---------------|
| Deutsche Basisprofile R4 (`de.basisprofil.r4`) | 1.5.4 | Base, Medikation, Biobank, ICU, Molgen, Onkologie, Seltene, MTB |
| Einwilligungsmanagement (`de.einwilligungsmanagement`) | 1.0.2 | Consent |
| ISiK (`de.gematik.isik`) | 5.0.0 - 5.1.0 | ICU, Pathologie, PROs |
| IHE-D Terminologie (`de.ihe-d.terminology`) | 3.0.1 | Medikation, Dokument |
| Deutsche Medikation (`de.fhir.medication`) | 1.0.x | Medikation |
| DVMD KDL (`dvmd.kdl.r4`) | 2025.0.1 | Dokument |

### Internationale Abhängigkeiten

| Paket | Version | Verwendet von |
|-------|---------|---------------|
| HL7 International Patient Summary (`hl7.fhir.uv.ips`) | 2.0.0 | Medikation, Laborbefund |
| HL7 Genomics Reporting (`hl7.fhir.uv.genomics-reporting`) | 3.0.x | Molekulargenetik, MTB |
| HL7 Structured Data Capture (`hl7.fhir.uv.sdc`) | 3.0.0 | PROs |
| HL7 mCODE (`hl7.fhir.us.mcode`) | 2.1.x | Pathologie |
| MIABIS (`eu.miabis.r4`) | 0.2.0 | Biobank |
| DICOM (`fhir.dicom`) | 2025.3.20250714 | Bildgebung |
| IHE FormatCode (`ihe.formatcode.fhir`) | 1.4.0 | Dokument |

## Installation

### Über die FHIR Package Registry (empfohlen)

Sobald das Paket auf packages.fhir.org verfügbar ist, genügt eine einzelne Abhängigkeit in der `sushi-config.yaml`:

```yaml
dependencies:
  de.medizininformatikinitiative.kerndatensatz.complete: 2026.0.1-rc.1
```

Alle 19 Modul-Dependencies werden automatisch von der FHIR Package Registry aufgelöst und heruntergeladen.

### Manuelle Installation

Solange das Paket noch nicht auf packages.fhir.org verfügbar ist, kann es vom [GitHub Release](https://github.com/medizininformatik-initiative/kerndatensatz-complete/releases/tag/v2026.0.1-rc.1) heruntergeladen und lokal installiert werden:

```bash
# Package herunterladen
curl -LO https://github.com/medizininformatik-initiative/kerndatensatz-complete/releases/download/v2026.0.1-rc.1/de.medizininformatikinitiative.kerndatensatz.complete-2026.0.1-rc.1.tgz

# In den lokalen FHIR-Cache installieren
fhir install de.medizininformatikinitiative.kerndatensatz.complete-2026.0.1-rc.1.tgz
```

Danach kann das Paket wie gewohnt als Dependency referenziert werden. Alle weiteren Module werden automatisch von packages.fhir.org aufgelöst.

> **Hinweis:** Der `fhir`-Befehl stammt aus dem [Firely Terminal (Simplifier CLI)](https://simplifier.net/downloads/firely-terminal). Im Zweifel Version 3.4.0 verwenden — neuere Versionen sind nicht getestet.
>
> ```bash
> dotnet tool install -g Firely.Terminal --version 3.4.0
> ```

## Weitere Informationen

- [Alle KDS-Repositories auf GitHub](https://github.com/orgs/medizininformatik-initiative/repositories?q=kerndatensatzmodul)
- [Übersicht über Versionen der KDS-Module](https://github.com/medizininformatik-initiative/kerndatensatz-meta/wiki/%C3%9Cbersicht-%C3%BCber-Versionen-der-Kerndatensatz%E2%80%90Module)
- [MII Kerndatensatz Meta Wiki](https://github.com/medizininformatik-initiative/kerndatensatz-meta/wiki)
- [MII Kerndatensatz auf Art-Decor](https://art-decor.org/art-decor/decor-project--mide-)
- [MII GitHub Organisation](https://github.com/medizininformatik-initiative)
- [MII FHIR Packages auf Simplifier](https://simplifier.net/organization/koordinationsstellemii/~packages)
