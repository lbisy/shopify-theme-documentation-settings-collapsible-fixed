# Toast

A toast is a temporary status message used for success, warning, error, or informational feedback. The **Toast** settings control its shape, position, duration, editor preview, and shadow.

## Open the Toast settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Open **Theme settings > Toast**.

![Toast settings and storefront preview](/images/en/settings/toast.png)

The example above uses an `8 px` radius, appears at the top center, dismisses after `3 s`, and uses a soft shadow with a slight downward offset.

## Display and timing

These settings control the toast shape, location, duration, and theme-editor preview.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Toast radius** | `8 px` | Roundness of the toast corners. Smaller values look sharper; larger values look softer and more rounded. |
| **Position** | **Top center** | Places the toast at the center of the top edge of the viewport. |
| **Auto-dismiss (seconds)** | `3 s` | How long a storefront toast remains visible before it closes automatically. |
| **Preview** | **Off** | Selects which toast type is displayed in the theme editor. **Off** hides the preview. |
| **Keep preview visible until dismissed** | **On** | Keeps the editor preview visible until it is closed manually, making visual inspection easier. |

**Preview** and **Keep preview visible until dismissed** affect only the theme editor. Storefront duration is controlled by **Auto-dismiss (seconds)**. A `3 s` duration suits short messages; use more time when the message is longer or requires a decision.

With **Top center**, verify that the toast does not cover the announcement bar, navigation, search, cart controls, or mobile safe areas.

## Shadow

Shadow settings help the toast remain visible over changing page backgrounds.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Toast shadow opacity** | `10%` | Visibility of the shadow. At `0%`, the shadow is disabled. |
| **Toast shadow horizontal offset** | `0 px` | Moves the shadow right with positive values and left with negative values. |
| **Toast shadow vertical offset** | `4 px` | Moves the shadow down with positive values and up with negative values. |
| **Toast shadow blur** | `16 px` | Softness and spread of the shadow edge. Higher values create a softer, wider shadow. |

Set opacity first, then adjust offsets and blur. The screenshot values create a centered, subtle elevation without a heavy outline. Test the shadow on both light and dark page backgrounds.

## Colors and message types

Toast colors come from **Theme settings > Colors > Feedback messages**. Each message type has its own background and foreground colors:

- Success
- Warning
- Error
- Information

Make sure the text and icons remain readable for every type. Do not rely on color alone to communicate meaning; pair the color with clear wording and, where available, an appropriate icon.

## Recommended adjustment order

1. Set the toast radius and position.
2. Choose an auto-dismiss duration that allows the message to be read.
3. Select a preview type and keep it visible while styling.
4. Set shadow opacity before offsets and blur.
5. Review all feedback-message colors.
6. Test desktop and mobile placement, then turn Preview back to **Off**.

The screenshot values (`8 px`, **Top center**, `3 s`, and a `10% / 0 px / 4 px / 16 px` shadow) are a balanced starting point for short, lightweight notifications.

## Save and test

Click **Save**, then trigger each toast type and check:

- The toast does not cover navigation or important actions.
- Short and long messages have enough time to be read.
- Text, icons, and close controls have sufficient contrast.
- The toast fits within narrow mobile screens and safe areas.
- The shadow remains subtle on light and dark backgrounds.
- Success, warning, error, and informational messages are easy to distinguish.
- Keyboard and screen-reader users can perceive important feedback.
