# Promise Section

The **Promise Section** combines an image, subtitle, heading, and expandable Accordion Items for ingredients, production, sustainability, animal policies, or service principles.

![Promise Section settings and storefront preview](/images/en/promise-section.png)

## Add the section

Open a template, click **Add section > Promise Section**, choose the image and headings, add one **Accordion Item** per promise, reorder the blocks, and click **Save**.

## Main settings

- **Color scheme**: background, headings, body, dividers, and arrows.
- **Image**: a relevant ingredient, production, nature, product, or brand scene.
- **Subtitle**: a short label such as `Our Promise`.
- **Heading** and **Heading size**
- **Padding Top / Bottom**

Replace image placeholders before launch. Use a sharp image with the subject in a crop-safe area and verify mobile image/text stacking. The image should support the promises rather than be unrelated decoration.

## Accordion Items

Each block has a short title and a detailed explanation. Reorder, hide, duplicate, or remove blocks in the left panel.

Use distinct titles and specific, verifiable explanations. Put the most important or frequently asked promise first, keep lengths reasonably similar, and do not hide information essential to purchase only inside an accordion.

Examples include:

- Responsible Beauty Commitment
- Honest & Transparent Process
- Gentle Yet Effective Formulas
- Thoughtfully Chosen Ingredients

Claims such as cruelty-free, sustainable, natural, or environmentally responsible must match actual policy and operations. Link to full policy details where useful.

## Interaction and accessibility

Customers should be able to expand and collapse by clicking the title or arrow and by focusing with `Tab` and pressing `Enter` or Space. The open state and arrow direction must remain clear. Test mouse, touch, and keyboard and ensure headings, body, dividers, and controls contrast with the background.

## Before publishing

Replace the image; proofread nonduplicate headings and details; expand and collapse every item; test long copy on desktop, tablet, and mobile; verify logical order, color contrast, spacing, image balance, and Custom CSS behavior; substantiate all brand, ingredient, environmental, and policy claims; then save and repeat the interaction on the storefront.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/promise-section.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Promise section

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Image<br>`image` | image_picker | Not declared | — |
| Subtitle<br>`subtitle` | inline_richtext | Our Promise | — |
| Heading<br>`heading` | inline_richtext | Thoughtfully Crafted for Your Skin | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Accordion item

`type`: `accordion_item`

#### Title

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`title_size` | select | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Title<br>`title` | inline_richtext | Accordion title | — |
| Content<br>`text` | richtext | &lt;p&gt;Accordion description text goes here.&lt;/p&gt; | — |

<!-- latest-schema:end -->
