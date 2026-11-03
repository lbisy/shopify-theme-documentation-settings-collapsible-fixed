# Featured Product

The **Featured Product** section displays one product on a homepage or other page. Customers can view media, title, price, and description, select variants and quantity, and add to cart or use accelerated checkout without first visiting the product page.

![Featured Product settings and storefront preview](/images/en/featured-product.png)

## Add the section

Open a template, click **Add section > Featured Product**, choose **Select Product**, arrange the product-information blocks, and click **Save**.

## Product and appearance

**Color Scheme** affects media controls, product information, variants, quantity, and purchase buttons. Check unavailable states and contrast.

**Select Product** reads the product's media, title, description, pricing, variants, inventory, and availability. If content remains empty, confirm that the product is active, published to Online Store, and has complete media and variant data.

::: warning Product availability
If the default variant is sold out, unavailable, or excluded from the current market, purchase controls become unavailable. Test every variant and verify synchronized media, price, stock, and buttons.
:::

## Media

- **Thumbnail position**: **Left** for a vertical list or **Bottom** for a horizontal row.
- **Desktop media width**: larger values emphasize media and reduce information width.
- **Bottom visible thumbnails**: `3`, `4`, `5`, or `6`, used only with Bottom position.

Check long titles, narrow descriptions, complete controls, selection state, scrollable thumbnail lists, and clear video/3D type indicators. Mobile rearranges content responsively.

## Product information blocks

- **Title**
- **Price**, including compare-at and sale states.
- **Description**
- **Variant picker**
- **Quantity selector**
- **Buy buttons**
- App blocks supplied by installed apps.

A practical order is Title → Price → Description → Variant picker → Quantity selector → Buy buttons. Keep price, options, and purchase actions easy to find. Removing a block affects only this section, not the product data.

Variant selection must update media, price, inventory, and availability. Quantity must respect inventory and purchase limits. Regular Add to cart uses the cart flow, while dynamic checkout can go directly to Shopify checkout.

## Padding, additional settings, and CSS

Use **Padding Top / Bottom** in `px`. Review any version-specific **Template settings** after theme updates. Prefer built-in media, block, and color controls before applying section-scoped **Custom CSS**.

## Before publishing

Verify the selected product and every media item; test both thumbnail positions; switch all variants and unavailable combinations; change and manually enter quantities at boundaries; test Add to cart and dynamic checkout; review long copy, sale prices, sold-out states, media width, mobile order, buttons, touch targets, and keyboard controls; then complete one real variant-to-cart-or-checkout flow after saving.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/featured-product.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Featured product

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Select product<br>`product` | product | Not declared | — |
| Gallery layout<br>`gallery_layout` | select | thumbnails | Thumbnails (`thumbnails`); Carousel (`carousel`)<br>info: Carousel shows a full-height image with pagination dots. Thumbnails keeps the existing thumbnail gallery. |
| Thumbnail position<br>`thumb_position` | select | left | Left (`left`); Bottom (`bottom`) |
| Desktop media width<br>`desktop_media_width` | range | 60 | 40–60 %; step 1 |
| Media aspect ratio<br>`media_aspect_ratio` | select | adapt | Adapt to image (`adapt`); Portrait (3:4) (`portrait_3_4`); Square (1:1) (`square_1_1`) |
| Desktop media height<br>`desktop_media_height` | select | balanced | Original (`original`); Compact (`compact`); Balanced (`balanced`); Full screen (`full_screen`) |
| Thumbnail size<br>`thumbnail_size` | select | standard | Compact (`compact`); Standard (`standard`); Large (`large`)<br>info: Controls thumbnail size for both left and bottom positions. |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: @app

`type`: `@app`

No local settings declared here; app/theme blocks define their own controls.

### Block: Title

`type`: `title`; `limit`: 1

#### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

### Block: Vendor

`type`: `vendor`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

### Block: Price

`type`: `price`; `limit`: 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Show product rating<br>`show_rating` | checkbox | true | — |

### Block: Description

`type`: `description`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

### Block: Variant picker

`type`: `variant_picker`; `limit`: 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Style<br>`picker_type` | select | button | Dropdown (`dropdown`); Pills (`button`) |
| Swatch shape<br>`swatch_shape` | select | circle | Circle (`circle`); Square (`square`); None (`none`) |

### Block: Quantity selector

`type`: `quantity_selector`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

### Block: Buy buttons

`type`: `buy_buttons`; `limit`: 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Show dynamic checkout buttons<br>`show_dynamic_checkout` | checkbox | true | info: Using the payment methods available on your store, customers see their preferred option, like PayPal or Apple Pay. |

### Block: Icon with text

`type`: `icon_with_text_group`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Position (desktop)<br>`icon_with_text_position_desktop` | select | form | Form column (`form`); Gallery column (`gallery`) |
| Direction<br>`direction` | select | vertical | Vertical (`vertical`); Horizontal (`horizontal`) |
| Icon and text gap<br>`icon_text_gap` | range | 8 | 4–32 px; step 2 |

#### Item 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Title<br>`item_1_title` | inline_richtext | Product details | — |
| Text<br>`item_1_text` | inline_richtext | Not declared | — |
| Icon<br>`item_1_icon` | select | icon-content-package | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`); Recycle (`icon-content-recycle`); Flask (`icon-content-flask`) |
| Link<br>`item_1_link` | url | Not declared | — |

#### Item 2

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Title<br>`item_2_title` | inline_richtext | Care instructions | — |
| Text<br>`item_2_text` | inline_richtext | Not declared | — |
| Icon<br>`item_2_icon` | select | icon-content-leaf | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`); Recycle (`icon-content-recycle`); Flask (`icon-content-flask`) |
| Link<br>`item_2_link` | url | Not declared | — |

#### Item 3

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Title<br>`item_3_title` | inline_richtext | Shipping information | — |
| Text<br>`item_3_text` | inline_richtext | Not declared | — |
| Icon<br>`item_3_icon` | select | icon-content-truck | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`); Recycle (`icon-content-recycle`); Flask (`icon-content-flask`) |
| Link<br>`item_3_link` | url | Not declared | — |

### Block: Custom liquid

`type`: `custom_liquid`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Custom liquid<br>`custom_liquid` | liquid | Not declared | — |

<!-- latest-schema:end -->
