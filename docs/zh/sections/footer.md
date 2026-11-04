# 页脚（Footer）

在页脚组中展示品牌信息、说明文字、链接列和 Follow on Shop 入口。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 在页脚组中选择或添加 Footer，设置配色、背景图、品牌名称和介绍内容。
3. 添加 Link column 内容块，填写栏目标题并选择菜单；按需设置 Enable follow on Shop。
4. 完成后点击 **保存**，分别检查桌面端和移动端效果。

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/footer.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Footer

可通过“添加分区”添加（声明了 presets）。

`enabled_on`: &#123;"groups": ["footer"]&#125;

`limit`: 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-1 | — |
| Background image<br>`bg_image` | image_picker：选择或上传图片 | 未声明 | — |

### Brand

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Brand name<br>`brand_name` | inline_richtext：编辑行内格式化文字 | Your brand | — |
| Brush texture image<br>`brush_image` | image_picker：选择或上传图片 | 未声明 | — |
| Location text<br>`location` | inline_richtext：编辑行内格式化文字 | Your location | — |

### Right content

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading<br>`content_heading` | inline_richtext：编辑行内格式化文字 | Invite customers to explore | — |
| Description<br>`content_text` | richtext：编辑格式化文字 | &lt;p&gt;Share a short brand message or introduce a featured collection.&lt;/p&gt; | — |
| Link<br>`content_link` | url：选择或填写链接 | 未声明 | — |
| Link text<br>`content_link_text` | text：输入文字 | See Our New Product | — |

### Follow on Shop

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Enable Follow on Shop button<br>`enable_follow_on_shop` | checkbox：勾选开启，取消关闭 | true | — |

### 内容块：Link column

`type`: `link_column`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Column heading<br>`heading` | inline_richtext：编辑行内格式化文字 | Catalog | — |
| Menu<br>`menu` | link_list：选择菜单 | footer | — |

<!-- latest-schema:end -->
