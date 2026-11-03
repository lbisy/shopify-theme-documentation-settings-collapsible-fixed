# Article

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/article.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Article

No presets declared; do not assume this can be added freely through Add section.

`enabled_on`: &#123;"templates": ["article"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Header color scheme<br>`header_color_scheme` | color_scheme | scheme-2 | — |
| Content color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Image<br>`image` | image_picker | Not declared | — |
| Image alt text<br>`image_alt` | text | About Us | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading<br>`heading` | inline_richtext | Not declared | — |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Eyebrow text<br>`eyebrow` | inline_richtext | Categories | — |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Maximum items<br>`max_items` | range | 8 | 1–10 ; step 1 |
| Social icon<br>`show_social` | checkbox | false | info: Manage social accounts (`/editor?context=theme&amp;category=social%20icon`) |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
