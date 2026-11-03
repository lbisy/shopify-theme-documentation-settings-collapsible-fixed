# 商品系列卡片列表（Collection list）

Collection list 用于选择多个商品系列，以卡片形式提供分类入口，适合展示商品分类或主题系列。分区标题和卡片标题均可分别设置桌面端与移动端字号。

## 添加与配置

1. 进入 **Shopify 后台 → 在线商店 → 主题 → 自定义**。
2. 打开需要编辑的页面模板，在页面内容区域点击 **添加分区 → Collection list**。
3. 设置配色、分区标题和标题对齐方式。
4. 点击 **Collections → 选择**，添加需要展示的商品系列，最多可选 **12 个**。
5. 调整卡片标题、导航箭头和上下间距，预览桌面端与移动端后点击 **保存**。

此分区不能添加到页眉、页脚或自定义弹层分组中。

## 配色（Color scheme）

选择分区使用的全局配色方案。截图中第二个配色缩略图带有蓝色选中边框。

点击 **编辑方案** 可以修改所选方案。修改全局方案会同时影响其他使用该方案的区域，请一起检查。

## 标题与商品系列（Heading）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Heading** | `Shop by category` | 设置显示在商品系列卡片上方的分区标题。 |
| **Desktop heading size** | **Extra large** | 设置桌面端分区标题的字号。 |
| **Mobile heading size** | **Extra large** | 单独设置移动端分区标题的字号。 |
| **Heading alignment** | **Center** | 设置分区标题左对齐（Left）或居中（Center）。 |
| **Collections** | 显示“选择”入口；截图未展示已选列表 | 选择此分区展示的商品系列，最多 12 个。 |

桌面端和移动端标题字号均可选择：**Extra small、Small、Medium、Large、Extra large、2X large、3X large、4X large**。

截图中的移动端标题字号是 **Extra large**；安装包声明的默认值是 **Medium**。这里记录的是截图当前配置，并不代表默认值发生变化。

Collections 使用商品系列选择器，不需要逐个添加 Collection 内容块。选择后请检查每张卡片是否进入对应的商品系列页面。

## 卡片（Cards）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Desktop card title size** | **Heading: Medium** | 设置桌面端商品系列卡片标题的字号样式。 |
| **Mobile card title size** | **Text: Large** | 单独设置移动端商品系列卡片标题的字号样式。 |
| **Show navigation arrows** | **开启** | 控制是否显示卡片列表的导航箭头。 |

**Desktop card title size** 可选：

- **Heading: Medium**
- **Heading: Small**
- **Text: Large**
- **Heading: Extra small**
- **Text: Default**

**Mobile card title size** 可选：

- **Text: Extra large**
- **Text: Large**
- **Text: Default**
- **Heading: Extra small**
- **Text: Small**

卡片标题字号与分区标题字号分别控制。商品系列名称较长时，请检查移动端换行效果。开启导航箭头后，还应检查卡片内容超出可见区域时是否便于浏览。

## 上下间距（Padding）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Padding top** | `32 px` | 调整分区顶部留白。 |
| **Padding bottom** | `32 px` | 调整分区底部留白。 |

两项均可通过滑块或数值输入框调整，范围为 **0–100 px**，步长为 **4 px**。截图值与安装包默认值一致，均为 `32 px`。

## 自定义 CSS 与移除分区

截图底部的 **自定义 CSS** 是主题编辑器提供的分区样式入口，不是 Collection list 新增的设置字段。需要局部样式调整时可展开使用。

点击 **移除分区** 会从当前模板移除此分区，不会删除 Shopify 后台中的商品系列。保存前请确认当前模板是否也被其他页面使用。

## 保存并检查

- 标题文字、对齐方式和配色符合预期。
- 已选择需要展示的商品系列，卡片链接进入正确页面。
- 桌面端与移动端的分区标题、卡片标题清晰，长名称没有异常换行。
- 导航箭头按预期显示和工作。
- 上下 `32 px` 留白与相邻分区协调。
