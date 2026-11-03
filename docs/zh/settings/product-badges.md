# Product badges

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `config/settings_schema.json` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
[完整核对报告](/zh/version-audit)
:::

入口：主题编辑器 → 主题设置 → Product badges

### Sale badge

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Background<br>`badge_sale_background` | color：选择颜色 | #d5ff83 | — |
| Text<br>`badge_sale_text` | color：选择颜色 | #263d29 | — |

### Sold out badge

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Background<br>`badge_sold_out_background` | color：选择颜色 | #677769 | — |
| Text<br>`badge_sold_out_text` | color：选择颜色 | #FFFFFF | — |

### Custom badge 1

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Product tag<br>`badge_custom_1_tag` | text：输入文字 | Best seller | info: Shown when a product tag exactly matches this value. The tag text is shown on the badge. |
| Background<br>`badge_custom_1_background` | color：选择颜色 | #263D29 | — |
| Text<br>`badge_custom_1_text` | color：选择颜色 | #FFFFFF | — |

### Custom badge 2

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Product tag<br>`badge_custom_2_tag` | text：输入文字 | New | info: Shown when a product tag exactly matches this value. The tag text is shown on the badge. |
| Background<br>`badge_custom_2_background` | color：选择颜色 | #e3e8da | — |
| Text<br>`badge_custom_2_text` | color：选择颜色 | #263d29 | — |

<!-- latest-schema:end -->
