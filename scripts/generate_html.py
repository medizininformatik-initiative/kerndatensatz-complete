#!/usr/bin/env python3
"""
Generate interactive HTML visualizations for MII FHIR profiles.
Creates one HTML file per module with accordion-based differential display.
"""

import json
from pathlib import Path
from typing import Dict, List, Any


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{MODULE_TITLE}} - MII Profile Differential</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }

        .header {
            background: #2c3e50;
            color: white;
            padding: 1rem 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .header h1 {
            font-size: 1.5rem;
            font-weight: 600;
        }

        .header .breadcrumb {
            font-size: 0.9rem;
            opacity: 0.8;
            margin-top: 0.5rem;
        }

        .header .breadcrumb a {
            color: #3498db;
            text-decoration: none;
        }

        .header .breadcrumb a:hover {
            text-decoration: underline;
        }

        .container {
            max-width: 1600px;
            margin: 0 auto;
            padding: 2rem;
        }

        .profile-selector {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 1.5rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        }

        .profile-selector select {
            width: 100%;
            padding: 0.5rem;
            font-size: 1rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            background: white;
        }

        .profile-card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
            overflow: hidden;
        }

        .profile-header {
            background: #ecf0f1;
            padding: 1rem 1.5rem;
            cursor: pointer;
            user-select: none;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #bdc3c7;
        }

        .profile-header:hover {
            background: #dfe4e8;
        }

        .profile-header.expanded {
            background: #3498db;
            color: white;
        }

        .profile-header .title {
            font-weight: 600;
            font-size: 1.1rem;
        }

        .profile-header .indicator {
            font-size: 1.2rem;
            transition: transform 0.3s;
        }

        .profile-header.expanded .indicator {
            transform: rotate(90deg);
        }

        .profile-body {
            display: none;
            padding: 1.5rem;
        }

        .profile-body.expanded {
            display: block;
        }

        .profile-info {
            background: #f8f9fa;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1.5rem;
            font-size: 0.9rem;
        }

        .profile-info p {
            margin: 0.3rem 0;
        }

        .profile-info .label {
            font-weight: 600;
            color: #7f8c8d;
            display: inline-block;
            width: 120px;
        }

        .two-panel {
            display: grid;
            grid-template-columns: 400px 1fr;
            gap: 1.5rem;
            min-height: 400px;
        }

        .elements-panel {
            border-right: 1px solid #ddd;
            padding-right: 1rem;
        }

        .elements-list {
            list-style: none;
        }

        .element-item {
            padding: 0.75rem 1rem;
            margin-bottom: 0.5rem;
            background: #f8f9fa;
            border-left: 3px solid #95a5a6;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.2s;
        }

        .element-item:hover {
            background: #e9ecef;
            transform: translateX(4px);
        }

        .element-item.active {
            background: #3498db;
            color: white;
            border-left-color: #2980b9;
        }

        .element-item .path {
            font-weight: 600;
            font-size: 0.95rem;
        }

        .element-item .badges {
            margin-top: 0.3rem;
        }

        .badge {
            display: inline-block;
            padding: 0.2rem 0.5rem;
            font-size: 0.75rem;
            border-radius: 3px;
            margin-right: 0.3rem;
            font-weight: 600;
        }

        .badge-ms {
            background: #e74c3c;
            color: white;
        }

        .badge-ext {
            background: #9b59b6;
            color: white;
        }

        .badge-card {
            background: #f39c12;
            color: white;
        }

        .badge-slice {
            background: #16a085;
            color: white;
        }

        .details-panel {
            padding-left: 1rem;
        }

        .details-empty {
            color: #95a5a6;
            font-style: italic;
            padding: 2rem;
            text-align: center;
        }

        .detail-section {
            margin-bottom: 1.5rem;
        }

        .detail-section h3 {
            font-size: 1.1rem;
            color: #2c3e50;
            margin-bottom: 0.75rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #3498db;
        }

        .detail-row {
            padding: 0.5rem 0;
            display: grid;
            grid-template-columns: 150px 1fr;
            gap: 1rem;
        }

        .detail-label {
            font-weight: 600;
            color: #7f8c8d;
        }

        .detail-value {
            color: #2c3e50;
        }

        .detail-value code {
            background: #ecf0f1;
            padding: 0.2rem 0.4rem;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9rem;
        }

        .type-list, .constraint-list {
            list-style: none;
        }

        .type-item, .constraint-item {
            background: #f8f9fa;
            padding: 0.5rem;
            margin: 0.3rem 0;
            border-radius: 4px;
            font-size: 0.9rem;
        }

        .binding-info {
            background: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 0.75rem;
            border-radius: 4px;
        }

        .no-profiles {
            text-align: center;
            padding: 3rem;
            color: #95a5a6;
        }

        @media (max-width: 1024px) {
            .two-panel {
                grid-template-columns: 1fr;
            }

            .elements-panel {
                border-right: none;
                border-bottom: 1px solid #ddd;
                padding-bottom: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>MII Profile Differential: {{MODULE_TITLE}}</h1>
        <div class="breadcrumb">
            <a href="index.html">← All Modules</a> / {{MODULE_NAME}}
        </div>
    </div>

    <div class="container">
        <div class="profile-selector">
            <select id="profileSelect" onchange="selectProfile(this.value)">
                <option value="">Select a profile...</option>
                {{PROFILE_OPTIONS}}
            </select>
        </div>

        <div id="profilesContainer">
            {{PROFILES_HTML}}
        </div>
    </div>

    <script>
        // Embedded profile data
        const profileData = {{PROFILE_DATA}};

        let currentProfileId = null;
        let currentElementIndex = null;

        // Initialize on load
        document.addEventListener('DOMContentLoaded', function() {
            // Auto-select first profile if available
            const profiles = Object.keys(profileData);
            if (profiles.length > 0) {
                selectProfile(profiles[0]);
            }
        });

        function selectProfile(profileId) {
            if (!profileId) return;

            currentProfileId = profileId;

            // Hide all profiles
            document.querySelectorAll('.profile-card').forEach(card => {
                card.style.display = 'none';
            });

            // Show selected profile
            const profileCard = document.getElementById('profile-' + profileId);
            if (profileCard) {
                profileCard.style.display = 'block';
                // Auto-expand if collapsed
                const body = profileCard.querySelector('.profile-body');
                const header = profileCard.querySelector('.profile-header');
                if (body && !body.classList.contains('expanded')) {
                    toggleProfile(profileId);
                }
            }

            // Update selector
            document.getElementById('profileSelect').value = profileId;

            // Clear element selection
            clearElementSelection();
        }

        function toggleProfile(profileId) {
            const card = document.getElementById('profile-' + profileId);
            if (!card) return;

            const header = card.querySelector('.profile-header');
            const body = card.querySelector('.profile-body');

            if (body.classList.contains('expanded')) {
                body.classList.remove('expanded');
                header.classList.remove('expanded');
            } else {
                body.classList.add('expanded');
                header.classList.add('expanded');
            }
        }

        function selectElement(profileId, elementIndex) {
            currentElementIndex = elementIndex;

            // Update active state
            document.querySelectorAll('.element-item').forEach(item => {
                item.classList.remove('active');
            });

            const elementItem = document.querySelector(`[data-profile="${profileId}"][data-element="${elementIndex}"]`);
            if (elementItem) {
                elementItem.classList.add('active');
            }

            // Show element details
            const detailsPanel = document.getElementById('details-' + profileId);
            if (detailsPanel) {
                const profile = profileData[profileId];
                const element = profile.differential[elementIndex];
                detailsPanel.innerHTML = renderElementDetails(element);
            }
        }

        function clearElementSelection() {
            document.querySelectorAll('.element-item').forEach(item => {
                item.classList.remove('active');
            });

            if (currentProfileId) {
                const detailsPanel = document.getElementById('details-' + currentProfileId);
                if (detailsPanel) {
                    detailsPanel.innerHTML = '<div class="details-empty">Click an element on the left to see details</div>';
                }
            }
        }

        function renderElementDetails(element) {
            let html = '<div class="detail-section">';
            html += '<h3>' + escapeHtml(element.path) + '</h3>';

            // Cardinality
            if (element.min !== undefined || element.max !== undefined) {
                html += '<div class="detail-row">';
                html += '<div class="detail-label">Cardinality</div>';
                html += '<div class="detail-value"><code>' + (element.min ?? '') + '..' + (element.max ?? '') + '</code>';
                if (element.mustSupport) {
                    html += ' <span class="badge badge-ms">Must Support</span>';
                }
                html += '</div></div>';
            }

            // Short description
            if (element.short) {
                html += '<div class="detail-row">';
                html += '<div class="detail-label">Short</div>';
                html += '<div class="detail-value">' + escapeHtml(element.short) + '</div>';
                html += '</div>';
            }

            // Definition
            if (element.definition) {
                html += '<div class="detail-row">';
                html += '<div class="detail-label">Definition</div>';
                html += '<div class="detail-value">' + escapeHtml(element.definition) + '</div>';
                html += '</div>';
            }

            html += '</div>';

            // Types
            if (element.type && element.type.length > 0) {
                html += '<div class="detail-section">';
                html += '<h3>Type Constraints</h3>';
                html += '<ul class="type-list">';
                element.type.forEach(type => {
                    html += '<li class="type-item">';
                    html += '<strong>Code:</strong> ' + escapeHtml(type.code);
                    if (type.profile) {
                        html += '<br><strong>Profile:</strong> ' + renderUrls(type.profile);
                    }
                    if (type.targetProfile) {
                        html += '<br><strong>Target Profile:</strong> ' + renderUrls(type.targetProfile);
                    }
                    html += '</li>';
                });
                html += '</ul></div>';
            }

            // Binding
            if (element.binding) {
                html += '<div class="detail-section">';
                html += '<h3>Terminology Binding</h3>';
                html += '<div class="binding-info">';
                html += '<div><strong>Strength:</strong> ' + escapeHtml(element.binding.strength) + '</div>';
                html += '<div><strong>ValueSet:</strong> <code>' + escapeHtml(element.binding.valueSet) + '</code></div>';
                if (element.binding.description) {
                    html += '<div><strong>Description:</strong> ' + escapeHtml(element.binding.description) + '</div>';
                }
                html += '</div></div>';
            }

            // Constraints
            if (element.constraints && element.constraints.length > 0) {
                html += '<div class="detail-section">';
                html += '<h3>Constraints</h3>';
                html += '<ul class="constraint-list">';
                element.constraints.forEach(c => {
                    html += '<li class="constraint-item">';
                    html += '<strong>' + escapeHtml(c.key) + '</strong> (' + escapeHtml(c.severity) + ')<br>';
                    html += escapeHtml(c.human);
                    if (c.expression) {
                        html += '<br><code>' + escapeHtml(c.expression) + '</code>';
                    }
                    html += '</li>';
                });
                html += '</ul></div>';
            }

            // Slicing
            if (element.slicing) {
                html += '<div class="detail-section">';
                html += '<h3>Slicing Information</h3>';
                html += '<div class="detail-row">';
                html += '<div class="detail-label">Rules</div>';
                html += '<div class="detail-value"><code>' + escapeHtml(element.slicing.rules) + '</code></div>';
                html += '</div>';
                if (element.slicing.description) {
                    html += '<div class="detail-row">';
                    html += '<div class="detail-label">Description</div>';
                    html += '<div class="detail-value">' + escapeHtml(element.slicing.description) + '</div>';
                    html += '</div>';
                }
                html += '</div>';
            }

            return html;
        }

        function renderUrls(urls) {
            if (Array.isArray(urls)) {
                return urls.map(url => '<code>' + escapeHtml(url) + '</code>').join(', ');
            }
            return '<code>' + escapeHtml(urls) + '</code>';
        }

        function escapeHtml(text) {
            if (!text) return '';
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }
    </script>
</body>
</html>
"""


def generate_module_html(module_name: str, module_data: Dict, output_dir: Path):
    """Generate HTML file for a single module."""
    profiles = module_data['profiles']

    if not profiles:
        print(f"  Skipping {module_name}: no profiles")
        return

    # Build profile options for selector
    profile_options = []
    for profile in profiles:
        profile_options.append(
            f'<option value="{profile["id"]}">{profile["title"]} ({profile["type"]})</option>'
        )

    # Build profiles HTML
    profiles_html = []
    profile_data_dict = {}

    for profile in profiles:
        profile_id = profile['id']
        profile_data_dict[profile_id] = profile

        # Build element list
        elements_html = []
        for idx, elem in enumerate(profile['differential']):
            # Extract simple path name
            path_parts = elem['path'].split('.')
            display_path = '.'.join(path_parts[1:]) if len(path_parts) > 1 else elem['path']

            # Build badges
            badges = []
            if elem.get('mustSupport'):
                badges.append('<span class="badge badge-ms">MS</span>')
            if elem.get('isExtension'):
                badges.append('<span class="badge badge-ext">EXT</span>')
            if elem.get('min') is not None or elem.get('max') is not None:
                badges.append('<span class="badge badge-card">⬆</span>')
            if elem.get('sliceName'):
                badges.append('<span class="badge badge-slice">SLICE</span>')

            badges_html = ''.join(badges)

            elements_html.append(f'''
                <li class="element-item"
                    data-profile="{profile_id}"
                    data-element="{idx}"
                    onclick="selectElement('{profile_id}', {idx})">
                    <div class="path">{display_path}</div>
                    <div class="badges">{badges_html}</div>
                </li>
            ''')

        # Build profile card
        profile_html = f'''
        <div class="profile-card" id="profile-{profile_id}" style="display:none;">
            <div class="profile-header" onclick="toggleProfile('{profile_id}')">
                <div class="title">{profile['title']}</div>
                <div class="indicator">▶</div>
            </div>
            <div class="profile-body">
                <div class="profile-info">
                    <p><span class="label">Name:</span> {profile['name']}</p>
                    <p><span class="label">Type:</span> {profile['type']}</p>
                    <p><span class="label">Base Definition:</span> {profile['parentName']}</p>
                    <p><span class="label">Status:</span> {profile['status']}</p>
                    <p><span class="label">Version:</span> {profile['version']}</p>
                    <p><span class="label">Elements:</span> {profile['elementCount']} differential elements</p>
                </div>

                <div class="two-panel">
                    <div class="elements-panel">
                        <h3>Differential Elements</h3>
                        <ul class="elements-list">
                            {''.join(elements_html)}
                        </ul>
                    </div>
                    <div class="details-panel" id="details-{profile_id}">
                        <div class="details-empty">Click an element on the left to see details</div>
                    </div>
                </div>
            </div>
        </div>
        '''
        profiles_html.append(profile_html)

    if not profiles_html:
        profiles_html.append('<div class="no-profiles">No profiles found for this module.</div>')

    # Replace placeholders
    html = HTML_TEMPLATE
    html = html.replace('{{MODULE_TITLE}}', module_name.capitalize())
    html = html.replace('{{MODULE_NAME}}', module_name)
    html = html.replace('{{PROFILE_OPTIONS}}', '\n'.join(profile_options))
    html = html.replace('{{PROFILES_HTML}}', '\n'.join(profiles_html))
    html = html.replace('{{PROFILE_DATA}}', json.dumps(profile_data_dict, ensure_ascii=False))

    # Write to file
    output_file = output_dir / f"{module_name}.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  Generated: {output_file.name}")


def generate_index_html(modules: Dict, output_dir: Path):
    """Generate master index page."""
    html = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MII Profile Differentials - Module Index</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            color: white;
            margin-bottom: 3rem;
        }

        .header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }

        .modules-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }

        .module-card {
            background: white;
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            text-decoration: none;
            color: inherit;
            display: block;
        }

        .module-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        }

        .module-card h2 {
            color: #2c3e50;
            font-size: 1.3rem;
            margin-bottom: 0.75rem;
        }

        .module-card .stats {
            color: #7f8c8d;
            font-size: 0.9rem;
        }

        .module-card .badge {
            background: #3498db;
            color: white;
            padding: 0.3rem 0.7rem;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            display: inline-block;
            margin-top: 0.5rem;
        }

        .footer {
            text-align: center;
            color: white;
            margin-top: 3rem;
            opacity: 0.8;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>MII Profile Differentials</h1>
            <p>Medizininformatik Initiative - FHIR Profile Visualization</p>
        </div>

        <div class="modules-grid">
"""

    # Sort modules by name
    sorted_modules = sorted(modules.items(), key=lambda x: x[0])

    for module_name, module_data in sorted_modules:
        profile_count = module_data['profileCount']
        html += f'''
            <a href="{module_name}.html" class="module-card">
                <h2>{module_name.capitalize()}</h2>
                <div class="stats">
                    <div class="badge">{profile_count} Profiles</div>
                </div>
            </a>
        '''

    html += """
        </div>

        <div class="footer">
            <p>Generated from MII Kerndatensatz 2025.0.x</p>
        </div>
    </div>
</body>
</html>
"""

    output_file = output_dir / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Generated: {output_file.name}")


def main():
    """Main entry point."""
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    profiles_dir = project_dir / "docs" / "profiles"

    # Load profile data
    data_file = profiles_dir / "profile_data.json"
    if not data_file.exists():
        print(f"Error: {data_file} not found. Run extract_profiles.py first.")
        return 1

    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("Generating HTML files...")
    print("=" * 60)

    # Generate module pages
    for module_name, module_data in data['modules'].items():
        print(f"\nModule: {module_name}")
        generate_module_html(module_name, module_data, profiles_dir)

    # Generate index page
    print("\nGenerating index page...")
    generate_index_html(data['modules'], profiles_dir)

    print("\n" + "=" * 60)
    print(f"✓ Generated {len(data['modules'])} module pages")
    print(f"✓ Open: {profiles_dir}/index.html")

    return 0


if __name__ == "__main__":
    exit(main())
