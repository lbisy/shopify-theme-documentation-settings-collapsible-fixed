# Newsletter Overlay

The **Newsletter Overlay** displays a subscription invitation above the current page. It supports display conditions, delay, repeat interval, placement, feedback messages, an image, and reorderable Text, Heading, and Form blocks.

![Newsletter Overlay settings and storefront preview](/images/en/newsletter-overlay.svg)

Unlike a [Newsletter Banner](/en/sections/newsletter-banner), the overlay opens automatically. Both can be used, but avoid repeatedly asking the same visitor to subscribe.

## Open the settings

In **Online Store > Themes > Customize**, open **Overlay > Newsletter Overlay**, configure display rules, copy, image, and colors, arrange the blocks, then click **Save**. Because this is a shared overlay, test it on the homepage, product, collection, and blog pages.

## Display Settings

### Display mode

- **Enable** uses the configured page, visitor, delay, and expiration rules.
- **Test** keeps the popup open for styling and content review.

Always switch back to **Enable** before publishing.

### Audience and timing

- **Show on home page** permits the overlay on the homepage.
- **Show for visitors** enables it for qualifying visitors. Eligibility can depend on login, subscription status, and browser records.
- **Delay** sets how many seconds to wait. Start around `3–5 s` and test the actual storefront.
- **Expire after** controls how many days a dismissed or seen-popup record remains before the visitor can qualify again.
- **Popup placement** selects a desktop position such as **Bottom right**.

Test new, returning, dismissed, subscribed, logged-in, private-window, and cleared-site-data states. Avoid covering navigation, cart, chat, cookie notices, or mobile safe areas.

## Text and style

- **Text alignment**: typically `left`, `center`, or `right`.
- **Email placeholder**: a concise prompt, not a replacement for a proper label or consent explanation.
- **Success toast**: clearly confirm completion without promising an unconfigured benefit.
- **Error toast**: explain that submission failed and suggest checking the address or trying again.
- **Left image**: a compressed, relevant image; ensure the popup still makes sense when it is hidden or cropped on mobile.
- **Color scheme**: background, text, fields, buttons, close control, and feedback colors.

Check text, controls, status messages, and keyboard focus for adequate contrast.

## Content blocks

- **Text**: a short supporting label or message.
- **Heading**: the main subscription value or offer.
- **Form**: email input and submit button. Keep this block when collecting addresses.

A clear order is Text → Heading → Form. If auxiliary text is unnecessary, remove Text but retain Heading and Form.

## Subscription, offers, and privacy

Explain how email will be used and the approximate frequency. Provide the privacy policy and obtain marketing consent where required. Do not preselect consent or make dismissal difficult.

If offering a discount, state its scope, minimum spend, expiration, and exclusions, and verify delivery and redemption. Confirm the actual subscriber record in Shopify admin rather than relying only on the success toast. Marketing messages must include an unsubscribe method.

## Example

| Setting | Example |
| --- | --- |
| Display mode | `Enable` |
| Show on home page / for visitors | On / On |
| Delay | `5 s` |
| Expire after | `7 day` |
| Popup placement | `Bottom right` |
| Text alignment | `left` |
| Email placeholder | `Enter your email address` |
| Success toast | `You are subscribed. Thank you.` |
| Error toast | `Submission failed. Check your email and try again.` |
| Text | `First visit?` |
| Heading | `Subscribe for new products and updates` |
| Form | Visible |

## Before publishing

Return Test mode to Enable; test page scope, visitor states, real delay, dismissal and expiration, every placement, blocks and languages, empty/invalid/valid/duplicate emails, feedback and the Shopify subscriber record, any full discount flow, keyboard focus and return, mobile keyboard and scrolling, contrast, privacy and consent, then complete one real visitor subscription after saving.
