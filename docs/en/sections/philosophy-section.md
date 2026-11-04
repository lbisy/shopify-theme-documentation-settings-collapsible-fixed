# Philosophy Section

The **Philosophy section** presents a brand principle or point of view through an introductory heading and a row of image-based philosophy cards. Use it to explain values such as craftsmanship, ingredient standards, responsible sourcing, design principles, or customer care.

![Philosophy Section settings and storefront preview](/images/en/philosophy-section.png)

## Add the section

1. Open **Shopify Admin → Online Store → Themes**.
2. Click **Customize** on the current theme.
3. Open the required page or template.
4. Click **Add section** and select **Philosophy section**.
5. Configure the introductory content, then click **Add Philosophy card** for each principle.
6. Drag the blocks in the left panel to arrange their display order.
7. Click **Save**.

## Section content

- **Color scheme**: controls the section background, headings, body copy, card text, and other theme-colored elements. Use **Edit scheme** to change the shared theme palette, and remember that editing a scheme can affect every section that uses it.
- **Subtitle**: a short eyebrow above the main heading, such as `Our Philosophy`.
- **Subtitle size**: controls the subtitle scale. The screenshot uses `XL`.
- **Heading**: the main statement for the section, such as `Created with Intention`.
- **Heading size**: controls the heading scale. The screenshot uses `2XL`.
- **Description**: rich text that supports the heading. Keep it concise so the cards remain the main focus.

Build a clear hierarchy: the Subtitle introduces the topic, the Heading states the central idea, and the Description adds one sentence of context. Check long headings on mobile because larger sizes wrap sooner.

## Philosophy card blocks

Click **Add Philosophy card** to add a value or principle. The example in the screenshot uses three cards. Open each block to replace its image, title, and supporting text; field names may appear as **Heading / Title** and **Description / Text**, depending on the theme version.

For each card:

- Use one clear image that directly supports the principle.
- Keep titles short and parallel, for example `Precision`, `Integrity`, and `Respect`.
- Limit the supporting text to one or two brief sentences.
- Use images with a consistent aspect ratio, composition, and visual style.
- Keep important subjects away from crop edges and verify the crop at mobile widths.

Blocks can be reordered from the left panel. Depending on the editor controls available in the current theme version, they can also be hidden, duplicated, or removed. Keep the card count focused; additional cards increase page length and may create an incomplete final row.

## Padding and Custom CSS

- **Padding top**: space above the section, in `px`.
- **Padding bottom**: space below the section, in `px`.

The screenshot uses `32 px` for both values. Start with equal spacing, then adjust according to the neighboring sections and the number of cards.

Use **Custom CSS** only for section-specific refinements that cannot be achieved with the provided settings. Keep selectors scoped to this section and retest desktop and mobile layouts after every change.

## Example configuration

| Setting | Example |
| --- | --- |
| Subtitle | `Our Philosophy` |
| Subtitle size | `XL` |
| Heading | `Created with Intention` |
| Heading size | `2XL` |
| Description | `Our skincare is crafted with precision, integrity, and respect for the skin.` |
| Card 1 | `Precision` with a craft or process image |
| Card 2 | `Integrity` with a materials or product image |
| Card 3 | `Respect` with a people, skin, or environment image |
| Padding top / bottom | `32 px / 32 px` |

## Resolve “missing translation” text

The screenshot shows unresolved preset strings such as `missing translation: "t:sections.philosophy-section.preset_blocks.card_1_title"`. Do not publish these placeholders.

First, open every **Philosophy card** block and replace the preset title and text with real content. If the message remains, or if the preset itself must be translated for multiple storefront languages, the theme locale files need matching keys for each card title and text, such as `sections.philosophy-section.preset_blocks.card_1_title` and `card_1_text`. Ask the theme developer to add or correct those locale entries.

## Before publishing

Verify the subtitle, heading, and description; replace all preset and missing-translation content; check every card image, title, and text; confirm image rights and meaningful alt text in the media library; review card order and incomplete rows; test image crops and heading wrapping on desktop and mobile; check color contrast and spacing; and confirm any Custom CSS is limited to this section before saving and reviewing the live storefront.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/philosophy-section.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Philosophy section

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Subtitle<br>`subtitle` | inline_richtext | Our Philosophy | — |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Heading<br>`heading` | inline_richtext | Created with Intention | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Description<br>`description` | richtext | &lt;p&gt;Our skincare is crafted with precision, integrity, and respect for the skin.&lt;/p&gt; | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Philosophy card

`type`: `card`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Image<br>`image` | image_picker | Not declared | — |

#### Title

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`title_size` | select | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Title<br>`title` | inline_richtext | Not declared | — |
| Description<br>`text` | richtext | &lt;p&gt;Card description&lt;/p&gt; | — |

#### Link

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Link<br>`link` | url | Not declared | — |
| Link label<br>`link_text` | text | Learn more | info: Shown under the description when a link is set. Leave blank to use the image link only. |

<!-- latest-schema:end -->
