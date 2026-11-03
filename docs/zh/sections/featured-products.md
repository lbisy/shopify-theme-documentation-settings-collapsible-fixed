# 精选商品（Featured products）

Featured products 将多个商品系列组织成标签页，顾客可切换标签查看对应商品。分区设置控制商品数量、列数、导航和品牌跑马灯；每个 **Collection** 小块配置一个标签的商品系列、标题和说明。

## 添加与配置

1. 进入 **Shopify 后台 → 在线商店 → 主题 → 自定义**。
2. 打开需要编辑的页面模板，在页面内容区域选择 **添加分区 → Featured products**。
3. 设置配色、标题字号、商品数量和布局。
4. 展开分区并点击 **添加 Collection**，选择商品系列，填写标题与说明。
5. 按需增加其他 Collection，拖动调整标签顺序。
6. 配置品牌跑马灯和上下间距，预览桌面端与移动端后点击 **保存**。

此分区不能添加到页眉、页脚或自定义弹层分组中。

## 常规（General）

**Color scheme** 选择分区使用的全局配色方案。截图中第一行第二个配色缩略图被选中。

点击 **编辑方案** 可修改所选方案，其他使用同一方案的区域也会受到影响。请检查标签选中状态、商品信息和按钮与背景的对比度。

## 字体与标题（Font / Heading）

截图中的 **Font** 为分组标题，本身没有独立输入控件。

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Heading size** | **2X large** | 设置商品系列标签标题的字号。 |

可选 **Extra small、Small、Medium、Large、Extra large、2X large、3X large、4X large**。截图值与安装包默认值一致。

## 商品设置（Product settings）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Maximum items** | `8` | 设置每个商品系列最多展示的商品数量。 |
| **Items per row on desktop** | `4` | 设置桌面端每行商品数量。 |
| **Items per row on mobile** | `2` | 设置移动端每行商品数量，可选 1 或 2。 |
| **Show navigation** | **关闭** | 控制商品浏览导航的显示。 |
| **Show pagination** | **关闭** | 控制轮播分页或当前位置指示的显示。 |
| **Show view all button** | **开启** | 显示进入对应商品系列的“查看全部”入口。 |
| **Desktop tab header behavior** | **Wrap to multiple lines** | 设置桌面端标签标题超出可用宽度时的排列方式。 |

**Maximum items** 范围为 **2–12**，步长为 **1**；**Items per row on desktop** 范围为 **2–4**，步长为 **1**。系列内商品不足上限时，只展示实际可用商品。

移动端两列能在同屏展示更多商品，请检查较长商品名称、价格和徽章是否拥挤。每行数量控制布局密度，Maximum items 控制整个系列的展示上限。

**Desktop tab header behavior** 可选：

- **Wrap to multiple lines**：标签较多或名称较长时换到下一行。
- **Horizontal drag/scroll**：使用横向拖动或滚动浏览标签。

截图中的 **Show view all button** 已开启，安装包默认关闭。其余本表截图值与默认值一致。即使导航与分页关闭，也应单独检查“查看全部”按钮是否正常显示，并随当前系列跳转到正确页面。

## 品牌跑马灯（Brand）

Brand 用于在商品展示之外添加装饰性品牌文字跑马灯。截图中的品牌文字编辑框为空，因此不会显示品牌文字跑马灯；下方方向、速度等设置可保留，填写文字后再预览效果。

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Brand name** | 空白 | 设置重复显示的品牌文字，支持行内富文本。 |
| **Brand marquee direction** | **Right to left** | 设置品牌文字的移动方向。 |
| **Pause marquee on hover** | **开启** | 在支持悬停的设备上，指针移到品牌跑马灯时暂停。 |
| **Brand marquee speed** | **Normal** | 设置移动速度，可选 Slow、Normal、Fast。 |
| **Brand marquee spacing** | `64 px` | 调整重复品牌文字之间的间距。 |
| **Brand marquee height** | `380 px` | 调整装饰品牌带占用的垂直空间，文字大小也随高度轻微缩放。 |

方向可选 **Right to left**（从右向左）或 **Left to right**（从左向右）。间距范围为 **24–160 px**，步长 **4 px**；高度范围为 **120–420 px**，步长 **10 px**。

安装包的 Brand name 默认文字为 `Your brand`，与截图空白状态不同；其余本表截图值与默认值一致。建议使用简短文字，避免品牌动效分散顾客对商品的注意力。移动端没有持续悬停状态，应单独检查速度与阅读体验。

## 上下间距（Padding）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Padding top** | `32 px` | 调整分区顶部留白。 |
| **Padding bottom** | `32 px` | 调整分区底部留白。 |

两项范围均为 **0–100 px**，步长 **4 px**。截图与安装包默认值均为 `32 px`。这里调整的是分区留白，与 Brand marquee height 控制的品牌带高度不同。

## Collection 小块

每个 **Collection** 小块对应一个系列标签。点击左侧已有的 Collection 编辑，或通过 **添加 Collection** 新增。

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Select collection** | **Face Masks** | 选择该标签展示的商品系列，商品从此系列读取。 |
| **Collection heading** | `Add On` | 自定义该系列的标签标题，支持行内富文本。 |
| **Collection content** | 空白 | 设置对应标签页中的补充说明，支持行内富文本。 |

### 选择商品系列

点击 **Select collection** 可选择或更换系列。截图选择 Face Masks；将标题改为 Add On 不会更换该系列或修改后台的系列名称。

### 自定义标签标题

**Collection heading** 优先作为标签标题。截图中标签显示 `Add On`，而商品仍来自 Face Masks。将此字段留空时，前台使用所选商品系列的名称。

可通过工具栏添加加粗、斜体或链接格式。标签标题较长时，请配合 Desktop tab header behavior 检查换行或横向滚动效果。

### 系列说明

**Collection content** 可用于简短介绍选品主题或系列特点。截图中为空，因此不显示此说明。安装包默认会提供示例说明文字；不需要时可像截图一样清空。

### 排序与移除

- 拖动左侧 Collection 小块，调整标签顺序。
- 点击 **添加 Collection**，加入另一个系列标签。
- 点击小块底部的 **移除区块**，只从此分区删除该标签，不会删除后台的商品系列或商品。

## 保存并检查

- 各标签对应正确的系列；截图示例为标题 Add On、系列 Face Masks。
- 每个系列最多展示 8 件商品，桌面端每行 4 件，移动端每行 2 件。
- 导航与分页关闭，“查看全部”开启且目标链接正确。
- 标签较多时按 Wrap to multiple lines 换行，没有遮挡商品内容。
- 品牌文字为空时不显示跑马灯；填写后再检查方向、速度、间距和悬停暂停。
- 上下 `32 px` 留白与相邻分区协调。
