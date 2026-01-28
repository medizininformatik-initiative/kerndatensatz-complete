# MII Profile Dependency Visualization

This document shows different approaches to visualizing FHIR profile dependencies in the MII Kerndatensatz.

## Approach 1: Mermaid Diagram (Markdown-friendly)

Mermaid diagrams work in GitHub, GitLab, and many markdown viewers.

```mermaid
graph TD
    %% Base FHIR Resources
    Patient[FHIR Patient]
    Observation[FHIR Observation]
    Condition[FHIR Condition]
    Procedure[FHIR Procedure]
    Encounter[FHIR Encounter]

    %% German Base Profiles
    DEPatient[DE Basisprofil Patient]
    DEObservation[DE Basisprofil Observation]

    %% MII Core Profiles
    MIIPatient[MII PR Person Patient]
    MIIDiagnosis[MII PR Diagnose Condition]
    MIIProcedure[MII PR Prozedur Procedure]
    MIIEncounter[MII PR Fall Encounter]
    MIILabor[MII PR Laborbefund Observation]

    %% Specialized MII Profiles
    MIIOnko[MII PR Onkologie Tumor]
    MIIICU[MII PR ICU Beatmung]
    MIIMolGen[MII PR MolGen Variante]

    %% Dependencies
    Patient --> DEPatient
    DEPatient --> MIIPatient

    Observation --> DEObservation
    DEObservation --> MIILabor

    Condition --> MIIDiagnosis
    Procedure --> MIIProcedure
    Encounter --> MIIEncounter

    Observation --> MIIOnko
    Observation --> MIIICU
    Observation --> MIIMolGen

    %% Cross-references
    MIIDiagnosis -.references.-> MIIPatient
    MIIProcedure -.references.-> MIIPatient
    MIIEncounter -.references.-> MIIPatient
    MIILabor -.references.-> MIIPatient
    MIILabor -.references.-> MIIEncounter

    %% Styling
    classDef baseResource fill:#e1f5ff,stroke:#0066cc,stroke-width:2px
    classDef deProfile fill:#fff4e6,stroke:#ff9800,stroke-width:2px
    classDef miiCore fill:#e8f5e9,stroke:#4caf50,stroke-width:2px
    classDef miiSpecial fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px

    class Patient,Observation,Condition,Procedure,Encounter baseResource
    class DEPatient,DEObservation deProfile
    class MIIPatient,MIIDiagnosis,MIIProcedure,MIIEncounter,MIILabor miiCore
    class MIIOnko,MIIICU,MIIMolGen miiSpecial
```

**Legend:**
- Solid arrows (→): Profile inheritance (Parent/BaseDefinition)
- Dotted arrows (-.->): Profile references (element.type.targetProfile)
- Colors:
  - Blue: Base FHIR resources
  - Orange: German base profiles
  - Green: MII core profiles
  - Purple: MII specialized profiles

## Approach 2: PlantUML Diagram (More detailed)

PlantUML offers more layout control and can show additional metadata.

```plantuml
@startuml MII_Profile_Dependencies

!define FHIR_COLOR #E1F5FF
!define DE_COLOR #FFF4E6
!define MII_CORE #E8F5E9
!define MII_SPECIAL #F3E5F5

skinparam packageStyle rectangle
skinparam linetype ortho

package "FHIR R4 Core" FHIR_COLOR {
  class Patient <<Resource>>
  class Observation <<Resource>>
  class Condition <<Resource>>
  class Procedure <<Resource>>
  class Encounter <<Resource>>
  class MedicationStatement <<Resource>>
}

package "DE Basisprofile" DE_COLOR {
  class "DEPatient" as DEPatient <<Profile>> {
    + Versichertennummer
    + Versicherungstyp
  }
  class "DEObservation" as DEObservation <<Profile>>
  class "DECondition" as DECondition <<Profile>>
}

package "MII Person" MII_CORE {
  class "MII_PR_Person_Patient" as MIIPatient <<Profile>> {
    + identifier: VersichertenId
    + identifier: PatientenId
    + address: Deutsche Adresse
    + birthDate: required
  }
  class "MII_PR_Person_ResearchSubject" as MIIResearch <<Profile>>
}

package "MII Diagnose" MII_CORE {
  class "MII_PR_Diagnose_Condition" as MIIDiagnose <<Profile>> {
    + code: ICD-10-GM
    + severity: required
    + recordedDate: required
  }
}

package "MII Laborbefund" MII_CORE {
  class "MII_PR_Labor_Observation" as MIILabor <<Profile>> {
    + category: laboratory
    + code: LOINC
    + value[x]: Quantity
  }
  class "MII_PR_Labor_DiagnosticReport" as MIIReport <<Profile>>
}

package "MII Prozedur" MII_CORE {
  class "MII_PR_Prozedur_Procedure" as MIIProzedur <<Profile>> {
    + code: OPS
    + performedDateTime: required
  }
}

package "MII Medikation" MII_CORE {
  class "MII_PR_Medikation_MedicationStatement" as MIIMedikation <<Profile>> {
    + medication: PZN/ATC
    + dosage: required
  }
}

package "MII Fall" MII_CORE {
  class "MII_PR_Fall_Encounter" as MIIFall <<Profile>> {
    + class: required
    + type: Kontaktart
    + period: required
  }
  class "MII_PR_Fall_Abteilungsfall" as MIIAbteilung <<Profile>>
}

package "MII Onkologie" MII_SPECIAL {
  class "MII_PR_Onko_Tumor" as MIITumor <<Profile>>
  class "MII_PR_Onko_TNM" as MIITNM <<Profile>>
}

package "MII ICU" MII_SPECIAL {
  class "MII_PR_ICU_Beatmung" as MIIBeatmung <<Profile>>
  class "MII_PR_ICU_Herzfrequenz" as MIIHerzfrequenz <<Profile>>
}

' Inheritance relationships
Patient -up-|> DEPatient
DEPatient -up-|> MIIPatient

Condition -up-|> DECondition
DECondition -up-|> MIIDiagnose

Observation -up-|> DEObservation
DEObservation -up-|> MIILabor

Procedure -up-|> MIIProzedur
Encounter -up-|> MIIFall
MIIFall -up-|> MIIAbteilung

Observation -up-|> MIITumor
Observation -up-|> MIIBeatmung
Observation -up-|> MIIHerzfrequenz

' Reference relationships
MIIDiagnose .right.> MIIPatient : subject
MIIProzedur .right.> MIIPatient : subject
MIILabor .right.> MIIPatient : subject
MIIFall .right.> MIIPatient : subject
MIIMedikation .right.> MIIPatient : subject

MIILabor .down.> MIIFall : encounter
MIIDiagnose .down.> MIIFall : encounter
MIIProzedur .down.> MIIFall : encounter

MIIReport .down.> MIILabor : result

legend right
  |= Line Type |= Meaning |
  | ──|> | Profile inherits from (baseDefinition) |
  | ·····> | Profile references (targetProfile) |

  |= Color |= Module |
  | Blue | FHIR R4 Core Resources |
  | Orange | German Base Profiles |
  | Green | MII Core Modules |
  | Purple | MII Extension Modules |
endlegend

@enduml
```

## Approach 3: Hierarchical Package View

```mermaid
graph TB
    subgraph "Package Dependencies"
        meta[de.basisprofil.r4]

        person[kerndatensatz.person<br/>↳ depends: meta]
        fall[kerndatensatz.fall<br/>↳ depends: person, meta]
        diagnose[kerndatensatz.diagnose<br/>↳ depends: person, fall, meta]
        labor[kerndatensatz.laborbefund<br/>↳ depends: person, fall, meta]
        prozedur[kerndatensatz.prozedur<br/>↳ depends: person, fall, meta]
        medikation[kerndatensatz.medikation<br/>↳ depends: person, fall, meta]

        onko[kerndatensatz.onkologie<br/>↳ depends: person, diagnose, labor, meta]
        icu[kerndatensatz.icu<br/>↳ depends: person, fall, meta]
        molgen[kerndatensatz.molgen<br/>↳ depends: person, diagnose, meta]

        meta --> person
        meta --> fall
        person --> fall

        person --> diagnose
        fall --> diagnose
        meta --> diagnose

        person --> labor
        fall --> labor
        meta --> labor

        person --> prozedur
        fall --> prozedur
        meta --> prozedur

        person --> medikation
        fall --> medikation
        meta --> medikation

        person --> onko
        diagnose --> onko
        labor --> onko

        person --> icu
        fall --> icu

        person --> molgen
        diagnose --> molgen
    end
```

## Usage

### Rendering Mermaid
Mermaid diagrams render automatically in:
- GitHub README/markdown files
- GitLab
- VS Code (with Mermaid extension)
- Many documentation tools

### Rendering PlantUML
PlantUML requires additional tools:
- Online: http://www.plantuml.com/plantuml/
- VS Code: PlantUML extension
- CLI: `plantuml diagram.puml`
- IntelliJ IDEA: Built-in support

### Interactive Navigation
See `profile-navigator.html` for an interactive web-based profile browser.

## Next Steps

1. **Extract actual profile data**: Run the profile extraction script to get real data from packages
2. **Generate visualization**: Use the extracted data to auto-generate diagrams
3. **Explore in UI**: Use the profile navigator to interactively explore relationships
