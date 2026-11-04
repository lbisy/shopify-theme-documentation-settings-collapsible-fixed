# 商品系列主分区（Collection）

配置单个商品系列页面的头图、说明、商品网格、筛选、排序和分页数量。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到商品系列模板并选择 Collection，设置头部配色、标题、说明、备用图片及图片遮罩。
3. 设置 Products per page、桌面端与移动端列数，并按需开启筛选和排序。
4. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 页面主分区
此分区未声明 presets，不会作为普通的“添加分区”选项出现。请在已使用它的对应模板中编辑；下方列出了安装包声明的可用模板范围。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/collection.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Collection

未声明 presets；不要据此假定可在任意页面通过“添加分区”添加。

`enabled_on`: &#123;"templates": ["collection"]&#125;

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Header color scheme<br>`header_color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Content color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |

### Font

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select：从选项中选择 | title-4xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Header<br>`header` | inline_richtext：编辑行内格式化文字 | Products | — |
| Description<br>`description` | richtext：编辑格式化文字 | &lt;p&gt;Describe the products and purpose of this collection.&lt;/p&gt; | — |
| Fallback collection image<br>`fallback_image` | image_picker：选择或上传图片 | 未声明 | info: Used when the All collection or a collection has no image. |
| Image blur<br>`image_blur` | range：拖动滑块调整数值 | 10 | 0–20 px; 步长 1<br>info: Blurs the collection image or fallback image behind the title. Set to 0 to turn it off. |
| Image overlay opacity<br>`image_scrim_opacity` | range：拖动滑块调整数值 | 50 | 0–100 %; 步长 5<br>info: Darkens the image so the text stays readable. Low values can make text hard to read on bright images. |

### Subtitle

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select：从选项中选择 | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Rotating badge text<br>`rotate_badge_text` | text：输入文字 | FEATURED • COLLECTION • | — |
| Badge center text<br>`rotate_badge_percent` | text：输入文字 | SHOP | — |
| Products per page<br>`products_per_page` | range：拖动滑块调整数值 | 12 | 3–24 ; 步长 3 |
| Enable filtering<br>`enable_filtering` | checkbox：勾选开启，取消关闭 | true | info: Customize filters in the Search &amp; Discovery app. |
| Desktop filter layout<br>`filter_type` | select：从选项中选择 | horizontal | Horizontal (`horizontal`); Vertical (`vertical`); Drawer (`drawer`) |
| Visible filter values before show more<br>`filter_visible_values_limit` | range：拖动滑块调整数值 | 6 | 3–12 ; 步长 1 |
| Enable sorting<br>`enable_sorting` | checkbox：勾选开启，取消关闭 | true | — |
| Desktop product card columns<br>`desktop_card_columns` | select：从选项中选择 | 4 | 3 columns (`3`); 4 columns (`4`) |
| Mobile product card columns<br>`mobile_card_columns` | select：从选项中选择 | 2 | 1 column (`1`); 2 columns (`2`) |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

<!-- latest-schema:end -->
