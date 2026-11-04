# 博客故事（Blog Stories）

Blog Stories（博客故事）分区用于在普通页面或首页展示精选文章。分区可包含主标题、介绍文字和多张 Article 卡片，适合发布产品故事、使用指南、品牌动态或行业内容。

![Blog Stories 设置面板与前台效果](/images/zh/blog-stories.png)

## 使用前准备

1. 进入 **Shopify 后台 → 内容 → 博客文章**。
2. 创建或编辑文章，填写标题、正文和摘要。
3. 上传文章特色图片，并按需设置作者、标签和搜索引擎信息。
4. 将文章分配到正确的博客，并设置为可见。
5. 保存文章后，再进入主题编辑器配置 Blog Stories 分区。

建议同一组文章使用相同或接近的特色图片比例，并控制标题和摘要长度，以保持卡片排列整齐。

## 添加分区

1. 进入 **Shopify 后台 → 在线商店 → 主题**。
2. 在当前主题上点击 **自定义**。
3. 打开需要编辑的页面或模板。
4. 点击 **添加分区**，选择 **Blog Stories**。
5. 选择博客并填写分区标题与说明。
6. 点击 **添加 Article**，配置需要展示的文章卡片。
7. 点击右上角的 **保存**。

## Color Scheme

选择当前分区使用的全局配色方案，影响背景、标题、说明、文章信息和阅读链接等元素。

点击 **编辑方案** 可进入全局颜色设置。修改方案本身会同时影响其他使用该方案的分区，因此应检查正文、链接和交互状态与背景之间是否具有足够的对比度。

## Font

面板中的 **Font** 为字体相关设置区域。分区内文字会沿用主题的字体配置；如需调整全站字体，可前往 **主题设置 → Typography**。

## Heading

### Heading size

设置分区主标题的字号。较大的字号适合突出博客栏目定位，但长标题可能在移动端占据多行。

### Heading

设置分区主标题。该字段支持基础富文本格式、链接和动态来源。

建议使用一句简洁文案概括文章主题，例如“产品故事与使用指南”或“品牌最新动态”。不需要标题时可以留空，避免保留无实际含义的默认内容。

## Subtitle

### Subtitle size

设置分区介绍文字的字号。该文字通常与主标题并列或显示在其附近，应保持次于主标题的视觉层级。

### Description

设置栏目说明。该字段支持富文本格式、链接、项目符号和编号列表，并可连接动态来源。

建议用一至两句话说明文章覆盖的主题以及顾客能够获得的信息。内容过长会增加分区顶部高度，也可能挤压文章卡片的首屏空间。

## Blog

选择该分区关联的 Shopify 博客，也可以连接符合条件的动态来源。

若前台没有显示预期文章，请检查：

- 已选择正确的博客。
- 文章已分配到该博客。
- 文章状态为可见，且发布时间没有设在未来。
- Article 内容块已正确配置且没有被隐藏。

更换 Blog 后，应重新检查现有 Article 内容块是否仍与栏目主题一致。

## Article 内容块

点击 **添加 Article** 可以增加一张文章卡片。卡片通常包含特色图片、辅助信息、文章标题和阅读链接；实际显示内容取决于所选文章以及当前主题版本提供的内容块设置。

在左侧分区列表中可以拖动 Article 调整顺序，也可以单独隐藏、复制或删除。选择某个 Article 后，完成该内容块面板中的文章、图片、文字和链接配置。

配置 Article 时建议：

- 每个内容块使用不同文章，避免重复入口。
- 将最重要或最新的文章放在前面。
- 为每篇文章上传清晰且比例一致的特色图片。
- 文章标题应准确概括正文，不使用与内容无关的吸引点击文案。
- 阅读链接文字保持一致，例如统一使用“阅读全文”。
- 卡片中的分类、标签或辅助文案保持简短，避免与文章标题争夺视觉重点。

如果卡片仍显示占位图片或默认文字，应返回文章后台及对应 Article 内容块，补充实际图片、标题和链接后再发布。

## Padding

- **Padding Top**：设置分区顶部与上一个分区之间的留白，单位为 `px`。
- **Padding Bottom**：设置分区底部与下一个分区之间的留白，单位为 `px`。

可先让上下间距保持一致，再根据标题行数、Description 长度和文章卡片数量进行调整。移动端内容会纵向排列，应避免过大的留白使文章入口离开首屏。

## 文章卡片与内容建议

- 特色图片应采用统一比例，并将人物、产品或文字主体放在安全区域内。
- 不要把文章标题只写在图片里；应保留可被搜索引擎和辅助技术识别的文本标题。
- 摘要应说明文章价值，而不是完整重复正文开头。
- 同一行卡片的标题长度尽量接近，减少高度差异。
- 图片、标题和阅读链接都应进入同一篇文章，不能指向不同目标。
- 文章涉及产品功效、环保数据或客户案例时，应保证信息真实并符合销售地区要求。
- 为特色图片填写准确的替代文本，避免只写“博客图片”或文件名。

## 配置示例

| 设置项 | 示例值 |
| --- | --- |
| Color Scheme | 与页面背景有明显对比的方案 |
| Heading size | `2XL` |
| Heading | `产品故事与实用指南` |
| Subtitle size | `Large` |
| Description | `了解新品设计、使用技巧和品牌动态。` |
| Blog | 品牌故事 |
| Article 1 | 新品设计理念 |
| Article 2 | 日常使用指南 |
| Article 3 | 材料与工艺介绍 |
| Padding Top / Bottom | `32 px / 32 px` |

## 发布前检查

1. 确认所选 Blog 正确，所有目标文章均已发布并处于可见状态。
2. 检查 Heading 与 Description 没有无意义的默认内容，长文案在移动端换行自然。
3. 确认每个 Article 指向不同且正确的文章，没有重复或空白内容块。
4. 检查文章特色图片的清晰度、比例、裁切和替代文本。
5. 核对卡片标题、辅助信息和文章正文，确保信息相互一致。
6. 实际点击图片、标题和阅读链接，确认均进入对应文章。
7. 测试文章数量较少和较多时的布局，并检查桌面端每行卡片数量与移动端纵向排列。
8. 使用键盘 `Tab` 和 `Enter` 测试所有文章链接，确认焦点状态清晰可见。
9. 检查配色方案下的标题、说明、卡片文字和链接对比度。
10. 检查上下间距以及该分区与前后内容的衔接，点击 **保存** 后再从实际店面完成浏览测试。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/blog-stories.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Blog stories

可通过“添加分区”添加（声明了 presets）。

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |

### Font

### Heading

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select：从选项中选择 | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Heading<br>`heading` | inline_richtext：编辑行内格式化文字 | Product stories, updates, and useful insights. | — |

### Subtitle

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select：从选项中选择 | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Description<br>`description` | richtext：编辑格式化文字 | &lt;p&gt;Introduce the stories, guides, or updates featured in this section.&lt;/p&gt; | — |
| Blog<br>`blog` | blog：选择博客 | 未声明 | — |
| Articles to show<br>`articles_limit` | range：拖动滑块调整数值 | 3 | 1–12 ; 步长 1<br>visible_if: &#123;&#123; section.settings.blog &#125;&#125; |
| Link text<br>`link_text` | text：输入文字 | Read more | visible_if: &#123;&#123; section.settings.blog &#125;&#125; |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

### 内容块：Article

`type`: `article`

#### Font

#### Title

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`card_title_size` | select：从选项中选择 | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

#### Subtitle

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Subtitle size<br>`card_subtitle_size` | select：从选项中选择 | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |
| Subtitle<br>`subtitle` | inline_richtext：编辑行内格式化文字 | Article category | — |
| Title<br>`title` | inline_richtext：编辑行内格式化文字 | Article title | — |
| Link<br>`link` | url：选择或填写链接 | 未声明 | — |
| Link text<br>`article_link_text` | text：输入文字 | Read more | — |

<!-- latest-schema:end -->
