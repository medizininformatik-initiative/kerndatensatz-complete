# MII KDS – Gesamtmodell - MII Kerndatensatz Complete v2027.0.0-ballot.19

* [**Table of Contents**](toc.md)
* [**Artifacts Summary**](artifacts.md)
* **MII KDS – Gesamtmodell**

## Logical Model: MII KDS – Gesamtmodell ( Experimental ) 

| | |
| :--- | :--- |
| *Official URL*:https://www.medizininformatik-initiative.de/fhir/core/complete/StructureDefinition/mii-kds-gesamt | *Version*:2027.0.0-ballot.19 |
| Active as of 2026-09-21 | *Computable Name*:MIIKDSGesamt |

 
Zentrales Logical Model, das alle Module des MII Kerndatensatzes als typisierte Slots zusammenführt. Inhalte stammen per Typ-Referenz aus den Modul-Logical-Models. 

**Usages:**

* This Logical Model is not used by any profiles in this Specification

You can also check for [usages in the FHIR IG Statistics](https://packages2.fhir.org/xig/resource/de.medizininformatikinitiative.kerndatensatz.complete|current/StructureDefinition/StructureDefinition-mii-kds-gesamt.json)

### Formal Views of Profile Content

 [Description of Profiles, Differentials, Snapshots and how the different presentations work](http://build.fhir.org/ig/FHIR/ig-guidance/readingIgs.html#structure-definitions). 

 

Other representations of profile: [CSV](StructureDefinition-mii-kds-gesamt.csv), [Excel](StructureDefinition-mii-kds-gesamt.xlsx) 



## Resource Content

```json
{
  "resourceType" : "StructureDefinition",
  "id" : "mii-kds-gesamt",
  "url" : "https://www.medizininformatik-initiative.de/fhir/core/complete/StructureDefinition/mii-kds-gesamt",
  "version" : "2027.0.0-ballot.19",
  "name" : "MIIKDSGesamt",
  "title" : "MII KDS – Gesamtmodell",
  "status" : "active",
  "experimental" : true,
  "date" : "2026-09-21T12:22:18+00:00",
  "publisher" : "Medizininformatik Initiative",
  "contact" : [{
    "name" : "Medizininformatik Initiative",
    "telecom" : [{
      "system" : "url",
      "value" : "https://www.medizininformatik-initiative.de"
    }]
  }],
  "description" : "Zentrales Logical Model, das alle Module des MII Kerndatensatzes als typisierte Slots zusammenführt. Inhalte stammen per Typ-Referenz aus den Modul-Logical-Models.",
  "jurisdiction" : [{
    "coding" : [{
      "system" : "urn:iso:std:iso:3166",
      "code" : "DE",
      "display" : "Germany"
    }]
  }],
  "fhirVersion" : "4.0.1",
  "kind" : "logical",
  "abstract" : false,
  "type" : "https://www.medizininformatik-initiative.de/fhir/core/complete/StructureDefinition/mii-kds-gesamt",
  "baseDefinition" : "http://hl7.org/fhir/StructureDefinition/Base",
  "derivation" : "specialization",
  "differential" : {
    "element" : [{
      "id" : "mii-kds-gesamt",
      "path" : "mii-kds-gesamt",
      "short" : "MII KDS – Gesamtmodell",
      "definition" : "Zentrales Logical Model, das alle Module des MII Kerndatensatzes als typisierte Slots zusammenführt. Inhalte stammen per Typ-Referenz aus den Modul-Logical-Models."
    },
    {
      "id" : "mii-kds-gesamt.person",
      "path" : "mii-kds-gesamt.person",
      "short" : "Person",
      "definition" : "Modul Person",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/LogicalModel/Person"
      }]
    },
    {
      "id" : "mii-kds-gesamt.fall",
      "path" : "mii-kds-gesamt.fall",
      "short" : "Fall",
      "definition" : "Modul Fall",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/core/modul-fall/StructureDefinition/LogicalModel/Fall"
      }]
    },
    {
      "id" : "mii-kds-gesamt.diagnose",
      "path" : "mii-kds-gesamt.diagnose",
      "short" : "Diagnose",
      "definition" : "Modul Diagnose",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/core/modul-diagnose/StructureDefinition/LogicalModel/Diagnose"
      }]
    },
    {
      "id" : "mii-kds-gesamt.prozedur",
      "path" : "mii-kds-gesamt.prozedur",
      "short" : "Prozedur",
      "definition" : "Modul Prozedur",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/core/modul-prozedur/StructureDefinition/LogicalModel/Prozedur"
      }]
    },
    {
      "id" : "mii-kds-gesamt.labor",
      "path" : "mii-kds-gesamt.labor",
      "short" : "Labor",
      "definition" : "Modul Laborbefund",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/LogicalModel/Laborbefund"
      }]
    },
    {
      "id" : "mii-kds-gesamt.medikation",
      "path" : "mii-kds-gesamt.medikation",
      "short" : "Medikation",
      "definition" : "Modul Medikation",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/core/modul-medikation/StructureDefinition/LogicalModel/BasismodulMedikation"
      }]
    },
    {
      "id" : "mii-kds-gesamt.biobank",
      "path" : "mii-kds-gesamt.biobank",
      "short" : "Biobank",
      "definition" : "Modul Biobank",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/StructureDefinition/LogicalModel/Biobank"
      }]
    },
    {
      "id" : "mii-kds-gesamt.icu",
      "path" : "mii-kds-gesamt.icu",
      "short" : "Intensivmedizin",
      "definition" : "Modul ICU (Typ-Referenz deaktiviert — Modul hat dangling parent URL)",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Base"
      }]
    },
    {
      "id" : "mii-kds-gesamt.mikrobio",
      "path" : "mii-kds-gesamt.mikrobio",
      "short" : "Mikrobiologie",
      "definition" : "Modul Mikrobiologie (Typ-Referenz deaktiviert — Modul hat dangling parent URL)",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "Base"
      }]
    },
    {
      "id" : "mii-kds-gesamt.molgen",
      "path" : "mii-kds-gesamt.molgen",
      "short" : "Molekulargenetik",
      "definition" : "Modul Molgen",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/LogicalModelMolGen"
      }]
    },
    {
      "id" : "mii-kds-gesamt.patho",
      "path" : "mii-kds-gesamt.patho",
      "short" : "Pathologie",
      "definition" : "Modul Pathologie",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/StructureDefinition/mii-lm-patho-logical-model"
      }]
    },
    {
      "id" : "mii-kds-gesamt.studie",
      "path" : "mii-kds-gesamt.studie",
      "short" : "Studie",
      "definition" : "Modul Studie",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/modul-studie/StructureDefinition/mii-lm-studie-logicalmodel"
      }]
    },
    {
      "id" : "mii-kds-gesamt.bildgebung",
      "path" : "mii-kds-gesamt.bildgebung",
      "short" : "Bildgebung",
      "definition" : "Modul Bildgebung",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/StructureDefinition/LogicalModel/Bildgebung"
      }]
    },
    {
      "id" : "mii-kds-gesamt.onkologie",
      "path" : "mii-kds-gesamt.onkologie",
      "short" : "Onkologie",
      "definition" : "Modul Onkologie",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/StructureDefinition/mii-lm-onko"
      }]
    },
    {
      "id" : "mii-kds-gesamt.mtb",
      "path" : "mii-kds-gesamt.mtb",
      "short" : "MTB",
      "definition" : "Modul Molekulares Tumorboard",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-mtb/StructureDefinition/mii-lm-mtb"
      }]
    },
    {
      "id" : "mii-kds-gesamt.seltene",
      "path" : "mii-kds-gesamt.seltene",
      "short" : "Seltene Erkrankungen",
      "definition" : "Modul Seltene Erkrankungen",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-seltene/StructureDefinition/LogicalModel/Seltene"
      }]
    },
    {
      "id" : "mii-kds-gesamt.pro",
      "path" : "mii-kds-gesamt.pro",
      "short" : "PROs",
      "definition" : "Modul Patient-Reported Outcomes",
      "min" : 0,
      "max" : "*",
      "type" : [{
        "code" : "https://www.medizininformatik-initiative.de/fhir/ext/modul-pro/StructureDefinition/mii-lm-pro"
      }]
    }]
  }
}

```
