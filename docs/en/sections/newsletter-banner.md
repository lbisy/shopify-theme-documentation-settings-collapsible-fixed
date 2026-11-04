# Newsletter Banner

The **Newsletter Banner** combines a heading, supporting copy, and email form with an optional background image and localized blur overlay. Place it near the end of a homepage, blog, or long content page.

![Newsletter Banner settings and storefront preview](/images/en/newsletter-banner.png)

## Add the section

Open a template, click **Add section > Newsletter Banner**, enter the headings and placeholder, add an optional background and blur overlay, adjust spacing, and click **Save**. The form is built in; no blocks are required.

## Copy and color

- **Color Scheme**: background, headings, input, button, focus, and feedback colors.
- **Heading size** and **Heading**
- **Subtitle size** and **Subtitle**
- **Input Placeholder**

State the real subscription value without promising an unavailable offer or fixed frequency. Placeholder text must match the current language but must not replace a field label, privacy notice, or consent information.

## Background image

Choose a high-resolution image with a safe area behind text and the form, or leave it blank for a solid scheme background.

- **Background image fit**: **Cover (fill frame)** fills the banner but can crop edges.
- **Background image position**: for example, **Center**.

Recheck position whenever fit, container size, or device width changes.

## Blur overlay

The localized blur improves readability over detailed images but does not replace proper contrast.

- **Enable blur overlay**
- **Blur radius** in `px`
- **Blur width / height** in percent
- **Horizontal / Vertical blur position** in percent

Start with a low radius. Size the overlay for wrapped titles, form states, and feedback, then test desktop, tablet, and mobile alignment.

## Privacy and submission

Explain email use, link to the privacy policy, obtain marketing consent where required, and never preselect consent. Test valid, invalid, existing, and new addresses and verify both feedback and the actual Shopify marketing record. Provide unsubscribe options in all later marketing emails.

## Example

| Setting | Example |
| --- | --- |
| Heading | `Subscribe for new products and content updates` |
| Heading / Subtitle size | `XL` / `3XL` |
| Background fit / position | `Cover` / `Center` |
| Placeholder | `Enter your email address` |
| Blur | On; `12 px`; `60% / 80%`; `50% / 50%` |
| Padding | `32 px / 32 px` |

## Before publishing

Replace and translate all copy; verify image rights, crop, fit, and position; align the blur to every content state; check contrast; test empty, invalid, valid, duplicate, network-error, and success states; confirm the Shopify record; test keyboard and mobile soft-keyboard behavior; review privacy and consent; verify Custom CSS isolation; then save and complete a real subscription.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/newsletter-banner.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Newsletter banner

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Font

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Heading<br>`heading` | inline_richtext | Stay in the loop | — |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-xl | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Subtitle<br>`subtitle` | inline_richtext | News, stories, and updates | — |
| Background image<br>`background_image` | image_picker | Not declared | — |
| Background image fit<br>`background_image_fit` | select | cover | Cover (fill frame) (`cover`); Contain (show full image) (`contain`) |
| Background image position<br>`background_image_position` | select | center | Center (`center`); Top (`top`); Bottom (`bottom`); Left (`left`); Right (`right`); Top left (`top left`); Top right (`top right`); Bottom left (`bottom left`); Bottom right (`bottom right`) |
| Input placeholder<br>`placeholder` | text | Enter your email address | — |

### Blur overlay

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Enable blur overlay<br>`enable_blur_overlay` | checkbox | true | — |
| Blur radius<br>`blur_radius` | range | 12 | 0–40 px; step 1 |
| Blur width<br>`blur_mask_width` | range | 60 | 10–100 %; step 5 |
| Blur height<br>`blur_mask_height` | range | 80 | 10–100 %; step 5 |
| Horizontal blur position<br>`blur_position_x` | range | 50 | 0–100 %; step 5 |
| Vertical blur position<br>`blur_position_y` | range | 50 | 0–100 %; step 5 |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
