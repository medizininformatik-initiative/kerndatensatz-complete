/**
 * Transform MII profile data into Cytoscape.js graph format
 */

class ProfileDataTransformer {
  constructor(profileData) {
    this.profileData = profileData;
    this.nodes = [];
    this.edges = [];
    this.baseResources = new Set();
    this.nodeIndex = new Map();
  }

  transform() {
    // First pass: Create all profile nodes and identify base resources
    for (const [moduleName, moduleData] of Object.entries(this.profileData.modules)) {
      for (const profile of moduleData.profiles) {
        this.createProfileNode(profile, moduleName);
        this.identifyBaseResource(profile);
      }
    }

    // Second pass: Create base resource nodes
    for (const baseResource of this.baseResources) {
      this.createBaseResourceNode(baseResource);
    }

    // Third pass: Create edges for inheritance relationships
    for (const [moduleName, moduleData] of Object.entries(this.profileData.modules)) {
      for (const profile of moduleData.profiles) {
        this.createInheritanceEdge(profile);
      }
    }

    // Fourth pass: Create same-type edges (profiles of same resource)
    this.createSameTypeEdges();

    return {
      elements: {
        nodes: this.nodes,
        edges: this.edges
      },
      stats: {
        totalProfiles: this.nodes.filter(n => !n.data.isBase).length,
        totalBaseResources: this.baseResources.size,
        modules: Object.keys(this.profileData.modules).length
      }
    };
  }

  createProfileNode(profile, moduleName) {
    const nodeClass = this.getNodeClass(profile);

    const node = {
      data: {
        id: profile.id,
        label: this.shortenTitle(profile.title),
        fullTitle: profile.title,
        type: profile.type,
        module: moduleName,
        baseDefinition: profile.baseDefinition,
        parentName: profile.parentName,
        differential: profile.differential,
        elementCount: profile.elementCount,
        version: profile.version,
        description: profile.description,
        url: profile.url,
        isBase: false,
        profileData: profile
      },
      classes: [nodeClass, `module-${moduleName}`, `type-${profile.type}`]
    };

    this.nodes.push(node);
    this.nodeIndex.set(profile.id, node);
  }

  createBaseResourceNode(baseResource) {
    const node = {
      data: {
        id: `base-${baseResource}`,
        label: baseResource,
        type: 'FHIR_BASE',
        isBase: true,
        description: `FHIR R4 ${baseResource} resource`
      },
      classes: ['fhir-base']
    };

    this.nodes.push(node);
    this.nodeIndex.set(`base-${baseResource}`, node);
  }

  createInheritanceEdge(profile) {
    const baseType = this.extractBaseType(profile.baseDefinition);
    const targetId = this.isMIIProfile(profile.baseDefinition)
      ? this.findMIIProfileIdFromUrl(profile.baseDefinition)
      : `base-${baseType}`;

    if (targetId) {
      this.edges.push({
        data: {
          id: `edge-${targetId}-${profile.id}`,
          source: targetId,
          target: profile.id,
          type: 'inherits',
          label: 'extends'
        },
        classes: ['inheritance-edge']
      });
    }
  }

  createSameTypeEdges() {
    // Group profiles by resource type
    const typeGroups = new Map();

    for (const node of this.nodes) {
      if (node.data.isBase) continue;

      const type = node.data.type;
      if (!typeGroups.has(type)) {
        typeGroups.set(type, []);
      }
      typeGroups.get(type).push(node.data.id);
    }

    // Create edges between profiles of same type (for comparison hints)
    // Only create edges between profiles from different modules
    for (const [type, profileIds] of typeGroups.entries()) {
      if (profileIds.length < 2) continue;

      // Create edges between profiles from different modules
      for (let i = 0; i < profileIds.length; i++) {
        for (let j = i + 1; j < profileIds.length; j++) {
          const node1 = this.nodeIndex.get(profileIds[i]);
          const node2 = this.nodeIndex.get(profileIds[j]);

          // Only connect if from different modules
          if (node1.data.module !== node2.data.module) {
            this.edges.push({
              data: {
                id: `sametype-${profileIds[i]}-${profileIds[j]}`,
                source: profileIds[i],
                target: profileIds[j],
                type: 'same-type'
              },
              classes: ['same-type-edge', 'hidden'] // Start hidden
            });
          }
        }
      }
    }
  }

  identifyBaseResource(profile) {
    const baseType = this.extractBaseType(profile.baseDefinition);
    if (baseType && !this.isMIIProfile(profile.baseDefinition)) {
      this.baseResources.add(baseType);
    }
  }

  extractBaseType(baseDefinitionUrl) {
    if (!baseDefinitionUrl) return null;

    const parts = baseDefinitionUrl.split('/');
    return parts[parts.length - 1];
  }

  isMIIProfile(url) {
    return url && url.includes('medizininformatik-initiative.de');
  }

  findMIIProfileIdFromUrl(url) {
    // Try to find profile by URL
    for (const node of this.nodes) {
      if (node.data.url === url) {
        return node.data.id;
      }
    }
    return null;
  }

  getNodeClass(profile) {
    if (this.isMIIProfile(profile.baseDefinition)) {
      return 'mii-extended-profile';
    }
    return 'mii-profile';
  }

  shortenTitle(title) {
    // Remove common prefixes for cleaner display
    return title
      .replace('MII PR ', '')
      .replace('MII_PR_', '')
      .replace(/^(Person|Diagnose|Labor|Fall|Prozedur|Medikation|Onko|ICU|MolGen|Patho|Biobank|Bildgebung|Meta)\s+/i, '');
  }
}

// Export for use in main script
if (typeof module !== 'undefined' && module.exports) {
  module.exports = ProfileDataTransformer;
}
