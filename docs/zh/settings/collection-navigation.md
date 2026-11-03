# Collection navigation

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `config/settings_schema.json` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
[完整核对报告](/zh/version-audit)
:::

入口：主题编辑器 → 主题设置 → Collection navigation

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Initially visible collections<br>`collection_navigation_batch_size` | range：拖动滑块调整数值 | 8 | 4–12 ; 步长 1<br>info: Controls how many collections appear in the quick navigation row and when the drawer first opens. |
| Collections per load<br>`collection_navigation_load_more_size` | range：拖动滑块调整数值 | 12 | 4–24 ; 步长 4<br>info: Controls how many additional collections the drawer loads each time. |

<!-- latest-schema:end -->
