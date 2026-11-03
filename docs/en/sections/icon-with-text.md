# Icon with Text

The **Icon with text** section presents multiple icons and short messages for materials, charity support, returns, delivery, or payment reassurance. It supports a carousel, responsive columns, horizontal or vertical arrangement, and separate desktop and mobile icon sizes.

![Icon with Text settings and storefront preview](/images/en/icon-with-text.png)

## Add the section

Open a template, click **Add section > Icon with text**, then add one **Item** per message. Select its icon, enter concise copy, reorder blocks, and click **Save**.

## Carousel and layout

**Enable carousel** lets customers browse Items beyond the visible area. Leave it off when all messages fit comfortably in the grid.

- **Desktop columns**
- **Mobile columns**: **1** gives more room; **2** reduces section height.
- **Item gap** in `px`

More columns provide less text width. Test every carousel item, the final position, long copy, and mobile two-column spacing.

## Icon and text

- **Direction**: **Vertical** places the icon above text; **Horizontal** places them side by side.
- **Icon size**: desktop size in `px`.
- **Icon size mobile**
- **Icon and text gap**

Use a consistent icon family and visual weight. Oversized icons compete with copy; tiny icons become difficult to recognize. Recheck alignment and gap whenever direction changes.

## Item blocks

Each Item should pair one intuitive icon with one short statement. Reorder, hide, duplicate, or remove blocks in the left panel. Keep copy lengths similar and do not mix heavy filled icons with fine line icons. Policy claims must match actual store terms, and essential information cannot rely on the icon alone.

## Example

| Setting | Example |
| --- | --- |
| Carousel | Off |
| Desktop / mobile columns | `3` / `1` |
| Item gap | `32 px` |
| Direction | `Vertical` |
| Desktop / mobile icon | `56 px` / `48 px` |
| Icon-text gap | `16 px` |
| Padding | `32 px / 32 px` |

## Before publishing

Confirm every icon matches its text and no block is empty or duplicated; prioritize the most decision-relevant messages; test responsive columns, icon sizes, wrapping, both directions, gaps, carousel reachability and controls, color contrast, and adjacent spacing. Save and check the actual storefront on desktop and mobile.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/icon-with-text.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Icon with text

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Carousel

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Enable carousel<br>`enable_carousel` | checkbox | false | — |

### Layout

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Desktop columns<br>`desktop_columns` | select | 3 | 2 columns (`2`); 3 columns (`3`); 4 columns (`4`) |
| Mobile columns<br>`mobile_columns` | select | 1 | 1 column (`1`); 2 columns (`2`) |
| Item gap<br>`item_gap` | range | 32 | 8–80 px; step 4 |

### Icon and text

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Direction<br>`direction` | select | vertical | Vertical (`vertical`); Horizontal (`horizontal`) |
| Icon size<br>`icon_size` | range | 56 | 20–96 px; step 2 |
| Icon size mobile<br>`icon_size_mobile` | range | 48 | 20–96 px; step 2 |
| Icon and text gap<br>`icon_text_gap` | range | 16 | 4–48 px; step 2 |
| Alignment<br>`alignment` | select | center | Left (`left`); Center (`center`) |

### Bottom wave

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Show bottom wave<br>`show_wave` | checkbox | false | — |
| Wave color scheme<br>`wave_color_scheme` | color_scheme | scheme-2 | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Item

`type`: `item`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Title<br>`title` | inline_richtext | Heading | — |
| Description<br>`text` | inline_richtext | Not declared | — |
| Icon<br>`icon` | select | icon-content-check | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Shield check (`icon-content-shield-check`); Check (`icon-content-check`); Heart (`icon-content-heart`); Hand heart (`icon-content-hand-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`) |
| Image icon<br>`image_icon` | image_picker | Not declared | — |
| Link<br>`link` | url | Not declared | — |

<!-- latest-schema:end -->
