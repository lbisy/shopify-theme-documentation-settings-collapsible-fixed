<!-- unlinked-document:start
文档显示状态：未在主页或目录中显示，且未被其他页面有效引用。
核对说明：已注释的目录入口和页面链接不计入有效引用；已排除构建的页面不作为引用来源。
保留正文供后续维护，此标记仅作为源码注释。
unlinked-document:end -->

# Formula details

Formula details combines a formula introduction with ingredient cards. The upper **Formula band** contains a heading, copy, attributes and an image. The lower **Ingredients** area introduces individual ingredients. Configure separate color schemes for the two areas, using **Attribute** and **Ingredient** blocks for their content.

## Example preview

![Formula details introduction band, attributes and ingredient cards example](/images/en/formula-details.png)

The screenshot uses a product template, with a dark formula band above a light ingredient area. The sidebar contains **3 Attribute blocks** and **3 Ingredient blocks**:

- Top left: A Closer Look at the Formula. and its introductory copy.
- Top middle: automatically numbered Texture, Formula and Finish attributes.
- Top right: the Band image area.
- Below: THE FORMULA heading, subtitle and Aloe Vera, Green Tea and Botanical Extracts cards.

The images are not configured in the screenshot, so the line drawings are theme placeholders. Choose Band image and each Ingredient's image before publishing.

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open the template you want to edit and choose **Add section → Formula details** in the page content area.
3. Choose color schemes for the ingredient area and formula band independently.
4. Enter Band heading and Band text, then select Band image.
5. Choose **Add block → Attribute** and enter an attribute name and description.
6. Set Ingredients heading and Ingredients subtitle, then add **Ingredient** blocks with images, names and descriptions.
7. Adjust ordering and padding, preview desktop and mobile, then click **Save**.

This section cannot be added to header, footer or custom overlay groups. Attribute and Ingredient blocks share a total limit of **8 blocks**, rather than eight of each type.

## Area color schemes

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Ingredients color scheme** | Second scheme thumbnail in the first row selected | Sets colors for the lower ingredient area. |
| **Band color scheme** | First scheme thumbnail in the first row selected | Sets colors for the upper formula band. |

Use each **Edit scheme** link to change its scheme. Global scheme changes also affect other areas using that scheme. The screenshot's dark and light backgrounds come from the store's current schemes; check attribute text and ingredient card readability separately.

## Formula band

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Band heading** | `A Closer Look at the Formula.` | Sets the upper band's heading as plain text. |
| **Heading size** | **Extra large** | Sets the Band heading size. |
| **Band text** | Example copy below | Adds supporting copy below the heading, with rich-text formatting. |
| **Band image** | No selected image thumbnail visible | Sets the image on the right of the formula band. |

Heading size offers **Extra small, Small, Medium, Large, Extra large, 2X large, 3X large and 4X large**. The screenshot's Extra large matches the package default. It controls the upper main heading; the ingredient heading and block names use their own preset styles.

The screenshot's Band text reads:

> Lightweight, refreshing, and thoughtfully crafted. Every texture, ingredient and detail is designed to bring out your skin's natural glow.

Band text supports paragraphs, bold, italic, links and lists. Keep copy concise to balance the attributes and image in the same band.

Use **Band image → Select** to choose or upload an image, or explore free images. An unset image displays a placeholder. It is configured independently from ingredient card images and does not automatically use the current product's featured image.

## Attribute blocks

Attributes appear within the upper band to describe texture, formulation or finish. Select an existing Attribute or use **Add block → Attribute**.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Name** | `Texture` | Sets the attribute name. |
| **Text** | `A cooling gel-cream texture that melts into the skin.` | Adds a short attribute description. |

Both fields are plain text. The screenshot's three attributes are:

| Number | Name | Text |
| --- | --- | --- |
| 01 | Texture | A cooling gel-cream texture that melts into the skin. |
| 02 | Formula | Botanical extracts and lightweight hydration for everyday use. |
| 03 | Finish | Soft. Fresh. Never heavy. |

Numbers are generated from Attribute order. Do not enter 01, 02 or 03 in Name. After reordering, check that names and descriptions match.

## Ingredients

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Ingredients heading** | `THE FORMULA` | Sets the ingredient area's heading. |
| **Ingredients subtitle** | `Powered by nature. Backed by science.` | Sets the supporting subtitle. |

Both are plain-text fields, and the screenshot matches the package's default copy. They introduce the ingredient area as a whole, independently of individual card names and descriptions.

## Ingredient blocks

The first screenshot shows three ingredient cards, but the supplied screenshots do not expand an Ingredient settings panel. The fields below come from the package definition; select an Ingredient block to edit them:

| Setting | Purpose |
| --- | --- |
| **Image** | Chooses or uploads the card image; an unset image displays a placeholder. |
| **Name** | Sets the ingredient name as plain text. |
| **Text** | Adds a short plain-text ingredient description. |

The screenshot shows:

| Number | Name | Text |
| --- | --- | --- |
| 01 | Aloe Vera | Soothes and hydrates. |
| 02 | Green Tea | Helps refresh the skin. |
| 03 | Botanical Extracts | Supports a healthy-looking glow. |

Choose each card's image independently. Ingredient numbering follows Ingredient order and is separate from Attribute numbering. Content is entered manually rather than extracted automatically from the current product.

Use coordinated images and check cropping, name wrapping and description length on desktop and mobile.

## Manage blocks

- Use **Add block** to choose Attribute or Ingredient for the upper attributes or lower ingredient cards.
- Drag blocks of the same type to change their order within that area. Block type determines placement; dragging a block beside another type does not change its purpose.
- Both types share an **8-block** limit. The screenshot uses six blocks.
- **Remove block** removes only the selected attribute or ingredient card, without deleting its original image from Shopify's file library.

## Padding

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Padding top** | `32 px` | Adjusts space above the section content. |
| **Padding bottom** | `32 px` | Adjusts space below the section content. |

Both controls range from **0–100 px**, in **4 px** steps. The screenshot and package defaults use `32 px` for both.

## Custom CSS and removing the section

**Custom CSS** is a section styling control provided by the theme editor. After adding local styles, check the color transition, attribute layout, ingredient cards and mobile presentation.

**Remove section** removes the entire Formula details section and its blocks from the current template. Use a block's Remove block action to remove only one attribute or ingredient.

## Save and check

- Verify separate band and ingredient color schemes with readable text.
- Balance the upper heading, copy, three attributes and image.
- Replace the Band image and ingredient image placeholders.
- Check numbering, ordering, names and descriptions for both block types.
- Keep the combined block count at eight or fewer.
- Review desktop/mobile cropping, text wrapping and `32 px` top and bottom padding.
