# 配方与成分介绍（Formula details）

结合顶部介绍区域、配方属性和成分内容块，展示配方理念、产品属性及成分说明。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到支持该分区的模板，点击 **添加分区**，选择 **Formula details**。
3. 设置顶部区域的配色、Band heading、Band text 和 Band image。
4. 添加 Attribute 内容块填写属性名称与说明，添加 Ingredient 内容块填写成分图片、名称与说明。
5. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 可添加位置
安装包未允许在页眉、页脚或自定义弹层分组中添加此分区，请在页面内容区域配置。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/formula-details.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Formula details

可通过“添加分区”添加（声明了 presets）。

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

`max_blocks`: 8

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Ingredients color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Band color scheme<br>`band_color_scheme` | color_scheme：选择全局配色方案 | scheme-4 | — |

### Formula band

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Band heading<br>`band_heading` | text：输入文字 | A Closer Look at the Formula. | — |

### Heading

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select：从选项中选择 | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Band text<br>`band_text` | richtext：编辑格式化文字 | Lightweight, refreshing, and thoughtfully crafted. Every texture, ingredient and detail is designed to bring out your skin's natural glow. | — |
| Band image<br>`band_image` | image_picker：选择或上传图片 | 未声明 | — |

### Ingredients

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Ingredients heading<br>`ingredients_heading` | text：输入文字 | THE FORMULA | — |
| Ingredients subtitle<br>`ingredients_subtitle` | text：输入文字 | Powered by nature. Backed by science. | — |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

### 内容块：Attribute

`type`: `attribute`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Name<br>`name` | text：输入文字 | Attribute | — |
| Text<br>`text` | text：输入文字 | Describe how this formula feels or performs. | — |

### 内容块：Ingredient

`type`: `ingredient`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |
| Name<br>`name` | text：输入文字 | Ingredient | — |
| Text<br>`text` | text：输入文字 | Share a concise benefit this ingredient brings. | — |

<!-- latest-schema:end -->
