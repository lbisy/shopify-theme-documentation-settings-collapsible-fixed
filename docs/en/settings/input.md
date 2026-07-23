# Input

The **Input** settings define the dimensions, border, radius, and shadow of fields used in search, contact forms, newsletter signup, customer details, and other text-entry areas.

## Open the Input settings

Go to **Shopify admin > Online Store > Themes**, click **Customize**, then open **Theme settings > Input**.

![Input settings](/images/en/settings/input.svg)

## Spacing

**Input horizontal padding** controls the space between text and the left and right edges. Higher values feel more open; lower values conserve space. Check long placeholders and fields containing icons.

**Input vertical padding** controls field height and the touch target. Keep enough vertical space for comfortable use on mobile.

## Border

**Input border thickness** sets the outline width. Thin borders suit most forms; thick borders increase separation; `0px` requires the background or shadow to make the field recognizable. Border color comes from the scheme's **Input border** setting.

**Input radius** controls corner roundness. Coordinate it with button radius so search, signup, and form layouts feel consistent.

## Shadow

- **Input shadow opacity** controls visibility; `0%` disables the shadow.
- **Input shadow horizontal offset** moves it right or left.
- **Input shadow vertical offset** moves it down or up.
- **Input shadow blur** controls edge softness; `0px` creates a hard edge.

Set opacity first. A shadow should not replace a clear input boundary, and a strong shadow can make a field look like a button.

## Colors and focus

Under **Theme settings > Colors**, configure:

- **Input text**
- **Input background**
- **Input border**
- **Input placeholder**

Configure focus-ring width and offset under **Theme settings > Focus**.

::: info Accessibility
Placeholder text must not replace a visible field label. Ensure adequate contrast among entered text, placeholder text, borders, and backgrounds.
:::

## Style ideas

- **Minimal form**: moderate padding, thin border, subtle radius, no shadow.
- **Soft rounded**: larger radius, generous vertical padding, and a faint blurred shadow.
- **Defined outline**: visible border, small radius, no shadow.
- **Slightly raised**: thin border with a low-opacity, lightly offset shadow.

## Save and test

Click **Save**. Check search, short and multiline form fields, newsletter layouts, light and dark schemes, keyboard focus, errors, autofill, long text, multiple languages, and mobile tapping. Finally, submit real test entries to verify input, clearing, autofill, validation, and error states.
