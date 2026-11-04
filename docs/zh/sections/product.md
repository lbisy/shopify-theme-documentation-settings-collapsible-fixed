# 商品详情主分区（Product）

配置商品详情页的媒体展示与商品信息区，通过内容块组织标题、价格、规格、库存提示和购买操作。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到商品模板并选择 Product，设置图库布局、缩略图位置、媒体宽度和比例等选项。
3. 按需配置 Title、Price、Variant picker、Quantity selector、Buy buttons 等内容块，再添加折叠内容、分享或支付图标等辅助信息。
4. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 页面主分区
此分区未声明 presets，不会作为普通的“添加分区”选项出现。请在已使用它的对应模板中编辑；下方列出了安装包声明的可用模板范围。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/product.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Product

未声明 presets；不要据此假定可在任意页面通过“添加分区”添加。

`enabled_on`: &#123;"templates": ["product"]&#125;

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Image layout<br>`gallery_layout` | select：从选项中选择 | thumbnails | Thumbnails (`thumbnails`); Carousel (`carousel`); Stacked (`stacked`); Grid (`grid`) |
| Thumbnail position<br>`thumbnail_position` | select：从选项中选择 | left | Left (`left`); Bottom (`bottom`)<br>info: Applies when Image layout is set to Thumbnails. |
| Desktop media width<br>`desktop_media_width` | range：拖动滑块调整数值 | 60 | 40–60 %; 步长 1 |
| Media aspect ratio<br>`media_aspect_ratio` | select：从选项中选择 | adapt | Adapt to image (`adapt`); Portrait (3:4) (`portrait_3_4`); Square (1:1) (`square_1_1`) |
| Desktop media height<br>`desktop_media_height` | select：从选项中选择 | balanced | Original (`original`); Compact (`compact`); Balanced (`balanced`); Full screen (`full_screen`)<br>info: Controls the maximum desktop gallery height. Original follows the media width and image ratio. |
| Thumbnail size<br>`thumbnail_size` | select：从选项中选择 | standard | Compact (`compact`); Standard (`standard`); Large (`large`)<br>info: Controls thumbnail size for both positions when Image layout is set to Thumbnails. |
| Magnifier preview size<br>`magnifier_preview_size` | range：拖动滑块调整数值 | 360 | 240–520 px; 步长 20 |
| Zoom overlay opacity<br>`zoom_overlay_opacity` | range：拖动滑块调整数值 | 90 | 0–100 %; 步长 5 |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

### 内容块：@app

`type`: `@app`

此处未声明本地设置（应用或主题区块需查看其自身定义）。

### 内容块：Title

`type`: `title`; `limit`: 1

#### Heading

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select：从选项中选择 | title-l | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

### 内容块：Vendor

`type`: `vendor`; `limit`: 1

此处未声明本地设置（应用或主题区块需查看其自身定义）。

### 内容块：Price

`type`: `price`; `limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Show product rating<br>`show_rating` | checkbox：勾选开启，取消关闭 | true | — |

### 内容块：Description

`type`: `description`; `limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Position (desktop)<br>`position_desktop` | select：从选项中选择 | form | Form column (`form`); Gallery column (`gallery`) |

### 内容块：Variant picker

`type`: `variant_picker`; `limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Style<br>`picker_type` | select：从选项中选择 | button | Dropdown (`dropdown`); Pills (`button`) |
| Swatch shape<br>`swatch_shape` | select：从选项中选择 | circle | Circle (`circle`); Square (`square`); None (`none`) |

### 内容块：Quantity selector

`type`: `quantity_selector`; `limit`: 1

此处未声明本地设置（应用或主题区块需查看其自身定义）。

### 内容块：Inventory notice

`type`: `inventory_notice`; `limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Low stock threshold<br>`low_stock_threshold` | range：拖动滑块调整数值 | 5 | 1–50 ; 步长 1<br>info: The low stock notice displays if your inventory is equal to or lower than this number. |
| Alignment<br>`alignment` | select：从选项中选择 | left | Left (`left`); Center (`center`); Right (`right`) |
| Display stock number<br>`show_stock_number` | checkbox：勾选开启，取消关闭 | true | — |

### 内容块：Buy buttons

`type`: `buy_buttons`; `limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Show dynamic checkout buttons<br>`show_dynamic_checkout` | checkbox：勾选开启，取消关闭 | true | info: Using the payment methods available on your store, customers see their preferred option, like PayPal or Apple Pay. |

### 内容块：Custom liquid

`type`: `custom_liquid`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Custom liquid<br>`custom_liquid` | liquid：编辑 Liquid 内容 | 未声明 | — |

### 内容块：Collapsible tab

`type`: `collapsible_tab`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Position (desktop)<br>`collapsible_tab_position_desktop` | select：从选项中选择 | form | Form column (`form`); Gallery column (`gallery`) |
| Open tab by default<br>`open_by_default` | checkbox：勾选开启，取消关闭 | false | — |
| Heading<br>`collapsible_tab_heading` | inline_richtext：编辑行内格式化文字 | Collapsible tab | — |
| Icon<br>`collapsible_tab_icon` | select：从选项中选择 | icon-content-check | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`) |
| Size<br>`collapsible_tab_size` | select：从选项中选择 | md | Small (`sm`); Medium (`md`); Large (`lg`); XL (`xl`) |
| Text<br>`collapsible_tab_text` | richtext：编辑格式化文字 | &lt;p&gt;Share information about your product, shipping, returns, or materials.&lt;/p&gt; | — |
| Image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |
| Image width<br>`image_width` | range：拖动滑块调整数值 | 1000 | 100–1000 px; 步长 20 |
| Alignment<br>`collapsible_tab_alignment` | select：从选项中选择 | left | Left (`left`); Center (`center`); Right (`right`) |
| Link<br>`link` | url：选择或填写链接 | 未声明 | — |
| Dynamic content<br>`dynamic_content` | page：选择页面 | 未声明 | info: Optional. Use a store page's body as this tab's text (for example Shipping or Returns). That page content replaces the Text field above. Icon, image, alignment, and link still apply. |
| Use page title for tab heading<br>`use_page_title` | checkbox：勾选开启，取消关闭 | false | info: Only works when a page is selected in Dynamic content. Replaces the Heading field with that page's title. |

### 内容块：Share

`type`: `share`; `limit`: 1

#### Share channels

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Share on Facebook<br>`show_share_facebook` | checkbox：勾选开启，取消关闭 | true | — |
| Share on X<br>`show_share_x` | checkbox：勾选开启，取消关闭 | true | — |
| Share on Pinterest<br>`show_share_pinterest` | checkbox：勾选开启，取消关闭 | true | — |
| Share on Tumblr<br>`show_share_tumblr` | checkbox：勾选开启，取消关闭 | true | — |
| Position (desktop)<br>`share_position_desktop` | select：从选项中选择 | form | Form column (`form`); Gallery column (`gallery`) |
| Alignment<br>`share_alignment` | select：从选项中选择 | center | Left (`left`); Center (`center`); Right (`right`) |

### 内容块：Callout

`type`: `callout`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Position (desktop)<br>`callout_position_desktop` | select：从选项中选择 | form | Form column (`form`); Gallery column (`gallery`) |
| Icon<br>`callout_icon` | select：从选项中选择 | icon-content-check | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`) |
| Icon size<br>`callout_icon_size` | range：拖动滑块调整数值 | 24 | 12–48 px; 步长 1 |
| Heading<br>`callout_heading` | text：输入文字 | 未声明 | — |
| Bold<br>`bold` | checkbox：勾选开启，取消关闭 | false | — |
| Text<br>`callout_text` | richtext：编辑格式化文字 | &lt;p&gt;Share a concise product benefit, care note, or delivery detail.&lt;/p&gt; | — |
| Show border<br>`show_border` | checkbox：勾选开启，取消关闭 | false | — |

### 内容块：Icon with text

`type`: `icon_with_text_group`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Position (desktop)<br>`icon_with_text_position_desktop` | select：从选项中选择 | form | Form column (`form`); Gallery column (`gallery`) |
| Direction<br>`direction` | select：从选项中选择 | vertical | Vertical (`vertical`); Horizontal (`horizontal`) |
| Icon and text gap<br>`icon_text_gap` | range：拖动滑块调整数值 | 8 | 4–32 px; 步长 2 |

#### Item 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Title<br>`item_1_title` | inline_richtext：编辑行内格式化文字 | Product details | — |
| Text<br>`item_1_text` | inline_richtext：编辑行内格式化文字 | 未声明 | — |
| Icon<br>`item_1_icon` | select：从选项中选择 | icon-content-package | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`); Recycle (`icon-content-recycle`); Flask (`icon-content-flask`) |
| Link<br>`item_1_link` | url：选择或填写链接 | 未声明 | — |

#### Item 2

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Title<br>`item_2_title` | inline_richtext：编辑行内格式化文字 | Care instructions | — |
| Text<br>`item_2_text` | inline_richtext：编辑行内格式化文字 | 未声明 | — |
| Icon<br>`item_2_icon` | select：从选项中选择 | icon-content-leaf | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`); Recycle (`icon-content-recycle`); Flask (`icon-content-flask`) |
| Link<br>`item_2_link` | url：选择或填写链接 | 未声明 | — |

#### Item 3

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Title<br>`item_3_title` | inline_richtext：编辑行内格式化文字 | Shipping information | — |
| Text<br>`item_3_text` | inline_richtext：编辑行内格式化文字 | 未声明 | — |
| Icon<br>`item_3_icon` | select：从选项中选择 | icon-content-truck | None (`none`); Package (`icon-content-package`); Truck (`icon-content-truck`); Airplane (`icon-content-airplane`); Gift (`icon-content-gift`); Tag (`icon-content-tag`); Currency (`icon-content-currency-circle-dollar`); Phone (`icon-content-phone`); Chat (`icon-content-chat`); Calendar (`icon-content-calendar-blank`); Clock (`icon-content-clock`); Globe (`icon-content-globe`); Location (`icon-content-map-pin`); Check (`icon-content-check`); Heart (`icon-content-heart`); Leaf (`icon-content-leaf`); Acorn (`icon-content-acorn`); Lightning (`icon-content-lightning`); Water off (`icon-content-drop-slash`); Smiley (`icon-content-smiley`); Stool (`icon-content-stool`); Recycle (`icon-content-recycle`); Flask (`icon-content-flask`) |
| Link<br>`item_3_link` | url：选择或填写链接 | 未声明 | — |

### 内容块：Payment icons

`type`: `payment_icons`; `limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading<br>`heading` | text：输入文字 | Secure online shopping | — |

### 内容块：Spacer

`type`: `spacer`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Position (desktop)<br>`spacer_position_desktop` | select：从选项中选择 | form | Form column (`form`); Gallery column (`gallery`) |
| Top spacing<br>`top_spacing` | select：从选项中选择 | small | None (`none`); Small (`small`); Medium (`medium`); Large (`large`) |
| Bottom spacing<br>`bottom_spacing` | select：从选项中选择 | small | None (`none`); Small (`small`); Medium (`medium`); Large (`large`) |
| Show dividing line<br>`show_dividing_line` | checkbox：勾选开启，取消关闭 | false | — |

<!-- latest-schema:end -->
