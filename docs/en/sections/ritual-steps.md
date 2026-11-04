# Ritual steps

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/ritual-steps.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Ritual steps

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

`max_blocks`: 5

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Layout style<br>`layout` | select | sticky_media | Sticky media (style A) (`sticky_media`); Scroll carousel (style B) (`scroll_carousel`) |
| Heading<br>`heading` | inline_richtext | The Ceylune Ritual | — |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Step

`type`: `step`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Step label<br>`label` | text | Cleanse | — |
| Step heading<br>`heading` | inline_richtext | Remove the unnecessary. | — |
| Step text<br>`text` | inline_richtext | Gentle cleansing for fresh, balanced skin. | — |
| Scene image (style A)<br>`image` | image_picker | Not declared | — |
| Product (style B)<br>`product` | product | Not declared | — |
| Product image override<br>`product_image` | image_picker | Not declared | info: Shown at a fixed height. Best: a transparent PNG about 1:2.5, at least 640 × 1600 px, with the product filling it. Wider images look smaller. Defaults to the product featured image. |
| Link label<br>`link_label` | text | Discover the ritual | — |
| Link<br>`link` | url | Not declared | — |

<!-- latest-schema:end -->
