// MII KDS Gesamt-Logical-Model (experimentell)
//
// Ein einziges Logical Model, das die bestehenden Modul-Logical-Models
// als typisierte Slots einbindet. Inhalte werden NICHT dupliziert —
// die Modul-LMs bleiben die kanonische Quelle, dieses LM ist nur
// der strukturelle Dach-Knoten für eine zentrale Baumansicht im IG.
//
// Solange experimental = true, ist dieses LM nicht Teil des stabilen
// complete-Release-Inhalts.
//
// Siehe Beads: mii-kerndatensatz-dev-ff7

Logical: MIIKDSGesamt
Parent: Base
Id: mii-kds-gesamt
Title: "MII KDS – Gesamtmodell"
Description: "Zentrales Logical Model, das alle Module des MII Kerndatensatzes als typisierte Slots zusammenführt. Inhalte stammen per Typ-Referenz aus den Modul-Logical-Models."

* ^url = "https://www.medizininformatik-initiative.de/fhir/core/complete/StructureDefinition/mii-kds-gesamt"
* ^experimental = true

// ─── Basismodule ───────────────────────────────────────────────────────────
* person       0..* https://www.medizininformatik-initiative.de/fhir/core/modul-person/StructureDefinition/LogicalModel/Person                       "Person"       "Modul Person"
* fall         0..* https://www.medizininformatik-initiative.de/fhir/core/modul-fall/StructureDefinition/LogicalModel/Fall                           "Fall"         "Modul Fall"
* diagnose     0..* https://www.medizininformatik-initiative.de/fhir/core/modul-diagnose/StructureDefinition/LogicalModel/Diagnose                   "Diagnose"     "Modul Diagnose"
* prozedur     0..* https://www.medizininformatik-initiative.de/fhir/core/modul-prozedur/StructureDefinition/LogicalModel/Prozedur                   "Prozedur"     "Modul Prozedur"
* labor        0..* https://www.medizininformatik-initiative.de/fhir/core/modul-labor/StructureDefinition/LogicalModel/Laborbefund                   "Labor"        "Modul Laborbefund"
* medikation   0..* https://www.medizininformatik-initiative.de/fhir/core/modul-medikation/StructureDefinition/LogicalModel/BasismodulMedikation     "Medikation"   "Modul Medikation"

// ─── Erweiterungsmodule ────────────────────────────────────────────────────
* biobank      0..* https://www.medizininformatik-initiative.de/fhir/ext/modul-biobank/StructureDefinition/LogicalModel/Biobank                      "Biobank"      "Modul Biobank"
// ICU und Mikrobio: ihre publizierten LMs haben Parent-URLs, die in den Release-Paketen nicht auflösbar sind.
// SUSHI splittet dadurch den Typ in code+profile und der IG-Publisher kann den Basis-Typ nicht laden.
// Bis die Module ihre Parent-Referenzen fixen, stehen diese Slots als Base-Platzhalter.
* icu          0..* Base "Intensivmedizin" "Modul ICU (Typ-Referenz deaktiviert — Modul hat dangling parent URL)"
* mikrobio     0..* Base "Mikrobiologie"   "Modul Mikrobiologie (Typ-Referenz deaktiviert — Modul hat dangling parent URL)"
* molgen       0..* https://www.medizininformatik-initiative.de/fhir/ext/modul-molgen/StructureDefinition/LogicalModelMolGen                         "Molekulargenetik" "Modul Molgen"
* patho        0..* https://www.medizininformatik-initiative.de/fhir/ext/modul-patho/StructureDefinition/mii-lm-patho-logical-model                  "Pathologie"   "Modul Pathologie"
* studie       0..* https://www.medizininformatik-initiative.de/fhir/modul-studie/StructureDefinition/mii-lm-studie-logicalmodel                     "Studie"       "Modul Studie"
* bildgebung   0..* https://www.medizininformatik-initiative.de/fhir/ext/modul-bildgebung/StructureDefinition/LogicalModel/Bildgebung                "Bildgebung"   "Modul Bildgebung"
* onkologie    0..* https://www.medizininformatik-initiative.de/fhir/ext/modul-onko/StructureDefinition/LogicalModel/Onkologie                       "Onkologie"    "Modul Onkologie"
* mtb          0..* https://www.medizininformatik-initiative.de/fhir/ext/modul-mtb/StructureDefinition/LogicalModel/mii-lm-mtb                       "MTB"          "Modul Molekulares Tumorboard"
* seltene      0..* https://www.medizininformatik-initiative.de/fhir/ext/modul-seltene/StructureDefinition/LogicalModel/Seltene                      "Seltene Erkrankungen" "Modul Seltene Erkrankungen"
* pro          0..* https://www.medizininformatik-initiative.de/fhir/ext/modul-pro/StructureDefinition/mii-lm-pro                                    "PROs"         "Modul Patient-Reported Outcomes"
