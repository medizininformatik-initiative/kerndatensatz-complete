# MII KDS Profil-Canonicals 2026 auf 2027 - MII Kerndatensatz Complete v2027.0.0-ballot.19

* [**Table of Contents**](toc.md)
* [**Artefaktübersicht**](artifacts.md)
* **MII KDS Profil-Canonicals 2026 auf 2027**

## ConceptMap: MII KDS Profil-Canonicals 2026 auf 2027 (Experimentell) 

| | |
| :--- | :--- |
| *Offizielle URL*:https://www.medizininformatik-initiative.de/fhir/core/complete/ConceptMap/mii-cm-kds-profile-canonicals-2026-2027 | *Version*:2027.0.0-ballot.19 |
| Draft Stand: 2026-09-26 | *Maschinenlesbarer Name*:mii_cm_kds_profile_canonicals_2026_2027 |

 
Migration der Profil-Canonicals (StructureDefinition.url) von der 2026er KDS-Linie auf die in dieser BOM gepinnte 2027er Ballot-Linie. Automatisch erzeugt aus dem Aehnlichkeits-Matching des MII KDS Version-Differs (Element- bzw. Composition-Fingerprints, Jaccard-Index). Qualitaetsstatus nach MapQual/ISO TS 21564: D12 = automatisiert ohne abgeschlossene menschliche Validierung — Entwurf zur Kuratierung, nicht fuer den produktiven Einsatz. Zeilen mit equivalence=equivalent sind inhaltsgleiche Umbenennungen (Jaccard 1.0); relatedto-Zeilen tragen den Aehnlichkeits-Score im Kommentar. 



## Resource Content

```json
{
  "resourceType" : "ConceptMap",
  "id" : "mii-cm-kds-profile-canonicals-2026-2027",
  "url" : "https://www.medizininformatik-initiative.de/fhir/core/complete/ConceptMap/mii-cm-kds-profile-canonicals-2026-2027",
  "version" : "2027.0.0-ballot.19",
  "name" : "mii_cm_kds_profile_canonicals_2026_2027",
  "title" : "MII KDS Profil-Canonicals 2026 auf 2027",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-09-26T09:29:37+00:00",
  "publisher" : "Medizininformatik Initiative",
  "contact" : [{
    "name" : "Medizininformatik Initiative",
    "telecom" : [{
      "system" : "url",
      "value" : "https://www.medizininformatik-initiative.de"
    }]
  }],
  "description" : "Migration der Profil-Canonicals (StructureDefinition.url) von der 2026er KDS-Linie auf die in dieser BOM gepinnte 2027er Ballot-Linie. Automatisch erzeugt aus dem Aehnlichkeits-Matching des MII KDS Version-Differs (Element- bzw. Composition-Fingerprints, Jaccard-Index). Qualitaetsstatus nach MapQual/ISO TS 21564: D12 = automatisiert ohne abgeschlossene menschliche Validierung — Entwurf zur Kuratierung, nicht fuer den produktiven Einsatz. Zeilen mit equivalence=equivalent sind inhaltsgleiche Umbenennungen (Jaccard 1.0); relatedto-Zeilen tragen den Aehnlichkeits-Score im Kommentar.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "purpose" : "Maschinelle Aufloesung alter Canonicals via $translate (system=urn:ietf:rfc:3986, code=<alte URL>).",
  "group" : [{
    "source" : "urn:ietf:rfc:3986",
    "target" : "urn:ietf:rfc:3986",
    "element" : [{
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/arterieller-blutdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-muv-arterieller-blutdruck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/arterieller-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-arterieller-druck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/atemfrequenz",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-atemfrequenz",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/atemwegsdruck-bei-mitl-exspiratorischem-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemwegsdruck-bei-mitl-exspiratorischem-gasfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/atemwegsdruck-bei-null-exspiratorischem-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemwegsdruck-bei-null-exspiratorischem-gasfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/atemzugvolumen-einstellung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemzugvolumen-einstellung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/atemzugvolumen-waehrend-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemzugvolumen-waehrend-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/beatmungsvolumen-pro-minute-maschineller",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungsvolumen-pro-minute-maschineller",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/beatmungszeit-hohem-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungszeit-hohem-druck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/beatmungszeit-niedrigem-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungszeit-niedrigem-druck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-abnahme-haemofiltration-einzelmesswerte",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-drainage-generisch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-generisch",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-drainage-op",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-op",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-drainage-wund",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-wund",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-fluessigkeit-gesamt",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-gallenfluessigkeit",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-gallengang",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-wund",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-magensonde",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-wund",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-opdrainage",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-op",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-pankreasdrainage",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-pankreasdrainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.833 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-stuhlgang",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-wund",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-urin",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-urin",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.857 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-ausfuhr-wunddrainage",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-wunddrainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.857 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-blutverlust",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-einfuhr-enterale-fluesse",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-enterale-fluesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-einfuhr-enterale-fluessigkeit",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-enterale-fluesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-einfuhr-fluessigkeit-gesamt",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-fluessigkeit-gesamt",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.833 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-einfuhr-oraler-fluesse",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-einfuhr-oraler-fluessigkeit",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluessigkeit",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.857 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-gesamte-ausfuhr",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-op",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-gesamte-einfuhr",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/bilanz-gesamte-tages-bilanz",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-gesamte-tages-bilanz",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.857 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/blutfluss-cardiovasculaeres-geraet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutfluss-cardiovasculaeres-geraet",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/blutfluss-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutfluss-extrakorporaler-gasaustausch",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/blutflussindex-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutflussindex-extrakorporaler-gasaustausch",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/dauer-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-dauer-extrakorporaler-gasaustausch",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/dauer-haemodialysesitzung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-dauer-haemodialysesitzung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/devicemetric-eingestellte-gemessene-parameter-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-devicemetric-eingestellte-gemessene-parameter-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/devicemetric-eingestellte-gemessene-parameter-extrakorporale-verfahren",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-devicemetric-eingestellte-gemessene-parameter-extrakorporale-verfahren",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/druckdifferenz-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-druckdifferenz-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/dynamische-kompliance",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-dynamische-kompliance",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/eingestellter-inspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-eingestellter-inspiratorischer-gasfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/einstellung-ausatmungszeit-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-einstellung-ausatmungszeit-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/einstellung-einatmungszeit-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-einstellung-einatmungszeit-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/endexspiratorischer-kohlendioxidpartialdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-endexspiratorischer-kohlendioxidpartialdruck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/exspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-exspiratorischer-gasfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/exspiratorischer-sauerstoffpartialdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-exspiratorischer-sauerstoffpartialdruck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/extrakorporales-verfahren",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-extrakorporales-verfahren",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-gasfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/haemodialyse-blutfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-haemodialyse-blutfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/herzfrequenz",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-herzfrequenz",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/horowitz-in-arteriellem-blut",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-horowitz-in-arteriellem-blut",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/icu-device",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-icu-device",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/inspiratorische-sauerstofffraktion",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorische-sauerstofffraktion",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/inspiratorische-sauerstofffraktion-eingestellt",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorische-sauerstofffraktion-eingestellt",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/inspiratorische-sauerstofffraktion-gemessen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorische-sauerstofffraktion-gemessen",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/inspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorischer-gasfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/ionisiertes-kalzium-nierenersatzverfahren",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-ionisiertes-kalzium-nierenersatzverfahren",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/koerpergewicht",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-koerpergewicht",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/koerpergroesse",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-muv-koerpergroesse",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/kopfumfang",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-kopfumfang",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/maximaler-beatmungsdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-maximaler-beatmungsdruck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mechanische-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-mechanische-atemfrequenz-beatmet",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-arterieller-blutdruck",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-arterieller-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-arterieller-druck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-atemfrequenz",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-atemwegsdruck-bei-mittlerem-expiratorischem-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemwegsdruck-bei-mittlerem-expiratorischem-gasfluss",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-atemwegsdruck-bei-null-expiratorischem-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemwegsdruck-bei-null-expiratorischem-gasfluss",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-atemzugvolumen-einstellung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemzugvolumen-einstellung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.625 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-atemzugvolumen-waehrend-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemzugvolumen-waehrend-beatmung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-beatmungsvolumen-pro-minute-maschineller-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungsvolumen-pro-minute-maschineller-beatmung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-beatmungszeit-hohem-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungszeit-hohem-druck",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-beatmungszeit-niedrigem-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungszeit-niedrigem-druck",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-abnahme-haemofiltration-einzelmesswerte",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-haemofiltration-einzelmesswerte",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.875 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-op",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-drainage-wund",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-gallengang",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.875 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-opdrainage",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.875 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-blutverlust",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.875 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-enterale-fluesse",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluesse",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-einfuhr-oraler-fluessigkeit",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-tagesbilanz-fluessigkeit",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.875 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-gesamte-ausfuhr",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.875 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-gesamte-einfuhr",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.875 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-gesamte-tages-bilanz",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-tagesbilanz-fluessigkeit",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.75 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-blutfluss-cardiovasculaeres-geraet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutfluss-cardiovasculaeres-geraet",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-blutfluss-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutfluss-extrakorporaler-gasaustausch",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-blutflussindex-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutflussindex-extrakorporaler-gasaustausch",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-dauer-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-dauer-extrakorporaler-gasaustausch",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-dauer-haemodialysesitzung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-dauer-haemodialysesitzung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-devicemetric-eingestellte-gemessene-parameter-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-dm-eingestellte-gemessene-parameter-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-devicemetric-eingestellte-gemessene-parameter-extrakorporale-verfahren",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-dm-eingest-gem-parameter-extrakorporale-verfahren",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-druckdifferenz-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-druckdifferenz-beatmung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-dynamische-kompliance",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-dynamische-kompliance",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-arterieller-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.333 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutfluss-cardiovasculaeres-geraet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.444 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutfluss-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.444 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-blutflussindex-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-dauer-extrakorporaler-gasaustausch",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-dauer-haemodialysesitzung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-haemofiltration-einzelmesswerte",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-devicemetric-eingestellte-gemessene-parameter-extrakorporale-verfahren",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-extrakorporales-verfahren",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.222 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-haemodialyse-blutfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-ionisiertes-kalzium-nierenersatzverfahren",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.333 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-parameter-von-extrakorporalen-verfahren",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-substituatfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-substituatvolumen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-venoeser-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.444 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-eingestellter-inspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-eingestellter-inspiratorischer-gasfluss",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-einstellung-ausatmungszeit-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-einstellung-ausatmungszeit-beatmung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-einstellung-einatmungszeit-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-einstellung-einatmungszeit-beatmung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-endexpiratorischer-kohlendioxidpartialdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-endexpiratorischer-kohlendioxidpartialdruck",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.625 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-exspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-exspiratorischer-gasfluss",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-exspiratorischer-sauerstoffpartialdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-exspiratorischer-sauerstoffpartialdruck",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.625 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-gasfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-haemodialyse-blutfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-haemodialyse-blutfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-herzfrequenz",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-horowitz-in-arteriellem-blut",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-horowitz-in-arteriellem-blut",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.625 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-icu-device",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-device",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-inspiratorische-sauerstofffraktion-eingestellt",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorischer-gasfluss",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.571 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-inspiratorische-sauerstofffraktion-gemessen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorischer-gasfluss",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.571 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-inspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorischer-gasfluss",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ionisiertes-kalzium-nierenersatzverfahren",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-ionisiertes-kalzium-nierenersatzverfahren",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-koerpergewicht",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-koerpergroesse",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-kopfumfang",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-maximaler-beatmungsdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-plateau-beatmungsdruck",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-mechanische-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-mechanische-atemfrequenz-beatmet",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-mittlerer-beatmungsdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-plateau-beatmungsdruck",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-positiv-endexpiratorischer-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-positiv-endexpiratorischer-druck",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-spontane-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontane-atemfrequenz-beatmet",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.625 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-spontane-mechanische-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontane-mechanische-atemfrequenz-beatmet",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-spontanes-atemzugvolumen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemzugvolumen-einstellung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-spontanes-mechanisches-atemzugvolumen-waehrend-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontanes-mechanisches-atemzugvolumen-waehrend-beatmung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-substituatfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-substituatfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-substituatvolumen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-substituatvolumen",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-unterstuetzungsdruck-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-unterstuetzungsdruck-beatmung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-venoeser-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-venoeser-druck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemwegsdruck-bei-mitl-exspiratorischem-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.273 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemwegsdruck-bei-null-exspiratorischem-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.273 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemzugvolumen-einstellung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-haemofiltration-einzelmesswerte",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.333 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-atemzugvolumen-waehrend-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmung",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungsvolumen-pro-minute-maschineller",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-haemofiltration-einzelmesswerte",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungszeit-hohem-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-beatmungszeit-niedrigem-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-devicemetric-eingestellte-gemessene-parameter-beatmung",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-druckdifferenz-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-dynamische-kompliance",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-eingestellter-inspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-tagesbilanz-fluessigkeit",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.25 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-einstellung-ausatmungszeit-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.4 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-einstellung-einatmungszeit-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.4 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-endexspiratorischer-kohlendioxidpartialdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-haemofiltration-einzelmesswerte",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-exspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.333 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-exspiratorischer-sauerstoffpartialdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-horowitz-in-arteriellem-blut",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.333 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorische-sauerstofffraktion",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.4 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorische-sauerstofffraktion-eingestellt",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-haemofiltration-einzelmesswerte",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.4 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorische-sauerstofffraktion-gemessen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-haemofiltration-einzelmesswerte",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.4 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-inspiratorischer-gasfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.333 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-maximaler-beatmungsdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-mechanische-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-mittlerer-beatmungsdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-parameter-von-beatmung",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul icu: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2026.0.1 -> 2026.0.2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-positiv-endexspiratorischer-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-haemofiltration-einzelmesswerte",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontane-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.4 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontane-mechanische-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.4 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontanes-atemzugvolumen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontanes-mechanisches-atemzugvolumen-waehrend",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-blutverlust",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.273 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-unterstuetzungsdruck-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-tagesbilanz-fluessigkeit",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.273 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-zeitverhaeltnis-ein-ausatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-bilanz-ausfuhr-op-drainage",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.364 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-zeitverhaeltnis-ein-ausatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-zeitverhaeltnis-ein-ausatmung",
        "equivalence" : "relatedto",
        "comment" : "Modul icu, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mittlerer-beatmungsdruck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-mittlerer-beatmungsdruck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/parameter-von-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-parameter-von-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/parameter-von-extrakorporalen-verfahren",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-parameter-von-extrakorporalen-verfahren",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/positiv-endexspiratorischer-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-positiv-endexspiratorischer-druck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/spontane-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontane-atemfrequenz-beatmet",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/spontane-mechanische-atemfrequenz-beatmet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-spontane-mechanische-atemfrequenz-beatmet",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/spontanes-atemzugvolumen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontanes-atemzugvolumen",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/spontanes-mechanisches-atemzugvolumen-waehrend",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-spontanes-mechanisches-atemzugvolumen-waehrend",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/substituatfluss",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-substituatfluss",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/substituatvolumen",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-substituatvolumen",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/unterstuetzungsdruck-beatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-unterstuetzungsdruck-beatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/venoeser-druck",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-ect-venoeser-druck",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/zeitverhaeltnis-ein-ausatmung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-icu/StructureDefinition/mii-pr-icu-vent-zeitverhaeltnis-ein-ausatmung",
        "equivalence" : "equivalent",
        "comment" : "Modul icu, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-kultur-nachweis",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-allgemeine-kultur",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.143 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-molekulare-diagnostik",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-molekulare-pathogenlast",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.105 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-mre-klasse",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-aviditaet",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.146 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-resistenzgene",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-titer",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.109 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-resistenzmutation",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-aviditaet",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.14 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/StructureDefinition/mii-pr-mikrobio-serologie-immunologie",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/ergebnis-zusammenfassung",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/mii-pr-molgen-molekulare-konsequenz",
        "equivalence" : "relatedto",
        "comment" : "Modul molgen, Jaccard 0.312 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/familienanamnese",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/mii-pr-molgen-familienanamnese",
        "equivalence" : "equivalent",
        "comment" : "Modul molgen, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/mii-pr-molgen-familienanamnese",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/familienanamnese",
        "equivalence" : "equivalent",
        "comment" : "Modul molgen, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/untersuchte-region",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/mii-pr-molgen-molekularer-biomarker",
        "equivalence" : "relatedto",
        "comment" : "Modul molgen, Jaccard 0.227 — Kuratierung ausstehend"
      }]
    }]
  }]
}

```
