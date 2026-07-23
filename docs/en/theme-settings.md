# Global Theme Settings

Open **Theme settings** in the theme editor to manage your store's brand styling and interactions in one place. Select an item below for detailed instructions.

<nav class="settings-grid" aria-label="Global theme settings">
  <a class="settings-card" href="/en/settings/layout"><span>Layout</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/colors"><span>Colors</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/typography"><span>Typography</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/logo"><span>Logo and favicon</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/animations"><span>Animations</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/product-cards"><span>Product cards</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/input"><span>Inputs</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/button"><span>Buttons</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/dialog"><span>Dialogs</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/toast"><span>Toast notifications</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/search"><span>Search</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/cart"><span>Cart</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/focus"><span>Focus styles</span><span class="setting-arrow" aria-hidden="true">›</span></a>
  <a class="settings-card" href="/en/settings/social-icon"><span>Social media</span><span class="setting-arrow" aria-hidden="true">›</span></a>
</nav>

<style scoped>
.settings-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px 14px; margin-top: 28px; }
.settings-card { display: grid; grid-template-columns: minmax(0, 1fr) 18px; align-items: center; min-height: 52px; padding: 10px 14px; color: var(--vp-c-text-1); font-weight: 500; text-decoration: none; border: 1px solid var(--vp-c-divider); border-radius: 6px; background: var(--vp-c-bg); transition: border-color 0.2s, color 0.2s, background-color 0.2s; }
.settings-card:hover, .settings-card:focus-visible { color: var(--vp-c-brand-1); border-color: var(--vp-c-brand-1); background: var(--vp-c-brand-soft); }
.setting-arrow { color: var(--vp-c-text-3); font-size: 24px; font-weight: 300; line-height: 1; text-align: right; }
.settings-card:hover .setting-arrow, .settings-card:focus-visible .setting-arrow { color: var(--vp-c-brand-1); }
@media (max-width: 640px) { .settings-grid { grid-template-columns: 1fr; gap: 10px; margin-top: 22px; } }
</style>
