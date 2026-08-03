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
