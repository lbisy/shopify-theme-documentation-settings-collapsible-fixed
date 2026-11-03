# 页眉（Header）

配置全站 Logo 位置、导航菜单、超级菜单以及国家和语言选择器。

## 打开与配置

1. 进入 Shopify 后台的 **在线商店 → 主题 → 自定义**。
2. 在页眉组内选择 Header，设置 Logo position，并选择 Menu。Logo 图片在全局主题设置中配置。
3. 按需设置菜单类型、桌面端触发方式、超级菜单系列及桌面端、移动端配色。
4. 完成后点击 **保存**，分别检查桌面端和移动端效果。

## 设置项说明

以下按后台分组列出全部设置项。英文名称用于与主题编辑器对照；每项均列出操作方式、默认值及可选值。内容块拥有独立设置时，列在对应内容块标题下。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/header.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。本页根据安装包整理，尚未进行 Shopify 实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
[完整核对报告](/zh/version-audit)
:::

入口：主题编辑器 → 对应页面模板或分区组 → Header

未声明 presets；不要据此假定可在任意页面通过“添加分区”添加。

`enabled_on`: &#123;"groups": ["header"]&#125;

`limit`: 1

### Header

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Logo position<br>`logo_position` | select：从选项中选择 | left | Left (`left`); Middle (`middle`); Middle center (`middle-center`)<br>info: Edit your logo in theme settings (`/editor?context=theme&amp;category=logo`) |

### Color

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-1 | — |
| Menu color scheme<br>`menu_color_scheme` | color_scheme：选择全局配色方案 | scheme-1 | — |
| Mobile menu color scheme<br>`mobile_menu_color_scheme` | color_scheme：选择全局配色方案 | scheme-1 | — |
| Menu<br>`menu` | link_list：选择菜单 | main-menu | — |

### Menu type

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Menu type<br>`menu_type` | select：从选项中选择 | dropdown | Dropdown menu (`dropdown`); Super menu (`super`) |
| Desktop menu trigger<br>`desktop_menu_trigger` | select：从选项中选择 | hover | Hover (`hover`); Click (`click`) |
| Super menu watermark<br>`super_menu_watermark_text` | text：输入文字 | Your brand | visible_if: &#123;&#123; section.settings.menu_type == 'super' &#125;&#125; |
| Enable product series tabs<br>`enable_super_menu_series` | checkbox：勾选开启，取消关闭 | false | visible_if: &#123;&#123; section.settings.menu_type == 'super' &#125;&#125; |
| Product series layout<br>`super_menu_series_layout` | select：从选项中选择 | left-right | Left / Right (`left-right`); Top / Bottom (`top-bottom`)<br>visible_if: &#123;&#123; section.settings.menu_type == 'super' and section.settings.enable_super_menu_series &#125;&#125; |
| Super menu left column width<br>`super_menu_primary_width` | range：拖动滑块调整数值 | 42 | 30–70 %; 步长 1<br>visible_if: &#123;&#123; section.settings.menu_type == 'super' and section.settings.enable_super_menu_series &#125;&#125; |
| Series collection 1<br>`super_collection_1` | collection：选择商品系列 | 未声明 | — |
| Series collection 2<br>`super_collection_2` | collection：选择商品系列 | 未声明 | — |
| Series collection 3<br>`super_collection_3` | collection：选择商品系列 | 未声明 | — |
| Products per series<br>`super_series_products_limit` | range：拖动滑块调整数值 | 6 | 3–12 ; 步长 1<br>visible_if: &#123;&#123; section.settings.menu_type == 'super' and section.settings.enable_super_menu_series &#125;&#125; |

### Localization

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Country/region selector<br>`enable_country_selector` | checkbox：勾选开启，取消关闭 | true | info: Manage countries/regions (`/admin/settings/markets`) |
| Language selector<br>`enable_language_selector` | checkbox：勾选开启，取消关闭 | true | info: Manage languages (`/admin/settings/languages`) |

<!-- latest-schema:end -->
