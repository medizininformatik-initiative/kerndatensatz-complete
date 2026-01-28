#!/usr/bin/env python3
"""
Extract MII FHIR Profile data from StructureDefinition files.
Generates JSON data structure for interactive HTML visualization.
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict


class ProfileExtractor:
    """Extract profile information from FHIR StructureDefinition files."""

    def __init__(self, fhir_cache_dir: str = None):
        """Initialize with FHIR package cache directory."""
        if fhir_cache_dir is None:
            fhir_cache_dir = os.path.expanduser("~/.fhir/packages")
        self.fhir_cache_dir = Path(fhir_cache_dir)
        self.profiles = {}
        self.modules = defaultdict(list)

    def extract_all_mii_profiles(self) -> Dict[str, Any]:
        """Extract all MII profiles from local package cache."""
        print("Scanning for MII packages...")

        # Find all MII package directories
        mii_packages = sorted(self.fhir_cache_dir.glob(
            "de.medizininformatikinitiative.kerndatensatz.*#2025.0.*"
        ))

        for pkg_dir in mii_packages:
            module_name = self._extract_module_name(pkg_dir.name)
            print(f"Processing module: {module_name}")

            package_json = pkg_dir / "package" / "package.json"
            if not package_json.exists():
                continue

            # Load package metadata
            with open(package_json, 'r', encoding='utf-8') as f:
                pkg_meta = json.load(f)

            # Find all StructureDefinition files
            sd_files = (pkg_dir / "package").glob("StructureDefinition-*.json")

            for sd_file in sd_files:
                profile = self._extract_profile(sd_file, module_name, pkg_meta)
                if profile:
                    self.profiles[profile['id']] = profile
                    self.modules[module_name].append(profile['id'])

        print(f"\nExtracted {len(self.profiles)} profiles from {len(self.modules)} modules")
        return self._build_output_structure()

    def _extract_module_name(self, package_dir_name: str) -> str:
        """Extract module name from package directory name."""
        # e.g., "de.medizininformatikinitiative.kerndatensatz.person#2025.0.0"
        parts = package_dir_name.split('#')[0].split('.')
        return parts[-1] if parts else "unknown"

    def _extract_profile(self, sd_file: Path, module: str, pkg_meta: Dict) -> Optional[Dict]:
        """Extract profile information from a StructureDefinition file."""
        try:
            with open(sd_file, 'r', encoding='utf-8') as f:
                sd = json.load(f)

            # Only process profiles (not extensions, logical models, etc.)
            if sd.get('kind') != 'resource' or sd.get('derivation') != 'constraint':
                return None

            profile_id = sd.get('id', sd.get('name', 'unknown'))

            # Extract differential elements
            differential_elements = []
            if 'differential' in sd and 'element' in sd['differential']:
                for elem in sd['differential']['element']:
                    if elem['path'] == sd.get('type'):
                        # Skip root element
                        continue
                    differential_elements.append(self._extract_element_info(elem))

            profile_data = {
                'id': profile_id,
                'url': sd.get('url', ''),
                'name': sd.get('name', profile_id),
                'title': sd.get('title', sd.get('name', profile_id)),
                'status': sd.get('status', 'unknown'),
                'description': sd.get('description', ''),
                'baseDefinition': sd.get('baseDefinition', ''),
                'type': sd.get('type', ''),
                'module': module,
                'version': pkg_meta.get('version', ''),
                'differential': differential_elements,
                'elementCount': len(differential_elements)
            }

            return profile_data

        except Exception as e:
            print(f"  Error processing {sd_file.name}: {e}")
            return None

    def _extract_element_info(self, element: Dict) -> Dict:
        """Extract relevant information from a differential element."""
        elem_info = {
            'path': element.get('path', ''),
            'short': element.get('short', ''),
            'definition': element.get('definition', ''),
            'min': element.get('min'),
            'max': element.get('max'),
            'mustSupport': element.get('mustSupport', False),
            'isModifier': element.get('isModifier', False)
        }

        # Extract type constraints
        if 'type' in element:
            types = []
            for t in element['type']:
                type_info = {'code': t.get('code', '')}
                if 'profile' in t:
                    type_info['profile'] = t['profile']
                if 'targetProfile' in t:
                    type_info['targetProfile'] = t['targetProfile']
                types.append(type_info)
            elem_info['type'] = types

        # Extract binding information
        if 'binding' in element:
            binding = element['binding']
            elem_info['binding'] = {
                'strength': binding.get('strength', ''),
                'valueSet': binding.get('valueSet', ''),
                'description': binding.get('description', '')
            }

        # Extract slicing information
        if 'slicing' in element:
            elem_info['slicing'] = {
                'discriminator': element['slicing'].get('discriminator', []),
                'rules': element['slicing'].get('rules', ''),
                'description': element['slicing'].get('description', '')
            }

        # Extract constraints
        if 'constraint' in element:
            elem_info['constraints'] = [
                {
                    'key': c.get('key', ''),
                    'severity': c.get('severity', ''),
                    'human': c.get('human', ''),
                    'expression': c.get('expression', '')
                }
                for c in element['constraint']
            ]

        # Check if this is an extension
        if '.extension' in elem_info['path'] or elem_info['path'].startswith('extension'):
            elem_info['isExtension'] = True
            if 'sliceName' in element:
                elem_info['sliceName'] = element['sliceName']

        # Check if this is a slice
        if 'sliceName' in element:
            elem_info['sliceName'] = element['sliceName']

        return elem_info

    def _build_output_structure(self) -> Dict:
        """Build final output structure with hierarchy information."""
        output = {
            'metadata': {
                'generated': 'auto',
                'totalProfiles': len(self.profiles),
                'modules': list(self.modules.keys())
            },
            'modules': {}
        }

        # Organize by module
        for module, profile_ids in self.modules.items():
            module_profiles = []
            for pid in profile_ids:
                profile = self.profiles[pid]

                # Try to find parent profile
                parent_name = self._get_parent_name(profile['baseDefinition'])
                profile['parentName'] = parent_name

                module_profiles.append(profile)

            # Sort by name
            module_profiles.sort(key=lambda p: p['name'])

            output['modules'][module] = {
                'name': module,
                'profileCount': len(module_profiles),
                'profiles': module_profiles
            }

        return output

    def _get_parent_name(self, base_definition_url: str) -> str:
        """Extract a readable name from baseDefinition URL."""
        if not base_definition_url:
            return "Unknown"

        # Extract the last part of the URL
        parts = base_definition_url.split('/')
        if len(parts) > 0:
            name = parts[-1]
            # Clean up common prefixes
            name = name.replace('mii-pr-', '').replace('MII-PR-', '')
            return name

        return "Unknown"

    def save_to_file(self, output_data: Dict, output_path: str):
        """Save extracted data to JSON file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
        print(f"\nSaved profile data to: {output_path}")


def main():
    """Main entry point."""
    import sys

    # Determine output directory
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    output_dir = project_dir / "docs" / "profiles"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / "profile_data.json"

    print("MII Profile Extractor")
    print("=" * 60)

    # Extract profiles
    extractor = ProfileExtractor()
    profile_data = extractor.extract_all_mii_profiles()

    # Save to file
    extractor.save_to_file(profile_data, str(output_file))

    # Print summary
    print("\nSummary:")
    print(f"  Total profiles: {profile_data['metadata']['totalProfiles']}")
    print(f"  Modules: {len(profile_data['metadata']['modules'])}")
    for module, data in profile_data['modules'].items():
        print(f"    - {module}: {data['profileCount']} profiles")

    return 0


if __name__ == "__main__":
    exit(main())
