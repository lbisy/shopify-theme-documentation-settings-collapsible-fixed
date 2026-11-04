# 博客列表主分区（Blog）

配置博客列表页的头部信息、装饰徽章、文章分页数量和阅读链接文字。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 切换到博客模板并选择 Blog，设置页头配色、标题、介绍文字与字号。
3. 配置 Articles per page、Link text 和装饰徽章内容，检查文章列表展示。
4. 完成后点击 **保存**，分别检查桌面端和移动端效果。

::: tip 页面主分区
此分区未声明 presets，不会作为普通的“添加分区”选项出现。请在已使用它的对应模板中编辑；下方列出了安装包声明的可用模板范围。
:::

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/blog.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Blog

未声明 presets；不要据此假定可在任意页面通过“添加分区”添加。

`enabled_on`: &#123;"templates": ["blog"]&#125;

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Header color scheme<br>`header_color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |

### Heading

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select：从选项中选择 | title-3xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Header<br>`header` | inline_richtext：编辑行内格式化文字 | Blog | — |
| Description<br>`description` | richtext：编辑格式化文字 | &lt;p&gt;Introduce your journal and the topics customers can explore.&lt;/p&gt; | — |

### Subtitle

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select：从选项中选择 | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Content color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |
| Rotating badge text<br>`rotate_badge_text` | text：输入文字 | STORIES • GUIDES • UPDATES • | — |
| Badge center text<br>`rotate_badge_percent` | text：输入文字 | READ | — |
| Articles per page<br>`articles_per_page` | range：拖动滑块调整数值 | 12 | 3–24 ; 步长 3 |
| Link text<br>`link_text` | text：输入文字 | Read more | — |

### Padding

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |
| Padding bottom<br>`padding_bottom` | range：拖动滑块调整数值 | 32 | 0–100 px; 步长 4 |

<!-- latest-schema:end -->
