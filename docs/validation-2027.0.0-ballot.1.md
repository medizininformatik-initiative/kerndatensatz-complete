# Validierungsbericht — BOM 2027.0.0-ballot.1

Stand: 2026-09-02 · HAPI FHIR 7.6.0 · alle 27 gepinnten Pakete aus dem Pre-Cache, kein Registry-Zugriff zur Laufzeit.

## Aufbau

BOM-Paket gebaut mit `./scripts/build-bom-package.sh`: 19 Module, **1371 Conformance-Ressourcen**, 1042 Examples, 11 MB, **0 Dateinamen-Kollisionen**.

HAPI startet in 30 Sekunden und indiziert **7144 Ressourcen** aus 27 Paketen — ohne einen einzigen Konflikt beim Laden.

## Die zentrale Frage: brechen die doppelten Canonicals?

**Nein.** Die Sorge war, dass Base und Meta transitiv in zwei Versionen gezogen werden (Issue `mii-kds-complete-d3d`), weil Bildgebung, Dokument, Studie und Kardiologie noch die 2026er Versionen deklarieren. Beim Laden der BOM tritt das nicht auf: die BOM pinnt je genau eine Version, HAPI lädt genau diese, es gibt keine doppelten Canonicals und keine Ladefehler.

Das Risiko bleibt für Konsumenten, die die Module **einzeln** statt über die BOM einbinden — genau dagegen hilft die BOM.

## Validierung: ein Beispiel je Modul, 16 Instanzen

| | Anzahl |
|---|---|
| Terminologie-Fehler | 14 |
| Strukturelle Fehler | 230 |

### Terminologie (14) — erwartbar

Kein Terminologieserver angebunden. ICD-10-GM, SNOMED CT und LOINC sind als `content=not-present` hinterlegt und können nicht expandiert werden. Ebenso fehlen ValueSets aus nur transitiv aufgelösten Paketen (`dvmd.kdl`, `ihe-d`, KBV). Kein Befund gegen die Module.

### Strukturell (230) — zwei echte Fehler

**1. Lungenfunktion 2027.0.0-ballot.rc1: mehrdeutiges Slicing** (224 der 230)

Das Profil `mii-pr-lungenfunktion-bodyplethysmographie` trennt seine Slices auf `DiagnosticReport.result` nicht sauber:

```
Element matches more than one slice - BF, FEV_FVC
Element matches more than one slice - BF, FEV
DiagnosticReport.result:BF: max allowed = 1, but found 14
```

Alle 14 Result-Einträge fallen in mehrere Slices gleichzeitig und landen zusätzlich alle in `BF`. **Das Modul validiert sein eigenes mitgeliefertes Beispiel nicht.** → `mii-kds-complete` Issue zum Slicing.

**2. 66 Profil-Referenzen ins Leere**

Beispiele verweisen in `meta.profile` auf StructureDefinitions, die in keinem gepinnten Paket enthalten sind:

| Modul | Referenzen | davon fehlend |
|---|---|---|
| ICU | 89 | **35** |
| MolGen | 73 | **14** |
| Kardiologie | 26 | **8** |
| MTB | 95 | **8** |
| Lungenfunktion | 64 | 1 |

Betroffen z.B. `mii-pr-icu-score-rass`, `mii-pr-icu-untersuchung-pupillenbefund`, `mii-pr-icu-ect-extrakorporales-verfahren`. Vermutlich umbenannt oder entfernt, ohne die Beispiele nachzuziehen.

### Kein Befund

Consent scheiterte an einer nicht auflösbaren Profilreferenz — das Profil *ist* im Paket, aber HAPI lädt Consent gar nicht (HAPI-1821-Workaround, Issue `mii-kds-complete-5e3`). Konfigurationslücke, kein Paketfehler.

## Nebenbefunde aus dem Build

- **ICU 2027.0.0**: zwei verschiedene ValueSets teilen sich dieselbe canonical URL (`mii-vs-icu-code-observation-extrakorporale-verfahren-loinc`). Verifiziert im unveränderten Registry-Paket.
- **Dokument und Seltene**: macOS-Resource-Forks (`._package.json`) in den publizierten Tarballs. Der Build filtert sie jetzt.
- **validation-server/Dockerfile**: der Pre-Cache lag unter `/root/.fhir/packages` mit Besitzer 1001, HAPI läuft aber als 65532 mit Home `/home/nonroot`. Der Cache war wirkungslos, HAPI lud bei jedem Start alle Pakete neu und scheiterte an `429 Too Many Requests`. Behoben.

## Reproduzieren

```bash
./scripts/check-module-versions.py      # Konsistenz + Registry-Abgleich
./scripts/build-bom-package.sh          # BOM-Paket bauen
cd validation-server && docker compose up -d hapi-fhir
```
