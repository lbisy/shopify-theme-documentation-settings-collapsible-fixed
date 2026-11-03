# Mood finder

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/mood-finder.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Mood finder

Has presets for the Add section picker.

`enabled_on`: &#123;"templates": ["product", "index", "page"]&#125;

`max_blocks`: 4

### General

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Eyebrow<br>`eyebrow` | text | Skin mood finder | — |
| Heading<br>`heading` | inline_richtext | What are you in the mood for? | — |
| Heading size<br>`heading_size` | select | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Subtext<br>`subtext` | richtext | &lt;p&gt;Find your skin's moment.&lt;/p&gt;&lt;p&gt;Choose what you need today.&lt;/p&gt; | — |
| Caption<br>`caption` | text | Choose your mood. We'll do the rest. | — |
| Show decoration<br>`show_decoration` | checkbox | true | — |
| Decoration image<br>`decoration_image` | image_picker | Not declared | info: Replaces the default botanical illustration. Shown from tablet width up. |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Mood

`type`: `mood`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Texture image<br>`image` | image_picker | Not declared | — |
| Eyebrow<br>`eyebrow` | text | Energized | — |
| Phrase<br>`phrase` | inline_richtext | Brighten the look | — |
| Product<br>`product` | product | Not declared | — |
| Tag line<br>`tag_line` | text | Not declared | — |
| Description<br>`description` | textarea | Not declared | — |

<!-- latest-schema:end -->
