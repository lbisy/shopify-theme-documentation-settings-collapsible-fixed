<!-- unlinked-document:start
文档显示状态：未在主页或目录中显示，且未被其他页面有效引用。
核对说明：已注释的目录入口和页面链接不计入有效引用；已排除构建的页面不作为引用来源。
保留正文供后续维护，此标记仅作为源码注释。
unlinked-document:end -->

# Scatter gallery

Scatter gallery combines images in a staggered arrangement with varied sizes and positions. Use it for brand imagery, product details or lifestyle scenes. Section settings control the color scheme, statement, desktop/mobile heading sizes, decoration and padding. Each **Image** block supplies one gallery image.

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open the template you want to edit and choose **Add section → Scatter gallery** in the page content area.
3. Set the color scheme, optionally enter a Statement, and adjust desktop and mobile heading sizes.
4. Expand the section and click **Add Image** to select images for the blocks.
5. Optionally choose a brush stroke decoration and adjust padding.
6. Preview desktop and mobile, then click **Save**.

This section cannot be added to header, footer or custom overlay groups.

## Screenshot layout

The screenshot contains **8 Image blocks**. **Add Image (8/8)** in the left sidebar indicates that the block limit has been reached. Images occupy different sizes and vertical positions, rather than a uniform grid.

The backpack, shoe, glasses, cap, watch and lamp drawings are decorative placeholders for unconfigured images. They do not indicate that actual product images have been selected. Choosing an image in each block replaces the corresponding placeholder.

<!-- Screenshot slot: full section and settings panel. Add the file to docs/public/images/en/ to enable the image reference below. -->
<!-- ![Scatter gallery layout and section settings](/images/en/scatter-gallery.png) -->

## General

**Color scheme** chooses the global scheme for the section. The screenshot selects the second scheme thumbnail in the first row.

Click **Edit scheme** to change it. Changes also affect other areas using the same scheme, so review background and heading contrast in those areas as well.

## Heading

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Statement** | Empty | Adds a statement or brand message to the gallery; leaving it blank hides the heading text. |
| **Heading size** | **Medium** | Sets the desktop Statement size. |
| **Mobile heading size** | **Medium** | Sets the mobile Statement size independently. |

Both size controls offer **Extra small, Small, Medium, Large, Extra large, 2X large, 3X large and 4X large**.

Statement is empty in the screenshot, leaving an image-only presentation. You can configure its sizes in advance and review the result after entering text. Statement is a plain-text field suitable for a short brand message or gallery introduction.

The desktop default is Medium, matching the screenshot. The mobile default is Extra small, which differs from the screenshot's Medium. The package also supplies sample Statement text, which has been cleared in the screenshot.

## Decoration

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Brush stroke image** | No selected image thumbnail visible | Adds an optional brush stroke or decorative image. |

Click **Select** to choose or upload imagery, or explore free images. Leaving this unset hides the decoration.

Brush stroke image is separate from the Image blocks and does not count toward the eight-block limit. Choose decoration suited to layering, then check its relationship to gallery images and text.

## Padding

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Padding top** | `32 px` | Adjusts space above the section content. |
| **Padding bottom** | `32 px` | Adjusts space below the section content. |

Both controls range from **0–100 px**, in **4 px** steps. The screenshot and package defaults use `32 px` for both. These controls adjust section spacing, rather than positioning individual images.

## Image blocks

Select an **Image** block in the left sidebar to open its settings. Each block has one image picker.

<!-- Screenshot slot: Image block settings. Add the file to docs/public/images/en/ to enable the image reference below. -->
<!-- ![Scatter gallery Image block settings](/images/en/scatter-gallery-image.png) -->

| Setting | Screenshot state | Purpose |
| --- | --- | --- |
| **Image** | Select and Explore free images controls shown; no selected image thumbnail visible | Chooses the image for this gallery slot. |

### Select and replace images

1. Click **Image → Select** to choose an existing file or upload an image, or explore free images.
2. Check its crop, subject placement and clarity in the storefront preview.
3. Open the remaining Image blocks to replace their placeholders.

Slots have different proportions. Use a coordinated mix of landscape and portrait imagery, leaving space around important subjects for cropping. Review desktop and mobile presentation rather than relying on the original image dimensions alone.

### Limits, ordering and removal

- You can add up to **8 Image blocks**. At 8/8, no additional block can be added.
- Drag blocks in the left sidebar to reorder them. Images follow the block order into the preset slots.
- Blocks have no separate position, size or link controls; the section layout determines the staggered arrangement.
- **Remove block** removes only the selected block, without deleting the original image from Shopify's file library.

This version retains eight layout slots and displays placeholders in unconfigured slots. After removing an Image block, check the order of subsequent images and any remaining placeholders.

## Custom CSS

The **Custom CSS** panel at the bottom of the screenshot is a section styling control provided by the theme editor. After adding local styles, check the staggered layout, image crops and text placement across screen sizes.

## Save and check

- Replace the eight slots' placeholders with the intended images.
- Leave Statement blank for no heading, or check its readability at the screenshot's Medium desktop/mobile sizes after entering text.
- Configure decoration separately and ensure it does not obscure important content.
- Verify the image-to-slot arrangement after reordering blocks.
- Check desktop/mobile cropping, spacing and the `32 px` top and bottom padding.
