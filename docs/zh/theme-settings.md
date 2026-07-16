# 全局主题设置

在主题编辑器中打开 **主题设置**，可以统一调整商店的品牌样式和交互方式。点击下面的项目查看详细说明。

<nav class="settings-grid" aria-label="全局主题设置列表">
  <a class="settings-card" href="/zh/settings/layout">
    <span>布局设置</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/colors">
    <span>颜色设置</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/typography">
    <span>排版（字体）</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/logo">
    <span>Logo 与网站图标</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/animations">
    <span>动画效果</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/product-cards">
    <span>商品卡片</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/input">
    <span>输入框</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/button">
    <span>按钮</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/dialog">
    <span>对话框</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/toast">
    <span>Toast 轻提示</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/search">
    <span>搜索行为</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/cart">
    <span>购物车</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/focus">
    <span>焦点样式</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
  <a class="settings-card" href="/zh/settings/social-icon">
    <span>社交媒体</span>
    <span class="setting-arrow" aria-hidden="true">›</span>
  </a>
</nav>

<style scoped>
.settings-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 12px 14px;
  margin-top: 28px;
}

.settings-card {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 18px;
  align-items: center;
  min-height: 52px;
  padding: 10px 14px;
  color: var(--vp-c-text-1);
  font-weight: 500;
  text-decoration: none;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background: var(--vp-c-bg);
  transition: border-color 0.2s, color 0.2s, background-color 0.2s;
}

.settings-card:hover,
.settings-card:focus-visible {
  color: var(--vp-c-brand-1);
  border-color: var(--vp-c-brand-1);
  background: var(--vp-c-brand-soft);
}

.setting-arrow {
  color: var(--vp-c-text-3);
  font-size: 24px;
  font-weight: 300;
  line-height: 1;
  text-align: right;
}

.settings-card:hover .setting-arrow,
.settings-card:focus-visible .setting-arrow {
  color: var(--vp-c-brand-1);
}

@media (max-width: 640px) {
  .settings-grid {
    grid-template-columns: 1fr;
    gap: 10px;
    margin-top: 22px;
  }
}
</style>
