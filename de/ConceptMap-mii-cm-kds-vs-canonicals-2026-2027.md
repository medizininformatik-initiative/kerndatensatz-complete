# MII KDS ValueSet-Canonicals 2026 auf 2027 - MII Kerndatensatz Complete v2027.0.0-ballot.19

* [**Table of Contents**](toc.md)
* [**Artefaktübersicht**](artifacts.md)
* **MII KDS ValueSet-Canonicals 2026 auf 2027**

## ConceptMap: MII KDS ValueSet-Canonicals 2026 auf 2027 (Experimentell) 

| | |
| :--- | :--- |
| *Offizielle URL*:https://www.medizininformatik-initiative.de/fhir/core/complete/ConceptMap/mii-cm-kds-vs-canonicals-2026-2027 | *Version*:2027.0.0-ballot.19 |
| Draft Stand: 2026-09-23 | *Maschinenlesbarer Name*:mii_cm_kds_vs_canonicals_2026_2027 |

 
Migration der ValueSet-Canonicals von der 2026er KDS-Linie auf die in dieser BOM gepinnte 2027er Ballot-Linie. Automatisch erzeugt aus dem Aehnlichkeits-Matching des MII KDS Version-Differs (Element- bzw. Composition-Fingerprints, Jaccard-Index). Qualitaetsstatus nach MapQual/ISO TS 21564: D12 = automatisiert ohne abgeschlossene menschliche Validierung — Entwurf zur Kuratierung, nicht fuer den produktiven Einsatz. Zeilen mit equivalence=equivalent sind inhaltsgleiche Umbenennungen (Jaccard 1.0); relatedto-Zeilen tragen den Aehnlichkeits-Score im Kommentar. 



## Resource Content

```json
{
  "resourceType" : "ConceptMap",
  "id" : "mii-cm-kds-vs-canonicals-2026-2027",
  "url" : "https://www.medizininformatik-initiative.de/fhir/core/complete/ConceptMap/mii-cm-kds-vs-canonicals-2026-2027",
  "version" : "2027.0.0-ballot.19",
  "name" : "mii_cm_kds_vs_canonicals_2026_2027",
  "title" : "MII KDS ValueSet-Canonicals 2026 auf 2027",
  "status" : "draft",
  "experimental" : true,
  "date" : "2026-09-23T09:27:22+00:00",
  "publisher" : "Medizininformatik Initiative",
  "contact" : [{
    "name" : "Medizininformatik Initiative",
    "telecom" : [{
      "system" : "url",
      "value" : "https://www.medizininformatik-initiative.de"
    }]
  }],
  "description" : "Migration der ValueSet-Canonicals von der 2026er KDS-Linie auf die in dieser BOM gepinnte 2027er Ballot-Linie. Automatisch erzeugt aus dem Aehnlichkeits-Matching des MII KDS Version-Differs (Element- bzw. Composition-Fingerprints, Jaccard-Index). Qualitaetsstatus nach MapQual/ISO TS 21564: D12 = automatisiert ohne abgeschlossene menschliche Validierung — Entwurf zur Kuratierung, nicht fuer den produktiven Einsatz. Zeilen mit equivalence=equivalent sind inhaltsgleiche Umbenennungen (Jaccard 1.0); relatedto-Zeilen tragen den Aehnlichkeits-Score im Kommentar.",
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
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-empfindlichkeit-einheiten-ucum",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-empfindlichkeit-einheiten-ucum",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-keimzahl-einheiten-ucum",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-keimzahl-einheiten-ucum",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.5 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-antigen-assay-einheiten-ucum",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-antigen-antikoerper-quantitativ-einheiten-ucum",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.286 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-aviditaet-snomedct",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-barlett-score-loinc",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-bartlett-score-loinc",
        "equivalence" : "equivalent",
        "comment" : "Modul mikrobiologie, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-clsi-hl7",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-susceptibility",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.833 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-eucast-snomedct",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-kultur-methode-snomedct",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-mikroskopiemethoden-snomedct",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-morphologie-snomedct",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-morphologie-ergebnis-snomed",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.276 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-mre-klasse-snomedct",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-positiv-negativ-snomedct",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-resistenzkategorie-status-ergebnis",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.5 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-qualitative-labor-ergebnisse-snomedct",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-detected-not-detected-snomed",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.667 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-resistenzgene-loinc",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-resistenzmutation-loinc",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-serologie-immunologie-loinc",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-serologischer-test-einheiten-ucum",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-empfindlichkeit-einheiten-ucum",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.273 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-voraussichtliche-empfindlichkeit-snomedct",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-molekulare-diagnostik-einheiten-ucum",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobio/ValueSet/mii-vs-mikrobio-molekulare-diagnostik-einheiten-ucum",
        "equivalence" : "relatedto",
        "comment" : "Modul mikrobiologie, Jaccard 0.714 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobiologie/ValueSet/mii-vs-mikrobio-kulturtests-loinc",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobiologie/ValueSet/mii-vs-mikrobio-mikroskopie-tests-loinc",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/modul-mikrobiologie/ValueSet/mii-vs-mikrobio-molekulare-diagnostik-loinc",
      "target" : [{
        "equivalence" : "unmatched",
        "comment" : "Modul mikrobiologie: entfaellt ersatzlos bzw. kein bestaetigter Nachfolger (2025.0.2 -> 2027.0.0-ballot2)"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-strahlentherapie-ende-grund",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-strahlentherapie-ende-grund",
        "equivalence" : "equivalent",
        "comment" : "Modul onkologie, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-strahlentherapie-stellungzurop",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-strahlentherapie-stellungzurop",
        "equivalence" : "equivalent",
        "comment" : "Modul onkologie, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-strahlentherapie-strahlenart",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-strahlentherapie-strahlenart",
        "equivalence" : "equivalent",
        "comment" : "Modul onkologie, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-strahlentherapie-strahlungseinheit",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-strahlentherapie-strahlungseinheit",
        "equivalence" : "equivalent",
        "comment" : "Modul onkologie, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-strahlentherapie-zielgebiet",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-strahlentherapie-zielgebiet",
        "equivalence" : "equivalent",
        "comment" : "Modul onkologie, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-systemische-therapie-ende-grund",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-ende-grund",
        "equivalence" : "equivalent",
        "comment" : "Modul onkologie, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-systemische-therapie-stellungzurop",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/ValueSet/mii-vs-onko-systemische-therapie-stellungzurop",
        "equivalence" : "equivalent",
        "comment" : "Modul onkologie, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    },
    {
      "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-seltene/ValueSet/von-seltene-betroffen-vs",
      "target" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-seltene/ValueSet/mii-vs-seltene-von-se-betroffen",
        "equivalence" : "equivalent",
        "comment" : "Modul seltene, Jaccard 1.0 — Kuratierung ausstehend"
      }]
    }]
  }]
}

```
