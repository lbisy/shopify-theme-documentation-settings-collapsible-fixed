# Button

The **Button** settings define the size, border, corner radius, and shadow of buttons throughout the store, including **Add to cart**, **Buy now**, **Submit**, and **Learn more**.

## Open the Button settings

Go to **Shopify admin > Online Store > Themes**, click **Customize**, then open **Theme settings > Button**.

![Button settings](/images/en/settings/button.svg)

## Spacing

**Button horizontal padding** controls the space to the left and right of a label. Higher values make buttons wider; lower values create a compact button. Check long labels and mobile layouts with multiple buttons in one row.

**Button vertical padding** controls the space above and below the label. Higher values create a taller, more prominent, and easier-to-tap button.

::: tip Recommendation
Keep a comfortable touch target, especially on mobile. Do not reduce vertical padding only to save space.
:::

## Border

**Button border thickness** controls the outline width. A thin border is subtle, a thick border creates emphasis, and `0px` removes the border. Its color comes from the active color scheme.

**Button radius** controls corner roundness. Small values look square and formal; medium values balance structure and softness; large values create a friendly, rounded style.

## Shadow

- **Button shadow opacity** controls visibility; `0%` disables the shadow.
- **Button shadow horizontal offset** moves it right with positive values and left with negative values.
- **Button shadow vertical offset** moves it down with positive values and up with negative values.
- **Button shadow blur** controls edge softness; `0px` creates a hard-edged shadow.

Set opacity first. If it is `0%`, the other shadow values have no visible effect.

::: warning Note
Very dark, highly offset, or heavily blurred shadows can reduce clarity. Test primary and secondary buttons on light and dark backgrounds and in hover, focus, and disabled states.
:::

## Style ideas

- **Flat and minimal**: moderate padding, thin border, subtle radius, and `0%` shadow.
- **Soft and rounded**: more vertical padding, larger radius, and a faint blurred shadow.
- **Strong outline**: small radius, visible border, and no shadow.
- **Raised emphasis**: moderate radius with a small offset and low-opacity shadow.

## Save and test

Click **Save**. Check that primary and secondary buttons feel consistent, long labels fit, mobile buttons remain easy to tap, borders and shadows work on every color scheme, and critical actions still work correctly.
