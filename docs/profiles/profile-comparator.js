/**
 * Profile Comparison functionality
 * Compares two MII FHIR profiles and shows differences
 */

class ProfileComparator {
  constructor() {
    this.selectedProfiles = [];
    this.modal = null;
  }

  initialize(modalId) {
    this.modal = document.getElementById(modalId);
  }

  addProfile(profileData) {
    // Check if already added
    if (this.selectedProfiles.find(p => p.id === profileData.id)) {
      alert('This profile is already selected for comparison');
      return false;
    }

    if (this.selectedProfiles.length >= 2) {
      alert('Maximum 2 profiles can be compared. Clear comparison first.');
      return false;
    }

    this.selectedProfiles.push(profileData);

    if (this.selectedProfiles.length === 2) {
      this.showComparison();
    } else {
      this.showSelectionStatus();
    }

    return true;
  }

  showSelectionStatus() {
    const status = document.getElementById('comparison-status');
    if (status) {
      status.innerHTML = `
        <div class="comparison-partial">
          <strong>Comparison Mode:</strong>
          ${this.selectedProfiles[0].title} selected.
          Select another profile to compare.
          <button onclick="profileComparator.clear()">Clear</button>
        </div>
      `;
      status.style.display = 'block';
    }
  }

  showComparison() {
    const [profile1, profile2] = this.selectedProfiles;

    const comparison = this.compareProfiles(
      profile1.differential,
      profile2.differential
    );

    this.modal.innerHTML = `
      <div class="comparison-overlay">
        <div class="comparison-container">
          <div class="comparison-header">
            <h2>Profile Comparison</h2>
            <button class="close-btn" onclick="profileComparator.close()">✕</button>
          </div>

          <div class="comparison-profiles">
            <div class="profile-box left">
              <div class="profile-title">${this.escapeHtml(profile1.title)}</div>
              <div class="profile-meta">
                <span class="badge">${profile1.module}</span>
                <span class="badge">${profile1.type}</span>
                <span class="badge">${profile1.elementCount} elements</span>
              </div>
            </div>
            <div class="vs-indicator">
              <span>VS</span>
            </div>
            <div class="profile-box right">
              <div class="profile-title">${this.escapeHtml(profile2.title)}</div>
              <div class="profile-meta">
                <span class="badge">${profile2.module}</span>
                <span class="badge">${profile2.type}</span>
                <span class="badge">${profile2.elementCount} elements</span>
              </div>
            </div>
          </div>

          <div class="comparison-summary">
            <div class="summary-stat">
              <div class="stat-number">${comparison.common.length}</div>
              <div class="stat-label">Common</div>
            </div>
            <div class="summary-stat different">
              <div class="stat-number">${comparison.different.length}</div>
              <div class="stat-label">Different</div>
            </div>
            <div class="summary-stat unique-left">
              <div class="stat-number">${comparison.uniqueLeft.length}</div>
              <div class="stat-label">Unique to Left</div>
            </div>
            <div class="summary-stat unique-right">
              <div class="stat-number">${comparison.uniqueRight.length}</div>
              <div class="stat-label">Unique to Right</div>
            </div>
          </div>

          <div class="comparison-tabs">
            <button class="tab-btn active" onclick="profileComparator.showTab('different')">
              Different (${comparison.different.length})
            </button>
            <button class="tab-btn" onclick="profileComparator.showTab('unique')">
              Unique Elements (${comparison.uniqueLeft.length + comparison.uniqueRight.length})
            </button>
            <button class="tab-btn" onclick="profileComparator.showTab('common')">
              Common (${comparison.common.length})
            </button>
          </div>

          <div class="comparison-content">
            <div id="tab-different" class="tab-content active">
              ${this.renderDifferentElements(comparison.different)}
            </div>
            <div id="tab-unique" class="tab-content">
              ${this.renderUniqueElements(comparison.uniqueLeft, comparison.uniqueRight, profile1.title, profile2.title)}
            </div>
            <div id="tab-common" class="tab-content">
              ${this.renderCommonElements(comparison.common)}
            </div>
          </div>
        </div>
      </div>
    `;

    this.modal.style.display = 'flex';
  }

  showTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
      tab.classList.remove('active');
    });
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.classList.remove('active');
    });

    // Show selected tab
    document.getElementById(`tab-${tabName}`).classList.add('active');
    event.target.classList.add('active');
  }

  compareProfiles(diff1, diff2) {
    const paths1 = new Map(diff1.map(d => [d.path, d]));
    const paths2 = new Map(diff2.map(d => [d.path, d]));

    const common = [];
    const different = [];
    const uniqueLeft = [];
    const uniqueRight = [];

    // Find common and different
    for (const [path, element1] of paths1) {
      if (paths2.has(path)) {
        const element2 = paths2.get(path);
        if (this.areElementsEqual(element1, element2)) {
          common.push({ path, left: element1, right: element2 });
        } else {
          different.push({ path, left: element1, right: element2 });
        }
      } else {
        uniqueLeft.push(element1);
      }
    }

    // Find unique to right
    for (const [path, element2] of paths2) {
      if (!paths1.has(path)) {
        uniqueRight.push(element2);
      }
    }

    return { common, different, uniqueLeft, uniqueRight };
  }

  areElementsEqual(el1, el2) {
    return (
      el1.min === el2.min &&
      el1.max === el2.max &&
      el1.mustSupport === el2.mustSupport &&
      el1.isModifier === el2.isModifier &&
      JSON.stringify(el1.type) === JSON.stringify(el2.type) &&
      JSON.stringify(el1.binding) === JSON.stringify(el2.binding)
    );
  }

  renderDifferentElements(elements) {
    if (elements.length === 0) {
      return '<div class="empty-state">No differences in constraints found.</div>';
    }

    return elements.map(el => `
      <div class="element-comparison">
        <div class="element-path">${this.escapeHtml(el.path)}</div>
        <div class="comparison-grid">
          <div class="comparison-side left">
            <h4>Left Profile</h4>
            ${this.renderElementDetails(el.left)}
          </div>
          <div class="comparison-arrow">
            <span>≠</span>
          </div>
          <div class="comparison-side right">
            <h4>Right Profile</h4>
            ${this.renderElementDetails(el.right)}
          </div>
        </div>
      </div>
    `).join('');
  }

  renderUniqueElements(uniqueLeft, uniqueRight, leftTitle, rightTitle) {
    return `
      <div class="unique-comparison">
        <div class="unique-section">
          <h3>Unique to ${this.escapeHtml(leftTitle)} (${uniqueLeft.length})</h3>
          ${uniqueLeft.length === 0
            ? '<div class="empty-state">No unique elements</div>'
            : this.renderElementList(uniqueLeft)
          }
        </div>
        <div class="unique-section">
          <h3>Unique to ${this.escapeHtml(rightTitle)} (${uniqueRight.length})</h3>
          ${uniqueRight.length === 0
            ? '<div class="empty-state">No unique elements</div>'
            : this.renderElementList(uniqueRight)
          }
        </div>
      </div>
    `;
  }

  renderCommonElements(elements) {
    if (elements.length === 0) {
      return '<div class="empty-state">No common elements found.</div>';
    }

    // Show first 20, then collapsible for rest
    const visible = elements.slice(0, 20);
    const hidden = elements.slice(20);

    let html = visible.map(el => `
      <div class="element-row common">
        <span class="element-path">${this.escapeHtml(el.path)}</span>
        ${this.renderBadges(el.left)}
        <span class="status-icon">✓</span>
      </div>
    `).join('');

    if (hidden.length > 0) {
      html += `
        <div class="show-more">
          <button onclick="this.nextElementSibling.style.display='block'; this.style.display='none';">
            Show ${hidden.length} more common elements
          </button>
          <div style="display:none;">
            ${hidden.map(el => `
              <div class="element-row common">
                <span class="element-path">${this.escapeHtml(el.path)}</span>
                ${this.renderBadges(el.left)}
                <span class="status-icon">✓</span>
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    return html;
  }

  renderElementList(elements) {
    return elements.map(el => `
      <div class="element-row unique">
        <span class="element-path">${this.escapeHtml(el.path)}</span>
        ${this.renderBadges(el)}
        ${el.short ? `<span class="element-short">${this.escapeHtml(el.short)}</span>` : ''}
      </div>
    `).join('');
  }

  renderElementDetails(element) {
    const details = [];

    if (element.min !== undefined || element.max !== undefined) {
      details.push(`
        <div class="detail-item">
          <span class="detail-label">Cardinality:</span>
          <span class="detail-value"><code>${element.min ?? ''}..${element.max ?? ''}</code></span>
        </div>
      `);
    }

    if (element.mustSupport) {
      details.push(`
        <div class="detail-item">
          <span class="badge must-support">Must Support</span>
        </div>
      `);
    }

    if (element.isModifier) {
      details.push(`
        <div class="detail-item">
          <span class="badge modifier">Modifier</span>
        </div>
      `);
    }

    if (element.type && element.type.length > 0) {
      const typeStr = element.type.map(t => {
        let str = t.code;
        if (t.profile) str += ` (profile)`;
        if (t.targetProfile) str += ` → ${t.targetProfile[0]?.split('/').pop() || 'target'}`;
        return str;
      }).join(', ');
      details.push(`
        <div class="detail-item">
          <span class="detail-label">Type:</span>
          <span class="detail-value"><code>${this.escapeHtml(typeStr)}</code></span>
        </div>
      `);
    }

    if (element.binding) {
      details.push(`
        <div class="detail-item">
          <span class="detail-label">Binding:</span>
          <span class="detail-value">
            <strong>${element.binding.strength}</strong><br>
            <code>${this.escapeHtml(element.binding.valueSet || '')}</code>
          </span>
        </div>
      `);
    }

    if (element.short) {
      details.push(`
        <div class="detail-item full-width">
          <span class="detail-label">Short:</span>
          <span class="detail-value">${this.escapeHtml(element.short)}</span>
        </div>
      `);
    }

    return details.length > 0
      ? details.join('')
      : '<div class="empty-state">No constraints</div>';
  }

  renderBadges(element) {
    const badges = [];
    if (element.mustSupport) badges.push('<span class="badge must-support">MS</span>');
    if (element.isModifier) badges.push('<span class="badge modifier">M</span>');
    if (element.min && element.min > 0) badges.push(`<span class="badge min">min:${element.min}</span>`);
    if (element.max && element.max !== '*') badges.push(`<span class="badge max">max:${element.max}</span>`);
    if (element.isExtension) badges.push('<span class="badge extension">EXT</span>');
    return badges.join(' ');
  }

  clear() {
    this.selectedProfiles = [];
    const status = document.getElementById('comparison-status');
    if (status) {
      status.style.display = 'none';
    }
  }

  close() {
    this.modal.style.display = 'none';
    this.clear();
  }

  escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }
}

// Create global instance
const profileComparator = new ProfileComparator();

// Export for use in main script
if (typeof module !== 'undefined' && module.exports) {
  module.exports = ProfileComparator;
}
