# 配方与成分介绍（Formula details）

Formula details 将配方介绍与成分卡片组合展示。顶部 **Formula band** 包含标题、说明、配方属性和图片；下方 **Ingredients** 区域介绍具体成分。两部分独立配置配色，并通过 **Attribute** 和 **Ingredient** 两类小块管理内容。

## 示例效果

![Formula details 配方介绍带、属性与成分卡片示例](/images/zh/formula-details.png)

截图使用商品模板，顶部是深色配方介绍带，下方是浅色成分区域。左侧列表包含 **3 个 Attribute** 和 **3 个 Ingredient**：

- 顶部左侧：标题 A Closer Look at the Formula. 及配方说明。
- 顶部中间：Texture、Formula、Finish 三项属性，带有自动编号。
- 顶部右侧：Band image 图片区域。
- 下方：THE FORMULA 标题、副标题及 Aloe Vera、Green Tea、Botanical Extracts 三张成分卡片。

截图中的图片尚未配置，线稿为主题占位内容。正式展示前，请分别选择 Band image 和各 Ingredient 的图片。

## 添加与配置

1. 进入 **Shopify 后台 → 在线商店 → 主题 → 自定义**。
2. 打开需要编辑的页面模板，在页面内容区域选择 **添加分区 → Formula details**。
3. 分别设置成分区域与顶部介绍带的配色。
4. 填写 Band heading、Band text，选择 Band image。
5. 点击 **Add block（添加区块）→ Attribute**，填写配方属性名称及说明。
6. 填写 Ingredients heading 和 Ingredients subtitle，再添加 **Ingredient** 小块，配置成分图片、名称与说明。
7. 调整顺序与上下间距，预览桌面端和移动端后点击 **保存**。

此分区不能添加到页眉、页脚或自定义弹层分组中。Attribute 与 Ingredient 合计最多 **8 个小块**，不是每类各 8 个。

## 两个区域的配色

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Ingredients color scheme** | 第一行第二个配色缩略图被选中 | 设置下方成分区域的配色。 |
| **Band color scheme** | 第一行第一个配色缩略图被选中 | 设置顶部配方介绍带的配色。 |

点击各自的 **Edit scheme（编辑方案）** 可修改对应方案。修改全局方案也会影响其他使用该方案的区域。截图中的深浅背景来自当前店铺配色，请分别检查属性文字和成分卡片的对比度。

## 配方介绍带（Formula band）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Band heading** | `A Closer Look at the Formula.` | 设置顶部介绍带的标题，为普通文字字段。 |
| **Heading size** | **Extra large** | 设置 Band heading 的字号。 |
| **Band text** | 下方示例文案 | 设置顶部标题下方的说明，支持富文本。 |
| **Band image** | 未显示已选图片缩略图 | 设置顶部介绍带右侧的图片。 |

Heading size 可选 **Extra small、Small、Medium、Large、Extra large、2X large、3X large、4X large**。截图的 Extra large 与安装包默认值一致。该设置控制顶部主标题，成分区域标题及小块名称使用各自的预设样式。

截图中的 Band text 为：

> Lightweight, refreshing, and thoughtfully crafted. Every texture, ingredient and detail is designed to bring out your skin's natural glow.

Band text 支持段落、加粗、斜体、链接和列表等格式。建议保持简洁，为同一行的属性和图片留出空间。

通过 **Band image → Select（选择）** 可选择或上传图片，也可浏览免费图片。未设置时显示占位图。它与下方各成分卡片的图片分别配置，不会自动读取当前商品主图。

## 配方属性小块（Attribute）

Attribute 显示在顶部介绍带中，用于介绍质地、配方或使用感受。点击已有 Attribute 编辑，或通过 **Add block → Attribute** 新增。

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Name** | `Texture` | 设置属性名称。 |
| **Text** | `A cooling gel-cream texture that melts into the skin.` | 设置该属性的简短说明。 |

Name 和 Text 都是普通文字字段。顶部三项示例为：

| 编号 | Name | Text |
| --- | --- | --- |
| 01 | Texture | A cooling gel-cream texture that melts into the skin. |
| 02 | Formula | Botanical extracts and lightweight hydration for everyday use. |
| 03 | Finish | Soft. Fresh. Never heavy. |

编号按 Attribute 的排列顺序自动生成，无需在 Name 中输入 01、02、03。调整顺序后请检查名称与说明是否匹配。

## 成分区域（Ingredients）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Ingredients heading** | `THE FORMULA` | 设置成分区域标题。 |
| **Ingredients subtitle** | `Powered by nature. Backed by science.` | 设置成分区域副标题。 |

两项均为普通文字字段，截图与安装包默认文字一致。它们控制整个成分区域的介绍，不是单张成分卡片的名称或说明。

## 成分小块（Ingredient）

第一张图展示了三张成分卡片，但本次截图没有展开 Ingredient 设置面板。以下字段按安装包定义整理，需点击对应小块编辑：

| 设置项 | 作用 |
| --- | --- |
| **Image** | 选择或上传该成分卡片的图片；未配置时显示占位图。 |
| **Name** | 填写成分名称，为普通文字字段。 |
| **Text** | 填写该成分的简短说明，为普通文字字段。 |

截图中的成分内容为：

| 编号 | Name | Text |
| --- | --- | --- |
| 01 | Aloe Vera | Soothes and hydrates. |
| 02 | Green Tea | Helps refresh the skin. |
| 03 | Botanical Extracts | Supports a healthy-looking glow. |

每张卡片独立选择图片，编号按 Ingredient 的顺序自动生成，与上方 Attribute 编号分别计算。这里手动填写的是展示内容，不会自动从当前商品提取成分资料。

建议使用风格、比例协调的素材，并在桌面端与移动端检查裁切、名称换行和说明长度。

## 管理小块

- 通过 **Add block** 选择 Attribute 或 Ingredient，分别添加顶部属性与下方成分。
- 拖动同类小块调整其所在区域的顺序；小块类型决定显示区域，不会因拖到另一类旁边就改变用途。
- 两类合计最多 8 个小块，截图已使用 6 个。
- 点击 **Remove block（移除区块）**，只移除当前属性或成分卡片，不删除 Shopify 文件库中的原图片。

## 上下间距（Padding）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Padding top** | `32 px` | 调整分区顶部留白。 |
| **Padding bottom** | `32 px` | 调整分区底部留白。 |

两项范围均为 **0–100 px**，步长 **4 px**。截图与安装包默认值均为 `32 px`。

## 自定义 CSS 与移除分区

**Custom CSS（自定义 CSS）** 是主题编辑器提供的分区样式入口。添加样式后，请检查深浅区域衔接、属性排列、成分卡片和移动端排版。

**Remove section（移除分区）** 会从当前模板移除整个 Formula details 及其小块。仅移除一项属性或成分时，请使用对应小块的 Remove block。

## 保存并检查

- 顶部配方带与成分区域的配色分别正确，文字清晰可读。
- 顶部标题、说明、三项属性与图片布局协调。
- Band image 和成分图片已替换占位线稿。
- Attribute 与 Ingredient 的编号、顺序、名称和说明对应正确。
- 两类小块合计未超过 8 个。
- 桌面端和移动端图片裁切、文字换行及上下 `32 px` 留白正常。
