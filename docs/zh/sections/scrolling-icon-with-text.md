# 滚动图标与文字（Scrolling icon with text）

Scrolling icon with text 将多组图标与短文字组成横向循环滚动带，适合展示促销信息、服务特点或品牌关键词。分区设置控制整体滚动与布局，每个 **Item** 小块单独配置文字、图标和链接。

## 添加与配置

1. 进入 **Shopify 后台 → 在线商店 → 主题 → 自定义**。
2. 打开需要编辑的页面模板，在页面内容区域选择 **添加分区 → Scrolling icon with text**。
3. 设置配色、滚动方向、速度、字号和间距。
4. 展开分区并点击 **添加 Item**，填写文字，按需选择图标和链接。
5. 添加其他 Item，拖动调整顺序，预览桌面端与移动端后点击 **保存**。

此分区不能添加到页眉、页脚或自定义弹层分组中。主题会重复排列已有内容以形成循环，无需为延长滚动带手动添加相同的小块。

## 配色（Color scheme）

选择分区使用的全局配色方案。截图中第一行第三个配色缩略图被选中。

点击 **编辑方案** 可调整所选方案。修改全局配色会影响其他使用同一方案的区域，请一起检查文字、图标与背景的对比度。

## 滚动（Scrolling）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Direction** | **Right to left** | 设置内容从右向左或从左向右移动。 |
| **Speed** | **Normal** | 设置滚动速度，可选 Slow、Normal、Fast。 |
| **Horizontal spacing** | `8 px` | 调整相邻滚动内容组之间的水平间距。 |
| **Desktop text size** | **Large** | 设置桌面端滚动文字字号。 |
| **Mobile text size** | **Text: Large** | 单独设置移动端滚动文字字号。 |
| **Bar vertical padding** | `24 px` | 调整滚动带内部上下留白。 |
| **Separator** | `*` | 在内容项后显示分隔字符。 |
| **Pause on hover** | **开启** | 在支持悬停的设备上，指针移到滚动带时暂停滚动。 |

### 方向、速度与间距

**Direction** 可选 **Right to left**（从右向左）或 **Left to right**（从左向右）。

**Speed** 中，Slow 更舒缓，Normal 为常规速度，Fast 动态感更强。文字较长时，应留出足够的阅读时间；触摸设备不支持持续悬停，请单独检查移动端的阅读体验。

**Horizontal spacing** 范围为 **0–120 px**，步长为 **4 px**。截图当前为 `8 px`，安装包默认值为 `40 px`。此设置调整相邻内容组的间隔，不是单个 Item 内图标与文字之间的距离。

### 桌面端与移动端字号

**Desktop text size** 可选：**Extra small、Small、Medium、Large、Extra large、2X large、3X large、4X large**。

**Mobile text size** 可选：**Heading: Large、Text: Extra large、Heading: Medium、Text: Large、Heading: Small、Text: Default、Heading: Extra small、Text: Small**。

截图中的 **Large** 和 **Text: Large** 分别与两端安装包默认值一致。调整后请检查长文字是否挤占过多滚动空间。

### 滚动带内部留白与分隔符

**Bar vertical padding** 范围为 **0–48 px**，步长为 **2 px**，截图与默认值均为 `24 px`。它控制滚动带内部空间，与下方分区的 Padding 分开调整。

**Separator** 在截图中为 `*`，也可改为其他简短字符；留空则不显示分隔字符。分隔符属于文字内容，与 Layout 中的分区分隔线不同。

## 布局（Layout）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Section width** | **Full width** | 设置分区使用全宽或固定页面内容宽度。 |
| **Show divider** | **关闭** | 控制是否显示滚动带上下的分隔线。 |

**Full width** 使用全宽布局；**Fixed width** 跟随页面内容宽度。截图选择 Full width，安装包默认选择 Fixed width。

Show divider 开启后会显示上下分隔线；关闭时不显示。它不会移除 Separator 中设置的 `*` 字符。

## 上下间距（Padding）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Padding top** | `0 px` | 调整分区顶部留白。 |
| **Padding bottom** | `0 px` | 调整分区底部留白。 |

两项范围均为 **0–100 px**，步长为 **4 px**。截图将两项设为 `0 px`，安装包默认均为 `32 px`。即使这里为零，Bar vertical padding 设置的内部留白仍然存在。

## Item 小块

每个 **Item** 对应一组滚动内容。点击左侧已有的 Item 可编辑，点击 **添加 Item** 可新增。

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Title** | `NEW IN 50% Discount` | 设置当前内容项的文字。 |
| **Image icon** | 未显示已选图片缩略图 | 选择或上传图片作为自定义图标。 |
| **Icon** | **None** | 选择主题内置图标；None 表示不使用内置图标。 |
| **Layout** | **Horizontal** | 设置单个 Item 内图标与文字的排列方向。 |
| **Link** | 未填写，显示“粘贴链接或搜索” | 为当前内容项设置可选的跳转链接。 |

### 文字与图标

**Title** 建议使用简短词组。Title 留空时，该 Item 不显示。

点击 **Image icon → 选择** 可选择或上传图片，也可浏览免费图片。设置图片图标后，它优先于 Icon 中选择的内置图标显示。

**Icon** 提供 None、Package、Truck、Airplane、Gift、Tag、Currency、Phone、Chat、Calendar、Clock、Globe、Location、Check、Heart、Leaf、Acorn、Lightning、Water off、Smiley 和 Stool 等选项。截图选择 None，与安装包默认的 Check 不同；如果同时未设置 Image icon，内容项只显示文字。

### 排列与链接

- **Horizontal**：图标与文字横向排列，为截图当前值及安装包默认值。
- **Vertical**：图标与文字纵向排列。它改变单个 Item 内部布局，不改变滚动带的横向滚动方向。
- **Link**：可选择或填写商品、商品系列、页面或其他链接。设置后，该内容项可点击；留空时不提供跳转。

拖动左侧 Item 调整顺序。点击小块底部的 **移除区块**，只删除当前 Item。

## 自定义 CSS

截图底部的 **自定义 CSS** 是主题编辑器提供的分区样式入口。优先通过现有字号、间距、宽度和留白设置调整样式；添加 CSS 后检查移动端布局与循环衔接。

## 保存并检查

- 内容从右向左以 Normal 速度滚动，多个循环之间无明显空档或跳动。
- `8 px` 水平间距和两端文字大小适合当前文案。
- `*` 分隔字符显示正确，分区分隔线保持关闭。
- 全宽布局、内部 `24 px` 留白与分区上下 `0 px` 留白符合预期。
- 桌面端悬停时暂停，移动端文字仍容易阅读。
- 各 Item 的图标、排列、链接与顺序正确。
