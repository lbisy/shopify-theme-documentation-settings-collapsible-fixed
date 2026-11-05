# 心情选品展示（Mood finder）

Mood finder 通过心情或使用情境引导顾客发现商品。顾客选择圆盘中的不同选项后，右侧会展示对应的推荐商品与说明。分区设置控制共用文案、配色和装饰，每个 **Mood** 小块单独配置选项图片、短语及关联商品。

## 示例效果

![Mood finder 圆盘选项、推荐商品与分区设置示例](/images/zh/mood-finder.png)

截图使用商品模板，分区由左侧介绍、中部四分圆盘和右侧推荐卡片组成。共有 **4 个 Mood**，左侧显示 **Add Mood（4/4）**，表示已达到小块数量上限。

| 圆盘位置 | Eyebrow | Phrase |
| --- | --- | --- |
| 左上 | Energized | Brighten the look |
| 右上 | Glow | Quiet radiance |
| 左下 | Comfort | Grounded warmth |
| 右下 | Clarity | Fresh focus |

截图中当前选中 **Energized**，右侧卡片显示标签 **BALM · RESTORE** 和 `Example product 1`。Mood 小块中的 Product 尚未选择，因此线稿和示例商品名称属于占位内容；正式使用前请分别选择真实商品。

点击圆盘的其他选项，可切换对应的推荐卡片。左侧介绍文案属于分区共用内容，不随单个 Mood 的商品设置更换。

## 添加与配置

1. 进入 **Shopify 后台 → 在线商店 → 主题 → 自定义**。
2. 打开首页、商品或普通页面模板，选择 **添加分区 → Mood finder**。截图使用的是商品模板。
3. 设置配色、眉题、标题、补充说明和底部提示文字。
4. 点击 **添加 Mood**，配置选项纹理图、眉题、短语和商品。
5. 为各 Mood 填写推荐卡片标签与说明，最多添加 **4 个 Mood**。
6. 按需设置装饰图片与分区留白，预览桌面端和移动端后点击 **保存**。

## 常规（General）

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Color scheme** | 第一行第二个配色缩略图被选中 | 选择整个分区使用的全局配色方案。 |
| **Eyebrow** | `Skin mood finder` | 设置分区主标题上方的短眉题，前台显示为大写文字。 |
| **Heading** | `What are you in the mood for?` | 设置分区主标题，支持行内富文本。 |
| **Heading size** | **Extra large** | 调整分区主标题字号。 |
| **Subtext** | 下方两段示例文案 | 设置主标题下方的介绍文字，支持富文本。 |
| **Caption** | `Choose your mood. We'll do the rest.` | 设置分区底部的简短提示文字。 |
| **Show decoration** | **开启** | 控制是否显示植物装饰插图。 |
| **Decoration image** | 未显示已选图片缩略图 | 选择自定义图片，替换默认植物插图。 |

### 配色与标题

点击 **Edit scheme（编辑方案）** 可修改所选配色方案，其他使用同一方案的区域也会受到影响。请检查当前选项、文字和推荐卡片的对比度。

Eyebrow 是普通文字字段；Heading 支持加粗、斜体和链接等行内格式。Heading size 可选 **Extra small、Small、Medium、Large、Extra large、2X large、3X large、4X large**，截图的 Extra large 与安装包默认值一致。该字号控制分区主标题，不控制右侧商品名称。

### 介绍与底部提示

截图中的 Subtext 为两段文字：

> Find your skin's moment.
>
> Choose what you need today.

Subtext 支持段落、列表等富文本格式。Caption 是独立的普通文字字段，在分区底部显示；不需要对应文案时可清空该字段。

### 装饰图片

截图开启 Show decoration，与默认值一致。未选择 Decoration image 时使用默认植物插图；选择自定义图片后替换默认插图。装饰从平板宽度起显示，较窄屏幕上不显示；关闭开关后隐藏装饰。

装饰图片与 Mood 小块的 Texture image 用途不同：前者用于整个分区的点缀，后者用于圆盘中某个选项的背景。

## Mood 小块

点击左侧已有的 **Mood** 编辑。每个小块定义一个圆盘选项及其右侧推荐卡片。

| 设置项 | 截图当前值 | 作用 |
| --- | --- | --- |
| **Texture image** | 未显示已选图片缩略图 | 设置当前圆盘选项的纹理或场景背景图。 |
| **Eyebrow** | `Energized` | 设置圆盘选项的短标签，前台呈现为大写。 |
| **Phrase** | `Brighten the look` | 设置标签下方的短语，支持行内富文本。 |
| **Product** | 未选择，显示 Select 入口 | 选择该心情对应的推荐商品。 |
| **Tag line** | `Balm · Restore` | 设置右侧推荐卡片中的简短标签。 |
| **Description** | 空白 | 为当前推荐卡片填写多行纯文字说明。 |

### 圆盘图片、标签与短语

点击 **Texture image → Select（选择）** 可选择或上传图片，也可浏览免费图片。未设置图片时，主题显示装饰占位图。选项会按圆盘区域裁切，请检查主体和标签的可读性。

小块 Eyebrow 与分区 Eyebrow 分别控制选项标签和分区眉题。Phrase 可通过工具栏设置加粗、斜体或链接；建议保持简短，避免在圆盘区域内过多换行。

### 推荐商品与卡片内容

**Product** 选择推荐商品后，右侧卡片使用该商品的名称、主图和链接。它不会自动填写圆盘短语或替换 Texture image。

**Tag line** 在卡片的商品名称上方显示。截图输入 `Balm · Restore`，前台呈现为 **BALM · RESTORE**。

**Description** 是当前 Mood 的独立说明字段，不是分区 Subtext，也不会自动读取商品详情描述。已选择真实商品时，留空则不显示该段自定义说明；需要说明时请手动填写。

截图未选商品且 Description 为空，因此卡片显示主题的示例说明：

> A gentle daily formula with plant-based hydrators selected for comfort and balance.

未选商品时卡片链接回退到全部商品页面；选择商品后进入该商品页面。请逐项测试卡片的箭头链接。

### 数量、排序与移除

- 最多添加 **4 个 Mood 小块**；达到 4/4 后不能继续添加。
- 拖动小块调整顺序后，检查圆盘位置与对应卡片的关系。
- 点击 **Remove block（移除区块）**，仅移除当前选项，不删除后台商品或图片文件。

## 上下间距（Padding）

本次截图没有展示 Padding 区域。安装包提供以下设置，可在分区面板中继续向下查看：

| 设置项 | 安装包默认值 | 范围与作用 |
| --- | --- | --- |
| **Padding top** | `32 px` | 顶部留白，范围 0–100 px，步长 4 px。 |
| **Padding bottom** | `32 px` | 底部留白，范围 0–100 px，步长 4 px。 |

## 保存并检查

- 四个圆盘选项的文字和图片正确，没有遗留占位图。
- 分区 Eyebrow、Heading、Subtext 和 Caption 分别出现在预期位置。
- 点击各心情后，选中状态与右侧推荐商品、标签和说明同步更新。
- 为每个 Mood 选择真实商品，替换 Example product 等示例内容并测试商品链接。
- 自定义卡片 Description 已按需要填写，不依赖商品详情自动生成。
- 桌面端与移动端文字清晰，装饰图片按屏幕宽度正常显示。
