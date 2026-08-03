# Focus

The **Focus** settings control the focus ring shown during keyboard navigation. The ring identifies the link, button, input, or other interactive element that currently receives keyboard input.

## Open the Focus settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Open **Theme settings > Focus**.

![Focus settings and storefront preview](/images/en/settings/focus.png)

The example above uses a `2 px` focus ring with a `2 px` gap between the ring and the focused element.

## Focus ring settings

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Focus ring width** | `2 px` | Thickness of the focus indicator. Larger values are more prominent; very small values can disappear on complex backgrounds. |
| **Focus ring offset** | `2 px` | Space between the ring and the element edge. A small gap helps separate the ring from borders and outlines. |

A `2 px` width and `2 px` offset provide a clear, compact starting point for most interfaces.

## Width and offset guidance

Do not reduce **Focus ring width** to `0 px`. Removing the visible indicator makes keyboard navigation difficult because visitors can no longer tell which control is active.

Use enough offset to distinguish the ring from button, input, card, and image borders. If the offset is too large, the ring can overlap nearby text or controls; if it is too small, it can blend into the element outline. Check that rounded elements display a complete ring without clipping.

## Focus ring color

Focus ring color is configured separately under **Theme settings > Colors > [color scheme] > Focus ring color**. Width and offset are global, while color belongs to each color scheme.

Choose a color that:

- Contrasts clearly with the surrounding background.
- Remains distinct from the element's border and fill.
- Stays visible on light, dark, image, and accent backgrounds.
- Is recognizable as the same focus state throughout the store.

Review every color scheme after changing width, offset, or focus ring color.

## What to test

Use `Tab` to move forward and `Shift + Tab` to move backward through the storefront. Test:

- Header navigation, search, account, language, and cart controls
- Product cards, product options, quantity controls, and purchase buttons
- Forms, selectors, checkboxes, and links
- Cart drawers, dialogs, overlays, and close controls
- Footer links and social icons

The focused element should always have a complete, unobscured indicator. Press the appropriate activation key, such as `Enter` or `Space`, to confirm each control still works.

## Recommended adjustment order

1. Set a visible focus ring width.
2. Add enough offset to separate the ring from element borders.
3. Configure focus ring color in every color scheme.
4. Test both forward and backward keyboard navigation.
5. Check light, dark, image, and high-contrast backgrounds.
6. Review desktop and narrow mobile layouts.

## Save and test

Click **Save**, then confirm:

- Every interactive element receives a visible focus indicator.
- The ring is not clipped by cards, dialogs, drawers, or containers.
- Width and offset remain clear at high browser zoom.
- The color is visible in every active color scheme.
- Focus order follows the visual and reading order.
- Opening and closing overlays returns focus to a logical location.

Focus visibility should take priority over decorative styling. Do not hide the ring merely because it changes the appearance of a component.
