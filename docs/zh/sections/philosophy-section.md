# 品牌理念（Philosophy Section）

Philosophy section（品牌理念）分区通过顶部介绍文字和一组图片卡片展示品牌的核心原则或观点，适合说明工艺标准、原料理念、责任采购、设计原则、可持续承诺或顾客服务理念。

![Philosophy section 设置面板与前台效果](/images/zh/philosophy-section.png)

## 添加分区

1. 进入 **Shopify 后台 → 在线商店 → 主题**。
2. 在当前主题上点击 **自定义**。
3. 打开需要编辑的页面或模板。
4. 点击 **添加分区**，选择 **Philosophy section**。
5. 配置分区顶部的介绍内容，再点击 **添加 Philosophy card** 增加理念卡片。
6. 在左侧面板拖动卡片内容块，调整前台显示顺序。
7. 点击右上角的 **保存**。

## 分区内容设置

- **Color scheme（配色方案）**：控制分区背景、标题、正文、卡片文字及其他跟随主题配色的元素。点击 **Edit scheme（编辑方案）** 可以修改全局方案；修改后也会影响其他使用同一方案的分区。
- **Subtitle（副标题）**：显示在主标题上方的简短引导文字，例如 `Our Philosophy`。
- **Subtitle size（副标题字号）**：设置副标题大小，截图中使用 `XL`。
- **Heading（标题）**：分区的核心主张，例如 `Created with Intention`。
- **Heading size（标题字号）**：设置主标题大小，截图中使用 `2XL`。
- **Description（说明）**：用于补充标题的富文本内容。建议保持简洁，让下方理念卡片继续承担主要信息。

建议建立清晰的信息层级：Subtitle 说明主题，Heading 表达核心观点，Description 用一句话补充背景。字号较大时应特别检查移动端换行，避免标题过长造成版面失衡。

## Philosophy card 内容块

点击 **添加 Philosophy card** 可以增加一项品牌原则。截图示例使用了三张卡片。打开每个内容块后，替换其图片、标题和说明文字；根据主题版本不同，字段名称可能显示为 **Heading / Title** 和 **Description / Text**。

配置每张卡片时建议：

- 使用一张与理念直接相关、主体清晰的图片。
- 标题保持简短且结构一致，例如“精准工艺”“诚信原则”“尊重肌肤”。
- 说明文字控制在一至两句，避免三张卡片长度差异过大。
- 所有卡片尽量使用一致的图片比例、构图方式和视觉风格。
- 重要主体不要贴近图片边缘，并检查移动端裁切效果。

可以在左侧面板拖动卡片调整顺序。根据当前主题版本提供的编辑器操作，也可以单独隐藏、复制或删除卡片。卡片数量不宜过多，否则会增加页面长度，并可能在最后一行出现不完整排列。

## Padding 与 Custom CSS

- **Padding top**：分区顶部留白，单位为 `px`。
- **Padding bottom**：分区底部留白，单位为 `px`。

截图中的上下间距均为 `32 px`。可以先保持相同数值，再根据前后分区的留白和卡片数量调整。

仅在内置设置无法实现需求时使用 **Custom CSS**。选择器应限制在当前分区范围内，并在每次修改后重新检查桌面端和移动端，避免影响主题中的其他模块。

## 配置示例

| 设置项 | 示例值 |
| --- | --- |
| Subtitle | `Our Philosophy` |
| Subtitle size | `XL` |
| Heading | `Created with Intention` |
| Heading size | `2XL` |
| Description | `我们的护肤产品以精准、诚信和尊重肌肤的原则精心打造。` |
| 卡片 1 | `精准工艺`，搭配工艺或制作过程图片 |
| 卡片 2 | `诚信原则`，搭配原料或产品图片 |
| 卡片 3 | `尊重肌肤`，搭配人物、肌肤或环境图片 |
| Padding top / bottom | `32 px / 32 px` |

## 处理 “missing translation” 提示

截图中的预设卡片出现了 `missing translation: "t:sections.philosophy-section.preset_blocks.card_1_title"` 等文字。这表示对应的主题翻译键没有被正确解析，不应将这些占位内容直接发布到店面。

首先逐个打开 **Philosophy card**，用真实的标题和说明替换预设内容。如果替换后仍然显示该提示，或者需要让新增预设适配多个店面语言，则需要在主题语言文件中补充每张卡片的标题和正文键，例如 `sections.philosophy-section.preset_blocks.card_1_title` 和 `card_1_text`。此类语言文件修改可交由主题开发人员完成。

## 发布前检查

1. 核对 Subtitle、Heading 和 Description，确保内容围绕同一个品牌理念。
2. 替换所有默认占位文字，并确认前台不再显示 `missing translation`。
3. 检查每张卡片的图片、标题、说明和排列顺序。
4. 确认图片清晰、拥有合法使用权，并在媒体库中配置有意义的替代文本。
5. 分别检查桌面端和移动端的图片裁切、标题换行以及最后一行卡片排列。
6. 检查文字与背景的对比度，以及分区和前后内容之间的间距。
7. 确认 Custom CSS 只影响当前分区，保存后再从实际店面完成最终浏览。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/philosophy-section.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Philosophy section

可通过“添加分区”添加（声明了 presets）。

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Subtitle<br>`subtitle` | inline_richtext：编辑行内格式化文字 | Our Philosophy | — |

### Subtitle

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select：从选项中选择 | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Heading<br>`heading` | inline_richtext：编辑行内格式化文字 | Created with Intention | — |

### Heading

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select：从选项中选择 | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Description<br>`description` | richtext：编辑格式化文字 | &lt;p&gt;Our skincare is crafted with precision, integrity, and respect for the skin.&lt;/p&gt; | — |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

### 内容块：Philosophy card

`type`: `card`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |

#### Title

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`title_size` | select：从选项中选择 | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Title<br>`title` | inline_richtext：编辑行内格式化文字 | 未声明 | — |
| Description<br>`text` | richtext：编辑格式化文字 | &lt;p&gt;Card description&lt;/p&gt; | — |

#### Link

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Link<br>`link` | url：选择或填写链接 | 未声明 | — |
| Link label<br>`link_text` | text：输入文字 | Learn more | info: Shown under the description when a link is set. Leave blank to use the image link only. |

<!-- latest-schema:end -->
