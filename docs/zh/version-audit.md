# 新版安装包与文档核对报告

`latest.zip` · Ceylune 1.0.0 · SHA-256: `68aee5dbbe45a5e1ff7f5a45551c319d819a98d2e1f3dcac3873c90736e895dd`

本次只读取压缩包中的设置定义、语言和源码，不执行其中的文件。未删除或注释旧文档，原说明保留供人工处理。

## 范围与标记

共 16 组全局设置、52 个分区、54 个分区内区块类型声明、770 个设置字段声明（包含配色子字段及区块字段；不同位置同名 ID 分别统计）。

- **安装包无此设置**：对应分区 schema 未声明该编辑器设置；不等于整个主题没有此功能。
- **待核对**：仅凭名称或旧说明无法确认对应关系。
- **补充页面**：当前文档原先没有独立页面；不能据此认定该功能是本版本首次新增。
- 本次没有旧版安装包，无法判定哪些字段是版本间新增或删除；本报告比较的是当前文档与这份新版包。
- 安装包仅提供英文 schema 语言文件，中文页面保留英文后台名称以便对照。

## 安装包无此设置：404 页面旧说明

404 页面原文混入了联系表单设置；以下六个独立控件未在 `sections/404.liquid` schema 中声明，已在中英文原文标题旁标注。标题、描述等共享名称不能证明其联系表单用途，相关原文也应人工修改。

| 原文项目 | 核对结果 |
| --- | --- |
| Button text | 安装包无此设置（404 分区范围） |
| Form background color | 安装包无此设置（404 分区范围） |
| Form text color | 安装包无此设置（404 分区范围） |
| Image | 安装包无此设置（404 分区范围） |
| Image alt text | 安装包无此设置（404 分区范围） |
| Success message | 安装包无此设置（404 分区范围） |

[404 原文及完整设置清单](/zh/sections/404)

## 其他不匹配的旧设置

| 页面 | 旧设置 | 标记 / 新版依据 |
| --- | --- | --- |
| [Animations](/zh/settings/animations) | Content reveal style、Media reveal style、Motion speed、Reveal behavior | 安装包未声明这四个独立控件，原文已逐处标注 |
| [Animations](/zh/settings/animations) | Enable motion | 名称已改为 Scroll and reveal animations，ID 为 `motion_enabled`；保留开关说明，核对其具体作用范围 |
| [Layout](/zh/settings/layout) | Setting Small Border Radius | Layout 中未声明此设置，已标注 |
| [Layout](/zh/settings/layout) | Page width：1000–1600 px | 范围不一致；新版为 1000–2000 px，默认 1600 px |

## 全局设置清单

| 页面 | 文档状态 | 来源 |
| --- | --- | --- |
| [Logo](/zh/settings/logo) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Typography](/zh/settings/typography) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Layout](/zh/settings/layout) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Colors](/zh/settings/colors) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Input](/zh/settings/input) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Button](/zh/settings/button) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Dialog](/zh/settings/dialog) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Product cards](/zh/settings/product-cards) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Product badges](/zh/settings/product-badges) | 补充页面 | `config/settings_schema.json` |
| [Toast](/zh/settings/toast) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Cart](/zh/settings/cart) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Search](/zh/settings/search) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Collection navigation](/zh/settings/collection-navigation) | 补充页面 | `config/settings_schema.json` |
| [Animations](/zh/settings/animations) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Focus](/zh/settings/focus) | 原页面补充完整清单 | `config/settings_schema.json` |
| [Social icon](/zh/settings/social-icon) | 原页面补充完整清单 | `config/settings_schema.json` |

## 分区与内容块清单

| 页面 | 文档状态 | 来源 |
| --- | --- | --- |
| [Not found](/zh/sections/404) | 原页面补充完整清单 | `sections/404.liquid` |
| [t:sections.about-stats.name](/zh/sections/about-stats) | 原页面补充完整清单 | `sections/about-stats.liquid` |
| [Announcement bar](/zh/sections/announcement-bar) | 补充页面 | `sections/announcement-bar.liquid` |
| [Article](/zh/sections/article) | 补充页面 | `sections/article.liquid` |
| [Before/after comparison](/zh/sections/before-after-comparison) | 原页面补充完整清单 | `sections/before-after-comparison.liquid` |
| [Blog stories](/zh/sections/blog-stories) | 原页面补充完整清单 | `sections/blog-stories.liquid` |
| [Blog](/zh/sections/blog) | 补充页面 | `sections/blog.liquid` |
| [Brand statement](/zh/sections/brand-statement) | 原页面补充完整清单 | `sections/brand-statement.liquid` |
| [Cart overlay](/zh/sections/cart-overlay) | 原页面补充完整清单 | `sections/cart-overlay.liquid` |
| [Cart](/zh/sections/cart) | 补充页面 | `sections/cart.liquid` |
| [t:sections.category-grid.name](/zh/sections/category-grid) | 原页面补充完整清单 | `sections/category-grid.liquid` |
| [Collection list](/zh/sections/collection-list) | 补充页面 | `sections/collection-list.liquid` |
| [Collection nav items](/zh/sections/collection-navigation-items) | 补充页面 | `sections/collection-navigation-items.liquid` |
| [Collection](/zh/sections/collection) | 补充页面 | `sections/collection.liquid` |
| [Collections grid](/zh/sections/collections) | 原页面补充完整清单 | `sections/collections.liquid` |
| [Custom Liquid](/zh/sections/custom-liquid) | 原页面补充完整清单 | `sections/custom-liquid.liquid` |
| [Editorial collage](/zh/sections/editorial-collage) | 补充页面 | `sections/editorial-collage.liquid` |
| [Feature tabs](/zh/sections/feature-tabs) | 补充页面 | `sections/feature-tabs.liquid` |
| [Featured product](/zh/sections/featured-product) | 原页面补充完整清单 | `sections/featured-product.liquid` |
| [Featured products](/zh/sections/featured-products) | 原页面补充完整清单 | `sections/featured-products.liquid` |
| [Footer](/zh/sections/footer) | 补充页面 | `sections/footer.liquid` |
| [Formula details](/zh/sections/formula-details) | 补充页面 | `sections/formula-details.liquid` |
| [t:sections.google-map.name](/zh/sections/google-map) | 原页面补充完整清单 | `sections/google-map.liquid` |
| [Header](/zh/sections/header) | 补充页面 | `sections/header.liquid` |
| [Icon with text](/zh/sections/icon-with-text) | 原页面补充完整清单 | `sections/icon-with-text.liquid` |
| [About us](/zh/sections/main-page-about) | 补充页面 | `sections/main-page-about.liquid` |
| [Contact us](/zh/sections/main-page-contact) | 补充页面 | `sections/main-page-contact.liquid` |
| [Mood finder](/zh/sections/mood-finder) | 补充页面 | `sections/mood-finder.liquid` |
| [Newsletter banner](/zh/sections/newsletter-banner) | 原页面补充完整清单 | `sections/newsletter-banner.liquid` |
| [Newsletter overlay](/zh/sections/newsletter-overlay) | 原页面补充完整清单 | `sections/newsletter-overlay.liquid` |
| [Page](/zh/sections/page) | 原页面补充完整清单 | `sections/page.liquid` |
| [Password footer](/zh/sections/password-footer) | 原页面补充完整清单 | `sections/password-footer.liquid` |
| [Password header](/zh/sections/password-header) | 原页面补充完整清单 | `sections/password-header.liquid` |
| [Password](/zh/sections/password) | 原页面补充完整清单 | `sections/password.liquid` |
| [Philosophy section](/zh/sections/philosophy-section) | 原页面补充完整清单 | `sections/philosophy-section.liquid` |
| [Pickup availability](/zh/sections/pickup-availability) | 原页面补充完整清单 | `sections/pickup-availability.liquid` |
| [Comparison table](/zh/sections/product-comparison-table) | 原页面补充完整清单 | `sections/product-comparison-table.liquid` |
| [Product recommendations](/zh/sections/product-recommendations) | 原页面补充完整清单 | `sections/product-recommendations.liquid` |
| [Product](/zh/sections/product) | 补充页面 | `sections/product.liquid` |
| [Promise section](/zh/sections/promise-section) | 原页面补充完整清单 | `sections/promise-section.liquid` |
| [Promo banner](/zh/sections/promo-bannder) | 原页面补充完整清单 | `sections/promo-bannder.liquid` |
| [Promotion countdown](/zh/sections/promotion-countdown) | 原页面补充完整清单 | `sections/promotion-countdown.liquid` |
| [Ritual steps](/zh/sections/ritual-steps) | 补充页面 | `sections/ritual-steps.liquid` |
| [Routine showcase](/zh/sections/routine-showcase) | 原页面补充完整清单 | `sections/routine-showcase.liquid` |
| [Scatter gallery](/zh/sections/scatter-gallery) | 补充页面 | `sections/scatter-gallery.liquid` |
| [Collection product list](/zh/sections/scroll-categories) | 原页面补充完整清单 | `sections/scroll-categories.liquid` |
| [Scrolling icon with text](/zh/sections/scrolling-icon-with-text) | 原页面补充完整清单 | `sections/scrolling-icon-with-text.liquid` |
| [Search overlay](/zh/sections/search-overlay) | 原页面补充完整清单 | `sections/search-overlay.liquid` |
| [Search](/zh/sections/search) | 补充页面 | `sections/search.liquid` |
| [Slideshow](/zh/sections/slides-show) | 原页面补充完整清单 | `sections/slides-show.liquid` |
| [Featured testimonial](/zh/sections/testimonial-featured) | 原页面补充完整清单 | `sections/testimonial-featured.liquid` |
| [Video banner](/zh/sections/video-banner) | 原页面补充完整清单 | `sections/video-banner.liquid` |

## 未找到对应定义的原页面

现有全局设置和分区独立页面均找到对应定义。

## 待核对与人工处理

- 历史截图与正文未进行 Shopify 实机验证；各页末尾新版 schema 清单优先作为字段依据。
- `custom-liquid` 的 Simple text、Product vendor、Existing snippet 是示例标题，不是编辑器设置，不标为缺失。
- `newsletter-overlay` 的 Audience and timing 是说明标题，不是单独的控件。
- 404 页关于联系表单、提交成功和图片的旧说明应一起检查，再手动删除或注释。
- 颜色子字段、内容块设置与分区设置分开列出；不要因为在分区顶层找不到就删除。
- 这里只确认 schema 声明，不保证前台代码使用了每个字段，也不把没有默认值的字段判为不支持。

## 安装包缺少的后台翻译

下列翻译键在安装包英文 schema 语言文件中未找到。文档保留原键作为证据；这是安装包翻译缺失，不代表设置项缺失。

- `t:sections.about-stats.block_settings.label`
- `t:sections.about-stats.block_settings.value`
- `t:sections.about-stats.blocks.stat`
- `t:sections.about-stats.content.padding`
- `t:sections.about-stats.content.stat_subtitle`
- `t:sections.about-stats.content.stat_title`
- `t:sections.about-stats.defaults.block_label`
- `t:sections.about-stats.defaults.block_value`
- `t:sections.about-stats.defaults.description_html`
- `t:sections.about-stats.defaults.link_text`
- `t:sections.about-stats.name`
- `t:sections.about-stats.settings.color_scheme`
- `t:sections.about-stats.settings.description`
- `t:sections.about-stats.settings.image`
- `t:sections.about-stats.settings.link`
- `t:sections.about-stats.settings.link_text`
- `t:sections.about-stats.settings.padding_bottom`
- `t:sections.about-stats.settings.padding_top`
- `t:sections.about-stats.settings.secondary_image`
- `t:sections.about-stats.settings.year_text`
- `t:sections.category-grid.block_settings.collection`
- `t:sections.category-grid.block_settings.custom_image`
- `t:sections.category-grid.block_settings.custom_link`
- `t:sections.category-grid.block_settings.custom_title`
- `t:sections.category-grid.block_settings.product`
- `t:sections.category-grid.block_settings.source_type`
- `t:sections.category-grid.blocks.item`
- `t:sections.category-grid.blocks_defaults.title`
- `t:sections.category-grid.content.card`
- `t:sections.category-grid.content.grid`
- `t:sections.category-grid.content.heading`
- `t:sections.category-grid.content.layout`
- `t:sections.category-grid.content.padding`
- `t:sections.category-grid.defaults.heading`
- `t:sections.category-grid.defaults.subheading`
- `t:sections.category-grid.defaults.view_all_label`
- `t:sections.category-grid.info.gap`
- `t:sections.category-grid.name`
- `t:sections.category-grid.options.1_column`
- `t:sections.category-grid.options.2_columns`
- `t:sections.category-grid.options.arch`
- `t:sections.category-grid.options.border`
- `t:sections.category-grid.options.center`
- `t:sections.category-grid.options.circle`
- `t:sections.category-grid.options.collection`
- `t:sections.category-grid.options.custom`
- `t:sections.category-grid.options.fixed_width`
- `t:sections.category-grid.options.full_width`
- `t:sections.category-grid.options.left`
- `t:sections.category-grid.options.none`
- `t:sections.category-grid.options.product`
- `t:sections.category-grid.options.right`
- `t:sections.category-grid.options.rounded`
- `t:sections.category-grid.options.soft`
- `t:sections.category-grid.options.square`
- `t:sections.category-grid.settings.color_scheme`
- `t:sections.category-grid.settings.desktop_columns`
- `t:sections.category-grid.settings.desktop_rows`
- `t:sections.category-grid.settings.gap`
- `t:sections.category-grid.settings.heading`
- `t:sections.category-grid.settings.heading_size`
- `t:sections.category-grid.settings.image_frame_style`
- `t:sections.category-grid.settings.image_shape`
- `t:sections.category-grid.settings.mobile_columns`
- `t:sections.category-grid.settings.padding_bottom`
- `t:sections.category-grid.settings.padding_top`
- `t:sections.category-grid.settings.section_width`
- `t:sections.category-grid.settings.show_arrow`
- `t:sections.category-grid.settings.show_grid_borders`
- `t:sections.category-grid.settings.subheading`
- `t:sections.category-grid.settings.subheading_size`
- `t:sections.category-grid.settings.text_alignment`
- `t:sections.category-grid.settings.view_all_label`
- `t:sections.category-grid.settings.view_all_link`
- `t:sections.google-map.content.padding`
- `t:sections.google-map.info.map_embed_code`
- `t:sections.google-map.name`
- `t:sections.google-map.settings.map_embed_code`
- `t:sections.google-map.settings.map_height`
- `t:sections.google-map.settings.padding_bottom`
- `t:sections.google-map.settings.padding_top`
- `t:sections.google-map.settings.show_map`
- `t:sections.scroll-categories.options.body_2xl`
- `t:sections.scroll-categories.options.body_3xl`
- `t:sections.slides-show.options.heading_2xl`
- `t:sections.slides-show.options.heading_3xl`
- `t:sections.slides-show.options.heading_4xl`
- `t:sections.slides-show.options.heading_h1`
- `t:sections.slides-show.options.heading_h2`
- `t:sections.slides-show.options.heading_h3`
- `t:sections.slides-show.options.heading_h4`
- `t:sections.slides-show.options.heading_h5`
- `t:sections.slides-show.options.heading_h6`
- `t:sections.slides-show.options.heading_xl`