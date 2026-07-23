# Featured Product

The **Featured Product** section displays one product on a homepage or other page. Customers can view media, title, price, and description, select variants and quantity, and add to cart or use accelerated checkout without first visiting the product page.

![Featured Product settings and storefront preview](/images/en/featured-product.svg)

## Add the section

Open a template, click **Add section > Featured Product**, choose **Select Product**, arrange the product-information blocks, and click **Save**.

## Product and appearance

**Color Scheme** affects media controls, product information, variants, quantity, and purchase buttons. Check unavailable states and contrast.

**Select Product** reads the product's media, title, description, pricing, variants, inventory, and availability. If content remains empty, confirm that the product is active, published to Online Store, and has complete media and variant data.

::: warning Product availability
If the default variant is sold out, unavailable, or excluded from the current market, purchase controls become unavailable. Test every variant and verify synchronized media, price, stock, and buttons.
:::

## Media

- **Thumbnail position**: **Left** for a vertical list or **Bottom** for a horizontal row.
- **Desktop media width**: larger values emphasize media and reduce information width.
- **Bottom visible thumbnails**: `3`, `4`, `5`, or `6`, used only with Bottom position.

Check long titles, narrow descriptions, complete controls, selection state, scrollable thumbnail lists, and clear video/3D type indicators. Mobile rearranges content responsively.

## Product information blocks

- **Title**
- **Price**, including compare-at and sale states.
- **Description**
- **Variant picker**
- **Quantity selector**
- **Buy buttons**
- App blocks supplied by installed apps.

A practical order is Title → Price → Description → Variant picker → Quantity selector → Buy buttons. Keep price, options, and purchase actions easy to find. Removing a block affects only this section, not the product data.

Variant selection must update media, price, inventory, and availability. Quantity must respect inventory and purchase limits. Regular Add to cart uses the cart flow, while dynamic checkout can go directly to Shopify checkout.

## Padding, additional settings, and CSS

Use **Padding Top / Bottom** in `px`. Review any version-specific **Template settings** after theme updates. Prefer built-in media, block, and color controls before applying section-scoped **Custom CSS**.

## Before publishing

Verify the selected product and every media item; test both thumbnail positions; switch all variants and unavailable combinations; change and manually enter quantities at boundaries; test Add to cart and dynamic checkout; review long copy, sale prices, sold-out states, media width, mobile order, buttons, touch targets, and keyboard controls; then complete one real variant-to-cart-or-checkout flow after saving.
