# Icon with Text

Icon with text combines icons, headings and descriptions in a multi-column section for shipping, payment reassurance and customer service information. Section settings control columns, spacing, icon sizes, alignment and the bottom wave. Each **Item** block has its own title, description, icon and optional link.

![Icon with Text settings and storefront preview](/images/en/icon-with-text.jpg)

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open the template you want to edit and choose **Add section → Icon with text**.
3. Set the color scheme, carousel behavior and desktop/mobile columns.
4. Expand the section and click **Add Item**. Enter a title and description and choose an icon for each item.
5. Adjust direction, icon sizes, alignment and spacing. Enable the bottom wave if needed.
6. Drag Items to reorder them. Preview desktop and mobile, then click **Save**.

The screenshots show three Items: **Free shipping**, **Secure checkout** and **Here for you**, displayed in three desktop columns.

## Color scheme

Choose the global color scheme for the section. The screenshot selects the second scheme thumbnail in the first row.

Click **Edit scheme** to change the selected scheme. Changes also affect other areas using that scheme. Check icon, title and description contrast against the background.

## Carousel

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Enable carousel** | **Disabled** | Controls whether Items are browsed as a carousel. |

When disabled, Items follow the configured column layout. When enabled, content is browsed as a carousel. The screenshot displays all three Items in one desktop row. If you enable the carousel, test navigation and confirm that every Item can be reached on desktop and mobile.

## Layout

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Desktop columns** | **3 columns** | Sets the desktop Item count per row: 2, 3 or 4 columns. |
| **Mobile columns** | **1 column** | Sets the mobile Item count per row: 1 or 2 columns. |
| **Item gap** | `48 px` | Sets spacing between separate Items. |

Item gap ranges from **8–80 px**, in **4 px** steps. The screenshot uses `48 px`; the package default is `32 px`. More columns leave less room for each Item, so check wrapping with longer descriptions.

## Icon and text

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Direction** | **Vertical** | Arranges the icon and text within each Item. |
| **Icon size** | `64 px` | Sets the desktop icon size. |
| **Icon size mobile** | `56 px` | Sets the mobile icon size independently. |
| **Icon and text gap** | `40 px` | Sets spacing between an Item's icon and text area. |
| **Alignment** | **Left** | Aligns content to the left or center. |

### Direction and alignment

- **Vertical** places the icon above the text, as shown in the screenshot.
- **Horizontal** places the icon and text side by side.
- **Left** aligns content to the left, matching the screenshot's icons and text.
- **Center** centers the content.

Direction and Alignment are independent. Vertical does not require centered content: the screenshot uses **Vertical + Left**.

### Icon sizes and internal spacing

Icon size and Icon size mobile both range from **20–96 px**, in **2 px** steps. The screenshot uses `64 px` and `56 px`; the package defaults are `56 px` and `48 px`, respectively.

Icon and text gap ranges from **4–48 px**, in **2 px** steps. The screenshot uses `40 px`; the package default is `16 px`. With Vertical selected, this is vertical spacing; with Horizontal selected, it is horizontal spacing. It is separate from Item gap, which controls spacing between different Items.

The screenshot selects Left alignment, while the package default is Center. After changing direction, alignment or text styles, review each icon-and-text arrangement.

## Bottom wave

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Show bottom wave** | **Enabled** | Displays a decorative wave at the bottom of the section. |
| **Wave color scheme** | Second scheme thumbnail in the first row selected | Chooses the color scheme for the bottom wave. |

The screenshot enables the wave; the package default is disabled. Wave color scheme is independent of the section's Color scheme. Use the corresponding **Edit scheme** link to adjust its colors.

Check the wave transition against the next section's background. In the screenshot, Icon with text sits above the footer, so review that boundary together.

## Padding

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Padding top** | `100 px` | Adjusts space above the section content. |
| **Padding bottom** | `100 px` | Adjusts space below the section content. |

Both controls range from **0–100 px**, in **4 px** steps. The screenshot uses `100 px` for both; the package defaults are `32 px` each. Larger padding gives the content more space, but also check mobile section height and the bottom wave.

## Item blocks

Each **Item** contains an icon, a title and a description. Select an existing Item in the left sidebar to edit it, or click **Add Item** to create another.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Title** | `Free shipping` | Sets the Item title, with inline rich-text formatting. |
| **Description** | `Complimentary shipping on orders over $99.` | Adds supporting copy beneath the title, with inline rich-text formatting. |
| **Icon** | **Truck** | Chooses a built-in theme icon. |
| **Image icon** | No selected image thumbnail visible | Selects or uploads a custom icon image. |
| **Link** | Empty, showing the paste-link-or-search placeholder | Optionally sets a destination for the Item. |

### Title and description

Title and Description support toolbar formatting such as bold, italic and links. Keep titles concise and use descriptions for service details. Shipping thresholds and support hours should match the store's actual policies.

The screenshots show these three messages:

| Title | Description |
| --- | --- |
| **Free shipping** | Complimentary shipping on orders over $99. |
| **Secure checkout** | Safe, simple, and secure payment every time. |
| **Here for you** | Our care team is available 7 days a week. |

### Built-in icons and custom images

**Icon** offers built-in choices such as Truck, Shield check and Hand heart. Select None to omit the built-in icon. The selected Free shipping Item uses Truck, matching its shipping message.

Use **Image icon → Select** to choose or upload an image, or explore free images. When set, Image icon takes precedence over the built-in Icon selection. Keep icon styles and visual sizes consistent, and check clarity at the screenshot's `64 px` desktop and `56 px` mobile sizes.

### Links and block management

Use **Link** to select or enter a shipping policy, service information or other destination. A configured link makes the Item clickable. The screenshot leaves it empty, providing no navigation.

- Drag Items in the left sidebar to change their order.
- Click **Add Item** to add another service message.
- **Remove block** at the bottom of the block settings removes only the selected Item.

## Custom CSS and removing the section

**Custom CSS** is a section styling control provided by the theme editor. Use the existing column, size, spacing and alignment settings first. After adding CSS, check desktop, mobile and carousel layouts.

**Remove section** removes the entire Icon with text section and its Item blocks from the current template. To remove one Item, use that block's Remove block action.

## Save and check

- Confirm three desktop columns, one mobile column, a `48 px` Item gap and a disabled carousel.
- Place icons above the text with Left alignment, using `64 px` desktop and `56 px` mobile sizes.
- Review the `40 px` icon-and-text gap and description wrapping.
- Match each title and description to its icon, and test any configured links.
- Enable the bottom wave and check its color transition into the next section.
- Review the `100 px` top and bottom padding on desktop and mobile.
