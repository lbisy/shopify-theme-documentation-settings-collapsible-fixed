# 图片热点与特色标签（Feature tabs）

Feature tabs 将一张主图上的编号标记与多组特色说明对应展示，适合介绍商品来源、制作过程、质地或使用体验。每个 **Item** 小块对应一个标记、一组说明和一个标签，可选择关联商品。

## 示例效果

![Feature tabs 主图标记、特色说明与标签导航示例](/images/zh/feature-tabs.png)

截图中的分区位于商品模板内，左侧为带编号标记的主图，右侧为当前特色说明与标签列表。共有 **4 个 Item**：

| 编号 | 标签 |
| --- | --- |
| 01 | Origin |
| 02 | Process |
| 03 | Texture |
| 04 | Ritual |

当前选中 **Origin**，计数显示 `01 / 04`，标题为 `From seed to serum.`。选中的标签行和对应编号使用突出样式。切换右侧标签，可查看其他 Item 的说明。

截图中的 Feature image 尚未选择，因此左侧显示装饰占位图。右侧的植物装饰则是 Show decoration 开启后的默认插图，与主图分别配置。

## 添加与配置

1. 进入 **Shopify 后台 → 在线商店 → 主题 → 自定义**。
2. 切换到首页、商品或普通页面模板，选择 **添加分区 → Feature tabs**。截图使用的是商品模板。
3. 设置配色、标题字号并选择 Feature image。
4. 点击 **添加 Item**，填写 Label、Heading 和 Text，调整对应标记的位置。
5. 按需为 Item 选择 Product link，重复添加其他内容，最多 **6 个 Item**。
6. 设置装饰图和上下留白，预览桌面端与移动端后点击 **保存**。

## 常规（General）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Color scheme** | 第一行第二个配色缩略图被选中 | 设置分区使用的全局配色方案。 |
| **Heading size** | **Extra large** | 设置 Item 说明区域的主标题字号。 |
| **Feature image** | 未显示已选图片缩略图 | 设置所有编号标记共用的主图。 |
| **Show decoration** | **开启** | 控制是否显示特色说明区域的装饰插图。 |
| **Decorative image** | 未显示已选图片缩略图 | 选择自定义装饰图，替换默认植物插图。 |

### 配色与标题字号

点击 **Edit scheme（编辑方案）** 可修改所选配色，其他使用同一方案的区域也会受到影响。请检查选中标签、编号、正文与背景之间的对比度。

Heading size 可选 **Extra small、Small、Medium、Large、Extra large、2X large、3X large、4X large**。截图选择 Extra large，与安装包默认值一致。它控制说明区域的大标题，不是标签文字，也不是单独的移动端字号控件；主题会根据屏幕宽度调整显示。

### 主图与装饰图

点击 **Feature image → Select（选择）** 可选择或上传图片，也可浏览免费图片。编号标记叠加在这张主图上；更换图片后，请重新定位每个 Item 的标记。

**Show decoration** 在截图中开启，与默认值一致。未选择 Decorative image 时，使用默认植物插图；选择自定义图片后替换该插图。装饰从平板宽度起显示，较窄屏幕上不显示。关闭开关后，不显示装饰插图。

Feature image 是用于定位标记的主图，Decorative image 是说明区域中的辅助装饰，两者用途不同。

## 上下间距（Padding）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Padding top** | `32 px` | 调整分区顶部留白。 |
| **Padding bottom** | `32 px` | 调整分区底部留白。 |

两项范围均为 **0–100 px**，步长 **4 px**。截图与安装包默认值均为 `32 px`。

## Item 小块

点击左侧已有的 Item 编辑，或通过 **Add Item（添加 Item）** 新增。每个小块对应一个编号及一项标签内容。

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Product link** | 未选择，显示 Select 入口 | 为当前主图编号关联商品链接，可选。 |
| **Marker horizontal position** | `22%` | 设置编号在主图中的横向位置。 |
| **Marker vertical position** | `28%` | 设置编号在主图中的纵向位置。 |
| **Label** | `Origin` | 设置标签文字，同时显示在当前说明的眉题位置。 |
| **Heading** | `From seed to serum.` | 设置当前特色说明的主标题。 |
| **Text** | 下方示例文案 | 设置主标题下方的详细说明，支持富文本。 |

### 商品链接与编号位置

Product link 仅用于关联当前编号的商品跳转，不会自动把主图替换为商品图片，也不会自动填写 Label、Heading 或 Text。截图未选择商品时，编号作为视觉标记显示；选择商品后，可通过对应编号访问商品页面。浏览不同特色说明请使用标签列表。

两个位置控件均为 **0–100%**，步长 **1%**：

- **Marker horizontal position**：数值越大，标记越靠右。
- **Marker vertical position**：数值越大，标记越靠下。

截图中的第一项为横向 `22%`、纵向 `28%`，与安装包默认值一致。每个 Item 的坐标独立设置；请避免标记互相重叠或压住重要主体，并在移动端重新检查位置。

### 标签、标题与正文

**Label** 是简短的普通文字字段，截图为 Origin。它显示在标签行中，在当前说明上方还会呈现为大写眉题 ORIGIN。

**Heading** 支持行内富文本，可使用加粗、斜体和链接。截图中的正文 Text 为：

> Share a concise benefit, ingredient story, or ritual step that helps customers understand why this detail matters.

Text 支持富文本段落、列表、加粗、斜体和链接等格式。建议每项围绕一个特色组织文字，避免内容过长影响两栏布局。

### 排序与移除

- 拖动左侧 Item 调整标签顺序，编号随显示顺序排列。
- 调整顺序后，检查每个编号的坐标与对应说明是否匹配。
- 最多添加 **6 个 Item**，不必为了编号添加额外小块。
- 点击 **Remove block（移除区块）**，仅删除当前 Item。

## 自定义 CSS 与移除分区

**Custom CSS（自定义 CSS）** 是主题编辑器提供的分区样式入口。添加局部样式后，请检查主图、编号、标签选中状态及移动端文字排版。

**Remove section（移除分区）** 会从当前模板移除整个 Feature tabs 及其 Item 小块。仅删除一项说明时，请使用对应 Item 的移除区块操作。

## 保存并检查

- 用实际图片替换左侧占位图，并逐项调整标记位置。
- Origin、Process、Texture、Ritual 四个标签与对应编号、说明匹配。
- 切换标签时，当前内容、计数和编号突出状态正确更新。
- 关联商品的编号跳转至正确商品；未选择商品的标记不作为商品链接。
- 默认植物装饰或自定义装饰在适用屏幕宽度下正常显示。
- Extra large 标题和上下 `32 px` 留白在桌面端与移动端均协调。
