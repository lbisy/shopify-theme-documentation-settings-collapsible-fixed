<!-- unlinked-document:start
文档显示状态：未在主页或目录中显示，且未被其他页面有效引用。
核对说明：已注释的目录入口和页面链接不计入有效引用；已排除构建的页面不作为引用来源。
保留正文供后续维护，此标记仅作为源码注释。
unlinked-document:end -->

# 公告栏（Announcement bar）

在页眉组内展示公告文字和链接，也可配置社交入口、国家及语言选择器。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 在页眉组中选择或添加 Announcement bar，设置配色、文字与链接。
3. 如需多条公告，添加 Announcement 内容块并填写各条文字；根据店铺需要设置社交、国家和语言选择器。
4. 完成后点击 **保存**，分别检查桌面端和移动端效果。

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/announcement-bar.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 对应页面模板或分区组 → Announcement bar

可通过“添加分区”添加（声明了 presets）。

`enabled_on`: &#123;"groups": ["header"]&#125;

`limit`: 1

`max_blocks`: 6

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-1 | — |
| Text<br>`text` | inline_richtext：编辑行内格式化文字 | See More | — |
| Link<br>`link` | url：选择或填写链接 | 未声明 | — |

### Public settings

Only displayed on large screens

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Social icon<br>`show_social` | checkbox：勾选开启，取消关闭 | false | info: Manage social accounts (`/editor?context=theme&amp;category=social%20icon`) |
| Country/region selector<br>`enable_country_selector` | checkbox：勾选开启，取消关闭 | false | info: Manage countries/regions (`/admin/settings/markets`) |
| Language selector<br>`enable_language_selector` | checkbox：勾选开启，取消关闭 | false | info: Manage languages (`/admin/settings/languages`) |

### 内容块：Announcement

`type`: `announcement`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Text<br>`announcement_text` | inline_richtext：编辑行内格式化文字 | Welcome to our store! | — |

<!-- latest-schema:end -->
