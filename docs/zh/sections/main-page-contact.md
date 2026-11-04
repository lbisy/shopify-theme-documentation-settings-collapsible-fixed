# 联系我们主分区（Contact us）

配置联系页面的介绍区域和表单外观，包括图片、标题、表单配色、提交按钮与成功提示。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 在使用该主分区的页面模板中选择 Contact us，分别设置页面配色和表单配色。
3. 选择图片、填写替代文字、标题和说明，设置 Button text、Success message 与 Watermark text。
4. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 页面主分区
此分区未声明 presets，不会作为普通的“添加分区”选项出现。请在已使用它的对应模板中编辑；下方列出了安装包声明的可用模板范围。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/main-page-contact.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Contact us

未声明 presets；不要据此假定可在任意页面通过“添加分区”添加。

`enabled_on`: &#123;"templates": ["page"]&#125;

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Form color scheme<br>`form_color_scheme` | color_scheme：选择全局配色方案 | scheme-5 | — |
| Image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |
| Image alt text<br>`image_alt` | text：输入文字 | Contact us | — |
| Heading<br>`heading` | inline_richtext：编辑行内格式化文字 | We're here to help | — |

### Heading

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select：从选项中选择 | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Description<br>`description` | richtext：编辑格式化文字 | &lt;p&gt;Tell customers how and when your team can help.&lt;/p&gt; | — |
| Button label<br>`button_text` | text：输入文字 | Send | — |
| Success message<br>`success_message` | textarea：输入多行文字 | Thank you for your message. We will get back to you soon. | — |
| Watermark text<br>`watermark_text` | text：输入文字 | Your brand | — |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

<!-- latest-schema:end -->
