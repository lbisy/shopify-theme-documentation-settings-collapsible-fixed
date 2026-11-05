<!-- unlinked-document:start
文档显示状态：未在主页或目录中显示，且未被其他页面有效引用。
核对说明：已注释的目录入口和页面链接不计入有效引用；已排除构建的页面不作为引用来源。
保留正文供后续维护，此标记仅作为源码注释。
unlinked-document:end -->

# Mood finder

Mood finder guides customers toward products through moods or everyday needs. Selecting an option on the wheel updates the recommended product and copy on the right. Section settings control shared text, colors and decoration. Each **Mood** block defines an option's image, phrase and associated product.

## Example preview

![Mood finder wheel, recommended product and section settings example](/images/en/mood-finder.png)

The screenshot uses a product template, with introductory text on the left, a four-part wheel in the center and a recommendation card on the right. It contains **4 Mood blocks**. **Add Mood (4/4)** indicates that the block limit has been reached.

| Wheel position | Eyebrow | Phrase |
| --- | --- | --- |
| Top left | Energized | Brighten the look |
| Top right | Glow | Quiet radiance |
| Bottom left | Comfort | Grounded warmth |
| Bottom right | Clarity | Fresh focus |

**Energized** is selected. Its card shows **BALM · RESTORE** and `Example product 1`. Product is not selected in the Mood block screenshot, so the line drawing and example name are placeholders. Select a real product for each option before publishing.

Select other wheel options to switch recommendation cards. The introductory copy on the left belongs to the section and remains shared across the Moods.

## Add and configure the section

1. Go to **Shopify admin → Online Store → Themes → Customize**.
2. Open a home, product or standard page template and choose **Add section → Mood finder**. The screenshot uses a product template.
3. Configure the color scheme, eyebrow, heading, supporting text and bottom caption.
4. Click **Add Mood** and set its texture image, eyebrow, phrase and product.
5. Enter the recommendation card's tag line and description for each Mood. Add up to **4 Mood blocks**.
6. Configure decoration and padding. Preview desktop and mobile, then click **Save**.

## General

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Color scheme** | Second scheme thumbnail in the first row selected | Chooses the section's global color scheme. |
| **Eyebrow** | `Skin mood finder` | Sets the short label above the section heading, displayed in uppercase. |
| **Heading** | `What are you in the mood for?` | Sets the section heading, with inline rich-text formatting. |
| **Heading size** | **Extra large** | Adjusts the section heading size. |
| **Subtext** | Two paragraphs shown below | Adds supporting copy under the heading, with rich-text formatting. |
| **Caption** | `Choose your mood. We'll do the rest.` | Sets the short caption at the bottom of the section. |
| **Show decoration** | **Enabled** | Controls the botanical illustration. |
| **Decoration image** | No selected image thumbnail visible | Replaces the default botanical illustration with a custom image. |

### Color scheme and heading

Click **Edit scheme** to change the selected scheme. Changes also affect other areas using it. Review contrast for the selected option, text and recommendation card.

Eyebrow is plain text. Heading supports inline formatting such as bold, italic and links. Heading size offers **Extra small, Small, Medium, Large, Extra large, 2X large, 3X large and 4X large**. The screenshot's Extra large matches the package default. This setting controls the section heading rather than the recommended product's name.

### Supporting text and caption

The screenshot's Subtext contains two paragraphs:

> Find your skin's moment.
>
> Choose what you need today.

Subtext supports rich-text paragraphs and lists. Caption is a separate plain-text field displayed at the bottom. Clear a field if its copy is not needed.

### Decoration

Show decoration is enabled in the screenshot, matching the default. Without a Decoration image, the default botanical illustration is used. A custom image replaces it. Decoration appears from tablet width upward and is hidden on narrower screens. Turn the toggle off to hide it.

Decoration image and each Mood's Texture image serve different purposes: the former decorates the overall section, while the latter fills an individual wheel option.

## Mood blocks

Select an existing **Mood** in the left sidebar. Each block configures one wheel option and its recommendation card.

| Setting | Current screenshot value | Purpose |
| --- | --- | --- |
| **Texture image** | No selected image thumbnail visible | Sets the texture or scene image for this wheel option. |
| **Eyebrow** | `Energized` | Sets the option's short label, displayed in uppercase. |
| **Phrase** | `Brighten the look` | Adds a short phrase below the label, with inline formatting. |
| **Product** | Not selected; Select control shown | Chooses the product recommended for this mood. |
| **Tag line** | `Balm · Restore` | Sets a short label on the recommendation card. |
| **Description** | Empty | Adds a custom multiline plain-text description to the card. |

### Wheel imagery, label and phrase

Use **Texture image → Select** to choose or upload an image, or explore free images. Without an image, the theme displays decorative placeholder artwork. Check subject cropping and label readability within the wheel segment.

The block Eyebrow controls the option label independently of the section Eyebrow. Phrase supports bold, italic and links. Keep it short to avoid excessive wrapping inside the wheel.

### Recommended product and card content

Selecting **Product** supplies the recommendation card's product name, featured image and destination. It does not automatically fill the wheel phrase or replace Texture image.

**Tag line** appears above the product name. The screenshot enters `Balm · Restore`, displayed as **BALM · RESTORE** on the card.

**Description** is custom copy for this Mood. It is separate from the section Subtext and does not automatically read the product's description. With a real product selected, leaving it blank omits this custom description; enter the copy you want to display.

With no product selected and Description empty, as in the screenshot, the theme displays sample copy:

> A gentle daily formula with plant-based hydrators selected for comfort and balance.

The card link falls back to the all-products page when no product is selected. Once configured, it opens the selected product. Test each card's arrow link.

### Limits, ordering and removal

- Add up to **4 Mood blocks**. At 4/4, no additional block can be added.
- After dragging blocks to reorder them, check their wheel positions and associated cards.
- **Remove block** removes only the selected option, without deleting products or image files from Shopify admin.

## Padding

The supplied screenshot does not show the Padding controls. The package provides these settings farther down the section panel:

| Setting | Package default | Range and purpose |
| --- | --- | --- |
| **Padding top** | `32 px` | Top spacing, 0–100 px in 4 px steps. |
| **Padding bottom** | `32 px` | Bottom spacing, 0–100 px in 4 px steps. |

## Save and check

- Verify all four wheel options' labels and imagery, replacing placeholders.
- Check the section Eyebrow, Heading, Subtext and Caption in their intended positions.
- Select each mood and confirm its active state, product, tag line and description update together.
- Select real products for every Mood, replacing Example product content and testing destinations.
- Enter custom card Descriptions as needed instead of relying on product descriptions to populate them.
- Review text readability and responsive decoration on desktop and mobile.
