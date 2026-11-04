# 场景商品展示（Routine showcase）

场景商品展示（Routine showcase）将商品信息、场景图片和悬浮商品图组合展示，适合介绍商品搭配、使用情境或护理流程。顾客切换步骤时，可以查看对应的商品与图片。分区设置控制共用的标题、背景、按钮和自动播放；每个 **Step** 小块单独配置商品、步骤标签和图片。

## 前台展示与步骤切换

截图中配置了 **3 个 Step**，分别为 **Cleanse、Treat、Protect**，当前显示第一步，右上角进度为 `01 / 03`。

- 左上显示分区统一的眉题、标题、说明和 Shop serums 行动链接。
- 左下显示当前步骤的商品名称、价格和商品简介。
- 中部以拱形场景图搭配悬浮商品图展示当前步骤。
- 右侧显示竖排标题，右下显示步骤缩略图与标签，可点击切换步骤。

截图中的 `Example product 1`、`¥20` 和商品线稿属于未选择商品时的示例展示，不代表已经配置了真实商品。完成各 Step 的商品和图片选择后，请重新检查前台效果。

<!-- 截图添加方式：将图片放入 docs/public/images/zh/，取消对应图片语句的注释，并删除该处“截图预留”提示。 -->
<!-- ![Routine showcase 前台展示、步骤进度与缩略图导航](/images/zh/routine-showcase-preview.png) -->

::: info 截图预留：前台展示
此处可添加包含完整分区、商品信息、拱形图片、步骤进度和缩略图导航的效果截图。
:::

## 添加与配置

1. 进入 **Shopify 后台 → 在线商店 → 主题 → 自定义**。
2. 打开需要编辑的页面模板，在页面内容区域选择 **添加分区 → Routine showcase**。
3. 设置配色、标题字号、背景和介绍文案。
4. 展开分区并点击 **添加 Step**，选择商品并配置步骤标签和图片。
5. 按需添加其他步骤，拖动调整顺序，最多添加 **5 个 Step**。
6. 配置按钮、自动播放和上下间距，预览桌面端与移动端后点击 **保存**。

此分区不能添加到页眉、页脚或自定义弹层分组中。

<!-- ![Routine showcase 配色、标题与背景设置](/images/zh/routine-showcase-settings.png) -->

::: info 截图预留：分区设置
此处可添加包含 Color scheme、Heading size、Background image、Eyebrow、Heading 和 Description 的设置面板截图。
:::

## 配色（Color scheme）

选择分区使用的全局配色方案。截图中第一行第二个配色缩略图带有蓝色选中边框。

点击 **编辑方案** 可修改该方案。修改全局配色会同时影响其他使用同一方案的区域，请一起检查文字、按钮和背景的对比度。

## 字体与分区标题（Font / Section heading）

截图中的 **Font** 是设置分组标题，本身没有独立输入控件。

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Heading size** | **Large** | 设置分区主标题字号。 |
| **Background image** | 未显示已选图片缩略图 | 选择分区整体背景图片。 |
| **Eyebrow** | `Ceylune` | 设置主标题上方的短眉题或品牌文字。 |
| **Heading** | `Serums & Treatments` | 设置分区主标题。 |
| **Description** | `Targeted care for balanced, luminous skin.` | 设置标题下方的补充说明。 |

**Heading size** 可选 **Extra small、Small、Medium、Large、Extra large、2X large、3X large、4X large**。截图当前为 Large，安装包默认值为 Extra small。这是字号设置，不是 HTML 标题层级选择。

**Background image** 可通过“选择”上传或选择图片，也可浏览免费图片。它是整个分区的背景，与 Step 中的场景图片、悬浮商品图片分别配置。请在不同屏幕上检查背景裁切与文字可读性。

Eyebrow 和 Heading 支持行内富文本，可使用加粗、斜体或链接。Description 支持富文本段落和列表；建议保持简短，避免移动端介绍区域过长。

这里的 Description 是整个分区共用的介绍文案，不是当前商品的简介。左下商品信息会跟随 Step 切换，商品名称、价格和简介从该 Step 所选的 Product 读取；简介可能以节选形式展示。

## 按钮（Button label / Button link）

<!-- ![Routine showcase 按钮、自动播放与间距设置](/images/zh/routine-showcase-autoplay.png) -->

::: info 截图预留：按钮、自动播放与间距
此处可添加包含 Button label、Button link、Autoplay steps、Autoplay interval 和 Padding 的设置面板截图。
:::

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Button label** | `Shop serums` | 设置分区行动入口的文字，支持行内富文本。 |
| **Button link** | `/collections` | 设置行动入口的目标地址；截图指向商品系列列表。 |

请同时设置清晰的按钮文字和有效链接。截图中的 Shop serums 是当前文案，链接仍指向 `/collections`；若要直接进入精华液系列，请选择对应商品系列链接，并在预览中测试。

## 步骤自动播放

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Autoplay steps** | **开启** | 自动切换展示步骤。 |
| **Autoplay interval (seconds)** | `5 s` | 设置自动切换的间隔时间。 |

间隔范围为 **3–10 秒**，步长为 **1 秒**。截图中的开启状态与 `5 s` 均与安装包默认值一致。添加多个 Step 后再测试自动播放；文案较长时可增加停留时间。

截图中的三个步骤会按配置顺序切换。请同时检查右上进度、当前商品信息和右下缩略图选中状态是否随步骤更新，并测试点击缩略图手动切换。

## 上下间距（Padding）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Padding top** | `32 px` | 调整分区顶部留白。 |
| **Padding bottom** | `32 px` | 调整分区底部留白。 |

两项范围均为 **0–100 px**，步长为 **4 px**。截图与安装包默认值均为 `32 px`。

## Step 小块

每个 **Step** 对应一个商品步骤。点击左侧已有 Step 编辑，或通过 **添加 Step** 新增，最多 5 个。

<!-- ![Routine showcase 的 Step 小块设置](/images/zh/routine-showcase-step.png) -->

::: info 截图预留：Step 小块
此处可添加包含 Product、Step label、Arch scene image 和 Floating product image 的小块设置截图。
:::

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Product** | 未选择，显示“选择”入口 | 选择当前步骤关联的商品，并提供其名称、价格和简介。 |
| **Step label** | `Cleanse` | 设置当前步骤标签。 |
| **Arch scene image** | 未显示已选图片缩略图 | 设置当前步骤的拱形场景图片。 |
| **Floating product image** | 未显示已选图片缩略图 | 设置叠加展示的悬浮商品图片；不设置时使用所选商品的主图。 |

### 商品与步骤标签

点击 **Product** 选择或更换当前步骤的商品。每个 Step 独立选择商品，无需在分区中选择商品系列。

本次截图中的 Product 尚未选择，场景图和悬浮图也尚未上传，因此前台仍显示示例商品与占位图。正式展示前，请为每个步骤选择对应商品。

**Step label** 建议使用简短步骤名称，例如截图中的 Cleanse。请确认步骤名称、所选商品和场景图片表达的是同一使用流程；修改标签不会更改商品本身的名称。

Step label 会显示在步骤导航中。可按截图的 Cleanse、Treat、Protect 分别配置三个步骤，添加顺序即为流程顺序。

### 场景图片（Arch scene image）

选择与当前步骤相关的使用场景或人物照片。此图片在拱形区域中展示；上传后应检查主体在拱形裁切范围内的位置，避免面部、商品或关键动作被裁掉。

### 悬浮商品图片（Floating product image）

此图片按固定高度展示。面板建议使用：

- **透明背景 PNG**。
- 宽高比例约 **1:2.5**。
- 尺寸至少 **640 × 1600 px**。
- 商品主体尽量填满画布，减少四周空白。

较宽的图片在相同展示高度下会显得更小。未单独选择 Floating product image 时，使用 Product 的商品主图；需要更清晰的抠图效果时，可为当前 Step 单独上传透明商品图。

商品也未选择时，主题会显示占位图，不会自动使用真实商品图片。分区 Background image、Step 的 Arch scene image 和 Floating product image 是三处不同的图片设置，请分别配置。

### 排序与移除

- 拖动左侧 Step 小块调整步骤顺序。
- 点击 **添加 Step** 增加下一步骤。
- 点击小块底部的 **移除区块**，只移除当前步骤，不删除后台商品。

## 自定义 CSS 与删除分区

截图底部的 **自定义 CSS** 是主题编辑器提供的分区样式入口。添加局部样式后请检查桌面端和移动端图片、文字的排版。

**删除分区** 会从当前模板移除整个 Routine showcase 及其 Step 小块。保存前请确认当前模板是否也被其他页面使用。

## 保存并检查

- 眉题 Ceylune、标题 Serums & Treatments 和说明文案显示正确。
- Shop serums 链接进入预期页面。
- 每个步骤选择了正确商品，标签与场景图片匹配。
- 示例商品和占位图已替换，商品名称、价格和简介随步骤正确切换。
- 拱形照片裁切合理，悬浮商品图清晰且没有过多空白。
- 多个步骤以 `5 s` 间隔自动切换，顺序符合预期。
- 右上步骤进度和右下缩略图选中状态同步更新，手动切换正常。
- 桌面端和移动端无文字或图片遮挡，上下 `32 px` 留白协调。
