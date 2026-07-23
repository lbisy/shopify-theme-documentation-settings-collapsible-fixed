# Cart Overlay

The **Cart Overlay** shows the cart in a side drawer after a customer opens the cart or adds a product. The customer remains on the current page while a backdrop separates the drawer from the page.

![Cart Overlay settings and storefront preview](/images/en/cart-overlay.svg)

## Open the settings

In **Online Store > Themes > Customize**, open **Overlay > Cart Overlay**. This shared overlay does not need to be added to individual templates.

::: info Enable the drawer
If the cart icon opens a full page, set **Theme settings > Cart > Cart type** to **Drawer**. Cart type determines the interaction; Cart Overlay controls drawer appearance and content.
:::

## Settings

- **Drawer position**: open from the **Left** or **Right**. Test both desktop and mobile placement and close-button reachability.
- **Color scheme**: drawer background, title, text, dividers, quantity controls, and footer actions.
- **Custom CSS**: section-specific overrides. Test empty and populated carts on desktop and mobile after adding any rule.

## Storefront content

The drawer includes the **Cart** title and close button, the item list or `Your cart is empty.` state, **Total**, **Clear all**, and **Checkout**. Numbers beside the action labels show the current item count.

Empty-cart actions may be disabled. After adding products, confirm product details, totals, counts, and button states update together. Copy and currency formatting follow the active store language, market, and currency.

Removing the section can stop the drawer from working. To use the full cart page instead, normally change Cart type to **Page** rather than deleting the overlay.

## Test and publish

- Verify the backdrop prevents accidental interaction with the page.
- Close with the button, backdrop, and `Esc`.
- Test empty, one-item, multi-item, and remove-last-item states.
- Change quantities and verify line totals, Total, and counts.
- Test **Clear all** and a complete **Checkout** transition.
- Use `Tab` and `Shift + Tab` and keep focus inside the open drawer.
- On mobile, review width, long titles, prices, quantity controls, footer actions, and safe areas.

Finally open the drawer both from a product add-to-cart action and the header icon, test light and dark schemes, and complete a desktop and mobile add-to-checkout flow.
