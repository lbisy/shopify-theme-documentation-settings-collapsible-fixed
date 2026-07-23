# Focus

The **Focus** settings control the focus ring shown during keyboard navigation. It identifies the link, button, input, or other interactive element that will respond when a visitor presses Enter or Space.

## Open the Focus settings

Go to **Shopify admin > Online Store > Themes**, click **Customize**, then open **Theme settings > Focus**.

![Focus settings](/images/en/settings/focus.svg)

## Focus ring width

**Focus ring width** controls line thickness.

- Larger values make the ring more noticeable.
- Smaller values create a lighter visual effect but can disappear on complex backgrounds or high-resolution screens.

Test buttons, text and image links, inputs, and selectors on light and dark backgrounds.

::: warning Accessibility
Do not set the width to `0px`. Removing the focus ring makes it difficult for keyboard-only visitors to understand their current position.
:::

## Focus ring offset

**Focus ring offset** controls the gap between the ring and the element.

- Small values keep the ring close to the edge.
- Large values create more separation and emphasis.
- `0px` places the ring directly against the outline.

A small offset can prevent the focus ring from blending into a button or input border. Excessive offset may overlap nearby content.

## Focus ring color

Set the color under **Theme settings > Colors > [color scheme] > Focus ring color**. It should contrast with the background, remain distinct from the element's border, and stay visible in every scheme.

Width and offset are global, while color belongs to each color scheme. Test light, dark, and accent schemes after making changes.

## Test keyboard focus

1. Open the storefront preview and click an empty area.
2. Press `Tab` to move forward and `Shift + Tab` to move backward.
3. Confirm every interactive element shows a complete focus ring.
4. Press `Enter` or `Space` to verify the focused control works.

Test header navigation, language and search controls, product cards and options, cart interfaces, forms, popups, footer links, and social icons.

## Save and check

Click **Save** and test desktop and mobile layouts. Visibility comes before brand styling: never hide the ring merely because it changes the appearance.
