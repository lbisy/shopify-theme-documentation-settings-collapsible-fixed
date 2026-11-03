# 错落图片画廊（Scatter gallery）

通过多张图片组成错落的视觉展示，适合营造品牌氛围或呈现场景照片。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到支持该分区的模板，点击 **添加分区**，选择 **Scatter gallery**。
3. 填写分区标题，分别设置桌面端和移动端标题字号，按需选择装饰图。
4. 添加 Image 内容块并逐一选择图片，通过内容块顺序组织图片。
5. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 可添加位置
安装包未允许在页眉、页脚或自定义弹层分组中添加此分区，请在页面内容区域配置。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/scatter-gallery.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
[完整核对报告](/zh/version-audit)
:::

入口：主题编辑器 → 对应页面模板或分区组 → Scatter gallery

可通过“添加分区”添加（声明了 presets）。

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

### General

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |

### Heading

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Statement<br>`heading` | text：输入文字 | Ceylune brings together innovation, transparency, and quality to redefine the skincare shopping experience. | — |
| Heading size<br>`heading_size` | select：从选项中选择 | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Mobile heading size<br>`heading_size_mobile` | select：从选项中选择 | title-xs | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

### Decoration

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Brush stroke image<br>`decoration_image` | image_picker：选择或上传图片 | 未声明 | — |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

### 内容块：Image

`type`: `image`; `limit`: 8

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |

<!-- latest-schema:end -->
