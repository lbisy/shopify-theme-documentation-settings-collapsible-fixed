# 编辑式图片拼贴（Editorial collage）

Editorial collage 将标题、说明和三张图片组合成杂志式图文布局，适合介绍品牌理念、商品外观、材质和使用细节。三张图片在分区设置中分别配置，无需添加图片小块。

## 示例效果

![Editorial collage 图文布局与三张图片设置示例](/images/zh/editorial-collage.png)

截图中的桌面端布局为：

| 位置 | 内容 |
| --- | --- |
| 左上 | Heading 标题和 Text 说明。 |
| 右上 | Texture image，适合纹理或氛围图。 |
| 左下 | Product image，适合商品主体图。 |
| 右下 | Detail image，适合局部细节或场景图。 |

截图尚未选择实际图片，因此三个区域显示线稿占位内容。替换图片后会沿用分区预设布局，并不是在此处选择 Shopify 商品或自动读取商品主图。

移动端会重新排列内容：介绍文字和 Texture image 上下排列，Product image 与 Detail image 在下方并排显示。请同时检查两端的裁切与文字换行。

## 添加与配置

1. 进入 **Shopify 后台 → 在线商店 → 主题 → 自定义**。
2. 打开需要编辑的页面模板，在页面内容区域选择 **添加分区 → Editorial collage**。截图位于商品模板中。
3. 设置配色，填写 Heading 和 Text，并选择标题字号。
4. 分别选择 Texture image、Product image 和 Detail image。
5. 调整上下间距，预览桌面端与移动端效果后点击 **保存**。

此分区不能添加到页眉、页脚或自定义弹层分组中。

## 配色（Color scheme）

选择分区使用的全局配色方案。截图中第一行第二个配色缩略图被选中。

点击 **Edit scheme（编辑方案）** 可修改所选方案，其他使用同一方案的区域也会受到影响。请检查标题、正文和图片之间的视觉衔接。

## 标题与说明（Heading / Text）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Heading** | `An object of everyday care.` | 设置图文区域的主标题，为普通文字字段。 |
| **Heading size** | **Extra large** | 设置主标题字号。 |
| **Text** | 下方示例文案 | 设置标题下方的介绍，支持富文本。 |

Heading size 可选 **Extra small、Small、Medium、Large、Extra large、2X large、3X large、4X large**。截图选择 Extra large，与安装包默认值一致；主题会根据屏幕宽度调整标题显示。

截图中的 Text 为：

> More than just skincare, Ceylune is a daily ritual: a moment of calm, a return to yourself. Crafted with nature's finest, it brings balance to your skin and peace to your mind.

标题和说明文案均与安装包的示例内容一致，可替换为自己的品牌介绍。Text 工具栏支持段落、加粗、斜体、链接和列表等格式。建议控制长度，避免介绍区域与相邻图片的比例失衡。

## 图片（Images）

| 设置项 | 截图状态 | 用途与桌面端位置 |
| --- | --- | --- |
| **Texture image** | 未显示已选图片缩略图 | 右上图片，可用于呈现纹理、原料、氛围或使用场景。 |
| **Product image** | 未显示已选图片缩略图 | 左下图片，可用于突出商品整体外观。 |
| **Detail image** | 未显示已选图片缩略图 | 右下图片，可用于展示细节、包装或补充场景。 |

点击各字段中的 **Select（选择）** 可选择或上传图片，也可通过 **Explore free images（浏览免费图片）** 查找素材。三个字段相互独立，没有单独的图片小块排序操作。

### 图片搭配与裁切

- 选择色调和风格协调的三张图片，分别表达氛围、商品主体和细节。
- 图片会按预设容器裁切，请为商品、人物及关键细节保留安全空间。
- 分别检查桌面端的大图和移动端下方并排图片，确保主体仍然清晰。
- 未选择某张图片时，该位置继续显示占位线稿；清空图片字段不会自动移除这个图片区域。

Product image 仅是图片选择字段，不会自动关联商品、价格或商品页链接。此分区没有单独的商品选择器或行动按钮设置。

## 上下间距（Padding）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Padding top** | `32 px` | 调整分区顶部留白。 |
| **Padding bottom** | `32 px` | 调整分区底部留白。 |

两项范围均为 **0–100 px**，步长 **4 px**。截图与安装包默认值均为 `32 px`。它们控制分区留白，不改变三个图片字段对应的位置。

## 自定义 CSS 与移除分区

**Custom CSS（自定义 CSS）** 是主题编辑器提供的分区样式入口。添加局部样式后，请检查图文对齐、图片裁切及移动端排列。

点击 **Remove section（移除分区）**，会从当前模板移除整个 Editorial collage。Shopify 文件库中的原图片不会因此删除。

## 保存并检查

- 标题与说明已替换为预期文案，Extra large 字号下换行自然。
- 三张占位图均已替换，并分别对应 Texture、Product 和 Detail 区域。
- 桌面端左上文案、右上纹理、左下商品、右下细节的关系正确。
- 移动端文字、上方图片及下方两张图片没有异常裁切或拥挤。
- 配色与图片协调，上下 `32 px` 留白与相邻分区衔接自然。
