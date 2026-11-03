# Featured products

Featured products organizes collections into tabs so customers can switch between their products. Section settings control product counts, columns, navigation and the brand marquee. Each **Collection** block defines one tab's collection, heading and supporting copy.

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open the template you want to edit and choose **Add section → Featured products** in the page content area.
3. Set the color scheme, heading size, product count and layout.
4. Expand the section and click **Add Collection**. Select a collection and enter its heading and supporting copy.
5. Add other Collection blocks as needed and drag to reorder the tabs.
6. Configure the brand marquee and padding. Preview desktop and mobile, then click **Save**.

This section cannot be added to header, footer or custom overlay groups.

## General

**Color scheme** selects the global scheme for the section. The screenshot selects the second scheme thumbnail in the first row.

Click **Edit scheme** to change the selected scheme. Changes also affect other areas using it. Check contrast for selected tabs, product information and buttons against their backgrounds.

## Font and heading

**Font** is a settings group label in the screenshot, without a separate input control.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Heading size** | **2X large** | Sets the collection tab heading size. |

Options are **Extra small, Small, Medium, Large, Extra large, 2X large, 3X large and 4X large**. The screenshot matches the package default.

## Product settings

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Maximum items** | `8` | Limits how many products are displayed from each collection. |
| **Items per row on desktop** | `4` | Sets the desktop product column count. |
| **Items per row on mobile** | `2` | Sets the mobile column count: 1 or 2. |
| **Show navigation** | **Disabled** | Controls product browsing navigation. |
| **Show pagination** | **Disabled** | Controls carousel pagination or position indicators. |
| **Show view all button** | **Enabled** | Shows a link to the corresponding collection. |
| **Desktop tab header behavior** | **Wrap to multiple lines** | Controls how desktop tab headings handle limited width. |

**Maximum items** ranges from **2–12**, in steps of **1**. **Items per row on desktop** ranges from **2–4**, in steps of **1**. If a collection has fewer available products than the limit, only those products are displayed.

Two mobile columns show more products at once. Check long product names, prices and badges for crowding. Columns control layout density; Maximum items controls the total display limit for each collection.

**Desktop tab header behavior** options:

- **Wrap to multiple lines**: wraps tabs onto additional lines when there are many tabs or long labels.
- **Horizontal drag/scroll**: lets customers browse tabs horizontally by dragging or scrolling.

The screenshot enables **Show view all button**, while the package default is disabled. All other screenshot values in this table match the defaults. Even with navigation and pagination disabled, check that View all appears and links to the correct active collection.

## Brand marquee

Brand adds a decorative scrolling text band alongside the product presentation. The screenshot's brand text editor is empty, so the brand marquee is not displayed. Direction, speed and other settings can remain configured; enter text to preview their effect.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Brand name** | Empty | Sets repeated brand text, with inline rich-text formatting. |
| **Brand marquee direction** | **Right to left** | Sets the direction of brand text movement. |
| **Pause marquee on hover** | **Enabled** | Pauses the marquee when hovered on devices that support hover. |
| **Brand marquee speed** | **Normal** | Sets the speed: Slow, Normal or Fast. |
| **Brand marquee spacing** | `64 px` | Adjusts spacing between repeated brand text. |
| **Brand marquee height** | `380 px` | Sets the decorative band's vertical space; text size scales subtly with height. |

Direction offers **Right to left** and **Left to right**. Spacing ranges from **24–160 px**, in **4 px** steps. Height ranges from **120–420 px**, in **10 px** steps.

The package default for Brand name is `Your brand`, unlike the empty screenshot value. All other screenshot values in this table match the defaults. Keep text concise so decorative motion does not distract from products. Touch devices do not support persistent hover, so review their speed and readability separately.

## Padding

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Padding top** | `32 px` | Adjusts space above the section content. |
| **Padding bottom** | `32 px` | Adjusts space below the section content. |

Both controls range from **0–100 px**, in **4 px** steps. The screenshot and package defaults use `32 px` for both. Section padding is separate from the brand band's Brand marquee height.

## Collection blocks

Each **Collection** block represents one collection tab. Select an existing Collection in the left sidebar to edit it, or click **Add Collection** to create another.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Select collection** | **Face Masks** | Chooses the collection supplying this tab's products. |
| **Collection heading** | `Add On` | Sets a custom tab heading, with inline rich-text formatting. |
| **Collection content** | Empty | Adds supporting copy within the corresponding tab, with inline rich-text formatting. |

### Select the collection

Use **Select collection** to choose or replace a collection. The screenshot selects Face Masks. Changing the heading to Add On does not replace that collection or rename it in Shopify admin.

### Customize the tab heading

**Collection heading** takes precedence as the tab title. In the screenshot, the tab displays `Add On` while its products still come from Face Masks. Leave this field blank to use the selected collection's name.

Use the toolbar for bold, italic or link formatting. With longer headings, check wrapping or horizontal scrolling under Desktop tab header behavior.

### Add supporting copy

**Collection content** can briefly describe the selection or collection. The screenshot leaves it empty, so this copy is not displayed. The package supplies sample copy by default; clear it if it is not needed.

### Reorder and remove blocks

- Drag Collection blocks in the left sidebar to change the tab order.
- Click **Add Collection** to add another collection tab.
- **Remove block** at the bottom of the block settings removes only that tab from the section. It does not delete the collection or products from Shopify admin.

## Save and check

- Verify each tab's source collection; the screenshot example uses Add On as the heading and Face Masks as the collection.
- Confirm the limit of 8 products per collection, with 4 desktop columns and 2 mobile columns.
- Keep navigation and pagination disabled, with View all enabled and linking correctly.
- Check that multiple tabs wrap without obscuring products.
- Confirm the marquee is hidden with empty brand text; after entering text, test direction, speed, spacing and hover pause.
- Review the `32 px` top and bottom padding alongside adjacent sections.
