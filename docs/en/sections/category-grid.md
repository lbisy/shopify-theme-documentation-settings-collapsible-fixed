# Category Grid

The **Category grid** creates image-card entry points to collections or content pages. It supports a heading, description, View all link, responsive grid controls, and card image styling.

![Category Grid settings and storefront preview](/images/en/category-grid.png)

## Add the section

Open a template, click **Add section > Category grid**, then add one **Item** for each category. Configure each image, label, and link and drag blocks to reorder them.

## Heading

- **Heading** and **Heading size**
- **Subheading** and **Subheading size**
- **View all label** and **View all link**; complete both or leave both blank.
- **Text alignment**: Left, Center, or Right.
- **Color scheme**: background, text, links, arrows, and card elements.

Keep descriptions short, test long headings on mobile, and click the View all destination in preview.

## Grid

- **Desktop columns**: cards per row.
- **Desktop rows**: number of visible rows.
- **Mobile columns**: **1 column** for more room or **2 columns** for greater density.
- **Gap**: horizontal and vertical spacing in `px`.

Match the Item count to the intended rows and columns. More columns make cards narrower, so review long labels and detailed imagery.

## Card

- **Image shape**: for example, **Circle**. Keep important subjects centered with safe space around them.
- **Image frame style**: **Soft**, **Border**, or **None**.
- **Show arrow**: reinforces that a card is clickable.

Use consistent image ratios and visual styles. Check the frame boundary on combinations of light images and light backgrounds.

## Item blocks

Each Item needs an image, visible label, and destination that all describe the same category. Put the most important and frequently visited categories first. Do not reuse one label for different destinations.

## Example

| Setting | Example |
| --- | --- |
| Heading | `Shop by category` |
| Heading size | `2XL` |
| Subheading | `Explore collections curated for your routine.` |
| View all | `View all` → All collections |
| Alignment | `Left` |
| Desktop grid | `4 columns / 2 rows` |
| Mobile columns | `2 columns` |
| Gap | `40 px` |
| Shape / frame | `Circle` / `Soft` |
| Show arrow | On |
| Padding | `32 px / 32 px` |

## Before publishing

Verify heading and View all content, every Item image/name/destination, grid size and empty positions, both mobile column options, crops and wrapping, spacing and visual consistency, keyboard access with `Tab` and `Enter`, contrast and image boundaries, and all links on desktop and mobile after saving.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/category-grid.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → t:sections.category-grid.name

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.category-grid.settings.color_scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### t:sections.category-grid.content.heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.category-grid.settings.heading<br>`heading` | inline_richtext | t:sections.category-grid.defaults.heading | — |
| t:sections.category-grid.settings.heading_size<br>`heading_size` | select | heading-2xl | t:sections.slides-show.options.heading_4xl (`heading-4xl`); t:sections.slides-show.options.heading_3xl (`heading-3xl`); t:sections.slides-show.options.heading_2xl (`heading-2xl`); t:sections.slides-show.options.heading_xl (`heading-xl`); t:sections.slides-show.options.heading_h1 (`heading-h1`); t:sections.slides-show.options.heading_h2 (`heading-h2`); t:sections.slides-show.options.heading_h3 (`heading-h3`) |
| t:sections.category-grid.settings.subheading<br>`subheading` | richtext | t:sections.category-grid.defaults.subheading | — |
| t:sections.category-grid.settings.subheading_size<br>`subheading_size` | select | body-lg | XL (`body-xl`); Large (`body-lg`); Medium (`body-md`); Small (`body-sm`) |
| t:sections.category-grid.settings.view_all_label<br>`view_all_label` | text | t:sections.category-grid.defaults.view_all_label | — |
| t:sections.category-grid.settings.view_all_link<br>`view_all_link` | url | Not declared | — |
| t:sections.category-grid.settings.text_alignment<br>`text_alignment` | select | left | t:sections.category-grid.options.left (`left`); t:sections.category-grid.options.center (`center`); t:sections.category-grid.options.right (`right`) |

### t:sections.category-grid.content.layout

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.category-grid.settings.section_width<br>`section_width` | select | fixed | t:sections.category-grid.options.full_width (`full`); t:sections.category-grid.options.fixed_width (`fixed`) |

### t:sections.category-grid.content.grid

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.category-grid.settings.desktop_columns<br>`desktop_columns` | range | 4 | 2–6 ; step 1 |
| t:sections.category-grid.settings.desktop_rows<br>`desktop_rows` | range | 2 | 2–4 ; step 1 |
| t:sections.category-grid.settings.mobile_columns<br>`mobile_columns` | select | 2 | t:sections.category-grid.options.1_column (`1`); t:sections.category-grid.options.2_columns (`2`) |
| t:sections.category-grid.settings.gap<br>`gap` | range | 8 | 0–40 px; step 4<br>info: t:sections.category-grid.info.gap |
| t:sections.category-grid.settings.show_grid_borders<br>`show_grid_borders` | checkbox | true | — |

### t:sections.category-grid.content.card

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.category-grid.settings.image_shape<br>`image_shape` | select | circle | t:sections.category-grid.options.circle (`circle`); t:sections.category-grid.options.square (`square`); t:sections.category-grid.options.rounded (`rounded`); t:sections.category-grid.options.arch (`arch`) |
| t:sections.category-grid.settings.image_frame_style<br>`image_frame_style` | select | soft | t:sections.category-grid.options.soft (`soft`); t:sections.category-grid.options.border (`border`); t:sections.category-grid.options.none (`none`) |
| t:sections.category-grid.settings.show_arrow<br>`show_arrow` | checkbox | true | — |

### t:sections.category-grid.content.padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.category-grid.settings.padding_top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| t:sections.category-grid.settings.padding_bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: t:sections.category-grid.blocks.item

`type`: `item`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| t:sections.category-grid.block_settings.source_type<br>`source_type` | select | custom | t:sections.category-grid.options.custom (`custom`); t:sections.category-grid.options.collection (`collection`); t:sections.category-grid.options.product (`product`) |
| t:sections.category-grid.block_settings.collection<br>`collection` | collection | Not declared | — |
| t:sections.category-grid.block_settings.product<br>`product` | product | Not declared | — |
| t:sections.category-grid.block_settings.custom_image<br>`custom_image` | image_picker | Not declared | — |
| t:sections.category-grid.block_settings.custom_title<br>`custom_title` | text | t:sections.category-grid.blocks_defaults.title | — |
| t:sections.category-grid.block_settings.custom_link<br>`custom_link` | url | Not declared | — |

<!-- latest-schema:end -->
