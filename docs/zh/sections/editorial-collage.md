# 编辑式图片拼贴（Editorial collage）

将标题、品牌说明与三张不同用途的图片组合展示，适合介绍品牌故事、商品质感和细节。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到支持该分区的模板，点击 **添加分区**，选择 **Editorial collage**。
3. 填写 Heading 和 Text，设置标题字号。
4. 分别选择 Texture image、Product image 和 Detail image，预览三张图片的裁切与搭配。
5. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 可添加位置
安装包未允许在页眉、页脚或自定义弹层分组中添加此分区，请在页面内容区域配置。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/editorial-collage.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
[完整核对报告](/zh/version-audit)
:::

入口：主题编辑器 → 对应页面模板或分区组 → Editorial collage

可通过“添加分区”添加（声明了 presets）。

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Heading<br>`heading` | text：输入文字 | An object of everyday care. | — |

### Heading

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select：从选项中选择 | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Text<br>`text` | richtext：编辑格式化文字 | More than just skincare, Ceylune is a daily ritual: a moment of calm, a return to yourself. Crafted with nature's finest, it brings balance to your skin and peace to your mind. | — |

### Images

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Texture image<br>`texture_image` | image_picker：选择或上传图片 | 未声明 | — |
| Product image<br>`product_image` | image_picker：选择或上传图片 | 未声明 | — |
| Detail image<br>`detail_image` | image_picker：选择或上传图片 | 未声明 | — |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

<!-- latest-schema:end -->
