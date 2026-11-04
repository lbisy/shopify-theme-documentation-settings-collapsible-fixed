---
search: false
---

<!-- unlinked-document:start
文档显示状态：未在主页或目录中显示，且未被其他页面有效引用。
核对说明：已注释的目录入口和页面链接不计入有效引用；已排除构建的页面不作为引用来源。
保留正文供后续维护，此标记仅作为源码注释。
unlinked-document:end -->

<!-- 新版本删除部分：保留文档内容，目录及引用入口已注释，并从本地搜索中隐藏。 -->

# About Stats

The **About Stats** section combines brand images, a year or short label, descriptive copy, a link, and key statistics. Use it for brand history, manufacturing standards, service results, sustainability commitments, or company scale.

![About Stats settings and storefront preview](/images/en/about-stats.png)

## Add the section

Open a template, click **Add section > About Stats**, add the images, description, and link, then add one **Stat** block for each metric and click **Save**.

## Main settings

- **Color scheme**: background, description, links, and statistics. Check large values and regular text for contrast.
- **Subtitle size** under Title: the larger introductory text size.
- **Heading size** under Subtitle: the secondary text size. Judge the actual hierarchy in preview rather than relying only on field names.
- **Image**: primary brand, product, team, craft, or store image.
- **Secondary Image**: an optional complementary viewpoint or detail.
- **Year Text**: a founding year, anniversary, or short phase label. It does not update automatically.
- **Description**: rich text for the brand introduction or central proposition.
- **Link** and **Link Text**: the destination and visible call to action. Complete both or leave both blank.

Use clear, high-resolution images with important subjects away from crop edges. Keep the two images visually related but not redundant. If only one image is needed, leave the secondary field empty and verify the layout remains balanced.

## Stat blocks

Each **Stat** pairs a short label with an emphasized value, such as `Regions served / 12` or `Recyclable packaging / 90%`. Reorder, hide, duplicate, or remove blocks in the left panel.

- Explain what is measured in the label.
- Use consistent formats and include required units.
- Use readable abbreviations for long values.
- Publish only current, verifiable data.
- Limit the number of metrics so mobile cards have enough room.

## Padding and content guidance

Use **Padding Top / Bottom** in `px`, starting with equal values and adjusting for image height, copy length, and metric count.

Keep Year Text, Description, and statistics focused on one brand theme. Let Description explain the value, Stats provide evidence, and the Link lead to more detail. Add accurate alt text to meaningful images. Environmental, quality, sales, and user-count claims must be supportable and comply with local advertising rules.

## Example

| Setting | Example |
| --- | --- |
| Subtitle / Heading size | `3XL` / `2XL` |
| Year Text | `Founded in 2018` |
| Description | `From material selection to packaging, we continuously improve every stage.` |
| Link Text | `Read our brand story` |
| Stat 1 | `Partner workshops / 12` |
| Stat 2 | `Recyclable packaging / 90%` |
| Stat 3 | `Regions served / 8` |
| Padding | `32 px / 32 px` |

## Before publishing

Verify image rights, quality, and responsive crops; review the year and rich-text formatting; test the link; validate every label, value, unit, and methodology; test small and large block counts on mobile; check contrast and keyboard focus; and review spacing before saving and testing on the storefront.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/about-stats.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → t:sections.about-stats.name

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.about-stats.settings.color_scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Font

### t:sections.about-stats.content.stat_title

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`stat_title_size` | select | body-3xl | t:sections.scroll-categories.options.body_3xl (`body-3xl`); t:sections.scroll-categories.options.body_2xl (`body-2xl`); XL (`body-xl`); Large (`body-lg`); Medium (`body-md`); Small (`body-sm`) |

### t:sections.about-stats.content.stat_subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`stat_subtitle_size` | select | heading-2xl | t:sections.slides-show.options.heading_4xl (`heading-4xl`); t:sections.slides-show.options.heading_3xl (`heading-3xl`); t:sections.slides-show.options.heading_2xl (`heading-2xl`); t:sections.slides-show.options.heading_xl (`heading-xl`); t:sections.slides-show.options.heading_h1 (`heading-h1`); t:sections.slides-show.options.heading_h2 (`heading-h2`); t:sections.slides-show.options.heading_h3 (`heading-h3`); t:sections.slides-show.options.heading_h4 (`heading-h4`); t:sections.slides-show.options.heading_h5 (`heading-h5`); t:sections.slides-show.options.heading_h6 (`heading-h6`) |
| t:sections.about-stats.settings.image<br>`image` | image_picker | Not declared | — |
| t:sections.about-stats.settings.secondary_image<br>`image_secondary` | image_picker | Not declared | — |
| t:sections.about-stats.settings.year_text<br>`year` | text | 2026© | — |
| t:sections.about-stats.settings.description<br>`description` | richtext | t:sections.about-stats.defaults.description_html | — |
| t:sections.about-stats.settings.link<br>`link` | url | Not declared | — |
| t:sections.about-stats.settings.link_text<br>`link_text` | text | t:sections.about-stats.defaults.link_text | — |

### t:sections.about-stats.content.padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.about-stats.settings.padding_top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| t:sections.about-stats.settings.padding_bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: t:sections.about-stats.blocks.stat

`type`: `stat`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.about-stats.block_settings.label<br>`label` | inline_richtext | t:sections.about-stats.defaults.block_label | — |
| t:sections.about-stats.block_settings.value<br>`value` | inline_richtext | t:sections.about-stats.defaults.block_value | — |

<!-- latest-schema:end -->
