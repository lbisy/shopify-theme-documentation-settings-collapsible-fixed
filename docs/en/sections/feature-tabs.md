<!-- unlinked-document:start
文档显示状态：未在主页或目录中显示，且未被其他页面有效引用。
核对说明：已注释的目录入口和页面链接不计入有效引用；已排除构建的页面不作为引用来源。
保留正文供后续维护，此标记仅作为源码注释。
unlinked-document:end -->

# Feature tabs

Feature tabs pairs numbered markers on a shared image with feature descriptions and tabs. Use it to explain product origins, production, texture or everyday use. Each **Item** block defines one marker, description and tab, with an optional product link.

## Example preview

![Feature tabs image markers, feature description and tab navigation example](/images/en/feature-tabs.png)

The screenshot shows the section within a product template, with the marked image on the left and feature content and tabs on the right. It has **4 Items**:

| Number | Label |
| --- | --- |
| 01 | Origin |
| 02 | Process |
| 03 | Texture |
| 04 | Ritual |

**Origin** is selected, the counter reads `01 / 04`, and the heading is `From seed to serum.`. The selected tab row and its corresponding marker are highlighted. Select another tab to view its Item content.

Feature image is not selected in the screenshot, so the left area displays a decorative placeholder. The botanical illustration on the right is the default decoration displayed with Show decoration enabled; it is configured separately from the main image.

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open a home, product or standard page template and choose **Add section → Feature tabs**. The screenshot uses a product template.
3. Set the color scheme and heading size, then choose a Feature image.
4. Click **Add Item**, enter its Label, Heading and Text, and position its marker.
5. Optionally select a Product link for each Item. Add other Items as needed, up to **6**.
6. Configure decoration and padding. Preview desktop and mobile, then click **Save**.

## General

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Color scheme** | Second scheme thumbnail in the first row selected | Sets the section's global color scheme. |
| **Heading size** | **Extra large** | Sets the main heading size in the Item content area. |
| **Feature image** | No selected image thumbnail visible | Chooses the shared image behind all markers. |
| **Show decoration** | **Enabled** | Controls the decorative illustration in the content area. |
| **Decorative image** | No selected image thumbnail visible | Replaces the default botanical illustration with a custom image. |

### Color scheme and heading size

Click **Edit scheme** to change the selected scheme. Changes affect other areas using it. Check contrast for selected tabs, markers and body text against their backgrounds.

Heading size offers **Extra small, Small, Medium, Large, Extra large, 2X large, 3X large and 4X large**. The screenshot's Extra large matches the package default. It controls the main feature heading, rather than tab labels or a separate mobile heading setting; the theme adapts its display to screen width.

### Main image and decoration

Use **Feature image → Select** to choose or upload an image, or explore free images. Markers overlay this shared image. After replacing it, reposition each Item's marker.

**Show decoration** is enabled in the screenshot, matching the default. If Decorative image is unset, the default botanical illustration is used. Selecting a custom image replaces it. Decoration is shown from tablet width upward and hidden on narrower screens. Disable the toggle to hide it.

Feature image supplies the marked visual; Decorative image is an additional illustration in the content area.

## Padding

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Padding top** | `32 px` | Adjusts space above the section content. |
| **Padding bottom** | `32 px` | Adjusts space below the section content. |

Both controls range from **0–100 px**, in **4 px** steps. The screenshot and package defaults use `32 px` for both.

## Item blocks

Select an existing Item in the left sidebar or use **Add Item**. Each block supplies one numbered marker and one tab's content.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Product link** | Not selected; Select control shown | Optionally links the current image marker to a product. |
| **Marker horizontal position** | `22%` | Sets the marker's horizontal position on the image. |
| **Marker vertical position** | `28%` | Sets the marker's vertical position on the image. |
| **Label** | `Origin` | Sets the tab label and the eyebrow above the active description. |
| **Heading** | `From seed to serum.` | Sets the feature heading for this Item. |
| **Text** | Example copy below | Adds the detailed feature description, with rich-text formatting. |

### Product link and marker position

Product link associates the marker with a product destination. It does not replace the shared Feature image or automatically fill Label, Heading or Text. Without a selected product, as in the screenshot, the number is a visual marker. With a product selected, the corresponding marker links to that product. Use the tab list to browse feature descriptions.

Both position controls range from **0–100%**, in **1%** steps:

- Increasing **Marker horizontal position** moves the marker to the right.
- Increasing **Marker vertical position** moves the marker downward.

The first Item uses `22%` horizontal and `28%` vertical, matching the package defaults. Coordinates are independent for each Item. Avoid overlapping markers or obscuring important subjects, and recheck positions on mobile.

### Label, heading and text

**Label** is a short plain-text field, set to Origin in the screenshot. It appears in the tab row and as the uppercase eyebrow ORIGIN above the active content.

**Heading** supports inline formatting such as bold, italic and links. The screenshot's Text reads:

> Share a concise benefit, ingredient story, or ritual step that helps customers understand why this detail matters.

Text supports rich-text paragraphs, lists, bold, italic and links. Keep each Item focused on one feature, and review longer copy within the two-column layout.

### Reorder and remove Items

- Drag Items in the left sidebar to change the tab order. Numbers follow the display order.
- After reordering, check marker coordinates against the corresponding content.
- You can add up to **6 Items**; markers do not require separate blocks.
- **Remove block** removes only the selected Item.

## Custom CSS and removing the section

**Custom CSS** is a section styling control provided by the theme editor. After adding local styles, check the main image, markers, active tabs and mobile text layout.

**Remove section** removes the entire Feature tabs section and its Item blocks from the current template. To remove a single feature, use that Item's Remove block action.

## Save and check

- Replace the placeholder with your main image and position every marker.
- Match Origin, Process, Texture and Ritual to the correct markers and descriptions.
- Check that content, counter and marker highlighting update when switching tabs.
- Test product destinations for linked markers; unconfigured markers are not product links.
- Review the default botanical or custom decoration at supported screen widths.
- Check the Extra large heading and `32 px` top and bottom padding on desktop and mobile.
