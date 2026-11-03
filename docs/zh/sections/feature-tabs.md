# 图片热点与特色标签（Feature tabs）

通过主图、定位标记和对应的文字内容介绍商品特色，可为每个内容块关联商品。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到支持该分区的模板，点击 **添加分区**，选择 **Feature tabs**。
3. 选择 Feature image；需要装饰图时开启 Show decoration，并可替换 Decorative image。
4. 添加 Item 内容块，填写标签、标题和说明，选择关联商品，用 Marker horizontal position 与 Marker vertical position 调整标记位置。最多添加 6 个内容块。
5. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 可添加位置
安装包仅允许在首页、商品模板和普通页面模板中添加此分区。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/feature-tabs.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
[完整核对报告](/zh/version-audit)
:::

入口：主题编辑器 → 对应页面模板或分区组 → Feature tabs

可通过“添加分区”添加（声明了 presets）。

`enabled_on`: &#123;"templates": ["product", "index", "page"]&#125;

`max_blocks`: 6

### General

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Heading size<br>`heading_size` | select：从选项中选择 | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Feature image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |
| Show decoration<br>`show_decoration` | checkbox：勾选开启，取消关闭 | true | — |
| Decorative image<br>`decorative_image` | image_picker：选择或上传图片 | 未声明 | info: Replaces the default botanical illustration. Shown from tablet width up. |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

### 内容块：Item

`type`: `item`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Product link<br>`product` | product：选择商品 | 未声明 | — |
| Marker horizontal position<br>`marker_x` | range：拖动滑块调整数值 | 22 | 0–100 %; 步长 1 |
| Marker vertical position<br>`marker_y` | range：拖动滑块调整数值 | 28 | 0–100 %; 步长 1 |
| Label<br>`label` | text：输入文字 | Origin | — |
| Heading<br>`heading` | inline_richtext：编辑行内格式化文字 | From seed to serum. | — |
| Text<br>`text` | richtext：编辑格式化文字 | &lt;p&gt;Share a concise benefit, ingredient story, or ritual step that helps customers understand why this detail matters.&lt;/p&gt; | — |

<!-- latest-schema:end -->
