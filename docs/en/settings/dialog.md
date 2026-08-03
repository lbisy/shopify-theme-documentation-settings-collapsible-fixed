# Dialog

The **Dialog** settings control the border, corner radius, and shadow of modal interfaces such as quick view windows, search overlays, newsletter popups, and other dialogs. The exact components affected depend on the features enabled in the theme.

## Open the Dialog settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Open **Theme settings > Dialog**.

![Dialog settings and storefront preview](/images/en/settings/dialog.png)

The example above uses no visible border, a `12 px` corner radius, and a soft shadow with a slight downward offset.

## Border

Border settings define the dialog outline and corner shape.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Dialog border thickness** | `0 px` | Width of the dialog outline. At `0 px`, the border is hidden. |
| **Dialog radius** | `12 px` | Roundness of the dialog corners. Smaller values look sharper; larger values look softer and more rounded. |

When the border is disabled, use sufficient contrast or a shadow to separate the dialog from the page. Border color comes from the active color scheme. Coordinate the radius with buttons, inputs, product cards, and other interface elements for a consistent visual language.

## Shadow

Shadow settings help the dialog appear above the page content.

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Dialog shadow opacity** | `10%` | Visibility of the shadow. At `0%`, the shadow is disabled. |
| **Dialog shadow horizontal offset** | `0 px` | Moves the shadow right with positive values and left with negative values. |
| **Dialog shadow vertical offset** | `8 px` | Moves the shadow down with positive values and up with negative values. |
| **Dialog shadow blur** | `24 px` | Softness and spread of the shadow edge. Higher values create a softer, wider shadow. |

Set opacity first, then adjust the offsets and blur. The values shown create a centered, softly floating effect: low opacity keeps the shadow subtle, `0 px` horizontal offset keeps it balanced, and the downward offset adds depth.

Avoid shadows that are too dark or wide. They can make the page feel heavy and may obscure nearby content, especially on smaller screens.

## Visual consistency and accessibility

Dialog background, text, and border colors usually follow the active color scheme. Verify that the dialog remains clearly separated from both light and dark page backgrounds and that its title, body text, inputs, buttons, and close icon have sufficient contrast.

Appearance settings do not replace interaction testing. Confirm that:

- Keyboard focus moves into the dialog when it opens.
- Focus remains visible and stays inside the dialog while it is open.
- The close control is easy to identify and operate.
- Focus returns to the element that opened the dialog after closing.

## Recommended adjustment order

1. Set the border thickness and corner radius.
2. Set shadow opacity.
3. Adjust horizontal and vertical offsets.
4. Fine-tune the shadow blur.
5. Check the active color schemes and page overlay.
6. Preview every dialog on desktop and mobile.

The screenshot values (`0 px`, `12 px`, `10%`, `0 px`, `8 px`, and `24 px`) are a balanced starting point for a clean, softly elevated dialog style.

## Save and test

Click **Save**, then open each type of dialog used by the store and check:

- The dialog is clearly separated from the page without an unnecessary outline.
- Corners and shadows are not clipped.
- The dialog fits within desktop and mobile screens.
- Titles, text, inputs, buttons, and the close icon remain readable and usable.
- Light and dark color schemes both provide enough contrast.
- Open, close, submit, cancel, and keyboard interactions work correctly.
