# 精选单品（Featured Product）

Featured Product（精选单品）分区用于在首页或其他页面直接展示一件指定商品。顾客无需先进入商品详情页，即可查看媒体、标题、价格和描述，选择变体与数量，并完成加购或快速结账。

![Featured Product 设置面板与前台效果](/images/zh/featured-product.png)

## 添加分区

1. 进入 **Shopify 后台 → 在线商店 → 主题**。
2. 在当前主题上点击 **自定义**。
3. 打开需要编辑的页面或模板。
4. 点击 **添加分区**，选择 **Featured Product**。
5. 在 **Select Product** 中选择需要展示的商品。
6. 添加、删除或排序商品信息区块。
7. 完成设置后，点击右上角的 **保存**。

## Color Scheme

选择当前分区使用的全局配色方案，影响背景、商品信息、媒体控件、变体选择器、数量控件和购买按钮等元素。

点击 **编辑方案** 可进入全局颜色设置。修改方案本身会同时影响其他使用该方案的分区，应检查标题、价格、边框、不可用状态和按钮与背景之间的对比度。

## Select Product

选择需要在该分区展示的 Shopify 商品。分区会读取所选商品的以下数据：

- 图片、视频、外部视频或 3D 模型等媒体。
- 商品标题和描述。
- 售价、原价和促销状态。
- 颜色、尺寸等变体选项。
- 库存与可售状态。

未选择商品时，主题编辑器可能显示占位内容。商品选择后仍未正常显示时，请确认商品处于启用状态、已发布到在线商店销售渠道，并具有完整的媒体和变体数据。

::: warning 商品可用性
如果默认变体缺货、不可购买或不适用于当前市场，购买按钮会显示不可用状态。测试时应切换所有变体，确认价格、媒体、库存提示和按钮状态能够同步变化。
:::

## Thumbnail position

设置商品缩略图相对于主媒体的位置：

- **Left**：缩略图纵向排列在主媒体左侧，适合媒体较多且桌面横向空间充足的布局。
- **Bottom**：缩略图横向排列在主媒体下方，为主媒体保留更完整的横向空间。

商品只有一项媒体时通常不需要缩略图导航。媒体较多时，应确认列表能够继续浏览，当前选中状态清晰，并且视频与 3D 模型具有容易识别的类型标记。

## Desktop media width

设置桌面端媒体区域在分区中占用的宽度比例，例如 `60%`。

增大数值会突出商品图片，同时压缩商品信息区域；减小数值则会为长标题、变体选择器和购买按钮留出更多空间。该设置主要影响桌面端，移动端会按照主题的响应式规则重新排列媒体与商品信息。

调整后应重点检查：

- 长商品标题是否出现过多换行。
- 商品描述是否形成过窄的文字列。
- 变体选项和购买按钮是否完整显示。
- 主媒体是否足够清晰且没有异常拉伸。

## Bottom visible thumbnails

设置主媒体底部一行直接显示的缩略图数量，可选择 `3`、`4`、`5` 或 `6`。该设置只在 **Thumbnail position** 选择 **Bottom** 时生效。

显示数量越多，单个缩略图越小；显示数量越少，缩略图更容易辨认，但顾客可能需要更多操作才能浏览全部媒体。可先使用 `4`，再根据商品媒体数量和页面宽度调整。

## Padding

- **Padding Top**：设置分区顶部留白，单位为 `px`，例如 `32 px`。
- **Padding Bottom**：设置分区底部留白，单位为 `px`，例如 `32 px`。

顶部间距影响分区与上一部分内容的衔接，底部间距影响它与后续分区的距离。调整时应同时检查桌面端和移动端。

## 商品信息区块

商品信息由左侧列表中的多个区块组成。可以拖动区块改变显示顺序，也可以通过 **添加区块** 增加主题支持的其他内容。

### Title

显示所选商品的标题。标题来自 Shopify 商品数据，应确保名称清晰、长度适中，并能与其他相似商品区分。

### Price

显示商品价格。商品促销时还可能同时显示原价、折后价或促销标记；切换变体后，价格应随所选变体更新。

如果商店启用了多市场或多货币，实际金额和货币格式会根据顾客所在市场及商店设置显示。

### Description

显示 Shopify 商品描述。精选单品通常位于首页等内容密集的页面，建议使用简洁描述突出核心特点，避免过长内容将购买按钮推到首屏之外。

### Variant picker

当商品具有颜色、尺寸或其他变体时，显示变体选择器。顾客切换选项后，媒体、价格、库存状态和购买按钮应同步更新。

应测试所有可用、缺货和不可用的组合，确保无效组合不能被错误加入购物车。

### Quantity selector

允许顾客设置购买数量。数量调整应遵守商品库存、购买上限和主题提供的数量规则。

测试时需要确认减少按钮不会让数量低于允许值，输入异常数量时能够得到清晰反馈。

### Buy buttons

显示加入购物车按钮，以及主题或商店配置允许的动态结账按钮。按钮状态取决于当前变体是否可售。

普通“加入购物车”通常会将商品加入购物车；动态结账按钮可能直接进入 Shopify 结账流程，不一定先打开购物车弹层。

### 应用区块

如果主题支持应用区块，可以通过 **添加区块** 插入已安装应用提供的内容，例如评分、订阅购买或个性化服务。应用区块的具体设置由对应应用决定。

## 区块顺序建议

推荐按照顾客决策顺序组织信息：

1. **Title**
2. **Price**
3. **Description**
4. **Variant picker**
5. **Quantity selector**
6. **Buy buttons**

可以根据商品类型调整顺序，但价格、变体和购买按钮应容易找到。删除区块只会移除当前分区中的显示内容，不会删除 Shopify 后台中的商品数据。

## 模板设置

展开 **模板设置** 可查看当前主题版本为 Featured Product 提供的附加配置。不同版本显示的选项可能不同；修改后应重新测试媒体、商品表单和移动端布局。

## 自定义 CSS

展开 **自定义 CSS** 可添加仅作用于当前分区的样式覆盖。建议优先使用媒体宽度、缩略图位置、区块排序和配色方案等现有设置。

添加 CSS 后，应检查不同商品标题长度、不同变体数量、促销价格、缺货状态以及桌面端和移动端布局。

## 删除分区

点击面板底部的 **删除分区** 会移除整个 Featured Product 及其商品信息区块，但不会删除 Shopify 后台中的商品。若只需隐藏某项信息，应移除对应区块。

## 参考配置

| 设置项 | 示例值 |
| --- | --- |
| Select Product | 目标商品 |
| Thumbnail position | `Left` |
| Desktop media width | `60%` |
| Bottom visible thumbnails | `4` |
| Padding Top / Bottom | `32 px / 32 px` |
| 商品信息区块 | Title、Price、Description、Variant picker、Quantity selector、Buy buttons |

## 发布前检查

1. 确认分区读取了正确商品的标题、描述、价格和媒体。
2. 逐一切换图片、视频和 3D 模型，检查加载、播放及选中状态。
3. 分别测试缩略图位于左侧和底部时的排列与浏览操作。
4. 切换所有变体，确认媒体、价格、库存和按钮状态同步更新。
5. 测试数量增加、减少、手动输入以及库存边界。
6. 测试加入购物车和动态结账按钮，并确认商品与数量正确。
7. 检查长标题、长描述、促销价格、缺货商品和不可用变体的排版。
8. 在桌面端检查媒体宽度，在移动端检查媒体顺序、按钮宽度和触控区域。
9. 使用键盘 `Tab`、方向键和 `Enter` 测试媒体、变体、数量及购买控件。
10. 点击 **保存**，并在实际店面完成一次从选择变体到加购或结账的完整流程。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/featured-product.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Featured product

可通过“添加分区”添加（声明了 presets）。

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Select product<br>`product` | product：选择商品 | 未声明 | — |
| Gallery layout<br>`gallery_layout` | select：从选项中选择 | thumbnails | Thumbnails (`thumbnails`); Carousel (`carousel`)<br>info: Carousel shows a full-height image with pagination dots. Thumbnails keeps the existing thumbnail gallery. |
| Thumbnail position<br>`thumb_position` | select：从选项中选择 | left | Left (`left`); Bottom (`bottom`) |
| Desktop media width<br>`desktop_media_width` | range：拖动滑块调整数值 | 60 | 40–60 %; 步长 1 |
| Media aspect ratio<br>`media_aspect_ratio` | select：从选项中选择 | adapt | Adapt to image (`adapt`); Portrait (3:4) (`portrait_3_4`); Square (1:1) (`square_1_1`) |
| Desktop media height<br>`desktop_media_height` | select：从选项中选择 | balanced | Original (`original`); Compact (`compact`); Balanced (`balanced`); Full screen (`full_screen`) |
| Thumbnail size<br>`thumbnail_size` | select：从选项中选择 | standard | Compact (`compact`); Standard (`standard`); Large (`large`)<br>info: Controls thumbnail size for both left and bottom positions. |

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
| Heading size<br>`heading_size` | select：从选项中选择 | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

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

此处未声明本地设置（应用或主题区块需查看其自身定义）。

### 内容块：Variant picker

`type`: `variant_picker`; `limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Style<br>`picker_type` | select：从选项中选择 | button | Dropdown (`dropdown`); Pills (`button`) |
| Swatch shape<br>`swatch_shape` | select：从选项中选择 | circle | Circle (`circle`); Square (`square`); None (`none`) |

### 内容块：Quantity selector

`type`: `quantity_selector`; `limit`: 1

此处未声明本地设置（应用或主题区块需查看其自身定义）。

### 内容块：Buy buttons

`type`: `buy_buttons`; `limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Show dynamic checkout buttons<br>`show_dynamic_checkout` | checkbox：勾选开启，取消关闭 | true | info: Using the payment methods available on your store, customers see their preferred option, like PayPal or Apple Pay. |

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

### 内容块：Custom liquid

`type`: `custom_liquid`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Custom liquid<br>`custom_liquid` | liquid：编辑 Liquid 内容 | 未声明 | — |

<!-- latest-schema:end -->
