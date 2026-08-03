# Input

The **Input** settings define the spacing, border, corner radius, and shadow shared by search fields, contact forms, newsletter signup, customer details, and other text-entry controls.

## Open the Input settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the current theme and click **Customize**.
3. Open **Theme settings > Input**.

![Input settings and storefront preview](/images/en/settings/input.png)

The screenshot shows a clean input style with comfortable padding, a thin border, moderately rounded corners, and no shadow.

## Spacing

Spacing controls the space between input content and the field edges.

| Setting | What it changes | Value shown |
| --- | --- | --- |
| **Input horizontal padding** | Space on the left and right of text and icons | `16 px` |
| **Input vertical padding** | Space above and below the content; also affects field height | `12 px` |

Increase horizontal padding for a more open appearance, but check long placeholders and fields with leading or trailing icons. Vertical padding should provide a comfortable touch target on mobile without making compact forms unnecessarily tall.

## Border

Border settings control the field outline and corner shape.

| Setting | What it changes | Value shown |
| --- | --- | --- |
| **Input border thickness** | Width of the input outline | `1 px` |
| **Input radius** | Roundness of the four corners | `8 px` |

A `1 px` border clearly separates the input from its background without looking heavy. An `8 px` radius creates moderately rounded corners. Coordinate the input radius with button and dialog styling so forms feel consistent.

The border color is configured separately in **Theme settings > Colors > Input border**.

## Shadow

Shadow settings control the depth around input fields.

| Setting | What it changes | Value shown |
| --- | --- | --- |
| **Input shadow opacity** | Overall shadow visibility | `0%` |
| **Input shadow horizontal offset** | Moves the shadow left or right | `0 px` |
| **Input shadow vertical offset** | Moves the shadow up or down | `0 px` |
| **Input shadow blur** | Softens the shadow edge | `0 px` |

With opacity set to `0%`, the shadow is disabled and the offset and blur values have no visible effect. If a shadow is added, set a low opacity first, then adjust offset and blur. Avoid a heavy shadow that makes an input look like a button.

## Colors and focus

Input structure is configured on this page, while visual states are controlled elsewhere:

- **Theme settings > Colors**: Input text, Input background, Input border, and Input placeholder.
- **Theme settings > Focus**: Focus-ring width and offset.

::: info Accessibility
Placeholder text must not replace a visible field label. Maintain clear contrast among entered text, placeholder text, borders, and backgrounds, and keep the keyboard focus ring visible.
:::

## Recommended adjustment order

1. Set horizontal and vertical padding.
2. Choose border thickness and radius.
3. Decide whether the design needs a shadow.
4. Configure input colors in the active color schemes.
5. Check keyboard focus and validation states.
6. Preview forms on desktop and mobile.

The values shown in the screenshot are a balanced starting point for a minimal form style. Increase the radius for a softer look, or add a low-opacity blurred shadow for slight elevation.

## Save and test

Click **Save**, then verify:

- Search, contact, newsletter, customer, and checkout-related inputs are consistent.
- Placeholder text and entered text are fully visible.
- Input height remains comfortable on mobile.
- Icons do not overlap long text.
- Borders remain visible on light and dark color schemes.
- `Tab` navigation shows a clear focus ring.
- Error, autofill, disabled, and completed states remain understandable.

Finally, submit representative forms to confirm typing, clearing, autofill, validation, and error handling all work correctly.
