# Reifegrad der KDS-Module

BOM `2027.0.0-ballot.10` · 20 Module · automatisch erzeugt von `scripts/build-status.py`

Der Reifegrad misst **Version und Abhängigkeiten zusammen**. Eine 2027er Versionsnummer allein sagt wenig — entscheidend ist, worauf das Paket intern zeigt.

| Stufe | Module |
|---|---|
| **finale Linie** | base, biobank, consent, dokument, kardiologie, laborbefund, medikation, meta, molgen, patho, pros, symptom |
| **Nummer ohne Umzug** | bildgebung, icu, lungenfunktion, mikrobiologie, studie |
| **noch 2026** | mtb, onkologie, seltene |

**30 offene 2026er Referenzen** über alle Module.

## Je Modul

| Modul | Version | Deps | offen auf 2026 | auf RCs |
|---|---|---|---|---|
| mtb | `2026.0.1` | 9 | base, biobank, consent, medikation, meta, molgen, onkologie, patho, studie | — |
| onkologie | `2026.0.3` | 6 | biobank, medikation, meta, molgen, base, studie | — |
| seltene | `2026.0.1` | 6 | meta, molgen, icu, studie, base, medikation | — |
| bildgebung | `2027.0.0-ballot.rc2` | 3 | meta, base, medikation | — |
| lungenfunktion | `2027.0.0-ballot.rc2` | 3 | meta, base, medikation | — |
| icu | `2027.0.0` | 1 | base | — |
| mikrobiologie | `2027.0.0-alpha.5` | 1 | laborbefund | — |
| studie | `2027.0.0-ballot.rc1` | 1 | meta | — |
| base | `2027.0.0-ballot` | 1 | — | — |
| biobank | `2027.0.0-ballot` | 1 | — | — |
| consent | `2027.0.0-ballot.rc1` | 0 | — | — |
| dokument | `2027.0.0-ballot.2` | 2 | — | — |
| kardiologie | `2027.0.0-ballot` | 2 | — | — |
| laborbefund | `2027.0.0-ballot` | 1 | — | — |
| medikation | `2027.0.0-ballot` | 1 | — | — |
| meta | `2027.0.0-ballot` | 0 | — | — |
| molgen | `2027.0.0-ballot.1` | 3 | — | — |
| patho | `2027.0.0-ballot` | 3 | — | — |
| pros | `2027.0.0-ballot.1` | 1 | — | — |
| symptom | `2027.0.0-ballot` | 1 | — | — |

## Graph

![Abhängigkeiten und Reifegrad](dependency-graph.png)

Quelle: `dependency-graph.dot`. Neu rendern mit

```bash
./scripts/build-status.py
```
