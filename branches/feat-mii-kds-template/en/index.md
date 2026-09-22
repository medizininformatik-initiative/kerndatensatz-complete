# Home - MII Kerndatensatz Complete v2027.0.0-ballot.19

* [**Table of Contents**](toc.md)
* **Home**

## Home

| | |
| :--- | :--- |
| *Official URL*:https://www.medizininformatik-initiative.de/fhir/core/complete/ImplementationGuide/de.medizininformatikinitiative.kerndatensatz.complete | *Version*:2027.0.0-ballot.19 |
| Active as of 2026-09-22 | *Computable Name*:MIIKerndatensatzComplete |

# MII Kerndatensatz Complete

Dieses Paket ist die **Bill of Materials (BOM)** des MII Kerndatensatzes — eine kuratierte Zusammenstellung aller KDS-Module mit ihren kompatiblen Versionen. Es enthält keine eigenen Profile, sondern definiert, welche Modulversionen zusammen getestet und freigegeben wurden.

### Warum eine BOM?

Die Module des Kerndatensatzes werden von verschiedenen Teams eigenständig weiterentwickelt und versioniert. Änderungen an einem Modul können Auswirkungen auf abhängige Module haben und müssen konsistent nach unten propagiert werden. Die BOM löst drei zentrale Herausforderungen:

1. **Konsistenz**: Sie stellt sicher, dass alle Modulversionen zueinander kompatibel sind und Änderungen in Abhängigkeiten berücksichtigt wurden.
1. **Verbindlichkeit**: Standorte und Projekte können sich auf einen definierten, geprüften Versionsstand des gesamten Kerndatensatzes beziehen.
1. **Flexibilität**: Modulteams können unabhängig weiterentwickeln und neue Versionen veröffentlichen. Standorte können bei Bedarf einzelne Module in neueren Versionen nutzen — etwa für projektspezifische Anforderungen — ohne auf ein neues BOM-Release warten zu müssen.

Während das [Meta-Modul](https://github.com/medizininformatik-initiative/kerndatensatz-meta) (`de.medizininformatikinitiative.kerndatensatz.meta`) modulübergreifende Ressourcen bereitstellt, die von den einzelnen KDS-Modulen als Grundlage genutzt werden (Extensions, CodeSystems, Naming-Conventions), dient dieses Complete-Paket als gebündelter Output: Eine einzelne Abhängigkeit, die alle Module des Kerndatensatzes in ein Projekt einbindet.

> **Ballot-Stand 2027.0.0 (Stand 2026-09-21)**Alle 21 Module sind auf die 2027er Ballot-Linie gepinnt. Die **aktuellen Fassungen** heißen `2027.0.0-ballot`, `…-ballot.1`, `…-ballot.2`, `…-ballot.3` bzw. `…-ballot2` (Mikrobiologie) — die früheren Release-Kandidaten (`…-ballot.rcN`) sind durchgehend abgelöst. Welche Version je Modul gepinnt ist, zeigt die [Gesamtübersicht](#gesamtübersicht).Mit **ICU `2027.0.0-ballot.3`** (publiziert 2026-09-17) ist die Ballot-Linie untereinander **kohärent**: Alle Module deklarieren Base und Meta der 2027er Linie, doppelte Canonicals beim transitiven Auflösen treten nicht mehr auf. Diese BOM bleibt dennoch ein **Ballot-Arbeitsstand zum Review, kein freigegebener Versionsstand**.Den Weg dorthin — die rc-Zwischenstände und die schrittweise aufgelösten 2026er-Kanten — dokumentiert die Git-Historie dieser Seite.

## Gesamtübersicht

Alle Module dieser BOM auf einen Blick — die gepinnte Ballot-Version, das Package auf Simplifier und der aktuelle IG-Build. Details (GitHub-Repos, QA-Fehlerzahlen, Releases) stehen in den [Modultabellen](#module) weiter unten.

| | | | |
| :--- | :--- | :--- | :--- |
| Base | [`…kerndatensatz.base`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.base) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatz-basis/) |
| Meta | [`…kerndatensatz.meta`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.meta) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatz-meta/) |
| Medikation | [`…kerndatensatz.medikation`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.medikation) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-medikation/) |
| Laborbefund | [`…kerndatensatz.laborbefund`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.laborbefund) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-labor/) |
| Biobank | [`…kerndatensatz.biobank`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.biobank) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-biobank/branches/release/v2027.0.0-ballot/) |
| ICU | [`…kerndatensatz.icu`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.icu) | 2027.0.0-ballot.3 | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-intensivmedizin/) |
| Mikrobiologie | [`…kerndatensatz.mikrobiologie`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.mikrobiologie) | 2027.0.0-ballot2 | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-mikrobiologie/) |
| Molekulargenetik | [`…kerndatensatz.molgen`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.molgen) | 2027.0.0-ballot.1 | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-GenetischeTests/) |
| Pathologie | [`…kerndatensatz.patho`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.patho) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-PathologieBefund/branches/dev/v2027/) |
| Studie | [`…kerndatensatz.studie`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.studie) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-studie/) |
| Bildgebung | [`…kerndatensatz.bildgebung`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.bildgebung) | 2027.0.0-ballot.1 | [IG](https://medizininformatik-initiative.github.io/kerndatensatz-bildgebung/) |
| Dokument | [`…kerndatensatz.dokument`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.dokument) | 2027.0.0-ballot.2 | [IG](https://medizininformatik-initiative.github.io/kerndatensatz-dokument/) |
| Onkologie | [`…kerndatensatz.onkologie`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.onkologie) | 2027.0.0-ballot.1 | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-onkologie/) |
| Seltene Erkrankungen | [`…kerndatensatz.seltene`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.seltene) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-seltene-erkrankungen/) |
| Molekulares Tumorboard | [`…kerndatensatz.mtb`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.mtb) | 2027.0.0-ballot.1 | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-molekulares-tumorboard/) |
| PROs | [`…kerndatensatz.pros`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.pros) | 2027.0.0-ballot.1 | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-proms/) |
| Consent | [`…kerndatensatz.consent`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.consent) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-consent/) |
| Kardiologie | [`…kerndatensatz.kardiologie`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.kardiologie) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatz-kardiologie/branches/release/v2027.0.0-ballot/) |
| Lungenfunktion | [`…kerndatensatz.lungenfunktion`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.lungenfunktion) | 2027.0.0-ballot.1 | [IG](https://medizininformatik-initiative.github.io/kerndatensatz-lungenfunktion/) |
| Symptome | [`…kerndatensatz.symptom`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.symptom) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatzmodul-symptome/) |
| Soziodemographie | [`…kerndatensatz.soziodemographie`](https://simplifier.net/packages/de.medizininformatikinitiative.kerndatensatz.soziodemographie) | 2027.0.0-ballot | [IG](https://medizininformatik-initiative.github.io/kerndatensatz-soziodemographie/) |

## Abhängigkeitsgraph

![](dep-graph-2027.png)

Automatisch generiert aus `dep-graph-2027.dot` via Graphviz. Knoten: grün = finale Version, gelb = Ballot/RC/Alpha, grau = in Entwicklung. Kanten: rot gestrichelt = das Modul deklariert noch die 2026er Version des Ziels, während diese BOM auf die 2027er Ballot-Linie pinnt.

## Module

> Die Einteilung in Basis- und Erweiterungsmodule folgt der bisherigen Konvention des Kerndatensatzes. Diese Kategorisierung spiegelt jedoch nicht den aktuellen Reifegrad, die Verbreitung oder den Innovationscharakter der einzelnen Module wider. Wir arbeiten derzeit an einer differenzierteren Klassifikation, die den dynamischen Entwicklungen im MII-Ökosystem besser gerecht wird.

### Basismodule

| | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Base (Person, Fall, Diagnose, Prozedur, Consent) | `de.medizininformatikinitiative.kerndatensatz.base` | 2027.0.0-ballot | [kerndatensatz-basis](https://github.com/medizininformatik-initiative/kerndatensatz-basis) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatz-basis/)· 22 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatz-basis/releases/tag/v2027.0.0-ballot)(2026-09-10) |
| Meta | `de.medizininformatikinitiative.kerndatensatz.meta` | 2027.0.0-ballot | [kerndatensatz-meta](https://github.com/medizininformatik-initiative/kerndatensatz-meta) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatz-meta/)· 0 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatz-meta/releases/tag/v2027.0.0-ballot)(2026-09-10) |
| Medikation | `de.medizininformatikinitiative.kerndatensatz.medikation` | 2027.0.0-ballot | [kerndatensatzmodul-medikation](https://github.com/medizininformatik-initiative/kerndatensatzmodul-medikation) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatzmodul-medikation/)· 1 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatzmodul-medikation/releases/tag/v2027.0.0-ballot)(2026-09-11) |
| Laborbefund | `de.medizininformatikinitiative.kerndatensatz.laborbefund` | 2027.0.0-ballot | [kerndatensatzmodul-labor](https://github.com/medizininformatik-initiative/kerndatensatzmodul-labor) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatzmodul-labor/)· 37 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatzmodul-labor/releases/tag/v2027.0.0-ballot)(2026-09-14) |

### Erweiterungsmodule

| | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Biobank | `de.medizininformatikinitiative.kerndatensatz.biobank` | 2027.0.0-ballot | [kerndatensatzmodul-biobank](https://github.com/medizininformatik-initiative/kerndatensatzmodul-biobank) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatzmodul-biobank/branches/release/v2027.0.0-ballot/)· 66 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatzmodul-biobank/releases/tag/v2027.0.0-ballot)(2026-09-16) |
| ICU | `de.medizininformatikinitiative.kerndatensatz.icu` | 2027.0.0-ballot.3 | [kerndatensatzmodul-intensivmedizin](https://github.com/medizininformatik-initiative/kerndatensatzmodul-intensivmedizin) | [2027.0.0-ballot.3](https://medizininformatik-initiative.github.io/kerndatensatzmodul-intensivmedizin/)· 698 Fehler | [v2026.0.2](https://github.com/medizininformatik-initiative/kerndatensatzmodul-intensivmedizin/releases/tag/v2026.0.2)(2026-03-18) |
| Mikrobiologie | `de.medizininformatikinitiative.kerndatensatz.mikrobiologie` | 2027.0.0-ballot2 | [kerndatensatzmodul-mikrobiologie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-mikrobiologie) | [2027.0.0-ballot2](https://medizininformatik-initiative.github.io/kerndatensatzmodul-mikrobiologie/)· 206 Fehler | [v2027.0.0-ballot2](https://github.com/medizininformatik-initiative/kerndatensatzmodul-mikrobiologie/releases/tag/v2027.0.0-ballot2)(2026-09-14) |
| Molekulargenetik | `de.medizininformatikinitiative.kerndatensatz.molgen` | 2027.0.0-ballot.1 | [kerndatensatzmodul-GenetischeTests](https://github.com/medizininformatik-initiative/kerndatensatzmodul-GenetischeTests) | [2027.0.0-ballot.1](https://medizininformatik-initiative.github.io/kerndatensatzmodul-GenetischeTests/)· 53 Fehler | [v2027.0.0-ballot.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-GenetischeTests/releases/tag/v2027.0.0-ballot.1)(2026-09-13) |
| Pathologie | `de.medizininformatikinitiative.kerndatensatz.patho` | 2027.0.0-ballot | [kerndatensatzmodul-PathologieBefund](https://github.com/medizininformatik-initiative/kerndatensatzmodul-PathologieBefund) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatzmodul-PathologieBefund/branches/dev/v2027/)· 25 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatzmodul-PathologieBefund/releases/tag/v2027.0.0-ballot)(2026-09-14) |
| Studie | `de.medizininformatikinitiative.kerndatensatz.studie` | 2027.0.0-ballot | [kerndatensatzmodul-studie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-studie) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatzmodul-studie/)· 0 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatzmodul-studie/releases/tag/v2027.0.0-ballot)(2026-09-14) |
| Bildgebung | `de.medizininformatikinitiative.kerndatensatz.bildgebung` | 2027.0.0-ballot.1 | [kerndatensatz-bildgebung](https://github.com/medizininformatik-initiative/kerndatensatz-bildgebung) | [2027.0.0-ballot.1](https://medizininformatik-initiative.github.io/kerndatensatz-bildgebung/)· 29 Fehler | [v2027.0.0-ballot.1](https://github.com/medizininformatik-initiative/kerndatensatz-bildgebung/releases/tag/v2027.0.0-ballot.1)(2026-09-15) |
| Dokument | `de.medizininformatikinitiative.kerndatensatz.dokument` | 2027.0.0-ballot.2 | [kerndatensatz-dokument](https://github.com/medizininformatik-initiative/kerndatensatz-dokument) | [2027.0.0-ballot.2](https://medizininformatik-initiative.github.io/kerndatensatz-dokument/)· 2 Fehler | [v2027.0.0-ballot.2](https://github.com/medizininformatik-initiative/kerndatensatz-dokument/releases/tag/v2027.0.0-ballot.2)(2026-09-14) |
| Onkologie | `de.medizininformatikinitiative.kerndatensatz.onkologie` | 2027.0.0-ballot.1 | [kerndatensatzmodul-onkologie](https://github.com/medizininformatik-initiative/kerndatensatzmodul-onkologie) | [2027.0.0-ballot.1](https://medizininformatik-initiative.github.io/kerndatensatzmodul-onkologie/)· 4669 Fehler | [v2027.0.0-ballot.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-onkologie/releases/tag/v2027.0.0-ballot.1)(2026-09-15) |
| Seltene Erkrankungen | `de.medizininformatikinitiative.kerndatensatz.seltene` | 2027.0.0-ballot | [kerndatensatzmodul-seltene-erkrankungen](https://github.com/medizininformatik-initiative/kerndatensatzmodul-seltene-erkrankungen) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatzmodul-seltene-erkrankungen/)· 353 Fehler | [v2026.0.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-seltene-erkrankungen/releases/tag/v2026.0.1)(2026-03-30) |
| Molekulares Tumorboard | `de.medizininformatikinitiative.kerndatensatz.mtb` | 2027.0.0-ballot.1 | [kerndatensatzmodul-molekulares-tumorboard](https://github.com/medizininformatik-initiative/kerndatensatzmodul-molekulares-tumorboard) | [2027.0.0-ballot.1](https://medizininformatik-initiative.github.io/kerndatensatzmodul-molekulares-tumorboard/)· 55 Fehler | [v2027.0.0-ballot.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-molekulares-tumorboard/releases/tag/v2027.0.0-ballot.1)(2026-09-15) |
| PROs | `de.medizininformatikinitiative.kerndatensatz.pros` | 2027.0.0-ballot.1 | [kerndatensatzmodul-proms](https://github.com/medizininformatik-initiative/kerndatensatzmodul-proms) | [2027.0.0-ballot.1](https://medizininformatik-initiative.github.io/kerndatensatzmodul-proms/)· 214 Fehler | [v2027.0.0-ballot.1](https://github.com/medizininformatik-initiative/kerndatensatzmodul-proms/releases/tag/v2027.0.0-ballot.1)(2026-09-11) |
| Consent | `de.medizininformatikinitiative.kerndatensatz.consent` | 2027.0.0-ballot | [kerndatensatzmodul-consent](https://github.com/medizininformatik-initiative/kerndatensatzmodul-consent) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatzmodul-consent/)· 0 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatzmodul-consent/releases/tag/v2027.0.0-ballot)(2026-09-14) |
| Kardiologie | `de.medizininformatikinitiative.kerndatensatz.kardiologie` | 2027.0.0-ballot | [kerndatensatz-kardiologie](https://github.com/medizininformatik-initiative/kerndatensatz-kardiologie) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatz-kardiologie/branches/release/v2027.0.0-ballot/)· 42 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatz-kardiologie/releases/tag/v2027.0.0-ballot)(2026-09-14) |
| Lungenfunktion | `de.medizininformatikinitiative.kerndatensatz.lungenfunktion` | 2027.0.0-ballot.1 | [kerndatensatz-lungenfunktion](https://github.com/medizininformatik-initiative/kerndatensatz-lungenfunktion) | [2027.0.0-ballot.1](https://medizininformatik-initiative.github.io/kerndatensatz-lungenfunktion/)· 1147 Fehler | [v2027.0.0-ballot.1](https://github.com/medizininformatik-initiative/kerndatensatz-lungenfunktion/releases/tag/v2027.0.0-ballot.1)(2026-09-15) |
| Symptome | `de.medizininformatikinitiative.kerndatensatz.symptom` | 2027.0.0-ballot | [kerndatensatzmodul-symptome](https://github.com/medizininformatik-initiative/kerndatensatzmodul-symptome) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatzmodul-symptome/)· 0 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatzmodul-symptome/releases/tag/v2027.0.0-ballot)(2026-09-11) |
| Soziodemographie | `de.medizininformatikinitiative.kerndatensatz.soziodemographie` | 2027.0.0-ballot | [kerndatensatz-soziodemographie](https://github.com/medizininformatik-initiative/kerndatensatz-soziodemographie) | [2027.0.0-ballot](https://medizininformatik-initiative.github.io/kerndatensatz-soziodemographie/)· 1 Fehler | [v2027.0.0-ballot](https://github.com/medizininformatik-initiative/kerndatensatz-soziodemographie/releases/tag/v2027.0.0-ballot)(2026-09-14) |

### Angekündigt, noch nicht publiziert

**Derzeit keine — Soziodemographie ist seit dem 16.09.2026 publiziert und in der Haupttabelle geführt.**

### Externe Abhängigkeiten

Die BOM pinnt nicht nur die MII-Module, sondern auch die externen Pakete, gegen die sie gebaut sind. Gepinnt wird jeweils **die höchste Version, die ein MII-Modul transitiv tatsächlich anfordert** — nicht die neueste verfügbare. Eine Version, gegen die kein Modul gebaut wurde, gehört nicht in eine BOM.

Pakete ohne Pin werden weiterhin transitiv aufgelöst; ihre Version ergibt sich aus dem anfordernden Modul.

#### In der BOM gepinnt

| | | | |
| :--- | :--- | :--- | :--- |
| Deutsche Basisprofile R4 (`de.basisprofil.r4`) | 1.6.0 | 14 Module (Base, Biobank, Bildgebung, Dokument, ICU, Kardiologie, Lungenfunktion, Medikation, MolGen, MTB, Onkologie, PROs, Seltene, Symptome) | einheitlich 1.6.0 — der frühere Tippfehler`de.basiprofil.r4`(Lungenfunktion) ist behoben |
| HL7 Terminology (`hl7.terminology.r4`) | 7.3.0 | ICU, Bildgebung, Consent, Lungenfunktion, Medikation, MolGen, MTB, Onkologie, PROs, Soziodemographie, Studie, Symptome | acht Module fordern noch 7.1.0 (Base, Meta, Biobank, Dokument, Kardiologie, Laborbefund, Mikrobiologie, Seltene) |
| HL7 Extensions R4 (`hl7.fhir.uv.extensions.r4`) | 5.3.0 | zwölf Module + CRMI 2.0.0 | sieben Module fordern noch 5.2.0 (Base, Meta, Dokument, Laborbefund, Mikrobiologie, PROs, Seltene) |
| HL7 Clinical Genomics (`hl7.fhir.uv.genomics-reporting`) | 3.0.0 | Molekulargenetik, MTB, Onkologie | einheitlich |
| HL7 Europe Base (`hl7.fhir.eu.base`) | 2.0.0 | Symptome (direkt), EU Laboratory (transitiv über Biobank) | einheitlich |
| HL7 Europe Laboratory (`hl7.fhir.eu.laboratory`) | 2.0.0 | Biobank | einheitlich |
| HL7 Europe Extensions R4 (`hl7.fhir.eu.extensions.r4`) | 1.3.0 | EU Base, EU Laboratory, Pathologie (direkt) | einheitlich |
| MIABIS (`eu.miabis.r4`) | 1.3.0 | Biobank | Umzug auf die neuen MIABIS-Pfade in`2027.0.0-ballot`vollzogen |
| ISiK (`de.gematik.isik`) | 6.0.0 | ICU, Dokument, Kardiologie, PROs | Pathologie fordert noch 5.1.2 |

#### Nur transitiv aufgelöst

| | | |
| :--- | :--- | :--- |
| Einwilligungsmanagement (`de.einwilligungsmanagement`) | 2.0.4 | Consent |
| Deutsche Medikation (`de.fhir.medication`) | 1.0.7 | Medikation |
| IHE-D Terminologie (`de.ihe-d.terminology`) | 3.0.1 | Medikation, Dokument |
| gematik Terminologie (`de.gematik.terminology`) | 1.0.6 – 1.0.9 | ISiK (transitiv) |
| DVMD KDL (`dvmd.kdl.r4`) | 2025.0.1 (Dokument), 2026.0.0 (ICU) | Dokument, ICU |
| DICOM (`fhir.dicom`) | 2025.3.20250714 | Bildgebung |
| IHE FormatCode (`ihe.formatcode.fhir`) | 1.4.0 | Dokument |
| HL7 International Patient Summary (`hl7.fhir.uv.ips`) | 2.0.0 (Medikation), 2.0.1 (Base, Laborbefund, Mikrobiologie) | Base, Laborbefund, Medikation, Mikrobiologie |
| HL7 Structured Data Capture (`hl7.fhir.uv.sdc`) | 4.0.0 | PROs, ISiK |
| HL7 CRMI (`hl7.fhir.uv.crmi`) | 2.0.0 | alle Module außer Pathologie und Soziodemographie |
| HL7 Cross-Version R5 (`hl7.fhir.uv.xver-r5.r4`) | 0.1.0 | Base, Dokument, ICU, Medikation, Mikrobiologie, MTB, Onkologie, Pathologie, PROs, Studie |

#### Graph der externen Abhängigkeiten

![](dep-graph-2027-extern.png)

Automatisch generiert aus `dep-graph-2027-extern.dot` via Graphviz. Durchgezogene Kästen = in der BOM gepinnt, gestrichelt = nur transitiv aufgelöst. Rote Kantenbeschriftung = das Modul fordert eine andere Version an als die BOM pinnt.

## Installation

### Über die FHIR Package Registry (empfohlen)

Sobald das Paket auf packages.fhir.org verfügbar ist, genügt eine einzelne Abhängigkeit in der `sushi-config.yaml`:

```
dependencies:
  de.medizininformatikinitiative.kerndatensatz.complete: 2027.0.0-ballot.12

```

Alle 20 Modul-Dependencies und die 8 gepinnten externen Pakete werden automatisch von der FHIR Package Registry aufgelöst und heruntergeladen.

### Manuelle Installation

Solange das Paket noch nicht auf packages.fhir.org verfügbar ist, kann es vom [GitHub Release](https://github.com/medizininformatik-initiative/kerndatensatz-complete/releases/tag/v2027.0.0-ballot.12) heruntergeladen und lokal installiert werden:

```
# Package herunterladen
curl -LO https://github.com/medizininformatik-initiative/kerndatensatz-complete/releases/download/v2027.0.0-ballot.12/de.medizininformatikinitiative.kerndatensatz.complete-2027.0.0-ballot.12.tgz

# In den lokalen FHIR-Cache installieren
fhir install de.medizininformatikinitiative.kerndatensatz.complete-2027.0.0-ballot.12.tgz

```

Danach kann das Paket wie gewohnt als Dependency referenziert werden. Alle weiteren Module werden automatisch von packages.fhir.org aufgelöst.

> **Hinweis:** Der `fhir`-Befehl stammt aus dem [Firely Terminal (Simplifier CLI)](https://simplifier.net/downloads/firely-terminal). Im Zweifel Version 3.4.0 verwenden — neuere Versionen sind nicht getestet.

```
dotnet tool install -g Firely.Terminal --version 3.4.0

```


## Weitere Informationen

* [Alle KDS-Repositories auf GitHub](https://github.com/orgs/medizininformatik-initiative/repositories?q=kerndatensatzmodul)
* [Übersicht über Versionen der KDS-Module](https://github.com/medizininformatik-initiative/kerndatensatz-meta/wiki/%C3%9Cbersicht-%C3%BCber-Versionen-der-Kerndatensatz%E2%80%90Module)
* [MII Kerndatensatz Meta Wiki](https://github.com/medizininformatik-initiative/kerndatensatz-meta/wiki)
* [MII Kerndatensatz auf Art-Decor](https://art-decor.org/art-decor/decor-project--mide-)
* [MII GitHub Organisation](https://github.com/medizininformatik-initiative)
* [MII FHIR Packages auf Simplifier](https://simplifier.net/organization/koordinationsstellemii/~packages)

