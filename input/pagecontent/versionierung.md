# Versionierung

### Versionsschema

Die KDS-Module und diese BOM versionieren nach **CalVer**: `JJJJ.minor.patch`
bezeichnet die Generation (z.B. `2026.0.1`, `2027.0.0`), Vorabstände tragen
Suffixe (`-ballot`, `-ballot.1`, `-rc…`, `-alpha…`). Wichtig für Werkzeuge:
Eine finale CalVer sortiert **über** jedem gleichnamigen Vorabstand — deshalb
pinnt die BOM Versionen exakt und pflegt in
[`ignored-versions.json`](https://github.com/medizininformatik-initiative/kerndatensatz-complete/blob/main/ignored-versions.json)
bekannte Fehlpublikationen (aktuell `icu 2027.0.0`: versehentlich publiziert,
unvollständig, niemals auflösen).

Die BOM selbst versioniert als `2027.0.0-ballot.N` — jedes Inkrement `N`
dokumentiert eine geprüfte Neuzusammenstellung der Modul-Pins, nachvollziehbar
in der Commit-Historie.

### Übergang in die 2027er Ballot-Linie

Die Tabelle fasst je Modul zusammen, wie sich die Profile von der letzten
Vorversion zur gepinnten Ballot-Version verändert haben — Datengrundlage ist
der [MII KDS Version-History-Explorer](https://medizininformatik-initiative.github.io/mii-kerndatensatz-versionhistory/),
der alle publizierten Profilversionen seit 2019 strukturell vergleicht
(Subway-Map-Ansicht je Profil).

<!-- VERSION-TRANSITIONS:START -->

| Modul | gepinnte Version | Profil-Übergänge | identisch* | erweitert | breaking | Canonical-Abrisse |
|-------|------------------|-----------------:|-----------:|----------:|---------:|------------------:|
| base | `2027.0.0-ballot` | 7 | 3 | 3 | 1 | 0 |
| bildgebung | `2027.0.0-ballot.1` | 11 | 6 | 1 | 3 | 0 |
| biobank | `2027.0.0-ballot` | 11 | 0 | 10 | 1 | 0 |
| consent | `2027.0.0-ballot` | 3 | 0 | 2 | 1 | 0 |
| dokument | `2027.0.0-ballot.2` | 1 | 0 | 1 | 0 | 0 |
| icu | `2027.0.0-ballot.3` | 76 | 4 | 68 | 3 | 0 |
| kardiologie | `2027.0.0-ballot` | _neu_ | 0 | 0 | 0 | 0 |
| laborbefund | `2027.0.0-ballot` | 3 | 0 | 1 | 2 | 0 |
| lungenfunktion | `2027.0.0-ballot.1` | _neu_ | 0 | 0 | 0 | 0 |
| medikation | `2027.0.0-ballot` | 5 | 3 | 2 | 0 | 0 |
| meta | `2027.0.0-ballot` | 1 | 0 | 1 | 0 | 0 |
| mikrobiologie | `2027.0.0-ballot2` | 7 | 0 | 0 | 7 | 6 |
| molgen | `2027.0.0-ballot.1` | 16 | 4 | 11 | 0 | 0 |
| mtb | `2027.0.0-ballot.1` | 49 | 2 | 45 | 2 | 0 |
| onkologie | `2027.0.0-ballot.1` | 73 | 15 | 42 | 12 | 0 |
| patho | `2027.0.0-ballot` | 17 | 14 | 1 | 2 | 0 |
| pros | `2027.0.0-ballot.1` | 23 | 22 | 1 | 0 | 0 |
| seltene | `2027.0.0-ballot` | 17 | 6 | 4 | 7 | 0 |
| soziodemographie | `2027.0.0-ballot` | _neu_ | 0 | 0 | 0 | 0 |
| studie | `2027.0.0-ballot` | 7 | 0 | 7 | 0 | 0 |
| symptom | `2027.0.0-ballot` | _neu_ | 0 | 0 | 0 | 0 |
| **Summe** | | **327** | **79** | **200** | **41** | **6** |

<small>*identisch = strukturgleich oder nur Canonical-Metadaten geändert. Übergänge = Profile mit durchgehender Canonical von der letzten Vorversion zur gepinnten Version; Canonical-Abrisse (beendete URLs, meist Umbenennungen) erscheinen nicht als Übergang — siehe Abschnitt Canonical-Kontinuität. Stand: 2026-09-23 · generiert mit <code>scripts/version-transitions.py</code> aus dem <a href="https://medizininformatik-initiative.github.io/mii-kerndatensatz-versionhistory/">Version-History-Explorer</a>-Datensatz</small>
<!-- VERSION-TRANSITIONS:END -->

### Canonical-Kontinuität

Nicht jede Profil-Änderung ist ein Übergang: Wenn ein Modul die **Canonical-URL
umbenennt**, endet die alte Linie und eine neue beginnt — für Standorte wirkt
das wie ein entferntes plus ein neues Profil, auch wenn die Struktur identisch
ist. Der markanteste Fall ist die **ICU-Umbenennungswelle**: Sie geschah bereits
im stabilen Release `2026.0.2 → 2026.0.3` (nur 25 von 69 URLs überleben);
`2027.0.0-ballot.3` führt die neuen URLs unverändert weiter. Wer von
`icu 2026.0.2` kommt, migriert die Canonicals also unabhängig vom Ballot.

Die Zuordnung alt → neu wird werkzeuggestützt kuratiert
([Rename-Kandidatenliste](https://github.com/medizininformatik-initiative/mii-kerndatensatz-versionhistory/blob/main/data/rename-candidates-2027.csv),
Ähnlichkeits-Matching über Element-Fingerprints) und fließt als Lineage in den
Explorer ein, damit umbenannte Profile als durchgehende Linien erscheinen.

### Abgrenzung

Der Strukturvergleich betrachtet StructureDefinitions (Elemente,
Kardinalitäten, Must-Support, Binding-Ziele). **Terminologische Änderungen** —
ValueSet-Zusammensetzungen bei gleichbleibender Canonical, Code-Umstellungen,
CodeSystem-Versionen — sind bewusst nicht Teil dieser Auswertung; ein
„identisches" Profil kann also gegen andere Codes validieren. Eine separate
Bewertung der ValueSets ist geplant.
