# Colors

The **Colors** settings create reusable color schemes for the storefront. Each scheme defines the colors used by backgrounds, text, borders, form inputs, buttons, badges, and feedback messages. Editing a scheme updates every section that uses it.

## Open the Colors settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the current theme and click **Customize**.
3. Open **Theme settings > Colors**.
4. Select the color scheme you want to edit, then click **Edit scheme**.

![Color schemes and storefront preview](/images/en/settings/colors.png)

::: warning Shared changes
Changing a scheme affects all sections that use that scheme. Check where it is assigned before making a major color change.
:::

## Manage color schemes

The scheme cards provide reusable palettes for different parts of the store. Use **Add Scheme** to create another palette when a page area needs a distinct visual treatment.

**Page background color scheme** sets the palette used behind sections and in areas without their own color scheme. Individual sections can select another scheme when the section settings support it.

Keep the number of schemes manageable. A practical setup might include a light content scheme, a dark brand scheme, and an accent scheme for promotional areas.

## General colors

General colors establish the base appearance of the selected scheme. The screenshots show the following Scheme 3 values:

| Setting | Purpose | Value shown |
| --- | --- | --- |
| **Background** | Base background used by the scheme | `#1B2900` |
| **Background gradient** | Optional gradient that replaces the solid background where supported | `No color chosen` |
| **Text color** | Main headings, body text, and supported icons | `#D5FF83` |
| **Border color** | Dividers, outlines, and component borders | `#111827` |
| **Focus ring color** | Keyboard-focus outline for interactive controls | `#1D4ED8` |

::: warning Background gradient
When a gradient is selected, it replaces **Background** at all applicable positions. Clear the gradient to return to the solid background color.
:::

Maintain strong contrast between text and background colors. The focus ring must also remain clearly visible so keyboard users can identify the active link, button, or input.

## Inputs

Input colors apply to search fields, contact forms, newsletter forms, and other text inputs.

| Setting | Purpose | Value shown |
| --- | --- | --- |
| **Input text** | Text entered by the customer | `#151515` |
| **Input background** | Input-field background | `#FFFFFF` |
| **Input border** | Default input outline | `#D6D6D6` |
| **Input placeholder** | Hint text shown before input | `#717171` |

Placeholder text should differ from entered text without becoming difficult to read. Test inputs in their default, focused, populated, validation-error, and disabled states.

## Primary button

Primary buttons represent the most important action on a page, such as **Add to cart**, **Buy now**, or **Submit**.

| Setting | Value shown |
| --- | --- |
| **Primary button background color** | `#F9FAFB` |
| **Primary button label color** | `#111827` |
| **Primary button border color** | `#F9FAFB` |

Primary buttons should be prominent within the scheme while keeping their labels easy to read.

## Secondary button

Secondary buttons support lower-priority actions such as **Learn more**, **Continue shopping**, or **Back**.

| Setting | Value shown |
| --- | --- |
| **Secondary button background color** | `Transparent` |
| **Secondary button label color** | `#FFFFFF` |
| **Secondary button border color** | `#F9FAFB` |

A transparent background creates an outline-style button. Check the label and border against every background where the scheme is used, including image-backed sections.

## Badges

Badge colors are used for compact product and status labels such as Sale, New, or Sold out.

| Setting | Value shown |
| --- | --- |
| **Badge background color** | `#1D4ED8` |
| **Badge label color** | `#FFFFFF` |
| **Badge border color** | `#1D4ED8` |

Badges are small, so use a simple, high-contrast combination and verify them against product images and card backgrounds.

## Feedback messages

Each feedback state has a background and foreground color. The foreground color is normally used for text, icons, and related outlines.

| State | Background | Foreground | Typical use |
| --- | --- | --- | --- |
| **Success** | `#ECFDF5` | `#065F46` | Completed actions and successful submissions |
| **Warning** | `#FFFBEB` | `#92400E` | Information that requires attention |
| **Error** | `#FEF2F2` | `#991B1B` | Failed actions, invalid fields, and blocking problems |
| **Info** | `#F4F4F5` | `#27272A` | General notices and supporting information |

::: info Accessibility
Do not communicate a status through color alone. Keep clear labels and status icons so success, warning, error, and information messages remain understandable to all visitors.
:::

## Remove a color scheme

**Remove color scheme** deletes the scheme currently being edited. Before removing it:

1. Confirm which sections use the scheme.
2. Assign a replacement scheme to those sections.
3. Record any color values you may need again.

Removal may not be directly reversible, so only remove a scheme after its dependencies have been checked.

## Recommended workflow

1. Choose or add a scheme for a clear purpose.
2. Set the background and text colors first.
3. Configure borders and the focus ring.
4. Style inputs, primary buttons, secondary buttons, and badges.
5. Configure all four feedback-message states.
6. Preview representative sections on desktop and mobile.
7. Click **Save** after checking contrast and component states.

Hex values can be copied between schemes to keep brand colors consistent. After saving, verify text, links, buttons, inputs, badges, messages, focus rings, and gradients everywhere the scheme is used.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `config/settings_schema.json` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → Theme settings → Colors

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| color_schemes<br>`color_schemes` | color_scheme_group | Not declared | — |

### color_schemes / Scheme fields

#### General colors

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Background<br>`background_color` | color | #f1f1f1 | — |
| Background gradient<br>`background_gradient_color` | color_background | Not declared | info: The background gradient will replace the background color at all applicable positions. |
| Text color<br>`text_color` | color | #263d29 | — |
| Border color<br>`border_color` | color | #263d29 | — |
| Focus ring color<br>`focus_ring_color` | color | #263d29 | — |

#### Inputs

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Input text<br>`input_text_color` | color | #263d29 | — |
| Input background<br>`input_background_color` | color | #FFFFFF | — |
| Input border<br>`input_border_color` | color | #677769 | — |
| Input placeholder<br>`input_placeholder_color` | color | #677769 | — |

#### Primary button

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Primary button background color<br>`primary_button_background_color` | color | #263d29 | — |
| Primary button label color<br>`primary_button_label_color` | color | #FFFFFF | — |
| Primary button border color<br>`primary_button_border_color` | color | #263d29 | — |

#### Secondary button

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Secondary button background color<br>`secondary_button_background_color` | color | #FFFFFF | — |
| Secondary button label color<br>`secondary_button_label_color` | color | #263d29 | — |
| Secondary button border color<br>`secondary_button_border_color` | color | #263d29 | — |

#### Badges

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Badge background color<br>`badge_background_color` | color | #FFFFFF | — |
| Badge label color<br>`badge_label_color` | color | #263d29 | — |
| Badge border color<br>`badge_border_color` | color | #263d29 | — |

#### Accent

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Accent color<br>`accent_color` | color | #D5FF83 | info: Used for highlights such as active slideshow pagination. |

#### Card surface

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Card background<br>`card_background_color` | color | #ffffff | — |

#### Feedback messages

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Success background color<br>`success_background_color` | color | #ECFDF5 | — |
| Success foreground color<br>`success_foreground_color` | color | #065F46 | — |
| Warning background color<br>`warning_background_color` | color | #FFFBEB | — |
| Warning foreground color<br>`warning_foreground_color` | color | #92400E | — |
| Error background color<br>`error_background_color` | color | #FEF2F2 | — |
| Error foreground color<br>`error_foreground_color` | color | #991B1B | — |
| Info background color<br>`info_background_color` | color | #F4F4F5 | — |
| Info foreground color<br>`info_foreground_color` | color | #27272A | — |

Role mapping: &#123;"background": &#123;"solid": "background_color", "gradient": "background_gradient_color"&#125;, "icons": "text_color", "links": "text_color", "on_primary_button": "primary_button_label_color", "on_secondary_button": "secondary_button_label_color", "primary_button": "primary_button_background_color", "primary_button_border": "primary_button_border_color", "secondary_button": "secondary_button_background_color", "secondary_button_border": "secondary_button_border_color", "text": "text_color"&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Page background color scheme<br>`page_canvas_color_scheme` | color_scheme | scheme-2 | info: Used behind sections and for areas without their own color scheme. |

<!-- latest-schema:end -->
