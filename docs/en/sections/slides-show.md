# Slideshow

Slideshow presents brand imagery, promotional copy and action links. Section settings control the shared height, text sizes, autoplay and padding. Edit each **Slide** block separately to configure its images and content.

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open the template you want to edit and choose **Add section → Slideshow** in the page content area.
3. Select **Slideshow** to configure the section settings below.
4. Expand the section and click **Add Slide** to configure images, text and links for each slide.
5. Drag Slide blocks to change their order. Preview desktop and mobile, then click **Save**.

This section cannot be added to header, footer or custom overlay groups.

## Color scheme and height

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Color scheme** | First scheme thumbnail selected | Chooses the global color scheme for the slideshow. |
| **Section height** | **Full screen** | Sets how the slideshow height is determined. |

Click **Edit scheme** to change the selected scheme. Changes also affect other areas using the same scheme.

**Section height** options:

- **Adapt to media**: adjusts the section height to the media proportions.
- **Small**: a smaller height.
- **Medium**: a medium height.
- **Large**: a larger height.
- **Full screen**: a full-screen presentation; also the package default.

With Full screen selected, check image cropping and make sure headings and links remain visible at different screen heights.

## Font and heading

**Font** is a settings group label in the screenshot; it does not have a separate input control.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Heading size** | **4X large** | Sets the slide headline size on desktop. |
| **Mobile heading size** | **4X large** | Sets the slide headline size independently on mobile. |

Both controls offer **Extra small, Small, Medium, Large, Extra large, 2X large, 3X large and 4X large**.

The screenshot sets both sizes to **4X large**. The package defaults are **3X large** and **Extra large**, respectively. These differ from the current screenshot configuration. With large sizes and long headlines, check mobile wrapping and possible overlap with other content.

## Subtitle

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Subtitle size** | **Default** | Adjusts the size of supporting text on the slides. |

Options are **Extra large, Large, Default and Small**. The screenshot uses **Default**; the package default is **Extra large**.

## Autoplay

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Autoplay slides** | **Enabled** | Switches slides automatically. Disable it to stop automatic switching. |
| **Autoplay speed** | `5 s` | Sets the interval between automatic slide changes. |

Autoplay speed ranges from **3–10 seconds**, in **1-second** steps. Higher values keep each slide visible longer. Both the enabled state and the `5 s` interval in the screenshot match the package defaults.

Add multiple Slide blocks when testing autoplay, and allow enough time for visitors to read the content.

## Padding

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Padding top** | `32 px` | Adjusts the space above the section content. |
| **Padding bottom** | `32 px` | Adjusts the space below the section content. |

Use the sliders or numeric inputs to adjust either value from **0–100 px**, in **4 px** steps. Both screenshot values match the package defaults of `32 px`.

## Individual slide content

Each **Slide** block represents one slide and has its own images, headline, body copy and link. The selected **Slide** in the screenshot's left sidebar is the block currently being edited. Its content changes do not replace the content of other Slide blocks.

### Add and open a Slide

1. Expand **Slideshow** in the editor's left sidebar.
2. Click **Add Slide** to create a slide, or select an existing **Slide** to edit it.
3. Configure **Slide image** and **Slide content** in the right panel.
4. Preview the current slide, then click **Save** at the top right.

### Slide image

| Setting | Screenshot state | Purpose |
| --- | --- | --- |
| **Desktop image** | Select and Explore free images controls shown; no selected image thumbnail visible | Chooses the main image for desktop. |
| **Mobile image** | Select and Explore free images controls shown; no selected image thumbnail visible | Optionally chooses a separate image for narrower screens. |

Click **Select** to choose or upload an image, or use **Explore free images** to find imagery. If Mobile image is not set, the desktop image is used everywhere. When set, the mobile image is used below the desktop breakpoint.

A landscape composition can suit desktop, while a separate mobile composition can work better on narrow screens. Check subject cropping on both and leave clear space for overlaid text. The section's **Section height** also affects the image presentation and cropping.

### Headline and link position

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Headline and link position** | **Top left** | Positions the headline and action link together. |
| **Headline** | `Ceylune, a quieter ritual` | Sets the headline for this slide. |

Headline supports inline formatting such as bold, italic and links. Adjust headline sizes for all slides under **Slideshow section settings → Heading size / Mobile heading size**, rather than within an individual Slide.

The available positions are listed below. Body text position uses the same options.

| Top | Middle | Bottom |
| --- | --- | --- |
| **Top left** | **Center left** | **Bottom left** |
| **Top center** | **Center** | **Bottom center** |
| **Top right** | **Center right** | **Bottom right** |

### Body text

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Body text position** | **Bottom left** | Positions the body copy independently of the headline and link. |
| **Body text** | Example copy below | Adds supporting copy for this slide, with rich-text formatting. |

The screenshot contains:

> **THE DAILY RITUAL**
>
> Thoughtfully formulated skincare for slower, more intentional moments.

To reproduce this layout, add a short bold label followed by a separate paragraph in the same Body text editor. The toolbar provides text styles, bold, italic, links and lists; a separate label block is not required.

The screenshot places the headline and link in the top-left area and the body copy in the bottom-left area. After changing positions or adding copy, check for overlap, especially with large mobile headlines.

### Action link

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Link label** | `Shop the collection` | Sets the visible action text, with inline rich-text formatting. |
| **Link URL** | `/collections/all` | Sets the destination; this address opens the all-products page. |

The link follows **Headline and link position**. Choose a collection, product or page appropriate to each slide, and make sure the label describes its destination.

The screenshot's `/collections/all` is the current configuration. The package declares `/collections` as the default destination. After saving, test the link in the storefront preview to confirm the intended page opens.

### Reorder and remove Slides

- Drag Slide blocks in the left sidebar to change the playback order.
- Use **Add Slide** to create additional slides, each with its own images and copy.
- Click **Remove block** at the bottom of a Slide's settings to remove only that slide.
- Removing a Slide and removing the entire Slideshow section are separate actions. After removing a slide, check the remaining order and autoplay behavior.

## Custom CSS and removing the section

The **Custom CSS** panel at the bottom of the screenshot is a section styling control provided by the theme editor. Use it for local styling adjustments.

**Remove section** removes the entire slideshow and its Slide blocks from the current template. Before saving, check whether other pages also use the template.

## Save and check

- Review image cropping at full-screen height on desktop and mobile.
- Ensure the `4X large` headings remain readable without overlapping body text or links.
- Confirm supporting text is readable with **Default** selected.
- Check that multiple slides autoplay in order at `5 s` intervals.
- Test every slide link.
- Confirm that the `32 px` top and bottom padding works with adjacent sections.
