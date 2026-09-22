# Testabdeckung - MII Kerndatensatz Complete v2027.0.0-ballot.19

* [**Table of Contents**](toc.md)
* **Testabdeckung**

## Testabdeckung

# Testabdeckung

Die MII-Testdaten bestehen aus zwei Schichten mit unterschiedlichen Zielen (siehe [mii-testdata](https://github.com/medizininformatik-initiative/mii-testdata)): **klinisch plausible Patienten-Bundles**, die das Zusammenspiel der Module testen, und **technische Modul-Instanzen**, deren Zweck die messbare Abdeckung der Profile ist. Die Vollständigkeitsmetrik der technischen Schicht ist die **Must-Support-Coverage**: der Anteil der MS-Elemente eines Moduls, die von mindestens einer Testdaten-Instanz befüllt werden.

### MS-Coverage gegen die Profile dieser BOM

Gemessen werden die Instanzen des jüngsten [mii-testdata-Releases](https://github.com/medizininformatik-initiative/mii-testdata/releases) gegen die **in dieser BOM gepinnten Profilversionen**. Eine niedrige Zahl hat dabei drei mögliche Ursachen, die die Tabelle nicht unterscheidet:

1. **Es gibt noch keine Testdaten**— bei den neuen Modulen (Kardiologie, Lungenfunktion, Soziodemographie, Symptome) schlicht der Arbeitsvorrat.
1. **Canonical-Umbenennungen zwischen den KDS-Generationen**— etliche Module haben auf dem Weg zur 2027er Linie Profile umbenannt (ICU z.B. behält nur 25 von 69 URLs); vorhandene Testdaten zeigen per`meta.profile`noch auf die alten Canonicals und zählen deshalb nicht. Das behebt der anstehende Umzug der Testdaten auf die 2027er Abhängigkeiten.
1. **Der Release-Stand hinkt hinterher**— gemessen wird das publizierte Release, nicht der`main`-Branch der Testdaten.

Die absoluten MS-Zahlen je Modul gehören zur Interpretation dazu: Die Module setzen Must-Support sehr unterschiedlich großzügig, eine Prozentzahl allein vergleicht deshalb keine Module miteinander.

| | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| base | 2027.0.0-ballot | 8 | 6 | 485 | 231 | 47.6 % |
| bildgebung | 2027.0.0-ballot.1 | 12 | 0 | 395 | 0 | 0.0 % |
| biobank | 2027.0.0-ballot | 11 | 1 | 313 | 12 | 3.8 % |
| consent | 2027.0.0-ballot | 3 | 1 | 78 | 25 | 32.1 % |
| dokument | 2027.0.0-ballot.2 | 1 | 0 | 70 | 0 | 0.0 % |
| icu | 2027.0.0-ballot.3 | 93 | 0 | 3007 | 0 | 0.0 % |
| kardiologie | 2027.0.0-ballot | 13 | 0 | 366 | 0 | 0.0 % |
| laborbefund | 2027.0.0-ballot | 3 | 3 | 154 | 91 | 59.1 % |
| lungenfunktion | 2027.0.0-ballot.1 | 48 | 0 | 1956 | 0 | 0.0 % |
| medikation | 2027.0.0-ballot | 5 | 5 | 441 | 307 | 69.6 % |
| meta | 2027.0.0-ballot | 1 | 0 | 0 | 0 | – |
| mikrobiologie | 2027.0.0-ballot2 | 21 | 0 | 1604 | 0 | 0.0 % |
| molgen | 2027.0.0-ballot.1 | 16 | 0 | 248 | 0 | 0.0 % |
| mtb | 2027.0.0-ballot.1 | 50 | 0 | 1525 | 0 | 0.0 % |
| onkologie | 2027.0.0-ballot.1 | 76 | 0 | 2050 | 0 | 0.0 % |
| patho | 2027.0.0-ballot | 15 | 3 | 479 | 24 | 5.0 % |
| pros | 2027.0.0-ballot.1 | 23 | 0 | 346 | 0 | 0.0 % |
| seltene | 2027.0.0-ballot | 23 | 0 | 618 | 0 | 0.0 % |
| soziodemographie | 2027.0.0-ballot | 15 | 0 | 153 | 0 | 0.0 % |
| studie | 2027.0.0-ballot | 7 | 1 | 79 | 3 | 3.8 % |
| symptom | 2027.0.0-ballot | 0 | 0 | 0 | 0 | – |
| **Gesamt** |   | **444** | **20** | **14367** | **693** | **4.8 %** |

#### Details je Profil

Stand: 2026-09-22 · Testdaten: [mii-testdata v2026.0.0-rc.1](https://github.com/medizininformatik-initiative/mii-testdata/releases/tag/v2026.0.0-rc.1) (268 Instanzen) · gemessen gegen die BOM-Pins · generiert mit `scripts/testdata-coverage.py` 

Die Detail-Auswertung (unbedeckte Element-IDs je Profil) liefert [`ms-coverage.py`](https://github.com/medizininformatik-initiative/mii-testdata/pull/46) im mii-testdata-Repo; die Schichten-Definition steht in [PR #45](https://github.com/medizininformatik-initiative/mii-testdata/pull/45).

