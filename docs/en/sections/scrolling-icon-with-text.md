# Scrolling icon with text

Scrolling icon with text repeats icons and short phrases in a horizontal scrolling band for promotions, service benefits or brand messages. Section settings control the overall motion and layout. Each **Item** block has its own text, icon and optional link.

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open the template you want to edit and choose **Add section → Scrolling icon with text** in the page content area.
3. Set the color scheme, scrolling direction, speed, text sizes and spacing.
4. Expand the section and click **Add Item**. Enter text and optionally select an icon and link.
5. Add other Items and drag to reorder them. Preview desktop and mobile, then click **Save**.

This section cannot be added to header, footer or custom overlay groups. The theme repeats existing content to create a continuous loop; you do not need to add duplicate blocks to extend the band.

## Color scheme

Choose the global color scheme for the section. The screenshot selects the third scheme thumbnail in the first row.

Click **Edit scheme** to adjust the scheme. Global scheme changes affect other areas using it, so check text and icon contrast against the background throughout those areas.

## Scrolling

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Direction** | **Right to left** | Moves the content from right to left or left to right. |
| **Speed** | **Normal** | Sets the scrolling speed: Slow, Normal or Fast. |
| **Horizontal spacing** | `8 px` | Adjusts horizontal spacing between adjacent content groups. |
| **Desktop text size** | **Large** | Sets the scrolling text size on desktop. |
| **Mobile text size** | **Text: Large** | Sets the scrolling text size independently on mobile. |
| **Bar vertical padding** | `24 px` | Adjusts internal space above and below the scrolling content. |
| **Separator** | `*` | Adds a separator character after each content item. |
| **Pause on hover** | **Enabled** | Pauses scrolling when hovered on devices that support hover. |

### Direction, speed and spacing

**Direction** offers **Right to left** and **Left to right**.

For **Speed**, Slow provides more reading time, Normal is the standard pace and Fast creates stronger motion. Allow enough time for longer text. Touch devices do not support persistent hover, so check mobile readability separately.

**Horizontal spacing** ranges from **0–120 px**, in **4 px** steps. The screenshot uses `8 px`; the package default is `40 px`. This controls spacing between content groups, rather than the gap between an icon and its text within an Item.

### Desktop and mobile text sizes

**Desktop text size** options: **Extra small, Small, Medium, Large, Extra large, 2X large, 3X large and 4X large**.

**Mobile text size** options: **Heading: Large, Text: Extra large, Heading: Medium, Text: Large, Heading: Small, Text: Default, Heading: Extra small and Text: Small**.

The screenshot's **Large** and **Text: Large** match the respective package defaults. After adjusting sizes, check that long phrases do not occupy too much of the scrolling band.

### Internal padding and separator

**Bar vertical padding** ranges from **0–48 px**, in **2 px** steps. Both the screenshot and package default use `24 px`. It controls internal band spacing separately from the section Padding below.

The screenshot uses `*` for **Separator**. Enter another short character or leave it blank to hide the separator. This text character is independent of the section divider lines under Layout.

## Layout

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Section width** | **Full width** | Chooses full width or the fixed page content width. |
| **Show divider** | **Disabled** | Controls divider lines above and below the scrolling band. |

**Full width** uses a full-width layout; **Fixed width** follows the page content width. The screenshot selects Full width, while the package default is Fixed width.

Enable Show divider to display top and bottom divider lines. Disabling it does not remove the `*` character configured under Separator.

## Padding

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Padding top** | `0 px` | Adjusts space above the section content. |
| **Padding bottom** | `0 px` | Adjusts space below the section content. |

Both controls range from **0–100 px**, in **4 px** steps. The screenshot uses `0 px` for both; the package defaults are `32 px` each. Setting these to zero does not remove the internal Bar vertical padding.

## Item blocks

Each **Item** represents one content group. Select an existing Item in the left sidebar to edit it, or click **Add Item** to create another.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Title** | `NEW IN 50% Discount` | Sets the text for this item. |
| **Image icon** | No selected image thumbnail visible | Selects or uploads an image as a custom icon. |
| **Icon** | **None** | Chooses a built-in theme icon; None disables the built-in icon. |
| **Layout** | **Horizontal** | Sets the arrangement of the icon and text within this Item. |
| **Link** | Empty, showing the paste-link-or-search placeholder | Optionally sets a destination for this item. |

### Text and icons

Keep **Title** concise. An Item with a blank Title is not displayed.

Click **Image icon → Select** to choose or upload an image, or explore free images. When an image icon is set, it takes precedence over the built-in Icon selection.

**Icon** options include None, Package, Truck, Airplane, Gift, Tag, Currency, Phone, Chat, Calendar, Clock, Globe, Location, Check, Heart, Leaf, Acorn, Lightning, Water off, Smiley and Stool. The screenshot selects None, while the package default is Check. With None selected and no Image icon set, the item displays text only.

### Arrangement and links

- **Horizontal**: places the icon and text side by side. This matches the screenshot and package default.
- **Vertical**: stacks the icon and text. It changes the internal Item layout, not the horizontal scrolling direction of the band.
- **Link**: choose or enter a product, collection, page or other destination. A configured link makes the item clickable; leaving it blank provides no navigation.

Drag Items in the left sidebar to change their order. **Remove block** at the bottom of the settings removes only the current Item.

## Custom CSS

The **Custom CSS** panel at the bottom of the screenshot is a section styling control provided by the theme editor. Use the text size, spacing, width and padding controls first. After adding CSS, check the mobile layout and loop continuity.

## Save and check

- Confirm content scrolls right to left at Normal speed without noticeable gaps or jumps across multiple cycles.
- Review the `8 px` spacing and desktop/mobile text sizes with your actual copy.
- Check the `*` separators and keep section divider lines disabled.
- Confirm the full-width layout, `24 px` internal padding and `0 px` section padding.
- Test hover pause on desktop and readability on mobile.
- Verify each Item's icon, arrangement, link and order.
