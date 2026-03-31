# MII Kerndatensatz Complete (2025)

Dieses Paket ist die **Bill of Materials (BOM)** des MII Kerndatensatzes für die **letzte stabile 2025er Generation** — eine retrospektive, kuratierte Zusammenstellung aller KDS-Module mit ihren letzten kompatiblen 2025er Versionen. Es enthält keine eigenen Profile, sondern definiert, welche Modulversionen zusammen den stabilen Stand vor der 2026er Release-Welle bilden.

### Warum eine BOM?

Die Module des Kerndatensatzes werden von verschiedenen Teams eigenständig weiterentwickelt und versioniert. Änderungen an einem Modul können Auswirkungen auf abhängige Module haben und müssen konsistent nach unten propagiert werden. Die BOM löst drei zentrale Herausforderungen:

1. **Konsistenz**: Sie stellt sicher, dass alle Modulversionen zueinander kompatibel sind und Änderungen in Abhängigkeiten berücksichtigt wurden.
2. **Verbindlichkeit**: Standorte und Projekte können sich auf einen definierten, geprüften Versionsstand des gesamten Kerndatensatzes beziehen.
3. **Flexibilität**: Modulteams können unabhängig weiterentwickeln und neue Versionen veröffentlichen. Standorte können bei Bedarf einzelne Module in neueren Versionen nutzen — etwa für projektspezifische Anforderungen — ohne auf ein neues BOM-Release warten zu müssen.

## Module

> **Hinweis:** In der 2025er Generation gab es noch kein `base`-Package — die Basismodule Person, Fall, Diagnose und Prozedur wurden als eigenständige Packages publiziert. Erst ab 2026.0.0 wurden sie im `base`-Package zusammengeführt.

### Basismodule

| Modul | Package | Version |
|-------|---------|---------|
| Person | `de.medizininformatikinitiative.kerndatensatz.person` | 2025.0.1 |
| Fall | `de.medizininformatikinitiative.kerndatensatz.fall` | 2025.0.1 |
| Diagnose | `de.medizininformatikinitiative.kerndatensatz.diagnose` | 2025.0.1 |
| Prozedur | `de.medizininformatikinitiative.kerndatensatz.prozedur` | 2025.0.1 |
| Meta | `de.medizininformatikinitiative.kerndatensatz.meta` | 2025.0.3 |
| Medikation | `de.medizininformatikinitiative.kerndatensatz.medikation` | 2025.0.1 |
| Laborbefund | `de.medizininformatikinitiative.kerndatensatz.laborbefund` | 2025.0.2 |

### Erweiterungsmodule

| Modul | Package | Version |
|-------|---------|---------|
| Biobank | `de.medizininformatikinitiative.kerndatensatz.biobank` | 2025.0.4 |
| Consent | `de.medizininformatikinitiative.kerndatensatz.consent` | 2025.0.4 |
| ICU | `de.medizininformatikinitiative.kerndatensatz.icu` | 2025.0.4 |
| Mikrobiologie | `de.medizininformatikinitiative.kerndatensatz.mikrobiologie` | 2025.0.1 |
| Molekulargenetik | `de.medizininformatikinitiative.kerndatensatz.molgen` | 2025.0.0 |
| Pathologie | `de.medizininformatikinitiative.kerndatensatz.patho` | 2025.0.2 |
| Studie | `de.medizininformatikinitiative.kerndatensatz.studie` | 2025.0.0 |
| Bildgebung | `de.medizininformatikinitiative.kerndatensatz.bildgebung` | 2025.0.2 |
| Onkologie | `de.medizininformatikinitiative.kerndatensatz.onkologie` | 2025.1.0 |

### Nicht in dieser Generation enthalten

Die folgenden Module wurden erst ab der 2026er Generation als stable Release publiziert:

| Modul | Erster stable Release |
|-------|-----------------------|
| Base (konsolidiertes Package) | 2026.0.0 |
| Dokument | 2026.0.1 |
| Seltene Erkrankungen | 2026.0.1 |
| PROs | 2026.2.0 |
| Molekulares Tumorboard | 2026.0.1 (2025 nur ballot-alpha) |

### Nationale Abhängigkeiten

| Paket | Version | Verwendet von |
|-------|---------|---------------|
| Deutsche Basisprofile R4 (`de.basisprofil.r4`) | 1.5.x | Person, Fall, Diagnose, Prozedur, Medikation, Biobank, ICU, Molgen, Onkologie |
| Einwilligungsmanagement (`de.einwilligungsmanagement`) | 2.0.0 | Consent (transitiv) |
| ISiK Vitalparameter (`de.gematik.isik-vitalparameter`) | 4.0.0 | ICU |
| ISiK Basismodul (`de.gematik.isik-basismodul`) | 4.0.0 | Pathologie |
| IHE-D Terminologie (`de.ihe-d.terminology`) | 3.0.1 | Medikation |
| KBV Schlüsseltabellen (`kbv.all.st`) | 1.27.0 | Diagnose, Prozedur |

### Internationale Abhängigkeiten

| Paket | Version | Verwendet von |
|-------|---------|---------------|
| HL7 International Patient Summary (`hl7.fhir.uv.ips`) | 1.1.x | Medikation, Laborbefund |
| HL7 Genomics Reporting (`hl7.fhir.uv.genomics-reporting`) | 2.0.0 | Molekulargenetik |
| HL7 mCODE (`hl7.fhir.us.mcode`) | 2.1.0 | Pathologie |
| DICOM (`fhir.dicom`) | 2024.2.20240331 | Bildgebung |

## Bekannte Einschränkungen

<div class="stu-note">
<p><b>Fehlende Snapshots in der FHIR Package Registry</b></p>
<p>Die folgenden 2025er Packages enthalten auf der FHIR Package Registry <b>keine Snapshots</b> in ihren StructureDefinitions. Downstream-Consumer, die Snapshots für Validierung oder Profilauswertung benötigen, müssen diese selbst generieren (z.B. mit dem HL7 FHIR Validator oder Firely SDK):</p>
<ul>
  <li><code>de.medizininformatikinitiative.kerndatensatz.consent</code> (2025.0.4)</li>
  <li><code>de.medizininformatikinitiative.kerndatensatz.icu</code> (2025.0.4)</li>
  <li><code>de.medizininformatikinitiative.kerndatensatz.studie</code> (2025.0.0)</li>
  <li><code>de.medizininformatikinitiative.kerndatensatz.mikrobiologie</code> (2025.0.1) — teilweise</li>
</ul>
<p>Dies ist ein bekanntes Problem der 2025er Publikationsinfrastruktur und wurde in der 2026er Generation behoben.</p>
</div>

## Installation

### Über die FHIR Package Registry (empfohlen)

Sobald das Paket auf packages.fhir.org verfügbar ist, genügt eine einzelne Abhängigkeit in der `sushi-config.yaml`:

```yaml
dependencies:
  de.medizininformatikinitiative.kerndatensatz.complete: 2025.0.0
```

Alle 16 Modul-Dependencies werden automatisch von der FHIR Package Registry aufgelöst und heruntergeladen.

### Manuelle Installation

Solange das Paket noch nicht auf packages.fhir.org verfügbar ist, kann es vom [GitHub Release](https://github.com/medizininformatik-initiative/kerndatensatz-complete/releases/tag/v2025.0.0) heruntergeladen und lokal installiert werden:

```bash
# Package herunterladen
curl -LO https://github.com/medizininformatik-initiative/kerndatensatz-complete/releases/download/v2025.0.0/de.medizininformatikinitiative.kerndatensatz.complete-2025.0.0.tgz

# In den lokalen FHIR-Cache installieren
fhir install de.medizininformatikinitiative.kerndatensatz.complete-2025.0.0.tgz
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
