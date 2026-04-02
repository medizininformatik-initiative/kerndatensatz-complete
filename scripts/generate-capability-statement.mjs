#!/usr/bin/env node
/**
 * Generates an aggregated CapabilityStatement for the MII Kerndatensatz Complete package.
 *
 * Reads all module CapabilityStatements + META SearchParameters from ~/.fhir/packages
 * and merges them into a single requirements CapabilityStatement.
 *
 * Usage: node scripts/generate-capability-statement.mjs
 */

import { readFileSync, readdirSync, writeFileSync, existsSync } from 'fs';
import { join, basename } from 'path';
import { homedir } from 'os';

const FHIR_PACKAGES_DIR = join(homedir(), '.fhir', 'packages');

// Read sushi-config.yaml to get dependencies and version
const sushiConfig = readFileSync('sushi-config.yaml', 'utf8');
const version = sushiConfig.match(/^version:\s*(.+)$/m)?.[1]?.trim();
const canonical = sushiConfig.match(/^canonical:\s*(.+)$/m)?.[1]?.trim();

// Extract dependencies from sushi-config.yaml
const deps = {};
const depSection = sushiConfig.split(/^dependencies:/m)[1];
if (depSection) {
  for (const match of depSection.matchAll(/^\s+(de\.medizininformatikinitiative\.kerndatensatz\.\S+):\s*(\S+)/gm)) {
    deps[match[1]] = match[2];
  }
}

console.log(`Version: ${version}`);
console.log(`Canonical: ${canonical}`);
console.log(`Dependencies: ${Object.keys(deps).length}`);

// Find package directories
function findPackageDir(packageId) {
  const version = deps[packageId];
  if (!version) return null;
  const dir = join(FHIR_PACKAGES_DIR, `${packageId}#${version}`);
  return existsSync(dir) ? dir : null;
}

// Read all CapabilityStatements from a package
function readCapabilityStatements(packageDir) {
  if (!packageDir) return [];
  const pkgDir = join(packageDir, 'package');
  const files = readdirSync(pkgDir).filter(f => f.startsWith('CapabilityStatement') && f.endsWith('.json'));
  return files.map(f => {
    const content = JSON.parse(readFileSync(join(pkgDir, f), 'utf8'));
    return content;
  });
}

// Read all SearchParameters from META package
function readMetaSearchParameters() {
  const metaDir = findPackageDir('de.medizininformatikinitiative.kerndatensatz.meta');
  if (!metaDir) {
    console.warn('META package not found!');
    return [];
  }
  const pkgDir = join(metaDir, 'package');
  const files = readdirSync(pkgDir).filter(f => f.startsWith('SearchParameter') && f.endsWith('.json'));
  return files.map(f => JSON.parse(readFileSync(join(pkgDir, f), 'utf8')));
}

// Expectation extension helper
const SHALL = {
  extension: [{
    url: "http://hl7.org/fhir/StructureDefinition/capabilitystatement-expectation",
    valueCode: "SHALL"
  }]
};

// Merge resources from all module CapabilityStatements
const resourceMap = new Map(); // resourceType -> { profiles: Set, searchParams: Map<name, {definition, type}> }

for (const [packageId, packageVersion] of Object.entries(deps)) {
  const dir = findPackageDir(packageId);
  if (!dir) {
    console.warn(`Package not found: ${packageId}#${packageVersion}`);
    continue;
  }

  const capStmts = readCapabilityStatements(dir);
  for (const cs of capStmts) {
    if (!cs.rest?.[0]?.resource) continue;

    const moduleName = packageId.split('.').pop();
    console.log(`  ${moduleName}: ${cs.rest[0].resource.length} resource type(s)`);

    for (const resource of cs.rest[0].resource) {
      const type = resource.type;
      if (!resourceMap.has(type)) {
        resourceMap.set(type, {
          profiles: new Set(),
          searchParams: new Map(),
          sourceModules: new Set()
        });
      }

      const entry = resourceMap.get(type);
      entry.sourceModules.add(moduleName);

      // Collect supported profiles (keep version suffix as-is from modules)
      if (resource.supportedProfile) {
        for (const p of resource.supportedProfile) {
          entry.profiles.add(p);
        }
      }

      // Collect search parameters from module CapabilityStatement
      if (resource.searchParam) {
        for (const sp of resource.searchParam) {
          if (!entry.searchParams.has(sp.name)) {
            entry.searchParams.set(sp.name, {
              definition: sp.definition,
              type: sp.type
            });
          }
        }
      }
    }
  }
}

// Add META SearchParameters to the resource map
const metaSPs = readMetaSearchParameters();
console.log(`\nMETA SearchParameters: ${metaSPs.length}`);

let metaAdded = 0;
for (const sp of metaSPs) {
  if (!sp.base) continue;

  for (const baseType of sp.base) {
    if (!resourceMap.has(baseType)) {
      // Only add META SPs for resource types we already have from modules
      continue;
    }

    const entry = resourceMap.get(baseType);
    const name = sp.code || sp.name;
    if (!entry.searchParams.has(name)) {
      entry.searchParams.set(name, {
        definition: sp.url,
        type: sp.type
      });
      metaAdded++;
    }
  }
}
console.log(`META SearchParameters added: ${metaAdded}`);

// Sort resource types alphabetically
const sortedTypes = [...resourceMap.keys()].sort();

console.log(`\nTotal resource types: ${sortedTypes.length}`);
for (const type of sortedTypes) {
  const entry = resourceMap.get(type);
  console.log(`  ${type}: ${entry.profiles.size} profiles, ${entry.searchParams.size} search params [${[...entry.sourceModules].join(', ')}]`);
}

// Build the aggregated CapabilityStatement
const capabilityStatement = {
  resourceType: "CapabilityStatement",
  id: "mii-cps-kerndatensatz-complete",
  url: `${canonical}/CapabilityStatement/mii-cps-kerndatensatz-complete`,
  version: version,
  name: "MII_CPS_Kerndatensatz_Complete",
  title: "MII CPS Kerndatensatz Complete CapabilityStatement",
  status: "active",
  experimental: false,
  date: new Date().toISOString().split('T')[0],
  publisher: "Medizininformatik Initiative",
  contact: [{
    telecom: [{
      system: "url",
      value: "https://www.medizininformatik-initiative.de"
    }]
  }],
  description: "Aggregiertes CapabilityStatement des MII Kerndatensatz Complete-Pakets. Beschreibt alle verpflichtenden Interaktionen, Profile und Suchparameter aus allen Modulen des MII Kerndatensatzes, die ein konformes System unterstützen muss.",
  jurisdiction: [{
    coding: [{
      system: "urn:iso:std:iso:3166",
      code: "DE",
      display: "Germany"
    }]
  }],
  kind: "requirements",
  fhirVersion: "4.0.1",
  format: ["xml", "json"],
  extension: [{
    url: "https://www.medizininformatik-initiative.de/fhir/modul-meta/StructureDefinition/mii-ex-meta-license-codeable",
    valueCodeableConcept: {
      coding: [{
        system: "http://hl7.org/fhir/spdx-license",
        code: "CC-BY-4.0",
        display: "Creative Commons Attribution 4.0 International"
      }]
    }
  }],
  rest: [{
    mode: "server",
    resource: sortedTypes.map(type => {
      const entry = resourceMap.get(type);
      const profiles = [...entry.profiles].sort();
      const searchParams = [...entry.searchParams.entries()]
        .sort(([a], [b]) => a.localeCompare(b));

      const resource = {
        extension: [SHALL.extension[0]],
        type: type,
        profile: `http://hl7.org/fhir/StructureDefinition/${type}`,
      };

      if (profiles.length > 0) {
        resource.supportedProfile = profiles;
        resource._supportedProfile = profiles.map(() => ({
          extension: [SHALL.extension[0]]
        }));
      }

      resource.interaction = [
        { ...SHALL, code: "read" },
        { ...SHALL, code: "search-type" }
      ];

      resource.searchParam = searchParams.map(([name, { definition, type }]) => {
        const param = { ...SHALL, name, type };
        if (definition) param.definition = definition;
        return param;
      });

      return resource;
    })
  }]
};

// Write the output
const outputPath = 'input/resources/CapabilityStatement-mii-cps-kerndatensatz-complete.json';
writeFileSync(outputPath, JSON.stringify(capabilityStatement, null, 2) + '\n');
console.log(`\nWritten to: ${outputPath}`);
