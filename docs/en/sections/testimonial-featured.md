# Featured Testimonials

The **Testimonial Featured** section displays customer reviews in a carousel with an optional hero image and floating information card.

![Featured Testimonials settings and storefront preview](/images/en/testimonial-featured.png)

## Add the section

Open a template, click **Add section > Testimonial Featured**, add the main image and optional floating card, add **Testimonial** blocks, configure automatic sliding, and click **Save**.

## Image and floating card

- **Color Scheme**
- **Image**
- **Show Floating Card**
- **Card Label**
- **Card Title**

Use an authorized product-use, brand, detail, or customer image with safe crop space. The layout must remain complete without an image, and review copy must remain real text rather than being embedded only in the image.

Keep floating-card copy short and relevant. Recheck its overlap whenever the image, language, or copy length changes, and turn it off when it has no meaningful content.

## Slider

- **Auto Slide**
- **Slide Delay** in seconds

Do not auto-slide a single testimonial. For multiple reviews, allow enough time to read each one; start around `5–6 s` for short copy and increase it for longer reviews. Controls and user interaction should not make reading difficult.

## Testimonial blocks

Each block can include rating, review copy, customer name, and identity information. Reorder, hide, duplicate, or remove blocks.

Use the real rating and preserve the customer's meaning. Minor corrections or excerpts must not change the conclusion or exaggerate results. Keep lengths similar to reduce carousel height shifts. Publish only authorized names or anonymized attribution and avoid unnecessary personal details.

Do not fabricate reviews, hide material relationships, or describe paid promotion as ordinary feedback. Beauty, health, performance, and earnings claims require substantiation and local advertising compliance. Remove order numbers, addresses, and contact information.

## Before publishing

Verify image rights, crop, and quality; testimonial publication permission; ratings, wording, attribution, and identity; remove defaults and sensitive data; check height changes among reviews; prevent floating-card overlap; allow enough delay; test pause/interaction behavior, carousel controls, keyboard, and touch; verify contrast, responsive layout, spacing, and Custom CSS; then save and browse every review on the storefront.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/testimonial-featured.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Featured testimonial

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading<br>`heading` | inline_richtext | Beyond clients. Trusted partners. | — |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

### Cards

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Top row card color scheme<br>`card_scheme_top` | color_scheme | scheme-1 | — |
| Bottom row card color scheme<br>`card_scheme_bottom` | color_scheme | scheme-2 | — |

### Marquee

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Marquee width<br>`marquee_width` | select | page | Page width (`page`); Full width (`full`) |
| Direction<br>`marquee_direction` | select | right_to_left | Right to left (`right_to_left`); Left to right (`left_to_right`) |
| Speed<br>`marquee_speed` | select | normal | Slow (`slow`); Normal (`normal`); Fast (`fast`) |
| Pause on hover<br>`marquee_pause_on_hover` | checkbox | true | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Testimonial

`type`: `testimonial`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Image<br>`image` | image_picker | Not declared | — |
| Show image<br>`show_image` | checkbox | true | — |
| Star rating<br>`rating` | range | 5 | 1–5 ; step 1 |
| Quote<br>`quote` | richtext | &lt;p&gt;Share a verified customer review that reflects a genuine product or shopping experience.&lt;/p&gt; | — |
| Author name<br>`author_name` | inline_richtext | Customer name | — |

<!-- latest-schema:end -->
