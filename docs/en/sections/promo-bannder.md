<!-- 新版本删除部分：保留源文档，目录入口已注释；此页面已排除构建，不生成页面或站内搜索内容。 -->

# Promo Banner

The **Promo Banner** combines a hero image, campaign heading, destination link, circular badge, and optional Card blocks for seasonal promotions, launches, brand events, or service promises.

![Promo Banner settings and storefront preview](/images/en/promo-bannder.png)

## Add the section

Open a template, click **Add section > Promo Banner**, upload the hero image, add copy and a destination, optionally enable the badge and Card blocks, then click **Save**.

## Hero content

- **Color Scheme**
- **Heading size** and **Subtitle size**
- **Hero Image**
- **Subtitle**
- **Heading**
- **Link** and **Link Text**

Use a high-resolution, crop-safe image with room for the copy and badge. Keep the heading focused on one core message and place detailed terms on the destination page. Complete both link fields or leave both blank.

## Badge

- **Show Badge**
- **Badge Text** around the outer ring
- **Badge Value** in the center

Keep the ring text short and the value readable on mobile. A displayed percentage does not create a discount or change prices; configure the actual promotion in Shopify and keep all terms consistent.

## Card blocks

Cards add supporting benefits, categories, guarantees, or related links below the hero. Give each card one topic, use consistent image ratios and copy lengths, align links with the card message, and check mobile page length as blocks increase.

## Before publishing

Verify image rights, quality, crops, and alt text; heading hierarchy and contrast; link destination; badge layout and factual accuracy; Card order, media, copy, and links; keyboard focus; responsive spacing; and Custom CSS isolation. Save, then complete the full banner-to-destination journey.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/promo-bannder.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Promo banner

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

`max_blocks`: 5

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Font

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Card

`type`: `card`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Main image<br>`image` | image_picker | Not declared | — |
| Heading<br>`heading` | inline_richtext | Introduce a collection | — |
| Description<br>`description` | inline_richtext | Add a short description for this panel. | — |
| Small image<br>`image_small` | image_picker | Not declared | — |
| Link<br>`link` | url | Not declared | — |
| Link text<br>`link_text` | text | Explore | — |
| Panel color scheme<br>`color_scheme` | color_scheme | scheme-4 | — |

<!-- latest-schema:end -->
