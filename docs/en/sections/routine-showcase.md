# Routine showcase

Routine showcase organizes products into steps, combining scene images, floating product images and shared introductory copy. Use it to present skincare routines, product pairings or a sequence of use. Section settings control the heading, background, button and autoplay. Each **Step** block has its own product, label and images.

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open the template you want to edit and choose **Add section → Routine showcase** in the page content area.
3. Set the color scheme, heading size, background and introductory copy.
4. Expand the section and click **Add Step**. Select a product and configure the step label and images.
5. Add other steps as needed and drag to reorder them. You can add up to **5 Step blocks**.
6. Configure the button, autoplay and padding. Preview desktop and mobile, then click **Save**.

This section cannot be added to header, footer or custom overlay groups.

<!-- To add screenshots: place the files in docs/public/images/en/, uncomment the corresponding image line below, and remove its screenshot placeholder callout. -->
<!-- ![Routine showcase color scheme, heading and background settings](/images/en/routine-showcase-settings.png) -->

::: info Screenshot placeholder: section settings
Add a settings panel screenshot showing Color scheme, Heading size, Background image, Eyebrow, Heading and Description here.
:::

## Color scheme

Choose the global color scheme for the section. The screenshot shows a blue selection border around the middle thumbnail in the second row.

Click **Edit scheme** to change the selected scheme. Changes affect other areas using that scheme, so review text and button contrast against the background throughout those areas.

## Font and section heading

**Font** is a settings group label in the screenshot, without a separate input control.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Heading size** | **Large** | Sets the section heading size. |
| **Background image** | No selected image thumbnail visible | Chooses the background for the whole section. |
| **Eyebrow** | `Ceylune` | Adds a short label or brand name above the heading. |
| **Heading** | `Serums & Treatments` | Sets the section heading. |
| **Description** | `Targeted care for balanced, luminous skin.` | Adds supporting copy below the heading. |

**Heading size** offers **Extra small, Small, Medium, Large, Extra large, 2X large, 3X large and 4X large**. The screenshot selects Large; the package default is Extra small. This controls visual size, not the HTML heading level.

Use **Background image → Select** to choose or upload an image, or explore free images. This is the overall section background, configured separately from each Step's scene and floating product images. Check cropping and text readability at different screen sizes.

Eyebrow and Heading support inline formatting such as bold, italic and links. Description supports rich-text paragraphs and lists. Keep copy concise to avoid an excessively tall introduction on mobile.

## Button

<!-- ![Routine showcase button, autoplay and padding settings](/images/en/routine-showcase-autoplay.png) -->

::: info Screenshot placeholder: button, autoplay and padding
Add a settings panel screenshot showing Button label, Button link, Autoplay steps, Autoplay interval and Padding here.
:::

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Button label** | `Shop serums` | Sets the section's action text, with inline rich-text formatting. |
| **Button link** | `/collections` | Sets the destination; the screenshot links to the collection list. |

Provide both clear action text and a valid destination. The screenshot uses Shop serums while linking to `/collections`. To send customers directly to a serum collection, choose that collection's link and test it in the preview.

## Step autoplay

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Autoplay steps** | **Enabled** | Switches displayed steps automatically. |
| **Autoplay interval (seconds)** | `5 s` | Sets the interval between automatic changes. |

The interval ranges from **3–10 seconds**, in **1-second** steps. Both the enabled state and `5 s` value match the package defaults. Add multiple Steps to test autoplay, and allow more time if your copy is longer.

## Padding

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Padding top** | `32 px` | Adjusts space above the section content. |
| **Padding bottom** | `32 px` | Adjusts space below the section content. |

Both controls range from **0–100 px**, in **4 px** steps. The screenshot and package defaults use `32 px` for both.

## Step blocks

Each **Step** represents one product step. Select an existing Step in the left sidebar or use **Add Step** to create another, up to 5.

<!-- ![Routine showcase Step block settings](/images/en/routine-showcase-step.png) -->

::: info Screenshot placeholder: Step block
Add a block settings screenshot showing Product, Step label, Arch scene image and Floating product image here.
:::

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Product** | Selected product displayed as `Revive Repair S…` | Chooses the product for this step. The screenshot truncates the name; open the selector to see it in full. |
| **Step label** | `Cleanse` | Sets the step label. |
| **Arch scene image** | A selected lifestyle portrait | Sets the scene image displayed in the arch. |
| **Floating product image** | A selected product bottle image | Sets the overlaid product image; falls back to the selected product's featured image when unset. |

### Product and step label

Use **Product** to select or replace the product for this step. Products are chosen independently per Step; a section-level collection selection is not required.

Keep **Step label** short, such as Cleanse in the screenshot. Check that the label, product and scene represent the same routine step. Changing the label does not rename the product.

### Arch scene image

Choose a lifestyle or portrait image relevant to the step. It appears in an arch-shaped area. Check that important subjects, faces and actions remain visible within the crop.

### Floating product image

The floating image is displayed at a fixed height. The panel recommends:

- A **transparent PNG**.
- A width-to-height ratio of approximately **1:2.5**.
- Dimensions of at least **640 × 1600 px**.
- A product that fills the canvas, with minimal surrounding whitespace.

Wider images look smaller at the same display height. If Floating product image is not set, the selected Product's featured image is used. Upload a separate transparent cutout for the Step when you need a cleaner product presentation.

### Reorder and remove Steps

- Drag Step blocks in the left sidebar to change the sequence.
- Click **Add Step** to add another step.
- **Remove block** at the bottom of the block settings removes only that step, without deleting the product from Shopify admin.

## Custom CSS and deleting the section

The **Custom CSS** panel at the bottom of the screenshot is a section styling control provided by the theme editor. After adding local styles, check image and text layouts on desktop and mobile.

**Remove section** removes the entire Routine showcase and its Step blocks from the current template. Before saving, check whether other pages also use that template.

## Save and check

- Verify the Ceylune eyebrow, Serums & Treatments heading and supporting copy.
- Confirm Shop serums opens the intended destination.
- Check that each Step uses the correct product, label and scene image.
- Review arch cropping and floating product clarity, avoiding excess image whitespace.
- Confirm multiple steps autoplay in the intended order at `5 s` intervals.
- Check desktop and mobile for overlaps and review the `32 px` top and bottom padding.
