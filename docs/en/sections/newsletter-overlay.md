# Newsletter Overlay

The **Newsletter Overlay** displays a subscription invitation above the current page. It supports display conditions, delay, repeat interval, placement, feedback messages, an image, and reorderable Text, Heading, and Form blocks.

![Newsletter Overlay settings and storefront preview](/images/en/newsletter-overlay.png)

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

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/newsletter-overlay.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Newsletter overlay

Has presets for the Add section picker.

`enabled_on`: &#123;"groups": ["custom.overlay"]&#125;

`limit`: 1

### Display settings

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Display mode<br>`display_mode` | select | enable | Enable (`enable`); Test (`test`)<br>info: Test mode always opens the popup. |
| Show on home page<br>`show_in_home` | checkbox | true | — |
| Show for visitors<br>`show_for_visitor` | checkbox | true | — |
| Delay<br>`delay` | range | 3 | 0–60 s; step 1 |
| Expire after<br>`expired` | range | 7 | 1–30 day; step 1 |
| Popup placement<br>`modal_placement` | select | bottom-right | Bottom left (`bottom-left`); Bottom right (`bottom-right`); Center (`center`) |

### Text and style

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Text alignment<br>`alignment` | text | left | — |
| Email placeholder<br>`placeholder` | text | Enter your email address | — |
| Success toast<br>`success_message` | text | Thanks for subscribing. | — |
| Error toast<br>`error_message` | text | Subscription failed. Please try again. | — |
| Left image<br>`image` | image_picker | Not declared | — |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Block: Text

`type`: `text`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Text<br>`text` | richtext | &lt;p&gt;First timer?&lt;/p&gt; | — |
| Text size<br>`body_text_size` | select | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |

### Block: Heading

`type`: `heading`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading<br>`heading` | inline_richtext | Sign up and get 20% off your first order | — |
| Heading size<br>`heading_text_size` | select | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

### Block: Form

`type`: `form`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

<!-- latest-schema:end -->
