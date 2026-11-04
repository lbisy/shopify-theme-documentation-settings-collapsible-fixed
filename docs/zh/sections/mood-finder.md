# 心情选品展示（Mood finder）

用不同心情或使用情境组织商品推荐，每个内容块可配置图片、推荐商品和介绍文字。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到支持该分区的模板，点击 **添加分区**，选择 **Mood finder**。
3. 填写分区引导文字、标题、补充说明和底部文字，按需设置装饰图。
4. 添加 Mood 内容块，选择图片与关联商品，填写短语、标签说明和描述。
5. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 可添加位置
安装包仅允许在首页、商品模板和普通页面模板中添加此分区。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/mood-finder.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Mood finder

可通过“添加分区”添加（声明了 presets）。

`enabled_on`: &#123;"templates": ["product", "index", "page"]&#125;

`max_blocks`: 4

### General

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Eyebrow<br>`eyebrow` | text：输入文字 | Skin mood finder | — |
| Heading<br>`heading` | inline_richtext：编辑行内格式化文字 | What are you in the mood for? | — |
| Heading size<br>`heading_size` | select：从选项中选择 | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Subtext<br>`subtext` | richtext：编辑格式化文字 | &lt;p&gt;Find your skin's moment.&lt;/p&gt;&lt;p&gt;Choose what you need today.&lt;/p&gt; | — |
| Caption<br>`caption` | text：输入文字 | Choose your mood. We'll do the rest. | — |
| Show decoration<br>`show_decoration` | checkbox：勾选开启，取消关闭 | true | — |
| Decoration image<br>`decoration_image` | image_picker：选择或上传图片 | 未声明 | info: Replaces the default botanical illustration. Shown from tablet width up. |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

### 内容块：Mood

`type`: `mood`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Texture image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |
| Eyebrow<br>`eyebrow` | text：输入文字 | Energized | — |
| Phrase<br>`phrase` | inline_richtext：编辑行内格式化文字 | Brighten the look | — |
| Product<br>`product` | product：选择商品 | 未声明 | — |
| Tag line<br>`tag_line` | text：输入文字 | 未声明 | — |
| Description<br>`description` | textarea：输入多行文字 | 未声明 | — |

<!-- latest-schema:end -->
