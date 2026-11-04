<!-- unlinked-document:start
文档显示状态：未在主页或目录中显示，且未被其他页面有效引用。
核对说明：已注释的目录入口和页面链接不计入有效引用；已排除构建的页面不作为引用来源。
保留正文供后续维护，此标记仅作为源码注释。
unlinked-document:end -->

# Product

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/product.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Product

No presets declared; do not assume this can be added freely through Add section.

`enabled_on`: &#123;"templates": ["product"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Image layout<br>`gallery_layout` | select | thumbnails | Thumbnails (`thumbnails`); Carousel (`carousel`); Stacked (`stacked`); Grid (`grid`) |
| Thumbnail position<br>`thumbnail_position` | select | left | Left (`left`); Bottom (`bottom`)<br>info: Applies when Image layout is set to Thumbnails. |
| Desktop media width<br>`desktop_media_width` | range | 60 | 40–60 %; step 1 |
| Media aspect ratio<br>`media_aspect_ratio` | select | adapt | Adapt to image (`adapt`); Portrait (3:4) (`portrait_3_4`); Square (1:1) (`square_1_1`) |
| Desktop media height<br>`desktop_media_height` | select | balanced | Original (`original`); Compact (`compact`); Balanced (`balanced`); Full screen (`full_screen`)<br>info: Controls the maximum desktop gallery height. Original follows the media width and image ratio. |
| Thumbnail size<br>`thumbnail_size` | select | standard | Compact (`compact`); Standard (`standard`); Large (`large`)<br>info: Controls thumbnail size for both positions when Image layout is set to Thumbnails. |
| Magnifier preview size<br>`magnifier_preview_size` | range | 360 | 240–520 px; step 20 |
| Zoom overlay opacity<br>`zoom_overlay_opacity` | range | 90 | 0–100 %; step 5 |

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
| Heading size<br>`heading_size` | select | title-l | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

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

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Position (desktop)<br>`position_desktop` | select | form | Form column (`form`); Gallery column (`gallery`) |

### Block: Variant picker

`type`: `variant_picker`; `limit`: 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Style<br>`picker_type` | select | button | Dropdown (`dropdown`); Pills (`button`) |
| Swatch shape<br>`swatch_shape` | select | circle | Circle (`circle`); Square (`square`); None (`none`) |

### Block: Quantity selector

`type`: `quantity_selector`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

### Block: Inventory notice

`type`: `inventory_notice`; `limit`: 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Low stock threshold<br>`low_stock_threshold` | range | 5 | 1–50 ; step 1<br>info: The low stock notice displays if your inventory is equal to or lower than this number. |
| Alignment<br>`alignment` | select | left | Left (`left`); Center (`center`); Right (`right`) |
| Display stock number<br>`show_stock_number` | checkbox | true | — |

### Block: Buy buttons

`type`: `buy_buttons`; `limit`: 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Show dynamic checkout buttons<br>`show_dynamic_checkout` | checkbox | true | info: Using the payment methods available on your store, customers see their preferred option, like PayPal or Apple Pay. |

### Block: Custom liquid

`type`: `custom_liquid`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Custom liquid<br>`custom_liquid` | liquid | Not declared | — |

### Block: Collapsible tab

`type`: `collapsible_tab`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Position (desktop)<br>`collapsible_tab_position_desktop` | select | form | Form column (`form`); Gallery column (`gallery`) |
| Open tab by default<br>`open_by_default` | checkbox | false | — |
| Heading<br>`collapsible_tab_heading` | inline_richtext | Collapsible tab | — |
| Icon<br>`collapsible_tab_icon` | select | icon-content-check | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`) |
| Size<br>`collapsible_tab_size` | select | md | Small (`sm`); Medium (`md`); Large (`lg`); XL (`xl`) |
| Text<br>`collapsible_tab_text` | richtext | &lt;p&gt;Share information about your product, shipping, returns, or materials.&lt;/p&gt; | — |
| Image<br>`image` | image_picker | Not declared | — |
| Image width<br>`image_width` | range | 1000 | 100–1000 px; step 20 |
| Alignment<br>`collapsible_tab_alignment` | select | left | Left (`left`); Center (`center`); Right (`right`) |
| Link<br>`link` | url | Not declared | — |
| Dynamic content<br>`dynamic_content` | page | Not declared | info: Optional. Use a store page's body as this tab's text (for example Shipping or Returns). That page content replaces the Text field above. Icon, image, alignment, and link still apply. |
| Use page title for tab heading<br>`use_page_title` | checkbox | false | info: Only works when a page is selected in Dynamic content. Replaces the Heading field with that page's title. |

### Block: Share

`type`: `share`; `limit`: 1

#### Share channels

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Share on Facebook<br>`show_share_facebook` | checkbox | true | — |
| Share on X<br>`show_share_x` | checkbox | true | — |
| Share on Pinterest<br>`show_share_pinterest` | checkbox | true | — |
| Share on Tumblr<br>`show_share_tumblr` | checkbox | true | — |
| Position (desktop)<br>`share_position_desktop` | select | form | Form column (`form`); Gallery column (`gallery`) |
| Alignment<br>`share_alignment` | select | center | Left (`left`); Center (`center`); Right (`right`) |

### Block: Callout

`type`: `callout`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Position (desktop)<br>`callout_position_desktop` | select | form | Form column (`form`); Gallery column (`gallery`) |
| Icon<br>`callout_icon` | select | icon-content-check | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`) |
| Icon size<br>`callout_icon_size` | range | 24 | 12–48 px; step 1 |
| Heading<br>`callout_heading` | text | Not declared | — |
| Bold<br>`bold` | checkbox | false | — |
| Text<br>`callout_text` | richtext | &lt;p&gt;Share a concise product benefit, care note, or delivery detail.&lt;/p&gt; | — |
| Show border<br>`show_border` | checkbox | false | — |

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

### Block: Payment icons

`type`: `payment_icons`; `limit`: 1

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading<br>`heading` | text | Secure online shopping | — |

### Block: Spacer

`type`: `spacer`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Position (desktop)<br>`spacer_position_desktop` | select | form | Form column (`form`); Gallery column (`gallery`) |
| Top spacing<br>`top_spacing` | select | small | None (`none`); Small (`small`); Medium (`medium`); Large (`large`) |
| Bottom spacing<br>`bottom_spacing` | select | small | None (`none`); Small (`small`); Medium (`medium`); Large (`large`) |
| Show dividing line<br>`show_dividing_line` | checkbox | false | — |

<!-- latest-schema:end -->
