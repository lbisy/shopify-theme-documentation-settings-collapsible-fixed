# Promotion Countdown

The **Promotion Countdown** displays remaining days, hours, minutes, and seconds with optional headings and a call-to-action button for launches, seasonal offers, member events, or reservation deadlines.

![Promotion Countdown settings and storefront preview](/images/en/promotion-countdown.png)

## Configure the section

- **Color Scheme**
- **Heading size** and **Heading**
- **Subtitle size** and **Sub Heading**
- **End Date**
- **Days / Hours / Minutes / Seconds Label**
- **Show CTA Button**, **CTA Text**, and **CTA Link**
- **Padding Top / Bottom**

Use this exact date format:

```text
YYYY-MM-DD HH:MM:SS
```

For example, `2027-01-15 20:00:00`.

::: warning Date and time
Verify the countdown on the actual storefront against the primary market's timezone. Past, empty, or malformed dates may not display correctly.
:::

Translate all four unit labels consistently and leave room for day counts longer than two digits. If the CTA is enabled, complete both text and link and make sure it leads to a page where the promised action can be completed.

The countdown, promotion rules, discount activation, and destination page must use the same deadline. Put inventory, regional restrictions, and detailed conditions on the campaign page rather than relying on the timer alone.

## Before publishing

Validate format, future date, timezone, units, long day counts, responsive headings, CTA, link destination, contrast, keyboard focus, number layout, and spacing. Test the state after expiration and plan to update or remove expired content, then save and complete the campaign journey.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/promotion-countdown.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Promotion countdown

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Font

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Heading<br>`heading` | inline_richtext | Something new is arriving | — |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-xl | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Subheading<br>`sub_heading` | inline_richtext | Coming soon | — |
| End date<br>`end_date` | text | 2026-12-31 23:59:59 | info: Format: YYYY-MM-DD HH:MM:SS (e.g., 2026-12-31 23:59:59) |
| Days label<br>`days_label` | text | Days | — |
| Hours label<br>`hours_label` | text | Hours | — |
| Minutes label<br>`minutes_label` | text | Minutes | — |
| Seconds label<br>`seconds_label` | text | Seconds | — |
| Show button<br>`show_cta` | checkbox | true | — |
| Button label<br>`cta_text` | text | Get Notification on Calendar | — |
| Button link<br>`cta_link` | url | Not declared | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
