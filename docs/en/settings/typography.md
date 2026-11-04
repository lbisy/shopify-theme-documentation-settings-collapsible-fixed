# Typography

The **Typography** settings control the store's fonts, text hierarchy, spacing, and global type scale. Configure these values while watching the storefront preview so headings and body copy remain consistent across desktop and mobile.

## Open the Typography settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the current theme and click **Customize**.
3. Open **Theme settings > Typography**.

![Typography settings and storefront preview](/images/en/settings/typography.png)

::: tip Live preview
Keep the preview visible while adjusting typography. Use the desktop and mobile preview buttons to check wrapping, spacing, and readability before saving.
:::

## Fonts

Choose the base font for headings and body text. The screenshot uses **Inter** for both.

| Setting | Applies to | Value shown |
| --- | --- | --- |
| **Heading > Font** | Page titles, section headings, product titles, and other prominent text | `Inter` |
| **Body > Font** | Paragraphs, navigation, buttons, labels, and product information | `Inter` |

Using one font for both groups creates a clean, consistent look. For more contrast, choose a distinctive heading font and a highly readable body font. If the store contains Chinese text, confirm that the chosen font includes Chinese glyphs or falls back cleanly to a compatible system font.

## Heading

The **Heading** group controls the appearance of all major headings.

| Setting | What it changes | Value shown |
| --- | --- | --- |
| **Weight** | Stroke thickness and visual emphasis | `Bold` |
| **Line height** | Vertical space between lines in multiline headings | `1.2` |
| **Letter spacing** | Space between heading characters | `Slightly tight` |
| **Text transform** | Automatic uppercase, lowercase, or capitalization behavior | `None` |

A bold weight and slightly tight spacing work well for large editorial headings. After changing these values, check long product names and multiline hero text for crowding or awkward wrapping.

## Subtitle

The **Subtitle** group styles supporting headings and short lead-in text.

| Setting | What it changes | Value shown |
| --- | --- | --- |
| **Font family** | Uses the heading font or body font | `Heading font` |
| **Weight** | Subtitle emphasis | `Medium` |
| **Line height** | Vertical spacing for multiline subtitles | `1.4` |
| **Letter spacing** | Space between subtitle characters | `Normal` |
| **Text transform** | Automatic capitalization behavior | `None` |

Subtitles should be visibly secondary to headings but strong enough to introduce a section. Avoid making subtitle weight and scale identical to the main heading.

## Body

The **Body** group controls the base size and spacing used by paragraphs and supporting interface text.

| Setting | What it changes | Value shown |
| --- | --- | --- |
| **Font size (desktop)** | Base body size on larger screens | `16 px` |
| **Font size (mobile)** | Base body size on phones | `14 px` |
| **Line height** | Vertical spacing between body-text lines | `1.6` |
| **Letter spacing** | Space between body characters | `Normal` |
| **Text transform** | Automatic capitalization behavior | `None` |

Desktop and mobile sizes can be adjusted independently. Keep body copy comfortable to read, especially in product descriptions, articles, policy pages, and other long-form content. Avoid applying uppercase to paragraphs; reserve it for short labels when needed.

## Scale

Scale controls resize heading and body systems proportionally after their base settings are established.

| Setting | What it changes | Value shown |
| --- | --- | --- |
| **Heading scale** | All heading sizes | `100%` |
| **Body scale** | Body and related text sizes | `100%` |

`100%` preserves the theme's default proportions. Increase or decrease scale only after choosing fonts, base sizes, weights, and line heights; otherwise several adjustments can compound and make text unexpectedly large or small.

## Recommended adjustment order

1. Select the heading and body fonts.
2. Set heading weight, line height, letter spacing, and text transform.
3. Configure the subtitle hierarchy.
4. Set desktop and mobile body sizes.
5. Fine-tune the heading and body scales.
6. Review representative pages in desktop and mobile previews.

::: info Starting point
The values shown in the screenshots provide a balanced starting point, but they are not mandatory. Adjust them to match the selected fonts, brand style, and amount of content.
:::

## Save and verify

Click **Save**, then check:

- Page titles, section headings, subtitles, and body text have a clear hierarchy.
- Long headings wrap cleanly without overlapping nearby content.
- Product descriptions and article text are comfortable to read.
- Navigation, buttons, and product-card labels remain fully visible.
- Desktop and mobile sizes both look balanced.
- Chinese and English characters display correctly with the selected fonts.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `config/settings_schema.json` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → Theme settings → Typography

### Font family

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Font<br>`type_header_font` | font_picker | instrument_sans_n4 | — |

### Body

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Font<br>`type_body_font` | font_picker | instrument_sans_n4 | — |

### Typography

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Weight<br>`heading_weight` | select | 500 | Regular (`400`); Medium (`500`); Bold (`700`) |
| Line height<br>`heading_line_height` | range | 1.0 | 1–2 ; step 0.1 |
| Letter spacing<br>`heading_letter_spacing` | select | -0.02em | Tighter (`-0.05em`); Tight (`-0.02em`); Slightly tight (`-0.01em`); Normal (`0em`); Wide (`0.02em`); Wider (`0.05em`); Widest (`0.1em`) |
| Text transform<br>`heading_text_transform` | select | none | None (`none`); Uppercase (`uppercase`); Lowercase (`lowercase`); Capitalize (`capitalize`) |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Font family<br>`subtitle_font_source` | select | heading | Heading font (`heading`); Body font (`body`) |
| Weight<br>`subtitle_weight` | select | 500 | Regular (`400`); Medium (`500`); Bold (`700`) |
| Line height<br>`subtitle_line_height` | range | 1.4 | 1–2 ; step 0.1 |
| Letter spacing<br>`subtitle_letter_spacing` | select | 0em | Tighter (`-0.05em`); Tight (`-0.02em`); Slightly tight (`-0.01em`); Normal (`0em`); Wide (`0.02em`); Wider (`0.05em`); Widest (`0.1em`) |
| Text transform<br>`subtitle_text_transform` | select | none | None (`none`); Uppercase (`uppercase`); Lowercase (`lowercase`); Capitalize (`capitalize`) |

### Body

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Font size (desktop)<br>`body_font_size` | range | 16 | 16–32 px; step 1 |
| Font size (mobile)<br>`body_font_size_mobile` | range | 14 | 14–32 px; step 1 |
| Line height<br>`body_line_height` | range | 1.4 | 1–2 ; step 0.1 |
| Letter spacing<br>`body_letter_spacing` | select | 0em | Tighter (`-0.05em`); Tight (`-0.02em`); Slightly tight (`-0.01em`); Normal (`0em`); Wide (`0.02em`); Wider (`0.05em`); Widest (`0.1em`) |
| Text transform<br>`body_text_transform` | select | none | None (`none`); Uppercase (`uppercase`); Lowercase (`lowercase`); Capitalize (`capitalize`) |

### Scale

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading scale<br>`heading_scale` | range | 100 | 100–150 %; step — |
| Body scale<br>`body_scale` | range | 100 | 100–150 %; step — |

<!-- latest-schema:end -->
