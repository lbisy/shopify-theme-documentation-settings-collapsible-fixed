# Newsletter Banner

The **Newsletter Banner** combines a heading, supporting copy, and email form with an optional background image and localized blur overlay. Place it near the end of a homepage, blog, or long content page.

![Newsletter Banner settings and storefront preview](/images/en/newsletter-banner.svg)

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
