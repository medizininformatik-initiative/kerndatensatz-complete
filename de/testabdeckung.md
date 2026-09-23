# Testabdeckung - MII Kerndatensatz Complete v2027.0.0-ballot.19

* [**Table of Contents**](toc.md)
* **Testabdeckung**

## Testabdeckung

# Testabdeckung

Die MII-Testdaten bestehen aus zwei Schichten mit unterschiedlichen Zielen (siehe [mii-testdata](https://github.com/medizininformatik-initiative/mii-testdata)): **klinisch plausible Patienten-Bundles**, die das Zusammenspiel der Module testen, und **technische Modul-Instanzen**, deren Zweck die messbare Abdeckung der Profile ist. Die Vollständigkeitsmetrik der technischen Schicht ist die **Must-Support-Coverage**: der Anteil der MS-Elemente eines Moduls, die von mindestens einer Testdaten-Instanz befüllt werden.

### MS-Coverage gegen die Profile dieser BOM

Gemessen werden die Testdaten-Instanzen gegen die **in dieser BOM gepinnten Profilversionen**. Mit dem Umzug der Testdaten auf die 2027er Ballot-Linie sind die früheren Hauptursachen niedriger Zahlen entfallen: Die Canonical-Umbenennungen sind nachgezogen, und alle Module — auch die neuen (Kardiologie, Lungenfunktion, Soziodemographie, Symptome) — haben eigene Instanzen.

Was in den verbleibenden Lücken steckt, ist auf der [Testabdeckung-Seite der Testdaten](https://medizininformatik-initiative.github.io/mii-testdata/testabdeckung.html) nach vier Kategorien aufgeschlüsselt: Upstream-Widersprüche (Profile, bei denen ein MS-Element strukturell unerfüllbar ist), fachlich bewusst ausgelassene Elemente, nicht verifizierbare Terminologie und Messgrenzen der Heuristik.

**Zum Vergleich mit der Zahl im Testdaten-Repo:** Dort steht eine höhere Gesamt-Coverage, weil sie nur Profile zählt, für die überhaupt Instanzen existieren. Diese Tabelle rechnet strenger — **alle** Profile der BOM gehen in den Nenner ein, auch solche ohne jede Instanz (Spalte „mit Instanz"). Beide Zahlen sind korrekt, sie beantworten verschiedene Fragen: **Wie gut sind die vorhandenen Testdaten?** gegen **Wie viel des KDS ist überhaupt abgedeckt?**

Nicht in den Nenner gehen **unerreichbare Must-Support-Slices**: Schränkt ein Profil eine `[x]`-Choice auf einen Typ ein, bleiben die geerbten Slices der anderen Typen samt MS-Flag im Snapshot stehen, obwohl keine konforme Instanz sie befüllen kann (betrifft vor allem die Mikrobiologie). Details in den [Ballot-Findings](https://github.com/medizininformatik-initiative/mii-testdata/blob/main/docs/ballot-findings-2027.md).

Abstrakte Profile werden nicht gezählt, weil Instanzen sie nicht direkt claimen können — deshalb steht **Symptome** mit 0 Profilen in der Tabelle: das Modul publiziert ausschließlich abstrakte Profile (`MII_PR_Symptom_Observation`, `MII_PR_Symptom_Condition`), die zur Ableitung gedacht sind.

Die absoluten MS-Zahlen je Modul gehören zur Interpretation dazu: Die Module setzen Must-Support sehr unterschiedlich großzügig, eine Prozentzahl allein vergleicht deshalb keine Module miteinander.

| | | | | | | |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| base | 2027.0.0-ballot | 8 | 8 | 485 | 356 | 73.4 % |
| bildgebung | 2027.0.0-ballot.1 | 12 | 12 | 393 | 336 | 85.5 % |
| biobank | 2027.0.0-ballot | 11 | 11 | 313 | 288 | 92.0 % |
| consent | 2027.0.0-ballot | 3 | 3 | 78 | 62 | 79.5 % |
| dokument | 2027.0.0-ballot.2 | 1 | 1 | 70 | 57 | 81.4 % |
| icu | 2027.0.0-ballot.3 | 93 | 93 | 3005 | 2199 | 73.2 % |
| kardiologie | 2027.0.0-ballot | 13 | 13 | 365 | 327 | 89.6 % |
| laborbefund | 2027.0.0-ballot | 3 | 3 | 154 | 122 | 79.2 % |
| lungenfunktion | 2027.0.0-ballot.1 | 48 | 39 | 1956 | 1333 | 68.1 % |
| medikation | 2027.0.0-ballot | 5 | 5 | 441 | 429 | 97.3 % |
| meta | 2027.0.0-ballot | 1 | 0 | 0 | 0 | – |
| mikrobiologie | 2027.0.0-ballot2 | 21 | 21 | 1448 | 1078 | 74.4 % |
| molgen | 2027.0.0-ballot.1 | 16 | 16 | 248 | 180 | 72.6 % |
| mtb | 2027.0.0-ballot.1 | 50 | 50 | 1522 | 1186 | 77.9 % |
| onkologie | 2027.0.0-ballot.1 | 76 | 76 | 2038 | 1883 | 92.4 % |
| patho | 2027.0.0-ballot | 15 | 14 | 479 | 398 | 83.1 % |
| pros | 2027.0.0-ballot.1 | 23 | 21 | 346 | 287 | 82.9 % |
| seltene | 2027.0.0-ballot | 23 | 23 | 618 | 568 | 91.9 % |
| soziodemographie | 2027.0.0-ballot | 15 | 15 | 153 | 144 | 94.1 % |
| studie | 2027.0.0-ballot | 7 | 7 | 79 | 75 | 94.9 % |
| symptom | 2027.0.0-ballot | 0 | 0 | 0 | 0 | – |
| **Gesamt** |   | **444** | **431** | **14191** | **11308** | **79.7 %** |

#### Details je Profil

Stand: 2026-09-23 · Testdaten: [mii-testdata](https://github.com/medizininformatik-initiative/mii-testdata), Branch `main` (1072 Instanzen) — das jüngste publizierte Release ist noch die 2026er Linie · gemessen gegen die BOM-Pins · generiert mit `scripts/testdata-coverage.py` 

Die Detail-Auswertung (unbedeckte Element-IDs je Profil) liefert [`scripts/ms-coverage.py`](https://github.com/medizininformatik-initiative/mii-testdata/blob/main/scripts/ms-coverage.py) im mii-testdata-Repo; die Schichten-Definition steht in [PR #45](https://github.com/medizininformatik-initiative/mii-testdata/pull/45).

