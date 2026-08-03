# Button

The **Button** settings control spacing, borders, corner radius, and shadows for buttons throughout the store, including **Add to cart**, **Buy now**, **Submit**, and **Learn more**.

## Open the Button settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Open **Theme settings > Button**.

![Button settings and storefront preview](/images/en/settings/button.png)

The example above uses comfortable padding, a thin border, an `8 px` corner radius, and no shadow.

## Spacing

Spacing controls the space between a button label and its edges.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Button horizontal padding** | `24 px` | Space to the left and right of the label. Increase it for wider buttons or reduce it for a more compact layout. |
| **Button vertical padding** | `12 px` | Space above and below the label. Increase it for taller, more prominent buttons and larger touch targets. |

Check long labels and layouts that place multiple buttons in one row. On mobile, keep enough vertical padding for comfortable tapping.

## Border

Border settings define the button outline and corner shape.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Button border thickness** | `1 px` | Width of the outline. Set it to `0 px` to remove the border. |
| **Button radius** | `8 px` | Roundness of the corners. Smaller values look sharper; larger values look softer and more rounded. |

Button border colors come from the active color scheme under **Theme settings > Colors**. For a consistent interface, coordinate the radius with inputs, dialogs, product cards, and other interactive elements.

## Shadow

Shadow settings can make buttons appear raised from the page.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Button shadow opacity** | `0%` | Visibility of the shadow. At `0%`, the shadow is disabled. |
| **Button shadow horizontal offset** | `0 px` | Moves the shadow right with positive values and left with negative values. |
| **Button shadow vertical offset** | `0 px` | Moves the shadow down with positive values and up with negative values. |
| **Button shadow blur** | `0 px` | Softness of the shadow edge. Higher values create a softer shadow. |

Set opacity first. When opacity is `0%`, the offsets and blur have no visible effect. If you add a shadow, begin with low opacity and small offsets, then preview it on both light and dark backgrounds.

## Colors and focus

Button geometry is configured here, while button colors are configured in **Theme settings > Colors**:

- **Primary button background color**, **label color**, and **border color**
- **Secondary button background color**, **label color**, and **border color**

Keep label contrast readable in every color scheme. Also verify that the keyboard focus ring remains clearly visible and is not obscured by the button border or shadow.

## Recommended adjustment order

1. Set horizontal and vertical padding.
2. Adjust border thickness and corner radius.
3. Decide whether the design needs a shadow.
4. Check primary and secondary button colors.
5. Preview hover, focus, and disabled states.
6. Review the result on desktop and mobile.

The values shown in the screenshot (`24 px`, `12 px`, `1 px`, `8 px`, and no shadow) are a balanced starting point for a clean, flat button style.

## Save and test

Click **Save**, then check:

- Primary and secondary buttons look consistent.
- Long labels fit without clipping or awkward wrapping.
- Buttons are easy to tap and do not overflow on mobile.
- Borders remain visible on light and dark color schemes.
- Hover, focus, and disabled states are distinguishable.
- Critical actions such as adding to cart, checkout, and form submission still work correctly.
