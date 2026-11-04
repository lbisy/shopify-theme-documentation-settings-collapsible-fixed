# 轻提示（Toast）

Toast 是用于显示成功、警告、错误或信息反馈的临时状态消息。**Toast** 设置用于控制提示框的形状、位置、停留时间、编辑器预览和阴影。

## 打开 Toast 设置

1. 在 Shopify 后台进入**在线商店 > 主题**。
2. 找到需要编辑的主题，点击**自定义**。
3. 打开**主题设置 > Toast**。

![Toast 设置与店铺预览](/images/zh/settings/toast.png)

上图使用 `8 px` 圆角，显示在页面顶部中央，`3 s` 后自动关闭，并添加了略微向下偏移的柔和阴影。

## 显示与停留时间

这些设置控制 Toast 的形状、位置、停留时间和主题编辑器预览。

| 设置项 | 图中数值 | 作用 |
| --- | ---: | --- |
| **Toast radius** | `8 px` | 控制提示框圆角大小。较小的数值更利落，较大的数值更柔和、圆润。 |
| **Position** | **Top center** | 将 Toast 放在视口顶部中央。 |
| **Auto-dismiss (seconds)** | `3 s` | 控制前台 Toast 自动关闭前的显示时间。 |
| **Preview** | **Off** | 选择在主题编辑器中显示的 Toast 类型。选择 **Off** 时隐藏预览。 |
| **Keep preview visible until dismissed** | **开启** | 让编辑器预览一直显示，直到手动关闭，便于检查外观。 |

**Preview** 和 **Keep preview visible until dismissed** 只影响主题编辑器。前台实际停留时间由 **Auto-dismiss (seconds)** 控制。`3 s` 适合简短消息；内容较长或需要用户做出判断时，应适当延长时间。

使用 **Top center** 时，请确认 Toast 不会遮挡公告栏、导航、搜索、购物车控件或移动设备的安全区域。

## 阴影（Shadow）

阴影可以让 Toast 在不断变化的页面背景上保持清晰可见。

| 设置项 | 图中数值 | 作用 |
| --- | ---: | --- |
| **Toast shadow opacity** | `10%` | 控制阴影可见度。设置为 `0%` 时关闭阴影。 |
| **Toast shadow horizontal offset** | `0 px` | 正值使阴影向右移动，负值使阴影向左移动。 |
| **Toast shadow vertical offset** | `4 px` | 正值使阴影向下移动，负值使阴影向上移动。 |
| **Toast shadow blur** | `16 px` | 控制阴影边缘的柔和程度和扩散范围。数值越大，阴影越柔和、范围越宽。 |

应先设置阴影不透明度，再调整偏移量和模糊度。截图中的数值会形成居中、轻微的悬浮效果，不需要醒目的轮廓。请分别在浅色和深色页面背景上检查阴影。

## 颜色与消息类型

Toast 颜色来自**主题设置 > Colors > Feedback messages**。每种消息类型都有独立的背景色和前景色：

- 成功（Success）
- 警告（Warning）
- 错误（Error）
- 信息（Information）

请确保每种类型的文字和图标都清晰可读。不要只依靠颜色传达含义，还应配合明确的文字，并在支持时使用适当的图标。

## 推荐调整顺序

1. 设置 Toast 圆角和位置。
2. 选择足以阅读消息的自动关闭时间。
3. 选择预览类型，并在调整样式时保持预览可见。
4. 先设置阴影不透明度，再调整偏移量和模糊度。
5. 检查所有反馈消息颜色。
6. 测试桌面端和移动端位置，完成后将 Preview 恢复为 **Off**。

截图中的数值（`8 px`、**Top center**、`3 s` 和 `10% / 0 px / 4 px / 16 px` 阴影）适合作为简短、轻量通知的均衡起点。

## 保存并测试

点击**保存**，然后触发每一种 Toast 并检查：

- Toast 是否遮挡导航或重要操作。
- 简短和较长消息是否都有足够的阅读时间。
- 文字、图标和关闭控件是否具有足够的对比度。
- Toast 是否完整显示在较窄的移动端屏幕和安全区域内。
- 阴影在浅色和深色背景上是否保持克制。
- 成功、警告、错误和信息消息是否容易区分。
- 键盘和屏幕阅读器用户是否能够感知重要反馈。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `config/settings_schema.json` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
:::

入口：主题编辑器 → 主题设置 → Toast

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Toast radius<br>`toast_radius` | range：拖动滑块调整数值 | 8 | 0–48 px; 步长 2 |
| Position<br>`toast_position` | select：从选项中选择 | bottom-right | Top left (`top-left`); Top center (`top-center`); Top right (`top-right`); Bottom left (`bottom-left`); Bottom center (`bottom-center`); Bottom right (`bottom-right`) |
| Auto-dismiss (seconds)<br>`toast_duration` | range：拖动滑块调整数值 | 3 | 0–15 s; 步长 1 |
| Preview<br>`toast_preview_type` | select：从选项中选择 | off | Off (`off`); Success (`success`); Warning (`warning`); Error (`error`); Info (`info`) |
| Keep preview visible until dismissed<br>`toast_preview_persistent` | checkbox：勾选开启，取消关闭 | true | — |

### Shadow

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Toast shadow opacity<br>`toast_shadow_opacity` | range：拖动滑块调整数值 | 10 | 0–100 %; 步长 5 |
| Toast shadow horizontal offset<br>`toast_shadow_horizontal_offset` | range：拖动滑块调整数值 | 0 | -20–20 px; 步长 2 |
| Toast shadow vertical offset<br>`toast_shadow_vertical_offset` | range：拖动滑块调整数值 | 4 | -20–20 px; 步长 2 |
| Toast shadow blur<br>`toast_shadow_blur` | range：拖动滑块调整数值 | 16 | 0–40 px; 步长 2 |

<!-- latest-schema:end -->
