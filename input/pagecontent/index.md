# MII Kerndatensatz Complete

Dieses Paket ist die **Bill of Materials (BOM)** des MII Kerndatensatzes — eine kuratierte Zusammenstellung aller KDS-Module mit ihren kompatiblen Versionen. Es enthält keine eigenen Profile, sondern definiert, welche Modulversionen zusammen getestet und freigegeben wurden.

### Warum eine BOM?

Die Module des Kerndatensatzes werden von verschiedenen Teams eigenständig weiterentwickelt und versioniert. Änderungen an einem Modul können Auswirkungen auf abhängige Module haben und müssen konsistent nach unten propagiert werden. Die BOM löst drei zentrale Herausforderungen:

1. **Konsistenz**: Sie stellt sicher, dass alle Modulversionen zueinander kompatibel sind und Änderungen in Abhängigkeiten berücksichtigt wurden.
2. **Verbindlichkeit**: Standorte und Projekte können sich auf einen definierten, geprüften Versionsstand des gesamten Kerndatensatzes beziehen.
3. **Flexibilität**: Modulteams können unabhängig weiterentwickeln und neue Versionen veröffentlichen. Standorte können bei Bedarf einzelne Module in neueren Versionen nutzen — etwa für projektspezifische Anforderungen — ohne auf ein neues BOM-Release warten zu müssen.

Während das [Meta-Modul](https://github.com/medizininformatik-initiative/kerndatensatz-meta) (`de.medizininformatikinitiative.kerndatensatz.meta`) modulübergreifende Ressourcen bereitstellt, die von den einzelnen KDS-Modulen als Grundlage genutzt werden (Extensions, CodeSystems, Naming-Conventions), dient dieses Complete-Paket als gebündelter Output: Eine einzelne Abhängigkeit, die alle Module des Kerndatensatzes in ein Projekt einbindet.

> **Ballot-Stand 2027.0.0 (Stand 2026-09-02)**
>
> Diese BOM bildet den laufenden Ballot ab: Module mit einem 2027.0.0-Release sind auf dieses gepinnt (Base, Meta, Biobank, Studie, Bildgebung, Dokument, ICU, Mikrobiologie), alle übrigen auf ihre höchste stabile 2026er Version.
>
> Die Ballot-Linie ist untereinander **noch nicht kohärent**: Die 2027.0.0-Releases deklarieren teilweise weiterhin die 2026er Basismodule als Abhängigkeit — Bildgebung erwartet Base 2026.0.1 und Meta 2026.0.0, Dokument erwartet Base 2026.0.0 und Meta 2026.0.0, Biobank und Studie erwarten Meta 2026.0.0, ICU 2027.0.0 erwartet Base 2026.0.1. Lediglich Base 2027.0.0-ballot.rc1 → Meta 2027.0.0-ballot.rc3 ist in sich stimmig.
>
> Beim Auflösen können Base und Meta dadurch transitiv in zwei Versionen gezogen werden, was bei der Validierung doppelte Canonicals erzeugt. Im Abhängigkeitsgraphen unten sind diese Stellen rot gestrichelt markiert. Diese BOM ist deshalb ein **Ballot-Arbeitsstand zum Review, kein freigegebener Versionsstand**.
>
> Neu in dieser BOM sind **Kardiologie** und **Lungenfunktion** (beide 2027.0.0-ballot.rc1). Lungenfunktion deklariert dabei die Abhängigkeit `de.basiprofil.r4` — ein Tippfehler, das Paket existiert nicht und die Abhängigkeit ist nicht auflösbar. **Soziodemographie** ist angekündigt, aber in keiner Registry publiziert und daher nicht gepinnt.
>
> Repariert gegenüber dem vorigen Stand: **Biobank 2027.0.0-ballot.rc2** verweist jetzt korrekt auf Meta 2027.0.0-ballot.rc3 statt auf 2026.0.0.


## Abhängigkeitsgraph

<img src="dep-graph-2027.png" alt="MII KDS 2027 Ballot Abhängigkeitsgraph" width="100%"/>

<small>Automatisch generiert aus <code>dep-graph-2027.dot</code> via Graphviz. Knoten: grün = finale Version, gelb = Ballot/RC/Alpha, grau = in Entwicklung. Kanten: rot gestrichelt = das Modul deklariert noch die 2026er Version des Ziels, während diese BOM auf die 2027er Ballot-Linie pinnt.</small>

## Module

> Die Einteilung in Basis- und Erweiterungsmodule folgt der bisherigen Konvention des Kerndatensatzes. Diese Kategorisierung spiegelt jedoch nicht den aktuellen Reifegrad, die Verbreitung oder den Innovationscharakter der einzelnen Module wider. Wir arbeiten derzeit an einer differenzierteren Klassifikation, die den dynamischen Entwicklungen im MII-Ökosystem besser gerecht wird.

### Basismodule

| Modul | Package | Version | GitHub | Release |
|-------|---------|---------|--------|---------|
| Base (Person, Fall, Diagnose, Prozedur, Consent) | `de.medizininformatikinitiative.kerndatensatz.base` | 2027.0.0-ballot.rc1 | [kerndatensatz-basis](https://github.com/medizininformatik-initiative/kerndatensatz-basis) | [v2027.0.0-ballot.rc1](https://github.com/medizininformatik-initiative/kerndatensatz-basis/releases/tag/v2027.0.0-ballot.rc1) (2026-09-01) |
| Meta | `de.medizininformatikinitiative.kerndatensatz.meta` | 2027.0.0-ballot.rc3 | [kerndatensatz-meta](https://github.com/medizininformatik-initiative/kerndatensatz-meta) | [v2027.0.0-ballot.rc3](https://github.com/medizininformatik-initiative/kerndatensatz-meta/releases/tag/v2027.0.0-ballot.rc3) (2026-09-01) |
| Medikation | `de.medizininformatikinitiative.kerndatensatz.medikation` | 2026.0.1 | [kerndatensatzmodul-medikation](https://github.com/medizininformatik-initiative/kerndatensatzmodul-medikation) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-medikation/releases/tag/v2026.0.1) (2026-02-13) |
| Laborbefund | `de.medizininformatikinitiative.kerndatensatz.laborbefund` | 2026.0.3 | [kerndatensatzmodul-labor](https://github.com/medizininformatik-initiative/kerndatensatzmodul-labor) | [2026.0.3](https://github.com/medizininformatik-initiative/kerndatensatzmodul-labor/releases/tag/2026.0.3) (2026-06-11) |

### Erweiterungsmodule

| Modul | Package | Version | GitHub | Release |
|-------|---------|---------|--------|---------|
| Biobank | `de.medizininformatikinitiative.kerndatensatz.biobank` | 2027.0.0-ballot.rc2 | [kerndatensatzmodul-biobank](https://github.com/medizininformatik-initiative/kerndatensatzmodul-biobank) | nur als Package publiziert, letztes GitHub-Release ist rc1 (2026-08-28) |
| ICU | `de.medizininformatikinitiative.kerndatensatz.icu` | 2027.0.0 | [kerndatensatzmodul-intensivmedizin](https://github.com/medizininformatik-initiative/kerndatensatzmodul-intensivmedizin) | nur als Package publiziert, kein GitHub-Release |
| Mikrobiologie | `de.medizininformatikinitiative.kerndatensatz.mikrobiologie` | 2027.0.0-alpha.5 | [kerndatensatzmodul-mikrobiologie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-mikrobiologie) | [2027.0.0-alpha.5](https://github.com/medizininformatik-initiative/kerndatensatzmodul-mikrobiologie/releases/tag/2027.0.0-alpha.5) (2026-06-18) |
| Molekulargenetik | `de.medizininformatikinitiative.kerndatensatz.molgen` | 2026.0.4 | [kerndatensatzmodul-GenetischeTests](https://github.com/medizininformatik-initiative/kerndatensatzmodul-GenetischeTests) | [v2026.0.4](https://github.com/medizininformatik-initiative/kerndatensatzmodul-GenetischeTests/releases/tag/v2026.0.4) (2026-01-02) |
| Pathologie | `de.medizininformatikinitiative.kerndatensatz.patho` | 2026.0.2 | [kerndatensatzmodul-PathologieBefund](https://github.com/medizininformatik-initiative/kerndatensatzmodul-PathologieBefund) | nur als Package publiziert, kein GitHub-Release |
| Studie | `de.medizininformatikinitiative.kerndatensatz.studie` | 2027.0.0-ballot.rc1 | [kerndatensatzmodul-studie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-studie) | [v2027.0.0-ballot.rc1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-studie/releases/tag/v2027.0.0-ballot.rc1) (2026-08-31) |
| Bildgebung | `de.medizininformatikinitiative.kerndatensatz.bildgebung` | 2027.0.0-ballot.rc2 | [kerndatensatz-bildgebung](https://github.com/medizininformatik-initiative/kerndatensatz-bildgebung) | [2027.0.0-ballot.rc2](https://github.com/medizininformatik-initiative/kerndatensatz-bildgebung/releases/tag/2027.0.0-ballot.rc2) (2026-08-31) |
| Dokument | `de.medizininformatikinitiative.kerndatensatz.dokument` | 2027.0.0-ballot.rc1 | [kerndatensatz-dokument](https://github.com/medizininformatik-initiative/kerndatensatz-dokument) | [v2027.0.0-ballot.rc1](https://github.com/medizininformatik-initiative/kerndatensatz-dokument/releases/tag/v2027.0.0-ballot.rc1) (2026-08-28) |
| Onkologie | `de.medizininformatikinitiative.kerndatensatz.onkologie` | 2026.0.3 | [kerndatensatzmodul-onkologie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-onkologie) | [v2026.0.3](https://github.com/medizininformatik-initiative/kerndatensatzmodul-onkologie/releases/tag/v2026.0.3) (2026-03-29) |
| Seltene Erkrankungen | `de.medizininformatikinitiative.kerndatensatz.seltene` | 2026.0.1 | [kerndatensatzmodul-seltene-erkrankungen](https://github.com/medizininformatik-initiative/kerndatensatzmodul-seltene-erkrankungen) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-seltene-erkrankungen/releases/tag/v2026.0.1) |
| Molekulares Tumorboard | `de.medizininformatikinitiative.kerndatensatz.mtb` | 2026.0.1 | [kerndatensatzmodul-molekulares-tumorboard](https://github.com/medizininformatik-initiative/kerndatensatzmodul-molekulares-tumorboard) | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-molekulares-tumorboard/releases/tag/v2026.0.1) (2026-03-30) |
| PROs | `de.medizininformatikinitiative.kerndatensatz.pros` | 2026.7.0 | [kerndatensatzmodul-proms](https://github.com/medizininformatik-initiative/kerndatensatzmodul-proms) | [v2026.7.0](https://github.com/medizininformatik-initiative/kerndatensatzmodul-proms/releases/tag/v2026.7.0) |
| Consent | `de.medizininformatikinitiative.kerndatensatz.consent` | 2026.0.1-rc-4 | [kerndatensatzmodul-consent](https://github.com/medizininformatik-initiative/kerndatensatzmodul-consent) | nur als Package publiziert, kein GitHub-Release |
| Kardiologie | `de.medizininformatikinitiative.kerndatensatz.kardiologie` | 2027.0.0-ballot.rc1 | [kerndatensatz-kardiologie](https://github.com/medizininformatik-initiative/kerndatensatz-kardiologie) | [v2027.0.0-ballot.rc1](https://github.com/medizininformatik-initiative/kerndatensatz-kardiologie/releases/tag/v2027.0.0-ballot.rc1) (2026-08-31) |
| Lungenfunktion | `de.medizininformatikinitiative.kerndatensatz.lungenfunktion` | 2027.0.0-ballot.rc1 | [kerndatensatz-lungenfunktion](https://github.com/medizininformatik-initiative/kerndatensatz-lungenfunktion) | nur als Package publiziert, kein GitHub-Release |

### Angekündigt, noch nicht publiziert

| Modul | Package | Version | GitHub | Status |
|-------|---------|---------|--------|--------|
| Soziodemographie | `de.medizininformatikinitiative.kerndatensatz.soziodemographie` | 2027.0.0-ballot.rc1 (im Repo) | [kerndatensatz-soziodemographie](https://github.com/medizininformatik-initiative/kerndatensatz-soziodemographie) | **in keiner Registry publiziert** |

Das Repo deklariert `packageId: de.medizininformatikinitiative.kerndatensatz.soziodemographie` in Version 2027.0.0-ballot.rc1 (`releaseLabel: ci-build`, `status: draft`), das Package ist aber weder auf packages.simplifier.net noch auf packages.fhir.org verfügbar — in keiner Version. Es gibt auch keine GitHub-Releases oder Tags.

Das Modul ist deshalb **nicht** in `package.json` und `sushi-config.yaml` gepinnt: eine nicht auflösbare Abhängigkeit würde jeden Konsumenten dieser BOM brechen. Sobald das Package publiziert ist, wird es nachgezogen.

### Externe Abhängigkeiten

Die BOM pinnt nicht nur die MII-Module, sondern auch die externen Pakete, gegen die sie gebaut sind. Gepinnt wird jeweils **die höchste Version, die ein MII-Modul transitiv tatsächlich anfordert** — nicht die neueste verfügbare. Eine Version, gegen die kein Modul gebaut wurde, gehört nicht in eine BOM.

Pakete ohne Pin werden weiterhin transitiv aufgelöst; ihre Version ergibt sich aus dem anfordernden Modul.

#### In der BOM gepinnt

| Paket | Version | Angefordert von | Anmerkung |
|-------|---------|-----------------|-----------|
| Deutsche Basisprofile R4 (`de.basisprofil.r4`) | 1.6.0 | Base, Biobank, ICU, Bildgebung, Dokument, Kardiologie | ältere Module fordern noch 1.5.x; Lungenfunktion fordert das nicht existierende `de.basiprofil.r4` |
| HL7 Terminology (`hl7.terminology.r4`) | 7.3.0 | ICU 2027.0.0 | Module uneinig: 5.0.0 / 6.1.0 / 6.5.0 / 7.1.0 / 7.2.0 / 7.3.0 |
| HL7 Extensions R4 (`hl7.fhir.uv.extensions.r4`) | 5.3.0 | Base 2026.0.1, CRMI 2.0.0 | Module uneinig: 5.1.0 / 5.2.0 / 5.3.0 |
| HL7 Clinical Genomics (`hl7.fhir.uv.genomics-reporting`) | 3.0.0 | Molekulargenetik, MTB | einheitlich |
| HL7 Europe Base (`hl7.fhir.eu.base`) | 2.0.0 | EU Laboratory (transitiv über Biobank) | einheitlich |
| HL7 Europe Laboratory (`hl7.fhir.eu.laboratory`) | 2.0.0 | Biobank 2027.0.0-ballot.rc1 | einheitlich |
| HL7 Europe Extensions R4 (`hl7.fhir.eu.extensions.r4`) | 1.3.0 | EU Base, EU Laboratory | einheitlich |
| MIABIS (`eu.miabis.r4`) | 0.2.0 | Biobank | **aktuell wäre 1.3.0** — Biobank hängt eine Major-Version zurück |
| ISiK (`de.gematik.isik`) | 6.0.0 | ICU 2027.0.0, Dokument 2027.0.0-ballot.rc1, Kardiologie | Pathologie fordert 5.1.0, PROs 5.1.1 |

#### Nur transitiv aufgelöst

| Paket | Version | Angefordert von |
|-------|---------|-----------------|
| Einwilligungsmanagement (`de.einwilligungsmanagement`) | 2.0.3 | Consent |
| Deutsche Medikation (`de.fhir.medication`) | 1.0.x | Medikation |
| IHE-D Terminologie (`de.ihe-d.terminology`) | 3.0.1 | Medikation, Dokument |
| gematik Terminologie (`de.gematik.terminology`) | 1.0.6 – 1.0.9 | ISiK (transitiv) |
| DVMD KDL (`dvmd.kdl.r4`) | 2025.0.1 (Dokument), 2026.0.0 (ICU) | Dokument, ICU |
| DICOM (`fhir.dicom`) | 2025.3.20250714 | Bildgebung |
| IHE FormatCode (`ihe.formatcode.fhir`) | 1.4.0 | Dokument |
| HL7 International Patient Summary (`hl7.fhir.uv.ips`) | 2.0.0 | Medikation, Laborbefund |
| HL7 Structured Data Capture (`hl7.fhir.uv.sdc`) | 3.0.0 (PROs), 4.0.0 (ISiK 6.0.0) | PROs, ISiK |
| HL7 mCODE (`hl7.fhir.us.mcode`) | 2.1.x | Pathologie |
| HL7 CRMI (`hl7.fhir.uv.crmi`) | 2.0.0 | Base, Meta |
| HL7 Cross-Version R5 (`hl7.fhir.uv.xver-r5.r4`) | 0.1.0 | Base, EU Laboratory, ISiK |

#### Graph der externen Abhängigkeiten

<img src="dep-graph-2027-extern.png" alt="Externe Abhängigkeiten der MII KDS Module" width="100%"/>

<small>Automatisch generiert aus <code>dep-graph-2027-extern.dot</code> via Graphviz. Durchgezogene Kästen = in der BOM gepinnt, gestrichelt = nur transitiv aufgelöst. Rote Kantenbeschriftung = das Modul fordert eine andere Version an als die BOM pinnt.</small>

## Installation

### Über die FHIR Package Registry (empfohlen)

Sobald das Paket auf packages.fhir.org verfügbar ist, genügt eine einzelne Abhängigkeit in der `sushi-config.yaml`:

```yaml
dependencies:
  de.medizininformatikinitiative.kerndatensatz.complete: 2027.0.0-ballot.1
```

Alle 19 Modul-Dependencies und die 8 gepinnten externen Pakete werden automatisch von der FHIR Package Registry aufgelöst und heruntergeladen.

### Manuelle Installation

Solange das Paket noch nicht auf packages.fhir.org verfügbar ist, kann es vom [GitHub Release](https://github.com/medizininformatik-initiative/kerndatensatz-complete/releases/tag/v2027.0.0-ballot.1) heruntergeladen und lokal installiert werden:

```bash
# Package herunterladen
curl -LO https://github.com/medizininformatik-initiative/kerndatensatz-complete/releases/download/v2027.0.0-ballot.1/de.medizininformatikinitiative.kerndatensatz.complete-2027.0.0-ballot.1.tgz

# In den lokalen FHIR-Cache installieren
fhir install de.medizininformatikinitiative.kerndatensatz.complete-2027.0.0-ballot.1.tgz
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
