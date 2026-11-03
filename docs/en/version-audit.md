# Latest package documentation audit

`latest.zip` · Ceylune 1.0.0 · SHA-256: `68aee5dbbe45a5e1ff7f5a45551c319d819a98d2e1f3dcac3873c90736e895dd`

The archive was read as data only. Existing documentation is preserved for manual review.

## Scope and labels

16 global groups, 52 sections, 54 local block type declarations, 770 setting declarations including nested color fields and block fields.

- **Not declared in package**: absent from the relevant section schema, not necessarily absent as a theme feature.
- **Needs review**: no reliable equivalence established.
- **Added page**: documentation was missing; this does not prove the feature is newly introduced.
- No previous archive was supplied, so this is a documentation-to-package audit, not a version-to-version diff.
- The archive provides English schema labels only.

## Not declared: old 404 page instructions

The old 404 guide describes a contact form. These six controls are not declared in the 404 section schema and are marked beside the original headings. Shared names such as Heading and Description do not establish a contact-form purpose; review the surrounding prose too.

| Original item | Result |
| --- | --- |
| Button text | Not declared in the 404 schema |
| Form background color | Not declared in the 404 schema |
| Form text color | Not declared in the 404 schema |
| Image | Not declared in the 404 schema |
| Image alt text | Not declared in the 404 schema |
| Success message | Not declared in the 404 schema |

[404 guide and complete reference](/en/sections/404)

## Other legacy setting mismatches

| Page | Old setting | Current evidence |
| --- | --- | --- |
| [Animations](/en/settings/animations) | Content reveal style, Media reveal style, Motion speed, Reveal behavior | Four independent controls not declared; marked inline |
| [Animations](/en/settings/animations) | Enable motion | Current label: Scroll and reveal animations; ID: `motion_enabled` |
| [Layout](/en/settings/layout) | Setting Small Border Radius | Not declared in Layout; marked inline |
| [Layout](/en/settings/layout) | Page width 1000–1600 px | Current range: 1000–2000 px; default: 1600 px |

## Global settings

| Page | Documentation status | Source |
| --- | --- | --- |
| [Logo](/en/settings/logo) | Reference appended | `config/settings_schema.json` |
| [Typography](/en/settings/typography) | Reference appended | `config/settings_schema.json` |
| [Layout](/en/settings/layout) | Reference appended | `config/settings_schema.json` |
| [Colors](/en/settings/colors) | Reference appended | `config/settings_schema.json` |
| [Input](/en/settings/input) | Reference appended | `config/settings_schema.json` |
| [Button](/en/settings/button) | Reference appended | `config/settings_schema.json` |
| [Dialog](/en/settings/dialog) | Reference appended | `config/settings_schema.json` |
| [Product cards](/en/settings/product-cards) | Reference appended | `config/settings_schema.json` |
| [Product badges](/en/settings/product-badges) | Added page | `config/settings_schema.json` |
| [Toast](/en/settings/toast) | Reference appended | `config/settings_schema.json` |
| [Cart](/en/settings/cart) | Reference appended | `config/settings_schema.json` |
| [Search](/en/settings/search) | Reference appended | `config/settings_schema.json` |
| [Collection navigation](/en/settings/collection-navigation) | Added page | `config/settings_schema.json` |
| [Animations](/en/settings/animations) | Reference appended | `config/settings_schema.json` |
| [Focus](/en/settings/focus) | Reference appended | `config/settings_schema.json` |
| [Social icon](/en/settings/social-icon) | Reference appended | `config/settings_schema.json` |

## Sections and blocks

| Page | Documentation status | Source |
| --- | --- | --- |
| [Not found](/en/sections/404) | Reference appended | `sections/404.liquid` |
| [t:sections.about-stats.name](/en/sections/about-stats) | Reference appended | `sections/about-stats.liquid` |
| [Announcement bar](/en/sections/announcement-bar) | Added page | `sections/announcement-bar.liquid` |
| [Article](/en/sections/article) | Added page | `sections/article.liquid` |
| [Before/after comparison](/en/sections/before-after-comparison) | Reference appended | `sections/before-after-comparison.liquid` |
| [Blog stories](/en/sections/blog-stories) | Reference appended | `sections/blog-stories.liquid` |
| [Blog](/en/sections/blog) | Added page | `sections/blog.liquid` |
| [Brand statement](/en/sections/brand-statement) | Reference appended | `sections/brand-statement.liquid` |
| [Cart overlay](/en/sections/cart-overlay) | Reference appended | `sections/cart-overlay.liquid` |
| [Cart](/en/sections/cart) | Added page | `sections/cart.liquid` |
| [t:sections.category-grid.name](/en/sections/category-grid) | Reference appended | `sections/category-grid.liquid` |
| [Collection list](/en/sections/collection-list) | Added page | `sections/collection-list.liquid` |
| [Collection nav items](/en/sections/collection-navigation-items) | Added page | `sections/collection-navigation-items.liquid` |
| [Collection](/en/sections/collection) | Added page | `sections/collection.liquid` |
| [Collections grid](/en/sections/collections) | Reference appended | `sections/collections.liquid` |
| [Custom Liquid](/en/sections/custom-liquid) | Reference appended | `sections/custom-liquid.liquid` |
| [Editorial collage](/en/sections/editorial-collage) | Added page | `sections/editorial-collage.liquid` |
| [Feature tabs](/en/sections/feature-tabs) | Added page | `sections/feature-tabs.liquid` |
| [Featured product](/en/sections/featured-product) | Reference appended | `sections/featured-product.liquid` |
| [Featured products](/en/sections/featured-products) | Reference appended | `sections/featured-products.liquid` |
| [Footer](/en/sections/footer) | Added page | `sections/footer.liquid` |
| [Formula details](/en/sections/formula-details) | Added page | `sections/formula-details.liquid` |
| [t:sections.google-map.name](/en/sections/google-map) | Reference appended | `sections/google-map.liquid` |
| [Header](/en/sections/header) | Added page | `sections/header.liquid` |
| [Icon with text](/en/sections/icon-with-text) | Reference appended | `sections/icon-with-text.liquid` |
| [About us](/en/sections/main-page-about) | Added page | `sections/main-page-about.liquid` |
| [Contact us](/en/sections/main-page-contact) | Added page | `sections/main-page-contact.liquid` |
| [Mood finder](/en/sections/mood-finder) | Added page | `sections/mood-finder.liquid` |
| [Newsletter banner](/en/sections/newsletter-banner) | Reference appended | `sections/newsletter-banner.liquid` |
| [Newsletter overlay](/en/sections/newsletter-overlay) | Reference appended | `sections/newsletter-overlay.liquid` |
| [Page](/en/sections/page) | Reference appended | `sections/page.liquid` |
| [Password footer](/en/sections/password-footer) | Reference appended | `sections/password-footer.liquid` |
| [Password header](/en/sections/password-header) | Reference appended | `sections/password-header.liquid` |
| [Password](/en/sections/password) | Reference appended | `sections/password.liquid` |
| [Philosophy section](/en/sections/philosophy-section) | Reference appended | `sections/philosophy-section.liquid` |
| [Pickup availability](/en/sections/pickup-availability) | Reference appended | `sections/pickup-availability.liquid` |
| [Comparison table](/en/sections/product-comparison-table) | Reference appended | `sections/product-comparison-table.liquid` |
| [Product recommendations](/en/sections/product-recommendations) | Reference appended | `sections/product-recommendations.liquid` |
| [Product](/en/sections/product) | Added page | `sections/product.liquid` |
| [Promise section](/en/sections/promise-section) | Reference appended | `sections/promise-section.liquid` |
| [Promo banner](/en/sections/promo-bannder) | Reference appended | `sections/promo-bannder.liquid` |
| [Promotion countdown](/en/sections/promotion-countdown) | Reference appended | `sections/promotion-countdown.liquid` |
| [Ritual steps](/en/sections/ritual-steps) | Added page | `sections/ritual-steps.liquid` |
| [Routine showcase](/en/sections/routine-showcase) | Reference appended | `sections/routine-showcase.liquid` |
| [Scatter gallery](/en/sections/scatter-gallery) | Added page | `sections/scatter-gallery.liquid` |
| [Collection product list](/en/sections/scroll-categories) | Reference appended | `sections/scroll-categories.liquid` |
| [Scrolling icon with text](/en/sections/scrolling-icon-with-text) | Reference appended | `sections/scrolling-icon-with-text.liquid` |
| [Search overlay](/en/sections/search-overlay) | Reference appended | `sections/search-overlay.liquid` |
| [Search](/en/sections/search) | Added page | `sections/search.liquid` |
| [Slideshow](/en/sections/slides-show) | Reference appended | `sections/slides-show.liquid` |
| [Featured testimonial](/en/sections/testimonial-featured) | Reference appended | `sections/testimonial-featured.liquid` |
| [Video banner](/en/sections/video-banner) | Reference appended | `sections/video-banner.liquid` |

## Existing pages without a matching schema

All existing settings and section pages have matching definitions.

## Manual review

- Screenshots and legacy prose require Shopify verification; use the appended schemas as the field reference.
- Simple text, Product vendor and Existing snippet in Custom Liquid are examples, not missing controls.
- Audience and timing in Newsletter Overlay is an explanatory heading.
- Review the old contact-form, submission and image prose on the 404 page before manually removing it.
- Nested color fields and block settings are listed separately.
- Schema presence alone does not verify storefront behavior.

## Missing schema translations

These keys are missing from the English schema locale. Raw keys are preserved as evidence; missing translations do not imply missing controls.

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