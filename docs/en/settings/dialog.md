# Dialog

The **Dialog** settings define the border, corner radius, and shadow of modal interfaces such as quick view, search overlays, newsletter popups, and other dialogs. The exact components affected depend on the features used on each page.

## Open the Dialog settings

Go to **Shopify admin > Online Store > Themes**, click **Customize**, then open **Theme settings > Dialog**.

![Dialog settings](/images/en/settings/dialog.svg)

## Border

**Dialog border thickness** sets the outline width. Small values create a light edge, larger values make the boundary more obvious, and `0px` removes the border. If the dialog and page have similar backgrounds, use a border or shadow to separate them. Border color usually comes from the active color scheme.

**Dialog radius** controls corner roundness. Small values feel structured and formal; medium values balance crispness and softness; large values create a modern, friendly appearance.

::: tip Recommendation
Coordinate dialog radius with buttons, inputs, and cards, although the values do not need to be identical.
:::

## Shadow

- **Dialog shadow opacity** controls visibility; `0%` disables the shadow.
- **Dialog shadow horizontal offset** moves the shadow right or left. A small value or `0px` usually looks naturally centered.
- **Dialog shadow vertical offset** moves it down or up. A slight downward offset often creates a natural floating effect.
- **Dialog shadow blur** controls edge softness; `0px` creates a hard shadow.

Set opacity first because all other shadow values are invisible at `0%`.

::: warning Note
Opacity, offset, and blur work together. A very dark or wide shadow can make the page feel heavy and obscure nearby content.
:::

## Style ideas

- **Minimal**: thin border, moderate radius, and no shadow.
- **Soft floating**: moderate radius, low opacity, slight downward offset, and generous blur.
- **Defined outline**: visible border, small radius, and little or no shadow.
- **Modern rounded**: large radius, no border or a thin border, and a soft shadow.

## Save and test

Click **Save**, then open every dialog used by the store. Check its boundary, radius, shadow, text, inputs, buttons, and close icon on light and dark schemes and on desktop and mobile. Use the keyboard to confirm focus enters the dialog, remains visible, and returns correctly after closing. Also test open, close, submit, and cancel actions.
