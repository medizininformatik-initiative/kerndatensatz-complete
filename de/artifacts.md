# Artefaktübersicht - MII Kerndatensatz Complete v2027.0.0-ballot.19

* [**Table of Contents**](toc.md)
* **Artefaktübersicht**

## Artefaktübersicht

Diese Seite bietet eine Liste der FHIR-Artefakte, die in diesem Implementierungsleitfaden definiert sind.

### Verhalten: CapabilityStatements 

Die folgenden Artefakte definieren die spezifischen Fähigkeiten, die verschiedene Systemtypen haben müssen, um diesem Implementierungsleitfaden zu entsprechen. Von Systemen, die mit dem Implementierungsleitfaden konform sind, wird erwartet, dass sie die Konformität mit einem oder mehreren der folgenden Capability Statements deklarieren.

| | |
| :--- | :--- |
| [ MII CPS Kerndatensatz Complete CapabilityStatement  ](CapabilityStatement-mii-cps-kerndatensatz-complete.md) | Aggregiertes CapabilityStatement des MII Kerndatensatz Complete-Pakets. Beschreibt alle verpflichtenden Interaktionen, Profile und Suchparameter aus allen Modulen des MII Kerndatensatzes, die ein konformes System unterstützen muss. |

### Terminologie: ConceptMaps 

Diese definieren Transformationen zur Konvertierung zwischen Codes durch Systeme, die mit diesem Implementierungsleitfaden konform sind.

| | |
| :--- | :--- |
| [ MII ICU Canonicals auf ISiK 6 (Governance-Uebergang)  ](ConceptMap-mii-cm-kds-icu-isik6-canonicals.md) | Migration der ICU-Profil-Canonicals, deren fachlicher Gegenstand in ISiK 6 unter gematik-Canonical weitergefuehrt wird — reine URL-Zuordnung, keine Konformitaetsaussage von der 2026er KDS-Linie auf die in dieser BOM gepinnte 2027er Ballot-Linie. Automatisch erzeugt aus dem Aehnlichkeits-Matching des MII KDS Version-Differs (Element- bzw. Composition-Fingerprints, Jaccard-Index). Qualitaetsstatus nach MapQual/ISO TS 21564: D12 = automatisiert ohne abgeschlossene menschliche Validierung — Entwurf zur Kuratierung, nicht fuer den produktiven Einsatz. Zeilen mit equivalence=equivalent sind inhaltsgleiche Umbenennungen (Jaccard 1.0); relatedto-Zeilen tragen den Aehnlichkeits-Score im Kommentar. |
| [ MII KDS Profil-Canonicals 2026 auf 2027  ](ConceptMap-mii-cm-kds-profile-canonicals-2026-2027.md) | Migration der Profil-Canonicals (StructureDefinition.url) von der 2026er KDS-Linie auf die in dieser BOM gepinnte 2027er Ballot-Linie. Automatisch erzeugt aus dem Aehnlichkeits-Matching des MII KDS Version-Differs (Element- bzw. Composition-Fingerprints, Jaccard-Index). Qualitaetsstatus nach MapQual/ISO TS 21564: D12 = automatisiert ohne abgeschlossene menschliche Validierung — Entwurf zur Kuratierung, nicht fuer den produktiven Einsatz. Zeilen mit equivalence=equivalent sind inhaltsgleiche Umbenennungen (Jaccard 1.0); relatedto-Zeilen tragen den Aehnlichkeits-Score im Kommentar. |
| [ MII KDS ValueSet-Canonicals 2026 auf 2027  ](ConceptMap-mii-cm-kds-vs-canonicals-2026-2027.md) | Migration der ValueSet-Canonicals von der 2026er KDS-Linie auf die in dieser BOM gepinnte 2027er Ballot-Linie. Automatisch erzeugt aus dem Aehnlichkeits-Matching des MII KDS Version-Differs (Element- bzw. Composition-Fingerprints, Jaccard-Index). Qualitaetsstatus nach MapQual/ISO TS 21564: D12 = automatisiert ohne abgeschlossene menschliche Validierung — Entwurf zur Kuratierung, nicht fuer den produktiven Einsatz. Zeilen mit equivalence=equivalent sind inhaltsgleiche Umbenennungen (Jaccard 1.0); relatedto-Zeilen tragen den Aehnlichkeits-Score im Kommentar. |

