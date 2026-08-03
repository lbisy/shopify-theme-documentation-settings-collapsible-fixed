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
