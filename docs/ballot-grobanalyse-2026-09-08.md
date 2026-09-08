# Grobanalyse Ballot-Reife — Stand 2026-09-08

21 Modul-Repos, gemessen über Registry, GitHub-API, GitHub Pages und die entpackten
Paketinhalte im lokalen Korpus.

## 1. Wer hat ein 2027er Package in der Registry?

**15 von 21.**

| | Module |
|---|---|
| **2027 publiziert** | base, bildgebung, biobank, consent, dokument, icu, kardiologie, laborbefund, lungenfunktion, meta, mikrobiologie, molgen, patho, pros, studie |
| **kein 2027er Package** | medikation, mtb, onkologie, seltene, soziodemographie, symptom |

Vier der sechs sind im Repo aber **schon weiter als in der Registry** — die Veröffentlichung
fehlt, nicht die Arbeit:

| Modul | sushi-config (Default-Branch) | publiziert |
|---|---|---|
| medikation | 2027.0.0-ballot.rc2 | 2026.0.1 |
| onkologie | 2027.0.0-ballot.rc1 | 2026.0.3 |
| seltene | 2027.0.0-ballot.rc1 | 2026.0.1 |
| soziodemographie | 2027.0.0-ballot.rc1 | *gar nichts* |

Bei Onkologie liegt zusätzlich ein GitHub-Release `v2027.0.0-ballot.rc1` als **Draft** vor.
Nur mtb (2026.0.1) und symptom (2026.0.0-rc.1 im Repo, 2024.0.0-ballot publiziert) sind
inhaltlich nicht auf der Ballot-Linie.

Zwei Module sind in der Registry **weiter als ihr eigener Default-Branch**: bildgebung
(Repo rc1, publiziert rc2) und icu (Repo ballot.rc1, publiziert final 2027.0.0).

## 2. GitHub Pages

| Stand | Module |
|---|---|
| **aktuell** | consent, dokument, laborbefund, lungenfunktion, medikation, mikrobiologie, molgen, patho, studie, symptom |
| **hinterher** | base (**41 Tage**), pros (6), onkologie (5), bildgebung (3), kardiologie (3), biobank (1), icu (1) |
| **keine Pages** | meta, mtb, seltene, soziodemographie |

`base` ist der Ausreißer: letzter Pages-Build 22. Juli, Branch-Head 1. September. Wer den
Guide dort ansieht, bekommt einen sechs Wochen alten Stand — bei dem Modul, auf dem alle
anderen aufsetzen.

Dass **meta gar keine Pages** hat, erklärt rückblickend, warum der QA-Report dort so schwer
zu finden war.

## 3. Wer ist mit den Dependencies auf 2027?

Gemessen an den MII-internen Abhängigkeiten der publizierten Pakete.

| Stand | Module |
|---|---|
| **vollständig auf 2027** | **molgen** (base rc1, biobank rc2, meta rc3) |
| teilweise | base, biobank, laborbefund (jeweils meta rc3, keine weiteren MII-Deps) |
| **keine MII-Deps** | consent, meta, soziodemographie |
| **noch auf 2026** | bildgebung, dokument, icu, kardiologie, lungenfunktion, medikation, mikrobiologie, mtb, onkologie, patho, pros, seltene, studie, symptom |

Von den 15 Modulen mit 2027er Package zeigen also nur **vier** überhaupt auf 2027er
Abhängigkeiten, und nur **molgen** vollständig. Elf tragen die Ballot-Versionsnummer, hängen
intern aber am 2026er Stand — darunter patho (base 2026.0.1, biobank 2026.0.1, meta 2026.0.0)
und pros, dessen Abhängigkeiten sich gegenüber 2026.7.0 gar nicht verändert haben.

## 4. Sind die Paketinhalte auf Simplifier?

**Ja, für alle 15 publizierten Module.** Jedes Paket ließ sich abrufen und entpacken, alle
enthalten ein vollständiges `package/` mit Manifest und Ressourcen. Der Korpus umfasst
1419 Conformance-Ressourcen.

Die einzige Lücke ist **soziodemographie** — in keiner Registry, in keiner Version. Das dortige
Paket im Korpus stammt aus einem lokalen SUSHI-Build.

## 5. CRMI: Deklaration und Verwendung

**Vier von 21 Modulen arbeiten mit CRMI** — und zwar dieselben vier, die es auch deklarieren.
Es gibt keinen Fall von „Dependency da, aber ungenutzt" oder umgekehrt.

| Modul | `hl7.fhir.uv.crmi` | CRMI-Profile | knowledgeCapability |
|---|---|---|---|
| base | 2.0.0 | **70** | 35 |
| laborbefund | 2.0.0 | **41** | 16 |
| meta | 2.0.0 | 9 | 4 |
| molgen | 2.0.0 | 4 | 1 |
| alle übrigen 17 | — | 0 | 0 |

Alle vier auf derselben CRMI-Version 2.0.0. Aber die **Tiefe unterscheidet sich stark**:

- **base** und **laborbefund** zeichnen breit aus — ValueSets, StructureDefinitions,
  CapabilityStatements, CodeSystems, jeweils als `crmi-shareable*` **und** `crmi-publishable*`.
  Laborbefund nutzt als einziges Modul `crmi-computablevalueset` durchgängig (9x), base nur 1x.
- **meta** bleibt bei 9 Auszeichnungen auf wenigen Ressourcen.
- **molgen** hat nur die vier IG-Ebenen-Profile (`crmi-shareableimplementationguide`,
  `crmi-publishableimplementationguide`, `crmi-implementationguide`, `crmi-manifestparameters`)
  — also die Hülle, ohne die einzelnen Artefakte auszuzeichnen.

`knowledgeRepresentationLevel` verwendet **kein einziges Modul**, obwohl es zum Muster gehört.

Vier Module tragen `knowledgeCapability` **ohne** CRMI-Dependency: bildgebung (2), icu (2),
kardiologie (3), lungenfunktion (4). Das sind vermutlich kopierte Fragmente ohne die
zugehörige Abhängigkeit.

> Onkologie kündigt in der Paketbeschreibung des unpublizierten `2027.0.0-ballot.rc1`
> „CRMI-Metadaten modulweit" an. In der publizierten 2026.0.3 ist davon nichts enthalten —
> das käme erst mit der Veröffentlichung.

## 6. Template und Claude-Skills

### IG-Template: sechs verschiedene Zustände

| Variante | Anzahl | Module |
|---|---|---|
| vendored `1.3.2` | 7 | biobank, lungenfunktion, medikation, molgen, onkologie, pros, soziodemographie |
| vendored `1.3.4` | 2 | patho, seltene |
| `ig.ini` → GitHub-URL des Templates | 4 | base, kardiologie, laborbefund, meta |
| `ig.ini` → `fhir.base.template#current` | 2 | icu, mtb |
| `ig.ini` → `fhir2.base.template#current` | 1 | dokument |
| kein Template erkennbar | 5 | bildgebung, consent, mikrobiologie, studie, symptom |

Neun Module vendoren das Template ins Repo, sieben ziehen es über `ig.ini` — davon drei auf
`#current`, also ohne feste Version. Das vendorte Template pinnt intern `fhir2.base.template`
bewusst auf `0.1.0`; die `#current`-Variante umgeht genau diese Reproduzierbarkeit.

Und die vendorte Version driftet bereits: **1.3.2 gegen 1.3.4**.

### Claude-Skills: nur 7 von 21 Repos, und jedes anders

| Modul | Skills | Config-Schema |
|---|---|---|
| onkologie | 8 | 1.0.0 |
| pros | 7 | 1.0.0 |
| biobank | 4 | 1.0.0 |
| molgen | 4 | 1.0.0 |
| seltene | 3 | 1.0.0 |
| medikation | 2 | — |
| mtb | 2 | 1.0.0 |
| **die übrigen 14** | **0** | — |

14 verschiedene Skills insgesamt, aber **kein einziger ist in allen sieben Repos vorhanden**.
Die verbreitetsten kommen auf fünf:

```
fhir-ig-analysis            5x   biobank, medikation, molgen, onkologie, pros
fix-ig-export-links         5x   molgen, mtb, onkologie, pros, seltene
mii-ig-migration            5x   biobank, medikation, molgen, onkologie, pros
mii-testdata-contribution   5x   molgen, mtb, onkologie, pros, seltene
```

Auffällig sind zwei Gruppen, die sich kaum überschneiden: `fhir-ig-analysis` +
`mii-ig-migration` (Migrations-Werkzeuge) gegen `fix-ig-export-links` +
`mii-testdata-contribution`. Nur molgen, onkologie und pros haben beide.

Dazu Zeichen von Kopieren statt Verteilen: seltene führt `fix-ig-export-links` **und**
`fix-ig-export-links-new` nebeneinander, onkologie bindet `fhir-ig-analysis` als Symlink ein,
die anderen als Verzeichnis. Eine Versionsangabe trägt keiner der Skills — nur die
`.claude/config.yaml` hat ein Schema-Feld, und das steht überall auf `1.0.0`.

Das Referenz-Repo `mii-kerndatensatz-dev` (`@medizininformatik-initiative/claude-skills`)
steht bei **1.1.1**. Ein Abgleich, welches Repo davon welchen Stand hat, ist nicht möglich,
weil die verteilten Kopien keine Version mitführen.

## Was daraus folgt

1. **Der Engpass ist die Veröffentlichung, nicht die Arbeit.** Vier Module sind im Repo auf
   der Ballot-Linie, aber nicht in der Registry — bei Onkologie hängt sogar ein fertiger
   Release-Draft. Das ist der billigste Hebel für mehr Ballot-Abdeckung.
2. **Die Ballot-Versionsnummer sagt wenig über die Ballot-Reife.** Nur molgen ist vollständig
   auf 2027er Abhängigkeiten; elf Module tragen die Nummer, ohne umgezogen zu sein.
3. **CRMI ist eine Insel.** Vier Module, sehr unterschiedliche Tiefe, `knowledgeRepresentationLevel`
   nirgends. Wenn CRMI Konvention werden soll, braucht es eine Festlegung, welche Auszeichnungen
   verbindlich sind.
4. **Template und Werkzeuge driften.** Sechs Template-Zustände, drei davon ohne feste Version;
   Skills in einem Drittel der Repos, ohne Versionierung und ohne gemeinsamen Kern.
