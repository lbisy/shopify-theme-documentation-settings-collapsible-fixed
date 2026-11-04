# 编辑式商品展示（Editorial Product Showcase）

按步骤介绍使用方法或搭配流程，可在每一步加入图片、商品和链接。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到支持该分区的模板，点击 **添加分区**，选择 **Ritual steps**。
3. 在 Layout 中选择 Sticky media 或 Scroll carousel，再设置标题与配色。
4. 添加 Step 内容块，填写步骤标签、标题和说明，选择步骤图片与商品，并配置需要展示的链接。
5. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 可添加位置
安装包未允许在页眉、页脚或自定义弹层分组中添加此分区，请在页面内容区域配置。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/ritual-steps.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Ritual steps

可通过“添加分区”添加（声明了 presets）。

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

`max_blocks`: 5

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Layout style<br>`layout` | select：从选项中选择 | sticky_media | Sticky media (style A) (`sticky_media`); Scroll carousel (style B) (`scroll_carousel`) |
| Heading<br>`heading` | inline_richtext：编辑行内格式化文字 | The Ceylune Ritual | — |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

### 内容块：Step

`type`: `step`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Step label<br>`label` | text：输入文字 | Cleanse | — |
| Step heading<br>`heading` | inline_richtext：编辑行内格式化文字 | Remove the unnecessary. | — |
| Step text<br>`text` | inline_richtext：编辑行内格式化文字 | Gentle cleansing for fresh, balanced skin. | — |
| Scene image (style A)<br>`image` | image_picker：选择或上传图片 | 未声明 | — |
| Product (style B)<br>`product` | product：选择商品 | 未声明 | — |
| Product image override<br>`product_image` | image_picker：选择或上传图片 | 未声明 | info: Shown at a fixed height. Best: a transparent PNG about 1:2.5, at least 640 × 1600 px, with the product filling it. Wider images look smaller. Defaults to the product featured image. |
| Link label<br>`link_label` | text：输入文字 | Discover the ritual | — |
| Link<br>`link` | url：选择或填写链接 | 未声明 | — |

<!-- latest-schema:end -->
