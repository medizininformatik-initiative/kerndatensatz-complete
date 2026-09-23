# Migration von v2026

Leitfaden für Standorte und Projekte, die von der 2026er KDS-Linie auf die
**2027er Ballot-Linie** dieser BOM wechseln. Die zugrunde liegenden Zahlen und
der Profil-für-Profil-Vergleich stehen auf der Seite
[Versionierung](versionierung.html); hier steht, **was zu tun ist**.

<img src="migration-2026-2027.svg" alt="Migrationsaufwand je Modul: Zusammensetzung der Profil-Übergänge von v2026 in die gepinnte Ballot-Version" style="max-width:100%"/>

<small>Generiert mit <code>scripts/migration-viz.py</code>. Grau = kein
Handlungsbedarf, Blau = nur Erweiterungen, Orange = breaking, Rot =
Canonical-Abriss. Sortiert nach Handlungsbedarf.</small>

### 1. Dependency umstellen

Eine Abhängigkeit statt 21: die BOM pinnt alle Module und die externen Pakete
in geprüft kompatiblen Versionen (siehe [Installation](index.html#installation)).
Beim Wechsel von einzeln deklarierten 2026er-Modulen die Einzeldeklarationen
**entfernen** — sonst entstehen doppelte Canonicals beim Auflösen.

Die 2027er Linie ist untereinander kohärent: Base und Meta werden nur noch in
je einer Version gezogen, die Validierungsprobleme durch doppelte Canonicals
der frühen Ballot-Phase entfallen.

### 2. Canonical-Umbenennungen migrieren (wichtigster Schritt)

Einige Module haben Profil-URLs umbenannt — Instanzen mit `meta.profile` auf
die alten Canonicals validieren dann gegen nichts mehr:

- **ICU**: die große Welle (nur 25 von 69 URLs bleiben) geschah **schon im
  stabilen Release `2026.0.2 → 2026.0.3`**. Wer von `2026.0.2` oder älter
  kommt, muss die Canonicals unabhängig vom Ballot migrieren; `2027.0.0-ballot.3`
  führt die neuen URLs unverändert weiter.
- **Mikrobiologie**: 6 Umbenennungen an der Ballot-Grenze.
- **Molekulargenetik**: 4 Umbenennungen.

Die kuratierte Zuordnung alt → neu entsteht in der
[Rename-Kandidatenliste](https://github.com/medizininformatik-initiative/mii-kerndatensatz-versionhistory/blob/main/data/rename-candidates-2027.csv)
(Ähnlichkeits-Matching über Element-Fingerprints; Spalte `confirmed` zeigt den
Kuratierungsstand). Für ETL-Strecken heißt das: `meta.profile`-Werte per
Mapping-Tabelle ersetzen, Profil-basierte Routing-/Validierungsregeln anpassen.

### 3. Breaking-Änderungen prüfen

41 Profil-Übergänge sind strukturell breaking (Elemente entfernt oder
inkompatibel geändert) — Schwerpunkte **Onkologie (12)**, Mikrobiologie (7),
Seltene Erkrankungen (7), Bildgebung (3), ICU (3). Welche Elemente konkret,
zeigt der [Version-History-Explorer](https://medizininformatik-initiative.github.io/mii-kerndatensatz-versionhistory/)
je Profil (bzw. `profile-pairwise-changes.csv` im selben Repo, Spalten
`elements_removed`/`elements_added`).

Die Mehrheit der Übergänge ist unkritisch: 79 Profile identisch, 200 nur
erweitert — bestehende Instanzen bleiben dort gültig.

#### Breaking-Änderungen im Detail

<!-- BREAKING-LIST:START -->

<details><summary><b>base</b> — 1 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_Diagnose_Condition</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><code>Condition.onset[x]:onsetPeriod</code>, <code>Condition.onset[x]:onsetPeriod.end</code>, <code>Condition.onset[x]:onsetPeriod.end.extension</code>, <code>Condition.onset[x]:onsetPeriod.end.extension:lebensphase-bis</code>, <code>Condition.onset[x]:onsetPeriod.end.extension:lebensphase-bis.url</code>, <code>Condition.onset[x]:onsetPeriod.end.extension:lebensphase-bis.value[x]</code>, <code>Condition.onset[x]:onsetPeriod.end.extension:lebensphase-bis.value[x].coding</code>, <code>Condition.onset[x]:onsetPeriod.end.extension:lebensphase-bis.value[x].coding.code</code> … +9 weitere</td></tr>
</table></details>
<details><summary><b>bildgebung</b> — 3 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_Bildgebung_Bildgebungsprozedur</td><td><code>2026.0.0</code> → <code>2027.0.0-ballot.1</code></td><td><code>Procedure.category.coding:sct.display</code></td></tr>
<tr><td>MII_PR_Bildgebung_Radiologische_Befundungsprozedur</td><td><code>2026.0.0</code> → <code>2027.0.0-ballot.1</code></td><td><code>Procedure.category.coding:sct.display</code>, <code>Procedure.code.coding:sct.display</code></td></tr>
<tr><td>MII_PR_Bildgebung_Radiologischer_Befund</td><td><code>2026.0.0</code> → <code>2027.0.0-ballot.1</code></td><td><code>DiagnosticReport.category.coding:diagnostic-service-sections.code</code>, <code>DiagnosticReport.category.coding:diagnostic-service-sections.display</code>, <code>DiagnosticReport.category.coding:diagnostic-service-sections.system</code>, <code>DiagnosticReport.category.coding:loinc.code</code>, <code>DiagnosticReport.category.coding:loinc.display</code>, <code>DiagnosticReport.category.coding:loinc.system</code>, <code>DiagnosticReport.category.coding:sct.code</code>, <code>DiagnosticReport.category.coding:sct.display</code> … +1 weitere</td></tr>
</table></details>
<details><summary><b>biobank</b> — 1 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>ProfileSpecimenBioprobeCore</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
</table></details>
<details><summary><b>consent</b> — 1 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_Consent_Einwilligung</td><td><code>2026.0.0</code> → <code>2027.0.0-ballot</code></td><td><code>Consent.category:loinc</code>, <code>Consent.category:loinc.coding</code>, <code>Consent.category:loinc.coding.code</code>, <code>Consent.category:loinc.coding.system</code>, <code>Consent.extension</code>, <code>Consent.extension:domainReference</code>, <code>Consent.extension:domainReference.extension</code>, <code>Consent.extension:domainReference.extension:domain</code> … +8 weitere</td></tr>
</table></details>
<details><summary><b>icu</b> — 3 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_ICU_Score</td><td><code>2026.0.0</code> → <code>2027.0.0-ballot.3</code></td><td><code>Observation.bodySite</code>, <code>Observation.category:assessment-scale.coding.code</code>, <code>Observation.category:assessment-scale.coding.system</code>, <code>Observation.category:survey.coding.code</code>, <code>Observation.category:survey.coding.system</code>, <code>Observation.component.interpretation</code>, <code>Observation.note</code>, <code>Observation.referenceRange</code></td></tr>
<tr><td>MII_PR_ICU_Score_RASS</td><td><code>2026.0.0</code> → <code>2027.0.0-ballot.3</code></td><td><code>Observation.value[x]:valueCodeableConcept</code>, <code>Observation.value[x]:valueCodeableConcept.coding</code>, <code>Observation.value[x]:valueCodeableConcept.coding:loinc</code>, <code>Observation.value[x]:valueCodeableConcept.extension</code>, <code>Observation.value[x]:valueCodeableConcept.extension:ordinalValue</code></td></tr>
<tr><td>MII_PR_ICU_VENT_Mittlerer_Beatmungsdruck</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot.3</code></td><td><code>Observation.effective[x]</code>, <code>Observation.value[x]:valueQuantity</code></td></tr>
</table></details>
<details><summary><b>laborbefund</b> — 2 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>DiagnosticReportLab</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot</code></td><td><code>DiagnosticReport.category:lab-category</code>, <code>DiagnosticReport.category:lab-category.coding</code>, <code>DiagnosticReport.category:lab-category.coding.code</code>, <code>DiagnosticReport.category:lab-category.coding.display</code>, <code>DiagnosticReport.category:lab-category.coding.system</code></td></tr>
<tr><td>ObservationLab</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot</code></td><td><code>Observation.category.coding:loinc-observation</code>, <code>Observation.category.coding:observation-category</code></td></tr>
</table></details>
<details><summary><b>mikrobiologie</b> — 7 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_Mikrobio_Diagnostic_Report</td><td><code>2025.0.2</code> → <code>2027.0.0-ballot2</code></td><td><code>DiagnosticReport.category.coding</code>, <code>DiagnosticReport.category.coding:loinc-microbiology-specialization</code>, <code>DiagnosticReport.category.coding:snomed-microbiology-studies</code></td></tr>
<tr><td>MII_PR_Mikrobio_Empfindlichkeit</td><td><code>2025.0.2</code> → <code>2027.0.0-ballot2</code></td><td><code>Observation.bodySite</code>, <code>Observation.category.coding</code>, <code>Observation.category.coding:loinc-microbiology-studies</code>, <code>Observation.category.coding:loinc-observation</code>, <code>Observation.category.coding:observation-category</code>, <code>Observation.component.value[x]</code>, <code>Observation.device</code>, <code>Observation.effective[x]</code> … +29 weitere</td></tr>
<tr><td>MII_PR_Mikrobio_Keimzahl</td><td><code>2025.0.2</code> → <code>2027.0.0-ballot2</code></td><td><code>Observation</code>, <code>Observation.bodySite</code>, <code>Observation.category.coding</code>, <code>Observation.category.coding:loinc-microbiology-studies</code>, <code>Observation.category.coding:loinc-observation</code>, <code>Observation.category.coding:observation-category</code>, <code>Observation.component.value[x]</code>, <code>Observation.device</code> … +29 weitere</td></tr>
<tr><td>MII_PR_Mikrobio_MRGN_Klasse</td><td><code>2025.0.2</code> → <code>2027.0.0-ballot2</code></td><td><code>Observation</code>, <code>Observation.bodySite</code>, <code>Observation.category.coding</code>, <code>Observation.category.coding:loinc-microbiology-studies</code>, <code>Observation.category.coding:loinc-observation</code>, <code>Observation.category.coding:observation-category</code>, <code>Observation.device</code>, <code>Observation.effective[x]</code> … +26 weitere</td></tr>
<tr><td>MII_PR_Mikrobio_Mikroskopie</td><td><code>2025.0.2</code> → <code>2027.0.0-ballot2</code></td><td><code>Observation</code>, <code>Observation.bodySite</code>, <code>Observation.category.coding</code>, <code>Observation.category.coding:loinc-microbiology-studies</code>, <code>Observation.category.coding:loinc-observation</code>, <code>Observation.category.coding:observation-category</code>, <code>Observation.component:BarlettScore</code>, <code>Observation.component:BarlettScore.code</code> … +38 weitere</td></tr>
<tr><td>MII_PR_Mikrobio_Virulenzfaktor</td><td><code>2025.0.2</code> → <code>2027.0.0-ballot2</code></td><td><code>Observation</code>, <code>Observation.bodySite</code>, <code>Observation.category.coding</code>, <code>Observation.category.coding:loinc-microbiology-studies</code>, <code>Observation.category.coding:loinc-observation</code>, <code>Observation.category.coding:observation-category</code>, <code>Observation.device</code>, <code>Observation.effective[x]</code> … +26 weitere</td></tr>
<tr><td>MII_PR_Mikrobio_voraussichtliche_Empfindlichkeit</td><td><code>2025.0.2</code> → <code>2027.0.0-ballot2</code></td><td><code>Observation</code>, <code>Observation.bodySite</code>, <code>Observation.category.coding</code>, <code>Observation.category.coding:loinc-microbiology-studies</code>, <code>Observation.category.coding:loinc-observation</code>, <code>Observation.category.coding:observation-category</code>, <code>Observation.device</code>, <code>Observation.effective[x]</code> … +26 weitere</td></tr>
</table></details>
<details><summary><b>mtb</b> — 2 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_MTB_Systemische_Therapie</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_MTB_Systemische_Vortherapie</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot.1</code></td><td><code>Procedure.basedOn</code>, <code>Procedure.basedOn:Therapieplan</code></td></tr>
</table></details>
<details><summary><b>onkologie</b> — 12 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_Onko_Allgemeiner_Leistungszustand_ECOG</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Onko_Allgemeiner_Leistungszustand_Karnofsky</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Onko_Diagnose_Primaertumor</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Onko_Fruehere_Tumorerkrankung</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Onko_Histologie_ICDO3</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Onko_Mamma_Operation</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><code>Procedure.performed[x]:performedDateTime</code></td></tr>
<tr><td>MII_PR_Onko_Nebenwirkung_Adverse_Event</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Onko_Prostata_Gleason_Grade_Group</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Onko_Prostata_Gleason_Pattern</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Onko_TNM_M_Kategorie</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><code>Observation.value[x].coding.system</code></td></tr>
<tr><td>MII_PR_Onko_TNM_N_Kategorie</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><code>Observation.value[x].coding.system</code></td></tr>
<tr><td>MII_PR_Onko_TNM_T_Kategorie</td><td><code>2026.0.3</code> → <code>2027.0.0-ballot.1</code></td><td><code>Observation.value[x].coding.system</code></td></tr>
</table></details>
<details><summary><b>patho</b> — 2 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_Patho_Report</td><td><code>2026.0.2</code> → <code>2027.0.0-ballot</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Patho_Specimen</td><td><code>2026.0.2</code> → <code>2027.0.0-ballot</code></td><td><code>Specimen.collection.bodySite.extension:lateralityQualifier</code>, <code>Specimen.collection.bodySite.extension:locationQualifier</code></td></tr>
</table></details>
<details><summary><b>seltene</b> — 7 Profile mit Breaking-Änderungen</summary>
<table><tr><th>Profil</th><th>Übergang</th><th>entfernte Elemente</th></tr>
<tr><td>MII_PR_Seltene_Blutgruppe</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Seltene_ClinicalDiagnosis</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><code>Condition.abatement[x]</code></td></tr>
<tr><td>MII_PR_Seltene_GeneticDiagnosis</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><code>Condition.abatement[x]</code></td></tr>
<tr><td>MII_PR_Seltene_Kopfumfang</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><i>inkompatible Änderung ohne entfernte Elemente (Kardinalität/Typ/Binding — siehe Explorer)</i></td></tr>
<tr><td>MII_PR_Seltene_Therapieempfehlung</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><code>MedicationRequest.extension:Evidenzgraduierung</code></td></tr>
<tr><td>MII_PR_Seltene_TherapieempfehlungNichtMedikamentoes</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><code>ServiceRequest.extension:Evidenzgraduierung</code></td></tr>
<tr><td>MII_PR_Seltene_Therapieempfehlung_Kombination</td><td><code>2026.0.1</code> → <code>2027.0.0-ballot</code></td><td><code>RequestGroup.extension:Evidenzgraduierung</code></td></tr>
</table></details>

<small>41 Breaking-Übergänge · Stand: 2026-09-23 · generiert mit <code>scripts/version-transitions.py</code></small>
<!-- BREAKING-LIST:END -->

### 4. Externe Abhängigkeiten anheben

| Paket | 2026er Streuung | 2027er Stand |
|-------|-----------------|--------------|
| `de.basisprofil.r4` | 1.5.x / 1.6.0, teils Tippfehler | einheitlich **1.6.0** |
| `de.gematik.isik` | 5.1.x / 6.0.0 | **6.0.0** (nur Patho noch 5.1.2) |
| `hl7.terminology.r4` | 5.0.0 – 7.2.0 | **7.3.0** (Nachzügler 7.1.0) |
| `hl7.fhir.uv.extensions.r4` | 5.1.0 / 5.2.0 | **5.3.0** (Nachzügler 5.2.0) |
| `eu.miabis.r4` | 0.2.0 | **1.3.0** — neue MIABIS-Pfade ohne `/fhir/`-Segment |

Lokale Ableitungen von diesen Paketen (eigene Profile auf ISiK-/Basisprofil-Basis)
auf die neuen Versionen heben.

### 5. Neue Module einplanen

**Kardiologie, Lungenfunktion, Soziodemographie und Symptome** sind neu in der
BOM — rein additiv, kein Migrationsaufwand, aber ggf. neue Datenquellen für
das DIZ-Mapping.

### 6. Validieren

Der [Validation-Server](https://github.com/medizininformatik-initiative/kerndatensatz-complete/tree/main/validation-server)
der BOM (HAPI + Blaze, vorkonfiguriert mit allen Pins) eignet sich als
Migrations-Prüfstand: 2026er Bestandsinstanzen dagegen validieren zeigt
Renames (Profil unbekannt) und Breaking-Änderungen (Validierungsfehler)
unmittelbar. Testdaten zum Vergleich liefert
[mii-testdata](https://github.com/medizininformatik-initiative/mii-testdata);
den Abdeckungsstand zeigt die Seite [Testabdeckung](testabdeckung.html).

> **Status**: Die 2027er Linie ist ein Ballot-Arbeitsstand. Produktive
> Migrationen sollten auf das finale 2027-Release warten — dieser Leitfaden
> dient der Aufwandsabschätzung und der Ballot-Prüfung.
