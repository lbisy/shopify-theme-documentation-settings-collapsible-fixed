# Cart and Search

The theme provides full Cart and Search pages plus **Cart Overlay** and **Search Overlay** interactions. This guide covers the page templates and the workflows to test before launch.

![Cart and Search settings](/images/en/cart-search.svg)

## Open the templates

1. Go to **Shopify admin > Online Store > Themes**.
2. Click **Customize** on the current theme.
3. In the page selector, open **Cart** or **Search**.
4. Under **Template**, select the **Cart** or **Search** section.
5. Configure it and click **Save**.

Overlay, Header, and Footer are shared groups. Configure the global cart behavior and predictive search under [Cart settings](/en/settings/cart) and [Search settings](/en/settings/search).

## Cart page

The Cart page displays products, an order summary, and checkout. The empty state includes a **Shop More** prompt; also test the populated state and every quantity and removal action.

### Page settings

- **Color scheme**: background, text, borders, and buttons.
- **Edit scheme**: opens global colors and can affect other sections.
- **Heading size**: for example, **3XL**.
- **Padding Top / Bottom**: vertical spacing in `px`.
- **Custom CSS**: section-specific overrides; use built-in settings first and test all breakpoints afterward.

Keep product prices, quantity controls, dividers, disclosure controls, and checkout clearly visible.

### Order Summary and shipping

- **Order Special Instruction**: customer order notes.
- **Estimate Shipping**: country/region, province, and postal-code estimate.
- **Estimate Total**: current estimated total.
- **Checkout**: enters Shopify checkout; the adjacent number is the current item count.

Shipping estimates depend on shipping zones, rates, and the entered address. Test deliverable and non-deliverable addresses. The displayed estimate is not necessarily the final checkout total because discounts, taxes, and shipping can be recalculated.

### Test empty and populated carts

- Empty state and **Shop More** link.
- Images, titles, variants, unit prices, and subtotals.
- Quantity changes and synchronized totals/counts.
- Removing the final item and returning to the empty state.
- Out-of-stock and quantity-limit feedback.
- Saving order notes through checkout.
- Opening the Shopify checkout page.

Choose **Drawer** under **Theme settings > Cart > Cart type** to keep customers on the current page, or **Page** to open this template.

## Search page

The Search page submits a query and displays full **PRODUCTS**, **ARTICLES**, and **PAGES** results, plus an empty state when nothing matches.

### Page settings

- **Color Scheme**
- **Search per page**, such as `12`.
- **Mobile product card columns (results and dropdown)**: **1 column** or **2 columns**.
- **Padding Top / Bottom**
- **Template settings** supplied by the current theme version.
- **Custom CSS** for this section only.

More results per page reduce pagination but increase page length. Two mobile columns are compact; one column is easier to read when titles and card details are long.

### Test results

1. Search a complete product title.
2. Search partial names, brands, and features.
3. Search terms matching articles or pages.
4. Switch result types and verify the selected state and content.
5. Search a term with no matches.
6. Create enough results to test pagination.

Product visibility depends on status, sales-channel publication, and Shopify search data. Recent updates may take a short time to appear.

### Predictive search and overlays

**Search Overlay** opens from the header; the full page displays submitted results. Configure it under **Overlay > Search Overlay** and toggle predictions under **Theme settings > Search**. See [Search Overlay](/en/sections/search-overlay).

**Cart Overlay** controls the drawer cart; see [Cart Overlay](/en/sections/cart-overlay). **Newsletter Overlay** is independent and does not control cart or search.

Test opening, closing, backdrop clicks, scrolling, and keyboard focus. On mobile, check browser chrome and safe-area overlap.

## Example

| Template | Setting | Example |
| --- | --- | --- |
| Cart | Heading size | `3XL` |
| Cart | Padding | `32 px / 32 px` |
| Search | Search per page | `12` |
| Search | Mobile columns | `2 columns` |
| Search | Padding | `32 px / 32 px` |

## Before publishing

Test empty, single-item, and multi-item carts; notes, shipping estimates, totals, checkout, search result types, predictions, filters, pagination, and both mobile column options. Use `Tab`, `Shift + Tab`, arrow keys, `Enter`, and `Esc`. Finally complete a desktop and mobile journey from search to add-to-cart to checkout.
