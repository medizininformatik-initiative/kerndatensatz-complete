---
name: build-bom-package
version: 1.0.0
description: Build the MII KDS Complete BOM package by assembling all module resources. No SUSHI or Firely Bake needed. Use when building, packaging, or releasing the kerndatensatz-complete package.
user_invocable: true
---

# Build BOM Package

Build the MII KDS Complete BOM package by downloading all module packages from the FHIR registry and assembling their conformance resources + examples into a single distributable package.

## When to Use

- Building the `kerndatensatz-complete` package for release
- Testing a new module version combination locally
- Creating a tarball for GitHub Release or Simplifier upload

## Prerequisites

- `node` (for parsing package.json)
- Internet access (to download packages from Simplifier registry)

No SUSHI, Firely Bake, or IG Publisher required.

## Your Task

Run the build script and verify the output.

### Step 1: Verify Configuration

Read `package.json` and `sushi-config.yaml` to confirm:
- Package name and version are correct
- All module dependencies are listed with intended versions
- Versions match between both files

### Step 2: Run the Build

```bash
./scripts/build-bom-package.sh
```

The script executes 5 phases:
1. **Download** - Fetches all KDS module packages from Simplifier (skips cached)
2. **Assemble** - Collects conformance resources + examples from all modules
3. **Metadata** - Copies package.json into the package
4. **Index** - Generates `.index.json` with resource inventory
5. **Pack** - Creates tarball (`.tgz`)

### Step 3: Verify Output

Check the build summary for:
- All modules downloaded successfully
- Resource and example counts look reasonable
- No download failures

Optional deeper inspection:
```bash
# List contents
tar -tzf de.medizininformatikinitiative.kerndatensatz.complete-*.tgz | head -30

# Check for unwanted files
tar -tzf de.medizininformatikinitiative.kerndatensatz.complete-*.tgz | grep -E '\.fsh$|\.claude|/\._'

# Verify package.json is included
tar -tzf de.medizininformatikinitiative.kerndatensatz.complete-*.tgz | grep package.json
```

### Step 4: Report

Display build summary with package name, version, size, file counts, and next steps.

## Options

| Flag | Description |
|------|-------------|
| `--skip-download` | Skip downloading, use cached packages only |
| `--output-dir DIR` | Write tarball to a specific directory |

## Error Handling

- **HTTP errors on download**: Check if version exists on Simplifier registry
- **Package not in cache**: Run without `--skip-download`
- **Node not found**: Install Node.js

## Architecture

This is a "fat BOM" approach: instead of declaring dependencies and letting tooling resolve them, we bundle all resources directly. This means consumers get everything in one package without transitive dependency resolution.

The script reads dependencies from `package.json`, downloads each module package from the Simplifier FHIR registry, extracts conformance resources (StructureDefinition, ValueSet, CodeSystem, etc.) and examples, then assembles them into a standard FHIR NPM package structure.
