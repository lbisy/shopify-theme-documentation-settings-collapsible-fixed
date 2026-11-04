# Feature tabs

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/feature-tabs.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Feature tabs

Has presets for the Add section picker.

`enabled_on`: &#123;"templates": ["product", "index", "page"]&#125;

`max_blocks`: 6

### General

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Heading size<br>`heading_size` | select | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Feature image<br>`image` | image_picker | Not declared | — |
| Show decoration<br>`show_decoration` | checkbox | true | — |
| Decorative image<br>`decorative_image` | image_picker | Not declared | info: Replaces the default botanical illustration. Shown from tablet width up. |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Item

`type`: `item`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Product link<br>`product` | product | Not declared | — |
| Marker horizontal position<br>`marker_x` | range | 22 | 0–100 %; step 1 |
| Marker vertical position<br>`marker_y` | range | 28 | 0–100 %; step 1 |
| Label<br>`label` | text | Origin | — |
| Heading<br>`heading` | inline_richtext | From seed to serum. | — |
| Text<br>`text` | richtext | &lt;p&gt;Share a concise benefit, ingredient story, or ritual step that helps customers understand why this detail matters.&lt;/p&gt; | — |

<!-- latest-schema:end -->
