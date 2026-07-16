# 分类网格

Category grid（分类网格）用于以卡片形式展示多个商品分类，并引导顾客进入对应的集合或页面。

## 添加分区和 Item

1. 进入 **在线商店 > 主题 > 自定义**。
2. 打开需要编辑的页面模板。
3. 点击 **添加分区**，选择 **Category grid**。
4. 展开左侧的 **Category grid**，点击 **添加 Item**。
5. 点击 Item，设置对应的图片、文字和链接。
6. 重复添加 Item，并拖动内容块调整显示顺序。
7. 完成后点击 **保存**。

![Category grid 设置](/images/zh/category-grid.svg)

## 基础设置

- **Color scheme**：选择该分区使用的全局配色方案。
- **Heading**：设置分区主标题。
- **Heading size**：选择主标题大小。
- **Subheading**：填写标题下方的辅助说明。
- **Subheading size**：选择辅助说明的字号。
- **View all label**：设置“查看全部”链接的文字。
- **View all link**：选择“查看全部”需要打开的集合或页面。
- **Text alignment**：选择文字左对齐、居中或右对齐。

不需要副标题或“查看全部”入口时，可将对应内容留空。

## Grid

- **Desktop columns**：设置桌面端每行显示的卡片数量。
- **Desktop rows**：设置桌面端显示的行数。
- **Mobile columns**：选择移动端每行显示 1 列或 2 列。
- **Gap**：调整卡片之间的间距。

移动端选择 2 列时，建议保持标题简短，并确认图片和文字不会过于拥挤。

## Card

- **Image shape**：选择分类图片的形状，例如 Circle。
- **Image frame style**：选择 **Soft**、**Border** 或 **None** 图片边框样式。
- **Show arrow**：控制卡片是否显示跳转箭头。

卡片图片建议使用相同比例和相近构图，使网格更加整齐。

## Padding

- **Padding top**：设置分区顶部留白。
- **Padding bottom**：设置分区底部留白。

## 自定义 CSS

展开 **自定义 CSS** 可以添加只针对当前分区的样式。非必要不建议修改，添加前请保留原代码备份。

## 管理与检查

- 点击 **添加 Item** 增加分类卡片。
- 拖动 Item 调整顺序，使用 **移除区块** 删除单个 Item。
- 点击面板底部的 **删除分区** 可移除整个 Category grid。
- 检查每张卡片的图片、文字和链接是否正确。
- 分别确认桌面端列数、行数以及移动端 1 列/2 列效果。
- 确认 View all 和卡片链接能够打开正确页面。
