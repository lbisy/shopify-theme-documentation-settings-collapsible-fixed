# Formula details

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/formula-details.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Formula details

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

`max_blocks`: 8

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Ingredients color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Band color scheme<br>`band_color_scheme` | color_scheme | scheme-4 | — |

### Formula band

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Band heading<br>`band_heading` | text | A Closer Look at the Formula. | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Band text<br>`band_text` | richtext | Lightweight, refreshing, and thoughtfully crafted. Every texture, ingredient and detail is designed to bring out your skin's natural glow. | — |
| Band image<br>`band_image` | image_picker | Not declared | — |

### Ingredients

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Ingredients heading<br>`ingredients_heading` | text | THE FORMULA | — |
| Ingredients subtitle<br>`ingredients_subtitle` | text | Powered by nature. Backed by science. | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Attribute

`type`: `attribute`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Name<br>`name` | text | Attribute | — |
| Text<br>`text` | text | Describe how this formula feels or performs. | — |

### Block: Ingredient

`type`: `ingredient`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Image<br>`image` | image_picker | Not declared | — |
| Name<br>`name` | text | Ingredient | — |
| Text<br>`text` | text | Share a concise benefit this ingredient brings. | — |

<!-- latest-schema:end -->
