# Footer

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/footer.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Footer

Has presets for the Add section picker.

`enabled_on`: &#123;"groups": ["footer"]&#125;

`limit`: 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-1 | — |
| Background image<br>`bg_image` | image_picker | Not declared | — |

### Brand

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Brand name<br>`brand_name` | inline_richtext | Your brand | — |
| Brush texture image<br>`brush_image` | image_picker | Not declared | — |
| Location text<br>`location` | inline_richtext | Your location | — |

### Right content

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading<br>`content_heading` | inline_richtext | Invite customers to explore | — |
| Description<br>`content_text` | richtext | &lt;p&gt;Share a short brand message or introduce a featured collection.&lt;/p&gt; | — |
| Link<br>`content_link` | url | Not declared | — |
| Link text<br>`content_link_text` | text | See Our New Product | — |

### Follow on Shop

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Enable Follow on Shop button<br>`enable_follow_on_shop` | checkbox | true | — |

### Block: Link column

`type`: `link_column`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Column heading<br>`heading` | inline_richtext | Catalog | — |
| Menu<br>`menu` | link_list | footer | — |

<!-- latest-schema:end -->
