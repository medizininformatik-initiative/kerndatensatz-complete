# Namens-Inventur der KDS-Module

Stand: 2026-09-03 · Quellen: `sushi-config.yaml` und `package.json`, GitHub-Tags/Releases, Package-Registry.

> **Korrektur.** Die erste Fassung las nur den **Default-Branch**. Das ist bei mehreren
> Modulen der falsche Stand: die 2027er Ballot-Arbeit läuft auf `migration/*`- und
> `release/*`-Branches, die vom Default-Branch aus unsichtbar sind. Die Tabelle unten
> zeigt weiterhin den Default-Branch; der Abschnitt
> [Führender Branch](#führender-branch-weicht-vom-default-ab) nennt die Abweichungen.

## Übersicht

| Repo | IG-ID (`sushi-config.id`) | IG-Name (`name`) | Package-ID | Version laut sushi | Letzter Tag | Registry |
|---|---|---|---|---|---|---|
| kerndatensatz-basis | `mii-ig-base` | MII_IG_Base | …kerndatensatz.base | 2027.0.0-ballot.rc1 | v2027.0.0-ballot.rc1 | 2027.0.0-ballot.rc1 |
| kerndatensatz-meta | `mii-ig-meta` | MII_IG_Meta | …kerndatensatz.meta | 2027.0.0-ballot.rc3 | v2027.0.0-ballot.rc3 | 2027.0.0-ballot.rc3 |
| kerndatensatzmodul-labor | `mii-ig-labor` | MII_IG_Labor | …kerndatensatz.**laborbefund** | 2027.0.0-ballot.rc3 | v2027.0.0-ballot.rc3 | 2027.0.0-ballot.rc3 |
| kerndatensatzmodul-medikation | `mii-ig-medikation` | MII_IG_Medikation | …kerndatensatz.medikation | 2026.0.1 | v2026.0.1 | 2026.0.1 |
| kerndatensatz-dokument | `mii-ig-dokument` | MII_IG_Dokument | …kerndatensatz.dokument | 2027.0.0-ballot.rc1 | v2027.0.0-ballot.rc1 | 2027.0.0-ballot.rc1 |
| kerndatensatz-bildgebung | `mii-ig-bildgebung` | MII_IG_Bildgebung | …kerndatensatz.bildgebung | **2027.0.0-ballot.rc1** | 2027.0.0-ballot.rc**2** | 2027.0.0-ballot.rc2 |
| kerndatensatz-lungenfunktion | `mii-ig-lungenfunktion` | MII_IG_Lungenfunktion | …kerndatensatz.lungenfunktion | 2027.0.0-ballot.rc1 | — | 2027.0.0-ballot.rc1 |
| kerndatensatz-soziodemographie | `mii-ig-soziodemographie` | MII_IG_Soziodemographie | …kerndatensatz.soziodemographie | 2027.0.0-ballot.rc1 | — | **nicht publiziert** |
| kerndatensatzmodul-proms | `mii-ig-pro` | MII_IG_PRO | …kerndatensatz.**pros** | 2026.7.0 | v2026.7.0 | 2026.7.0 |
| kerndatensatzmodul-studie | `mii-ig-studie` | MII_IG_Medizinisches_Forschungsvorhaben | …kerndatensatz.studie | 2027.0.0-ballot.rc1 | v2027.0.0-ballot.rc1 | 2027.0.0-ballot.rc1 |
| kerndatensatzmodul-biobank | `mii-ig-biobank-de-**v2026**` | MII_IG_Biobank_DE | …kerndatensatz.biobank | 2027.0.0-ballot.rc2 | v2027.0.0-ballot.rc1 | 2027.0.0-ballot.rc2 |
| kerndatensatzmodul-GenetischeTests | `mii-ig-molgen-de-**v2026**` | MII_IG_MolGen_DE | …kerndatensatz.molgen | **2027.0.0-ballot.rc1** | v2026.0.4 | 2026.0.4 |
| kerndatensatzmodul-onkologie | `mii-ig-onko-de-**v2026**` | MII_IG_Onko_DE | …kerndatensatz.onkologie | 2026.0.3 | v2026.0.0 | 2026.0.3 |
| kerndatensatzmodul-intensivmedizin | `mii-ig-icu-de-**v2026**` | MII_IG_ICU | …kerndatensatz.icu ⚠ | **2027.0.0-ballot.rc1** | v2026.0.2 | 2027.0.0 |
| kerndatensatzmodul-seltene-erkrankungen | `mii-ig-seltene-erkrankungen-**v2026**-de` | MIIIGModulSelteneErkrankungen | …kerndatensatz.seltene ⚠ | 2026.0.1 | v2026.0.1 | 2026.0.1 |
| kerndatensatzmodul-PathologieBefund | `mii-ig-modul-patho` | MII_IG_Modul_Patho | …kerndatensatz.patho | **2027.0.0-ballot.rc** ❌ | v2026.0.0 | 2026.0.2 |
| kerndatensatzmodul-molekulares-tumorboard | `mii-**kerndatensatzmodul**-molekulares-tumorboard` | MII_IG_MTB_DE | …kerndatensatz.mtb ⚠ | 2026.0.1 | v2026.0.1 | 2026.0.1 |
| kerndatensatz-kardiologie | `mii-**kerndatensatzmodul**-kardiologie` | MII_IG_MODUL_KARDIO_DE | …kerndatensatz.kardiologie ⚠ | 2027.0.0-ballot.rc1 | v2027.0.0-ballot.rc1 | 2027.0.0-ballot.rc1 |
| kerndatensatzmodul-mikrobiologie | `kerndatensatzmodul-mikrobiologie` ❌ | Kerndatensatzmodul Mikrobiologie | …kerndatensatz.mikrobiologie ❌ | 2027.0.0-alpha.6 | 2027.0.0-alpha.5 | 2027.0.0-alpha.5 |
| kerndatensatzmodul-symptome | `mii-ig-symptom` | MII_IG_Symptom | …kerndatensatz.symptom | 2026.0.0-rc.1 | v2024.0.0-ballot | 2024.0.0-ballot |
| kerndatensatzmodul-consent | — kein IG-Projekt — | — | …kerndatensatz.consent | — | — | 2026.0.1-rc-4 |

⚠ = `packageId` fehlt in `sushi-config.yaml`, kommt aus `package.json`
❌ = fehlerhaft

## Führender Branch weicht vom Default ab

Bei diesen Modulen trägt **nicht** der Default-Branch den Ballot-Stand:

| Modul | Default-Branch | führender Branch | was dort anders ist |
|---|---|---|---|
| medikation | `master` 2026.0.1 | `migration/2026.0.1-template…` | **2027.0.0-ballot.rc1** — die gesamte Ballot-Vorbereitung |
| symptome | `master` 2026.0.0-rc.1 | `migration/2027.0.0-ballot…` | **2027.0.0-ballot.rc1** |
| seltene | `dev` 2026.0.1, ID `mii-ig-seltene-erkrankungen-v2026-de` | `migration/2026.0.1-template…` | **2027.0.0-ballot.rc1** und ID bereinigt zu **`mii-ig-seltene`** |
| mikrobiologie | `main`, ID `kerndatensatzmodul-mikrobiologie` | Branch `v2027.0.0-ballot.rc1` | ID bereinigt zu **`mii-ig-mikrobiologie`** |

**Zwei der Namensprobleme sind also auf Branches längst behoben** — sie sind nur nie im
Default-Branch angekommen. Wer die Konventionsdiskussion führt, sollte das wissen: bei
seltene und mikrobiologie geht es nicht ums Ob, sondern ums Mergen.

Umgekehrt ist bei **onkologie** der Default-Branch (`dev`, 2026.0.3, ID `…-v2026`) der
gute Stand, während `main` mit 2026.0.0 und der ID `mii-ig-onko-de-**v2025**` zurückliegt.
Bei **meta** ist `main` korrekt auf ballot.rc3, während `dev` und `master` auf 2026.0.0
stehengeblieben sind.

## Was in keinem Branch und keinem Tag steht

| Modul | publiziert | wo die Version herkommt |
|---|---|---|
| bildgebung | 2027.0.0-ballot.**rc2** | Tag `2027.0.0-ballot.rc2` enthält intern `version: 2027.0.0-ballot.rc1` — die Nummer wurde in der Pipeline gesetzt, nie in der `sushi-config` |
| icu | **2027.0.0** (final) | weder Branch noch Tag; `main` steht auf `2027.0.0-ballot.rc1` |
| patho | **2026.0.2** | weder Branch noch Tag; `main` steht auf dem fehlerhaften `2027.0.0-ballot.rc` |

Bei diesen drei lässt sich aus dem Repository nicht rekonstruieren, aus welchem Stand das
publizierte Paket gebaut wurde.

## Die Brüche

### 1. Das Jahr klebt in der IG-ID

Fünf Module tragen `v2026` in der IG-ID, obwohl sie 2027er Ballot-Versionen bauen:

```
mii-ig-biobank-de-v2026              baut 2027.0.0-ballot.rc2
mii-ig-molgen-de-v2026               baut 2027.0.0-ballot.rc1
mii-ig-onko-de-v2026                 baut 2026.0.3
mii-ig-icu-de-v2026                  baut 2027.0.0-ballot.rc1
mii-ig-seltene-erkrankungen-v2026-de baut 2026.0.1
```

Die ID ist Teil der ImplementationGuide-Ressource und taucht in Canonicals auf. Eine Jahreszahl darin bedeutet entweder jährliche Umbenennung mit gebrochenen Referenzen oder eine dauerhaft irreführende ID.

### 2. Vier verschiedene ID-Konventionen

| Muster | Module |
|---|---|
| `mii-ig-<modul>` | base, meta, labor, medikation, dokument, bildgebung, lungenfunktion, soziodemographie, pro, studie, symptom, modul-patho |
| `mii-ig-<modul>-de-v2026` | biobank, molgen, onko, icu, seltene |
| `mii-kerndatensatzmodul-<modul>` | mtb, kardiologie |
| `<repo-name>` ohne Präfix | mikrobiologie |

### 3. Tags mal mit, mal ohne `v`

`v2027.0.0-ballot.rc1` (die meisten) gegen `2027.0.0-ballot.rc2` (bildgebung) und `2027.0.0-alpha.5` (mikrobiologie). Wer Tags automatisiert auf Versionen abbildet, muss beide Formen abfangen.

### 4. Package-Name weicht vom Modulnamen ab

| Repo/IG | Package |
|---|---|
| `mii-ig-labor` | `…kerndatensatz.laborbefund` |
| `mii-ig-pro` (Repo: proms) | `…kerndatensatz.pros` |

Dazu die laufende Umbenennung auf einem Labor-Branch von `laborbefund` nach `labor`.

### 5. Konkrete Fehler

- **Patho**: `version: 2027.0.0-ballot.rc` — die Nummer hinter `rc` fehlt. Keine gültige Version.
- **Mikrobiologie**: `releaseLabel: 2026.0.0-alpha.6` — dort gehört ein Label hin (`ballot`, `release`, `ci-build`), keine Version. Und die genannte Jahreszahl widerspricht `version: 2027.0.0-alpha.6`.
- **Mikrobiologie**: kein `packageId` in `sushi-config.yaml`, und `package.json` heißt `"name": "project"`. Die publizierte Package-ID `…kerndatensatz.mikrobiologie` steht in keiner der beiden Dateien — sie kommt aus der Build-Pipeline.
- **Consent** ist kein IG-Projekt: keine `sushi-config.yaml`, keine `ig.ini`, nur Profil- und Terminologie-Verzeichnisse. Das Package entsteht außerhalb des IG-Publisher-Wegs.

### 6. sushi-config, Tag und Registry driften auseinander

| Modul | sushi-config | Tag | Registry |
|---|---|---|---|
| molgen | 2027.0.0-ballot.rc1 | v2026.0.4 | 2026.0.4 |
| icu | 2027.0.0-ballot.rc1 | v2026.0.2 | **2027.0.0** |
| bildgebung | 2027.0.0-ballot.rc1 | 2027.0.0-ballot.rc2 | 2027.0.0-ballot.rc2 |
| onkologie | 2026.0.3 | v2026.0.0 | 2026.0.3 |
| patho | 2027.0.0-ballot.rc | v2026.0.0 | 2026.0.2 |
| symptome | 2026.0.0-rc.1 | v2024.0.0-ballot | 2024.0.0-ballot |
| mikrobiologie | 2027.0.0-alpha.6 | 2027.0.0-alpha.5 | 2027.0.0-alpha.5 |

Bei ICU steht in der `sushi-config` noch die Ballot-RC, publiziert ist längst das finale `2027.0.0`. Bei MolGen und Patho ist es umgekehrt: die `sushi-config` ist auf 2027 vorgelaufen, veröffentlicht wurde nie etwas davon.
