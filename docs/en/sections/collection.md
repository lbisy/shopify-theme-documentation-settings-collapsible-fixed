# Collection

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/collection.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Collection

No presets declared; do not assume this can be added freely through Add section.

`enabled_on`: &#123;"templates": ["collection"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Header color scheme<br>`header_color_scheme` | color_scheme | scheme-2 | — |
| Content color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Font

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-4xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Header<br>`header` | inline_richtext | Products | — |
| Description<br>`description` | richtext | &lt;p&gt;Describe the products and purpose of this collection.&lt;/p&gt; | — |
| Fallback collection image<br>`fallback_image` | image_picker | Not declared | info: Used when the All collection or a collection has no image. |
| Image blur<br>`image_blur` | range | 10 | 0–20 px; step 1<br>info: Blurs the collection image or fallback image behind the title. Set to 0 to turn it off. |
| Image overlay opacity<br>`image_scrim_opacity` | range | 50 | 0–100 %; step 5<br>info: Darkens the image so the text stays readable. Low values can make text hard to read on bright images. |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Rotating badge text<br>`rotate_badge_text` | text | FEATURED • COLLECTION • | — |
| Badge center text<br>`rotate_badge_percent` | text | SHOP | — |
| Products per page<br>`products_per_page` | range | 12 | 3–24 ; step 3 |
| Enable filtering<br>`enable_filtering` | checkbox | true | info: Customize filters in the Search &amp; Discovery app. |
| Desktop filter layout<br>`filter_type` | select | horizontal | Horizontal (`horizontal`); Vertical (`vertical`); Drawer (`drawer`) |
| Visible filter values before show more<br>`filter_visible_values_limit` | range | 6 | 3–12 ; step 1 |
| Enable sorting<br>`enable_sorting` | checkbox | true | — |
| Desktop product card columns<br>`desktop_card_columns` | select | 4 | 3 columns (`3`); 4 columns (`4`) |
| Mobile product card columns<br>`mobile_card_columns` | select | 2 | 1 column (`1`); 2 columns (`2`) |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
