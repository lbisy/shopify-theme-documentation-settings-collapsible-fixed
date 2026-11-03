# 邮件订阅弹层（Newsletter Overlay）

Newsletter Overlay（邮件订阅弹层）用于在店面以弹窗形式展示订阅邀请。它支持展示条件、延迟时间、重复显示间隔、弹窗位置、订阅反馈文案、左侧图片以及可排序的文字和表单内容块。

![Newsletter Overlay 设置面板与前台效果](/images/zh/newsletter-overlay.png)

## 与邮件订阅横幅的区别

- **Newsletter Overlay**：按设置条件自动弹出，会覆盖在当前页面上方。
- **Newsletter Banner**：作为普通内容分区固定显示在页面中，不会自动弹出。

两者可以同时使用，但应避免在同一浏览流程中反复要求顾客订阅。邮件订阅横幅的说明可参见[邮件订阅横幅](/zh/sections/newsletter-banner)。

## 打开设置

1. 进入 **Shopify 后台 → 在线商店 → 主题**。
2. 在当前主题上点击 **自定义**。
3. 在左侧找到 **Overlay** 分组。
4. 展开并点击 **Newsletter Overlay**。
5. 配置展示规则、文案、图片和配色。
6. 添加或排列 Text、Heading 和 Form 内容块。
7. 点击右上角的 **保存**。

Newsletter Overlay 位于跨页面使用的 Overlay 分组中。修改后应在首页、商品页、商品系列页和博客页分别测试，而不能只检查编辑器当前页面。

## Display Settings

### Display mode

设置弹层的运行模式：

- **Enable**：按照页面范围、访客条件、延迟和有效期等设置正常展示。
- **Test**：测试模式会始终打开弹层，方便在主题编辑器中预览内容和样式。

测试完成后必须切回 **Enable**。如果将 Test 模式发布到正式店面，弹层可能在不符合正常展示条件时仍然出现，严重干扰浏览。

### Show on home page

控制正常模式下是否允许在首页显示弹层。关闭后应确认首页不会自动出现，但其他符合条件的页面仍按主题规则工作。

首页通常是流量最大的入口。启用前应检查弹层不会在页面刚打开时遮挡重要导航、Cookie 同意提示或其他促销弹窗。

### Show for visitors

控制正常模式下是否向符合条件的店面访客展示弹层。访客资格可能受到登录状态、既有订阅状态及浏览器记录影响，具体判断以当前主题实现为准。

修改后应至少测试：

- 未登录的新访客。
- 已关闭过弹层的访客。
- 已成功提交邮箱的访客。
- 已登录顾客。
- 清除网站数据或使用无痕窗口后的状态。

如果 **Show on home page** 和 **Show for visitors** 都关闭，正常模式下可能没有符合条件的自动展示场景；发布前应从实际店面验证。

### Delay

设置满足展示条件后等待多久打开弹层，单位为秒。

延迟太短会在顾客尚未了解页面内容时打断浏览；延迟太长则可能在顾客离开前没有机会展示。可以从 `3 s` 开始测试，并根据页面长度、流量来源和移动端体验调整。

Test 模式用于持续预览，可能不会反映正常模式下的实际延迟逻辑。时间设置应在 Enable 模式和实际店面中验证。

### Expire after

设置弹层的展示记录经过多少天后失效。它通常用于控制顾客关闭或看过弹层后，多久可以再次满足展示条件。

例如设置为 `7 day` 时，应在真实浏览器中测试关闭、订阅和重新访问后的行为。浏览器隐私模式、Cookie 或本地存储清理、跨设备访问以及主题更新都可能影响记录。

该设置不是订阅资格或优惠券的到期时间，也不会自动删除顾客邮箱。

### Popup placement

设置弹层在桌面页面中的显示位置，例如 **Bottom right**。应从下拉菜单中选择当前主题提供的位置。

选择位置时应避免覆盖页眉导航、购物车、在线客服、Cookie 提示和其他固定控件。移动端空间有限，主题可能自动调整弹层尺寸或位置，因此必须使用真实手机测试。

## Text & Style

### Text alignment

设置弹层文案的对齐方式。填写当前主题支持的值，通常可使用 `left`、`center` 或 `right`。

输入值应使用正确拼写。修改后检查 Text、Heading 和 Form 是否形成一致的阅读顺序；多语言店铺还应测试从右到左语言。

### Email placeholder

设置邮箱输入框内的提示文字，例如“请输入邮箱地址”。该字段支持动态来源。

占位文字应简短并与页面语言一致。它会在顾客输入后消失，因此不能代替完整字段标签、营销同意说明或隐私政策。

### Success toast

设置订阅提交成功后的提示文字。该字段支持动态来源。

提示应明确说明操作已经完成，不要承诺系统并未自动发送的优惠码、欢迎邮件或礼品。若订阅后还有下一步，应使用简短、可执行的说明。

### Error toast

设置订阅失败后的提示文字。该字段支持动态来源。

错误提示应说明提交未完成，并引导顾客检查邮箱格式或稍后重试。避免只显示“错误”等无法帮助顾客解决问题的文字。

### Left image

选择弹层左侧的图片，也可以连接符合条件的动态来源。

建议使用构图简洁、与订阅主题相关且文件经过压缩的图片。重要信息不要只放在图片内；移动端可能隐藏、裁切或缩小图片，应确保没有图片时弹层仍然容易理解。

### Color scheme

选择弹层使用的全局配色方案，影响背景、文字、输入框、按钮、关闭控件及提示信息。

点击 **编辑方案** 可进入全局颜色设置。修改方案本身会同时影响其他使用该方案的分区，因此应检查输入提示、按钮、成功和错误反馈以及键盘焦点状态与背景之间的对比度。

## 内容块

Newsletter Overlay 支持通过内容块组织弹层内容。在左侧可以拖动内容块调整顺序，也可以单独隐藏、复制或删除。

### Text

用于展示简短的辅助文字，例如访客提示、活动类型或发送频率。它通常放在主标题之前，内容应简短。

### Heading

用于展示弹层的主要订阅文案。应明确说明订阅价值和适用条件，不使用虚假稀缺性或无法兑现的优惠承诺。

如果标题包含首单折扣、赠品或其他利益，应先确认对应折扣规则、适用商品、有效期和发放流程已经配置完成。

### Form

显示邮箱输入框和提交按钮。正常收集订阅时必须保留 Form 内容块；删除或隐藏后，弹层只能展示信息，顾客无法提交邮箱。

建议将 Form 放在 Heading 和必要说明之后，并确保输入框、提交按钮、成功提示和错误提示都可被键盘操作和辅助技术识别。

## 推荐内容顺序

一组清晰的排列方式是：

1. Text：简短辅助提示。
2. Heading：订阅价值或活动说明。
3. Form：邮箱输入与提交按钮。

不需要辅助提示时可以删除 Text，但应保留 Heading 和 Form，使顾客清楚理解订阅目的及提交方式。

## 订阅、优惠与隐私

- 清楚说明邮箱用途、邮件内容和大致发送频率。
- 在适当位置提供隐私政策，并根据目标市场要求取得营销同意。
- 不要预先替顾客作出同意选择，也不要用关闭困难的弹窗强迫订阅。
- 如果承诺折扣，应说明适用范围、最低消费、有效期和排除商品，并确认优惠能够正常发放。
- 邮箱的保存位置、营销状态和后续自动化取决于主题表单、Shopify 设置及营销应用。
- 实际提交后应在 Shopify 后台核对订阅记录，而不是只看到成功提示就认为流程完成。
- 后续营销邮件应提供清晰的取消订阅方式。

## 配置示例

| 设置项 | 示例值 |
| --- | --- |
| Display mode | `Enable` |
| Show on home page | 开启 |
| Show for visitors | 开启 |
| Delay | `5 s` |
| Expire after | `7 day` |
| Popup placement | `Bottom right` |
| Text alignment | `left` |
| Email placeholder | `请输入邮箱地址` |
| Success toast | `订阅成功，感谢关注。` |
| Error toast | `提交失败，请检查邮箱后重试。` |
| Left image | 品牌或产品氛围图 |
| Text | `首次访问？` |
| Heading | `订阅新品与内容更新` |
| Form | 保留并显示 |

## 发布前检查

1. 使用 Test 模式完成排版预览后，将 Display mode 切回 Enable。
2. 分别测试首页和其他页面，确认 Show on home page 的范围正确。
3. 使用新访客、已关闭弹层访客、已订阅访客和已登录顾客测试 Show for visitors。
4. 在 Enable 模式下测量实际 Delay，并确认页面加载后不会过早打断顾客。
5. 关闭弹层后重新访问，验证 Expire after 和重复显示行为。
6. 测试不同 Popup placement，并确认不会与 Cookie 提示、聊天按钮或购物车控件重叠。
7. 检查 Text、Heading 和 Form 的顺序、对齐及多语言内容。
8. 使用空值、格式错误邮箱、有效邮箱和重复邮箱测试表单。
9. 核对 Success toast、Error toast 及 Shopify 后台的实际订阅记录。
10. 如果承诺优惠，完成从订阅到接收和使用优惠的完整流程。
11. 使用键盘打开、填写、提交和关闭弹层，并确认关闭后焦点返回原页面。
12. 在移动端测试软键盘、弹层滚动、关闭按钮和屏幕安全区域。
13. 检查图片、文字、输入框、按钮及反馈信息与背景之间的对比度。
14. 确认隐私政策、营销同意和取消订阅流程符合目标市场要求。
15. 点击 **保存**，再从实际店面完成一次正常访客订阅流程。

<!-- latest-schema:start -->
## 新版安装包设置项（核对清单）

::: warning 版本核对说明
依据 `latest.zip` 内 `sections/newsletter-overlay.liquid` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。
“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。
[完整核对报告](/zh/version-audit)
:::

入口：主题编辑器 → 对应页面模板或分区组 → Newsletter overlay

可通过“添加分区”添加（声明了 presets）。

`enabled_on`: &#123;"groups": ["custom.overlay"]&#125;

`limit`: 1

### Display settings

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Display mode<br>`display_mode` | select：从选项中选择 | enable | Enable (`enable`); Test (`test`)<br>info: Test mode always opens the popup. |
| Show on home page<br>`show_in_home` | checkbox：勾选开启，取消关闭 | true | — |
| Show for visitors<br>`show_for_visitor` | checkbox：勾选开启，取消关闭 | true | — |
| Delay<br>`delay` | range：拖动滑块调整数值 | 3 | 0–60 s; 步长 1 |
| Expire after<br>`expired` | range：拖动滑块调整数值 | 7 | 1–30 day; 步长 1 |
| Popup placement<br>`modal_placement` | select：从选项中选择 | bottom-right | Bottom left (`bottom-left`); Bottom right (`bottom-right`); Center (`center`) |

### Text and style

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Text alignment<br>`alignment` | text：输入文字 | left | — |
| Email placeholder<br>`placeholder` | text：输入文字 | Enter your email address | — |
| Success toast<br>`success_message` | text：输入文字 | Thanks for subscribing. | — |
| Error toast<br>`error_message` | text：输入文字 | Subscription failed. Please try again. | — |
| Left image<br>`image` | image_picker：选择或上传图片 | 未声明 | — |
| Color scheme<br>`color_scheme` | color_scheme：选择全局配色方案 | scheme-2 | — |

### 内容块：Text

`type`: `text`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Text<br>`text` | richtext：编辑格式化文字 | &lt;p&gt;First timer?&lt;/p&gt; | — |
| Text size<br>`body_text_size` | select：从选项中选择 | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |

### 内容块：Heading

`type`: `heading`

| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |
| --- | --- | --- | --- |
| Heading<br>`heading` | inline_richtext：编辑行内格式化文字 | Sign up and get 20% off your first order | — |
| Heading size<br>`heading_text_size` | select：从选项中选择 | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

### 内容块：Form

`type`: `form`; `limit`: 1

此处未声明本地设置（应用或主题区块需查看其自身定义）。

<!-- latest-schema:end -->
