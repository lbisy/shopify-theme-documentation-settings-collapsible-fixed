# Brand Statement

The **Brand Statement** section uses large text to emphasize a philosophy, value proposition, or core promise. An optional brushstroke image can add visual focus between sections on a homepage or brand story.

![Brand Statement settings and storefront preview](/images/en/brand-statement.png)

## Add the section

Open a template, click **Add section > Brand Statement**, enter the statement, optionally add a brushstroke decoration, set size, colors, and spacing, then click **Save**. No content blocks are required.

## Main settings

- **Color scheme**: section background, statement text, and decoration.
- **Statement text**: rich text, links, lists, and dynamic sources.
- **Heading size**: overall statement size.
- **Brushstroke decoration image**: optional transparent PNG or WebP.
- **Padding Top / Bottom**: vertical spacing in `px`.
- **Custom CSS**: small section-scoped adjustments such as text width or decoration position.

Focus the statement on one clear idea in one to three concise sentences: why the brand exists, what it values, and what it delivers. Emphasize only key words, link only to directly relevant supporting pages, and use lists only when the content genuinely needs them.

Large type increases section height and can produce awkward isolated words or punctuation. Check every language separately because English and Chinese have very different line lengths.

The decoration must never cover text or contain essential terms, prices, or claims. Compress it, verify visibility on light and dark schemes, and check mobile scaling and cropping. Leave it blank when it adds no value.

## Copy guidance

Use customer-friendly, specific language instead of jargon or unverifiable superlatives. Ensure the statement matches actual products, service, and brand-story content. Environmental, performance, quality, or market-leading claims require evidence and must comply with local advertising rules. Do not communicate essential information only through color or decoration.

## Example

| Setting | Example |
| --- | --- |
| Statement text | `We use transparent sourcing and durable design to create products made for long-term use.` |
| Heading size | `2XL` |
| Decoration | Transparent brand brushstroke |
| Padding | `32 px / 32 px` |

## Before publishing

Replace defaults; proofread grammar, punctuation, and claims; review wrapping, alignment, and height on desktop and mobile; check bold, italic, and link contrast; test links with mouse and keyboard; ensure the image does not obscure content; check file size and spacing; verify Custom CSS isolation; then save and test the storefront.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/brand-statement.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Brand statement

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Statement text<br>`statement` | richtext | &lt;p&gt;Share a concise statement that expresses your brand's point of view.&lt;/p&gt; | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Brushstroke decoration image<br>`brushstroke_image` | image_picker | Not declared | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
