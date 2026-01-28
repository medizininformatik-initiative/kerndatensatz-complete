# MII Profile Graph Explorer

Interactive graph-based visualization for exploring and comparing FHIR profiles from the MII Kerndatensatz.

## Overview

This tool helps implementers:
- **Visualize profile relationships** - See inheritance chains and dependencies
- **Compare profiles** - Understand differences between similar profiles (e.g., rare disease Condition vs onko Condition)
- **Navigate the ecosystem** - Filter by module or resource type
- **Make informed decisions** - Compare differential elements side-by-side

## Quick Start

```bash
# Open in browser
open docs/profiles/graph.html
```

Or navigate to: `file:///path/to/docs/profiles/graph.html`

## Features

### 1. Interactive Graph Visualization

**Powered by Cytoscape.js** - Industry-standard graph visualization for biological networks

**Node Types:**
- **Blue circles**: MII profiles extending FHIR base resources
- **Purple circles**: MII profiles extending other MII profiles
- **Gray rounded rectangles**: FHIR base resources (Patient, Observation, etc.)

**Edges:**
- **Solid arrows**: Inheritance relationships (extends)
- **Dashed lines**: Same resource type (for comparison hints - toggle with button)

### 2. Navigation & Controls

#### Filters (Left Sidebar)
- **Module Filter**: Show/hide profiles by module (person, diagnose, onko, etc.)
- **Type Filter**: Show/hide by resource type (Observation, Condition, Procedure, etc.)
- **Layout Selector**:
  - **Hierarchical**: Top-down inheritance view (default, best for understanding relationships)
  - **Force-Directed**: Organic clustering (good for seeing groups)
  - **Circular**: Radial layout (alternative view)

#### Controls (Right Sidebar)
- **Zoom In/Out**: Keyboard shortcuts: `+` / `-`
- **Fit to Screen**: Auto-zoom to show all visible nodes
- **Reset View**: Return to initial state
- **Show/Hide Comparisons**: Toggle dashed edges between profiles of same type

### 3. Profile Details Panel

**Click any profile node** → Bottom panel expands showing:
- Module, resource type, version
- Description
- All differential elements with badges:
  - `MS` = Must Support
  - `min:N` = Minimum cardinality
  - `max:N` = Maximum cardinality
  - `M` = Modifier element
  - `EXT` = Extension

**Actions:**
- **Add to Comparison**: Select for side-by-side comparison
- **Focus in Graph**: Center and zoom on this node

### 4. Profile Comparison

**Use Case**: "Should I use rare disease Condition or onko Condition?"

**How to Compare:**
1. Click first profile → "Add to Comparison"
2. Click second profile → Comparison modal opens automatically

**Comparison Shows:**
- **Summary Statistics**: Common, Different, Unique counts
- **Tabs**:
  - **Different**: Elements with different constraints (cardinality, bindings, etc.)
  - **Unique Elements**: Elements only in one profile
  - **Common**: Elements with same constraints

**Element-by-Element View:**
- Side-by-side comparison of constraints
- Highlights: cardinality, Must Support, types, bindings
- Clear indication of what differs

## Use Cases

### Use Case 1: Understanding Profile Hierarchy

**Question**: "What's the inheritance chain for MII onko profiles?"

**Steps**:
1. Filter to show only "onkologie" module
2. Use Hierarchical layout
3. Follow arrows from FHIR base → MII profiles → Extended profiles

**Result**: Visual understanding of profile layering

### Use Case 2: Choosing Between Similar Profiles

**Question**: "Should I use MII Person Patient or MII Person Patient Pseudonymisiert?"

**Steps**:
1. Filter to "person" module + "Patient" type
2. Click "Person Patient" → Add to Comparison
3. Click "Person Patient Pseudonymisiert" → Comparison opens
4. Review "Different" tab to see what changes

**Result**: Clear understanding of which profile fits your use case

### Use Case 3: Finding All Observation Profiles

**Question**: "What Observation profiles are available across all modules?"

**Steps**:
1. Filter to show only "Observation" type
2. Enable "Show Comparisons" to see connections
3. Review nodes from different modules (labor, onko, icu, etc.)

**Result**: Complete view of Observation profiles across MII

### Use Case 4: Exploring Module Dependencies

**Question**: "What profiles does the onkologie module extend from other modules?"

**Steps**:
1. Filter to "onkologie" module
2. Look for purple nodes (extend other MII profiles)
3. Follow arrows to see dependencies

**Result**: Understanding of cross-module dependencies

## Technical Details

### Architecture

```
graph.html (Main visualization)
├── Cytoscape.js (Graph rendering)
├── profile-data-transformer.js (Data preparation)
├── profile-comparator.js (Comparison logic)
└── profile_data.json (Source data)
```

### Data Flow

1. **Load**: Fetch `profile_data.json` (103 profiles)
2. **Transform**: Convert to Cytoscape graph format
   - Create nodes for profiles + FHIR base resources
   - Create edges for inheritance + same-type relationships
3. **Render**: Initialize Cytoscape with cose-bilkent layout
4. **Interact**: User clicks, filters, compares

### Performance

- **103 profiles**: Renders in < 1 second
- **Smooth interactions**: 60 FPS zoom/pan
- **Efficient filtering**: Instant updates
- **Layout algorithms**: Optimized for biological networks

### Browser Compatibility

- Chrome 90+ ✓
- Firefox 88+ ✓
- Safari 14+ ✓
- Edge 90+ ✓

**No plugins required** - Pure web standards

## File Structure

```
docs/profiles/
├── graph.html                      # Main interactive visualization
├── profile-data-transformer.js     # Graph data transformer
├── profile-comparator.js           # Comparison functionality
├── profile_data.json              # Source profile data
└── GRAPH_README.md                # This file
```

## Keyboard Shortcuts

- `+` : Zoom in
- `-` : Zoom out
- `F` : Fit to screen
- `R` : Reset view
- `ESC` : Close side panel / comparison modal

## Tips & Tricks

### Tip 1: Finding Related Profiles

Enable "Show Comparisons" to see dashed lines between profiles of the same resource type across modules. Great for discovering alternatives.

### Tip 2: Focusing on a Subset

1. Uncheck all modules except the ones you care about
2. Select specific resource types
3. Use "Fit to Screen" to focus on visible nodes

### Tip 3: Understanding Constraints

Click a profile → Scroll through differential elements. Each badge tells you about constraints:
- `MS` = Required in your implementation
- `min:1` = Must provide at least one
- `M` = Changes meaning of resource

### Tip 4: Comparing Across Modules

To see how different modules handle the same resource type:
1. Filter to one resource type (e.g., "Condition")
2. Keep all modules visible
3. Select profiles from different modules for comparison

### Tip 5: Layout Selection

- **Start with Hierarchical** - Best for understanding relationships
- **Switch to Force-Directed** - Better for seeing module clusters
- **Use Circular** - Alternative when graphs are dense

## Troubleshooting

### Graph Not Loading

**Problem**: Blank screen or loading spinner stuck

**Solution**:
1. Check browser console for errors (F12)
2. Ensure `profile_data.json` exists in same directory
3. Serve via HTTP server if file:// has CORS issues:
   ```bash
   cd docs/profiles
   python3 -m http.server 8000
   # Open http://localhost:8000/graph.html
   ```

### Nodes Overlapping

**Problem**: Too many nodes, hard to see

**Solution**:
1. Use filters to show fewer profiles
2. Switch layout (try Force-Directed)
3. Zoom in on specific area
4. Use "Focus in Graph" after selecting a profile

### Comparison Not Working

**Problem**: Can't select second profile for comparison

**Solution**:
1. Clear current comparison (button in yellow status box)
2. Try again
3. Maximum 2 profiles can be compared at once

## Advanced Usage

### Filtering by Multiple Criteria

Combine module and type filters:
- Show only Observation profiles from labor + icu modules
- See all onko profiles that are Condition type

### Finding Circular Dependencies

Rare, but possible:
1. Look for purple nodes (extended profiles)
2. Follow arrows - if they loop back, there's a dependency cycle
3. May indicate profiles that reference each other

### Identifying Most-Used Patterns

Look for FHIR base resources with many outgoing edges:
- Many profiles extend Observation
- Common patterns emerge (lab, vital signs, surveys)

## Related Tools

- **index.html**: Module-based profile browser with dropdown navigation
- **Module HTML files**: Per-module profile lists (person.html, diagnose.html, etc.)
- **profile_data.json**: Raw extracted profile data

## Future Enhancements

Potential additions:
- Search bar for finding profiles by name
- Element-level graph showing profile → element relationships
- Export comparison as PDF/CSV
- Save filter configurations
- Deep linking to specific graph states

## Credits

- **Visualization**: [Cytoscape.js](https://js.cytoscape.org/)
- **Layout Algorithm**: cose-bilkent (compound spring embedder)
- **Data Source**: MII Kerndatensatz 2025.0.x packages
- **License**: CC-BY-4.0 (MII data), MIT (visualization tool)

## Feedback

Questions or suggestions? Open an issue or contribute!

---

**Last Updated**: 2025-12-03
**Profiles**: 103
**Modules**: 13
**Version**: MII Kerndatensatz 2025.0.x
