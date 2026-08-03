# Product cards

The **Product cards** settings control product image ratio, border, corner radius, and shadow across collection pages, search results, featured product grids, and product recommendations.

## Open the Product cards settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Open **Theme settings > Product cards**.

![Product cards settings and storefront preview](/images/en/settings/product-cards.png)

The example above adapts each card to its product image, uses an `8 px` corner radius, and displays no border or shadow.

## Image

The image setting controls the shape of the product media area.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Image ratio** | **Adapt to image** | Preserves each source image's aspect ratio and minimizes cropping. |

**Adapt to image** is useful when product compositions vary or when showing the complete image is more important than keeping every card the same height. If source images have different aspect ratios, image areas—and the vertical position of titles, prices, badges, and buttons—may not align across a row.

For a more uniform grid, prepare primary product images with consistent dimensions, aspect ratios, subject scale, and background treatment. Preview any fixed ratio before using it because image edges may be cropped.

## Border

Border settings define the product card outline and corner shape.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Card border thickness** | `0 px` | Width of the card outline. At `0 px`, the border is hidden. |
| **Card radius** | `8 px` | Roundness of the card corners. Smaller values look sharper; larger values look softer and more rounded. |

When the border is disabled, cards rely on spacing, background contrast, or shadow for separation. Border color comes from the active color scheme. Check that rounded corners do not clip product images, badges, quick-action controls, or focus rings.

## Shadow

Shadow settings can add depth and visually separate cards from the page.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Card shadow opacity** | `0%` | Visibility of the shadow. At `0%`, the shadow is disabled. |
| **Card shadow horizontal offset** | `0 px` | Moves the shadow right with positive values and left with negative values. |
| **Card shadow vertical offset** | `0 px` | Moves the shadow down with positive values and up with negative values. |
| **Card shadow blur** | `0 px` | Softness of the shadow edge. Higher values create a softer, wider shadow. |

Set opacity first. When opacity is `0%`, the offsets and blur have no visible effect. Product grids show many cards at once, so use low-opacity shadows and restrained offsets to avoid making the page feel crowded.

## Visual consistency and product content

Coordinate the card radius with buttons, inputs, dialogs, and other cards. Also review the complete card content, not only the image:

- Long product titles and vendor names
- Regular prices, sale prices, and compare-at prices
- Sale, sold-out, and custom badges
- Color swatches and quick-add controls
- Hover media and keyboard focus indicators

Test light and dark color schemes separately. A borderless card that works on one background may need more contrast on another.

## Recommended adjustment order

1. Choose the image ratio.
2. Set the border thickness and corner radius.
3. Decide whether the design needs a shadow.
4. If needed, set opacity before offsets and blur.
5. Check product content and interactive controls.
6. Preview collection, search, featured, and recommendation grids on desktop and mobile.

The screenshot values (**Adapt to image**, `0 px`, `8 px`, and no shadow) are a balanced starting point for a clean, borderless product grid.

## Save and test

Click **Save**, then check:

- Product images remain clear and important details are not cropped.
- Cards align acceptably when source image ratios differ.
- Long titles, prices, badges, swatches, and buttons fit correctly.
- Rounded corners do not clip images, controls, or focus rings.
- Desktop and mobile grids have comfortable spacing.
- Light and dark color schemes provide enough card separation.
- Collection pages, search results, featured products, and recommendations all display correctly.
