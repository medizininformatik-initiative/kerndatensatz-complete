# Validierungsbericht — BOM 2027.0.0-ballot.1

Stand: 2026-09-03 · HAPI FHIR 7.6.0 · alle 27 gepinnten Pakete als lokale Tarballs, verifiziert offline (`--network none`).

## Aufbau

BOM-Paket gebaut mit `./scripts/build-bom-package.sh`: 19 Module, **1373 Conformance-Ressourcen**, 1047 Examples, 11 MB, **0 Dateinamen-Kollisionen**.

HAPI startet in 26 Sekunden und indiziert **7049 Ressourcen** aus 27 Paketen — ohne einen einzigen Konflikt beim Laden.

### Wie die Pakete zu HAPI kommen

**HAPIs `JpaPackageCache` liest den Dateisystem-Cache unter `~/.fhir/packages` nicht.** Ohne weitere Konfiguration lädt der Server bei jedem Start jedes Paket erneut von `packages.fhir.org` — und scheitert dort früher oder später an `429 Too Many Requests` mit `HAPI-1301: Unable to locate package`. Ein Lauf, der durchgeht, ist dann Zufall, kein Beleg.

Der Server bekommt die Pakete deshalb über `packageUrl: file:///app/packages/<name>-<version>.tgz`. Der Dockerfile lädt die Tarballs im Build, bereinigt sie (base64-PNGs wegen HAPI-1821, Examples, macOS-Resource-Forks) und packt sie neu; ein fehlgeschlagener Download bricht den Build jetzt ab, statt still ein unvollständiges Image zu erzeugen.

Gegenprobe: `docker run --network none` startet den Server vollständig durch — 7049 Ressourcen, 0 Registry-Versuche, 0 Ladefehler.

## Die zentrale Frage: brechen die doppelten Canonicals?

**Nein.** Die Sorge war, dass Base und Meta transitiv in zwei Versionen gezogen werden (Issue `mii-kds-complete-d3d`), weil Bildgebung, Dokument, Studie und Kardiologie noch die 2026er Versionen deklarieren. Beim Laden der BOM tritt das nicht auf: die BOM pinnt je genau eine Version, HAPI lädt genau diese, es gibt keine doppelten Canonicals und keine Ladefehler.

Das Risiko bleibt für Konsumenten, die die Module **einzeln** statt über die BOM einbinden — genau dagegen hilft die BOM.

## Validierung: ein Beispiel je Modul, 16 Instanzen

| | Anzahl |
|---|---|
| Terminologie-Fehler | 15 |
| Strukturelle Fehler | 238 |

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

### Laborbefund 2027.0.0-ballot.rc3 — ohne Befund

Alle sechs mitgelieferten Beispiele validieren **fehlerfrei** gegen ihre Profile: 0 Terminologie-, 0 strukturelle Fehler.

## Nebenbefunde aus dem Build

- **ICU 2027.0.0**: zwei verschiedene ValueSets teilen sich dieselbe canonical URL (`mii-vs-icu-code-observation-extrakorporale-verfahren-loinc`). Verifiziert im unveränderten Registry-Paket.
- **Dokument und Seltene**: macOS-Resource-Forks (`._package.json`) in den publizierten Tarballs. Der Build filtert sie jetzt.
- **validation-server/Dockerfile**: der Pre-Cache unter `~/.fhir/packages` war grundsätzlich wirkungslos (siehe oben) und der Download-Loop prüfte nicht, ob `curl` erfolgreich war — ein unvollständiges Image lief grün durch. Beides behoben: lokale Tarballs über `packageUrl`, Retry über beide Registries, harter Abbruch bei Fehlschlag.

## Reproduzieren

```bash
./scripts/check-module-versions.py      # Konsistenz + Registry-Abgleich
./scripts/build-bom-package.sh          # BOM-Paket bauen
cd validation-server && docker compose up -d hapi-fhir
```
