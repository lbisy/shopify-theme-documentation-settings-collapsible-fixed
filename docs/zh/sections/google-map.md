# Google 地图

**Google map** 分区用于在页面或模板中嵌入可交互的 Google 地图，适合展示商店、展厅、自提点、服务区域或其他需要向顾客公开的地点。

![Google 地图 设置面板与前台效果](/images/zh/google-map.png)

## 添加分区

1. 进入 **Shopify 后台 → 在线商店 → 主题**。
2. 找到需要编辑的主题，点击 **自定义**。
3. 打开需要显示地图的页面或模板。
4. 点击 **添加分区 → Google map**。
5. 开启 **Show Google map**。
6. 在 **Map embed code** 中粘贴完整的 Google Maps `<iframe>`。
7. 调整地图高度和分区上下间距。
8. 在预览区确认地图正常显示，然后点击**保存**。

该分区不会根据普通地址文字搜索或生成地图，而是直接渲染设置中提供的嵌入代码。

## Show Google map（显示地图）

**Show Google map** 用于控制嵌入地图是否显示。截图中该开关已开启。

在准备分区、临时隐藏地点或排查嵌入问题时，可以关闭地图并保留已填写的代码。发布前应确认关闭状态不会留下异常空白，同时检查隐私或 Cookie 同意工具能否正确处理第三方地图。

## 获取 Google Maps 嵌入代码

最简单的方式是使用 Google Maps 生成的嵌入 HTML：

1. 在桌面浏览器中打开 Google Maps。
2. 搜索准确的商店、地址或地点。
3. 打开 **Share（分享）**，选择 **Embed a map（嵌入地图）**。
4. 选择合适的初始地图视图或尺寸。
5. 点击 **Copy HTML（复制 HTML）**。
6. 将完整的 `<iframe>...</iframe>` 代码粘贴到 **Map embed code**。

不要只填写地址，也不要粘贴 **Send a link（发送链接）** 中的普通分享网址。该字段需要 iframe HTML。粘贴后请确认 `src` 指向 Google Maps 嵌入网址，并且 iframe 的开始与结束标签完整。

## Map embed code（地图嵌入代码）

截图中的代码使用 Google Maps 嵌入网址，并包含全宽显示、无边框、延迟加载、全屏权限和 referrer policy。常见结构如下：

```html
<iframe
  src="https://www.google.com/maps/embed?..."
  width="100%"
  height="450"
  style="border: 0"
  loading="lazy"
  allowfullscreen
  referrerpolicy="strict-origin-when-cross-origin"
  title="显示商店位置的地图">
</iframe>
```

以上代码仅用于说明结构。实际使用时必须复制目标地点生成的完整网址，不要直接使用省略号 `...`。

建议保留或补充以下 iframe 属性：

- **`src`**：目标地点完整的 Google Maps 嵌入网址。
- **`width="100%"`**：让地图宽度跟随响应式分区。
- **`style="border: 0"`**：移除浏览器默认 iframe 边框。
- **`loading="lazy"`**：地图接近可视区域时再加载。
- **`allowfullscreen`**：允许支持的地图视图进入全屏。
- **`referrerpolicy`**：保留 Google 生成的值；当前 API 示例推荐 `strict-origin-when-cross-origin`。
- **`title`**：填写清楚的无障碍说明，例如“显示上海门店位置的地图”。

::: warning 只粘贴可信 iframe
该字段能够接收标记代码。只应使用 Google Maps 或店主明确批准的来源，不要加入未知脚本、事件处理代码、追踪代码、客户数据、密码、未限制使用范围的 API 密钥或与地图无关的 HTML。
:::

## Map height（地图高度）

**Map height** 控制嵌入地图在页面上的可见高度，单位为像素。截图中的值为 `640 px`。

较高的地图更便于操作缩放和路线控件，但也会占据较多页面空间；较低的地图更加紧凑，但必须保留足够的交互区域。Google Maps 嵌入地图不应缩小到官方支持的最小尺寸以下。

Google 复制出的 iframe 自身也可能包含 `height` 属性。主题的 **Map height** 用于控制最终分区高度；如果页面结果与设置值不一致，请检查 iframe 内联高度、Custom CSS 或主题样式是否发生冲突。

应分别检查常见桌面端、平板和窄屏手机。桌面端合适的高度在移动端可能显得过长。

## Padding（上下间距）

- **Padding top**：控制地图上方的留白。
- **Padding bottom**：控制地图下方的留白。

截图中两个值均为 `32 px`，可作为均衡的初始设置。相邻分区本身留白较大时可以适当减小；地图需要与文字、表单或页脚清楚分隔时可以适当增大。

## Custom CSS（自定义 CSS）

仅在 Map height 和 Padding 无法满足需求时，使用 **Custom CSS** 做小范围、分区级的外观调整，例如修改外层容器宽度、圆角或溢出方式。

由于 Google iframe 属于跨域内容，Shopify 页面中的 CSS 无法修改地图内部的道路、标签、标记或控件。不要遮挡 Google 署名、地图控件或键盘焦点；主题升级后应重新检查自定义规则。

## 地点准确性与顾客指引

发布前请确认：

- 地图标记指向实际入口或自提地点，而不是仅显示城市或行政区范围。
- Google Maps 中的商家名称、地址和路线终点准确。
- **Directions（路线）** 等可见地图控件可以正常使用。
- 在相邻文字分区中提供地址、营业时间、电话以及无障碍入口或停车说明，不要让地图成为关键信息的唯一来源。
- 存在多个地点时，应为地图添加清楚标签，或链接到专门的门店列表页面。

## 隐私、可用性与性能

Google Maps 属于第三方内容，可能根据访客地区和 Google 配置发起外部请求或使用 Cookie。请确认商店隐私说明和 Cookie 同意工具能够按照销售市场的要求处理该嵌入内容。

浏览器隐私工具、内容安全策略、Cookie 同意设置或地区网络限制都可能阻止地图加载。应同时提供文字地址和直接路线链接作为后备方案。延迟加载可以减少首屏工作量，但地图加载后仍会使用第三方资源。

## 截图配置示例

| 设置项 | 截图中的示例值 |
| --- | --- |
| Show Google map | 开启 |
| Map embed code | 完整的 Google Maps `<iframe>` |
| Map height | `640 px` |
| Padding top | `32 px` |
| Padding bottom | `32 px` |

本次截图仅用于识别设置项，不作为文档中的示例图片使用。

## 发布前检查

1. 确认 iframe 来自目标地点的 Google Maps 页面。
2. 检查地图标记、商家名称、地址、路线和初始缩放级别。
3. 确认地图填满分区宽度，且不会产生横向滚动。
4. 在桌面端、平板和移动端检查高度与上下间距。
5. 测试缩放、拖动、路线、全屏和键盘焦点等可用操作。
6. 确认 iframe 具有清楚的无障碍标题，并用文字重复关键地点信息。
7. 配合商店的 Cookie 同意和内容安全设置进行测试。
8. 检查 Google Maps 被阻止或无法访问时的后备内容。
9. 确认 Custom CSS 不会遮挡地图署名或控件。
10. 保存主题，并在主题编辑器之外的预览店面或正式店面完成测试。

嵌入实现详情可参考 Google 的[地图嵌入文档](https://developers.google.com/maps/documentation/embed/embedding-map)。
