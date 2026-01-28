# MII Profile Differential Visualization

Interactive HTML visualization of FHIR profile differentials from the Medizininformatik Initiative (MII) Kerndatensatz.

## Overview

This visualization system extracts and displays differential elements from MII FHIR profiles, making it easy to understand:
- What constraints each profile adds compared to its base
- Cardinality changes (e.g., 0..1 → 1..1)
- Type constraints and target profiles
- Terminology bindings and ValueSets
- Must Support flags
- Extensions added
- FHIRPath constraints

## Files Generated

```
docs/profiles/
├── README.md                 # This file
├── profile_data.json        # Raw extracted profile data
├── index.html               # Master index page
├── bildgebung.html          # Imaging module (11 profiles)
├── biobank.html             # Biobank module (12 profiles)
├── diagnose.html            # Diagnosis module (2 profiles)
├── fall.html                # Encounter module (2 profiles)
├── laborbefund.html         # Laboratory module (3 profiles)
├── medikation.html          # Medication module (10 profiles)
├── meta.html                # Meta module (3 profiles)
├── molgen.html              # Molecular genetics module (14 profiles)
├── onkologie.html           # Oncology module (37 profiles)
├── patho.html               # Pathology module (16 profiles)
├── person.html              # Person module (8 profiles)
├── prozedur.html            # Procedure module (2 profiles)
└── studie.html              # Study module (5 profiles)
```

**Total: 103 profiles across 13 modules**

## Usage

### Open in Browser

1. **Open the master index:**
   ```bash
   open docs/profiles/index.html
   ```
   Or navigate to: `file:///path/to/docs/profiles/index.html`

2. **Select a module** from the grid (e.g., "Person", "Diagnose", "Labor")

3. **In the module view:**
   - Use the dropdown to select a profile
   - Profile accordion expands automatically
   - Left panel shows differential elements
   - Click any element to see details in right panel

### Navigation

- **Breadcrumb**: Use "← All Modules" to return to index
- **Profile selector**: Dropdown at top to switch between profiles
- **Element list**: Left panel with badges indicating:
  - `MS` = Must Support
  - `EXT` = Extension
  - `⬆` = Cardinality constraint
  - `SLICE` = Sliced element

### Reading Differentials

Each profile shows **only what it changes** compared to its base definition:

```
FHIR Patient (base)
  └─ identifier: 0..*
     └─ type: Identifier

MII PR Person Patient (differential)
  └─ identifier: 1..* {MS} ⬆
     ├─ Slice: versichertenId_GKV (1..1)
     └─ Slice: pid (1..*)
```

**What you see:**
- **Cardinality**: `0..* → 1..*` (now required)
- **Must Support**: Added `{MS}` flag
- **Slices**: Two new identifier slices

## UI Layout

```
┌─────────────────────────────────────────────────────────┐
│ [Profile Selector Dropdown]                             │
├──────────────────┬──────────────────────────────────────┤
│                  │                                       │
│  Elements        │  Details Panel                       │
│  (Left)          │  (Right - click element to show)     │
│                  │                                       │
│  • identifier ⬆  │  ┌─────────────────────────────┐    │
│  • name {MS} ⬆   │  │ identifier                  │    │
│  • birthDate ⬆   │  │ ─────────────────────────   │    │
│  + extension     │  │ Cardinality: 1..* {MS}      │    │
│                  │  │ Slices:                     │    │
│                  │  │  - versichertenId_GKV       │    │
│                  │  │  - pid                      │    │
│                  │  └─────────────────────────────┘    │
│                  │                                       │
└──────────────────┴──────────────────────────────────────┘
```

## Features

### Interactive Elements

- **Expandable accordion**: Click profile header to expand/collapse
- **Click to view details**: Click any element in left panel
- **Persistent detail panel**: Details stay visible until another element is clicked
- **Auto-selection**: First profile auto-loads on page open

### Element Details Shown

When you click an element, the right panel displays:

1. **Cardinality**: Min/max with Must Support flag
2. **Short description**: Brief element description
3. **Definition**: Full FHIR definition text
4. **Type constraints**:
   - Code (e.g., `Identifier`, `HumanName`)
   - Profile restrictions
   - Target profile for references
5. **Terminology bindings**:
   - Binding strength (required, extensible, preferred, example)
   - ValueSet canonical URL
   - Description
6. **Constraints**: FHIRPath invariants with human-readable text
7. **Slicing info**: Discriminators and rules

### Visual Indicators

- **Blue highlight**: Active/selected element
- **Badges**: Quick identification of element properties
- **Color coding**: Different badge colors for different properties
- **Hover effects**: Elements lift on hover for better UX

## Regenerating

If MII packages are updated:

```bash
# 1. Extract updated profile data
python3 scripts/extract_profiles.py

# 2. Regenerate HTML visualizations
python3 scripts/generate_html.py
```

## Technical Details

### Data Source

Profiles are extracted from local FHIR package cache:
```
~/.fhir/packages/de.medizininformatikinitiative.kerndatensatz.*#2025.0.*/
```

### Extraction Process

1. **scan packages**: Find all MII packages matching version 2025.0.x
2. **Parse StructureDefinitions**: Load JSON files
3. **Extract differentials**: Only changed/added elements
4. **Build hierarchy**: Map baseDefinition relationships
5. **Generate JSON**: Structured data for HTML embedding

### HTML Structure

- **Self-contained**: Each HTML file includes all data and code
- **No external dependencies**: Works offline, no CDN required
- **Embedded JavaScript**: Interactivity built-in
- **Responsive**: Works on desktop and tablet
- **Print-friendly**: CSS optimized for printing

## Examples

### Example 1: MII Person Patient

**Module**: person
**Profile**: MII_PR_Person_Patient
**Base**: http://hl7.org/fhir/StructureDefinition/Patient

**Differential elements (8)**:
- `identifier` - 1..* {MS} with 2 slices
- `name` - 1..* {MS}
- `gender` - 0..1 with extension
- `birthDate` - 1..1 {MS}
- `address` - 1..* {MS} using DE Basisprofil
- `extension:GenderOtherDE` - 0..1
- `extension:Vitalstatus` - 0..1

### Example 2: MII Labor Observation

**Module**: laborbefund
**Profile**: MII_PR_Labor_Laboruntersuchung
**Base**: http://hl7.org/fhir/StructureDefinition/Observation

**Key constraints**:
- `category` - Must include "laboratory"
- `code` - Bound to LOINC (extensible)
- `value[x]` - Quantity with UCUM units
- `specimen` - Required reference to Specimen
- `hasMember` - References to other Observations

## Modules Overview

| Module | Profiles | Description |
|--------|----------|-------------|
| **person** | 8 | Patient demographics, research subjects |
| **diagnose** | 2 | ICD-10-GM diagnoses |
| **fall** | 2 | Encounters and episodes of care |
| **prozedur** | 2 | OPS procedures |
| **medikation** | 10 | Medications and prescriptions |
| **laborbefund** | 3 | Laboratory observations and reports |
| **biobank** | 12 | Biospecimen and biobank data |
| **consent** | 5 | Consent management |
| **onkologie** | 37 | Cancer-related observations and data |
| **icu** | 14 | Intensive care PDMS data |
| **molgen** | 14 | Molecular genetics and genomics |
| **patho** | 16 | Pathology reports and findings |
| **bildgebung** | 11 | Imaging procedures and reports |

## Browser Compatibility

Works in all modern browsers:
- Chrome/Edge 90+
- Firefox 88+
- Safari 14+

**No plugins or extensions required.**

## License

Content extracted from MII Kerndatensatz packages (CC-BY-4.0).
Visualization tool: MIT License.

## Links

- **MII Homepage**: https://www.medizininformatik-initiative.de/
- **FHIR Spec**: https://hl7.org/fhir/R4/
- **Package Registry**: https://simplifier.net/organization/koordinationsstellemii

---

**Generated**: 2025-12-03
**Source Version**: MII Kerndatensatz 2025.0.x
**Total Profiles**: 103
