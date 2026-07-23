# Collection Product List

The **Collection** section is the main content of a collection template. It displays products from the current collection and provides filtering, sorting, pagination, and responsive product-grid controls.

![Collection settings and storefront preview](/images/en/collections.svg)

## Add or configure the section

Open **Collections > Default collection** in the theme editor and select **Collection**. Create and assign separate collection templates when different collections require different layouts.

## Content and color

- **Color Scheme**: background, text, controls, and product-area colors.
- **Heading size**
- **Header**: preferably connect a dynamic source for the current collection title.
- **Description**: preferably connect the current collection description.
- **Subtitle size**: filter and sort labels.
- **Rotate Badge Text / Percent**: short brand claim and center value.

Dynamic sources allow a shared template to show the correct title and description for every collection. Keep badge claims short, accurate, and clear on mobile.

## Product display

- **Products per page**: maximum before pagination.
- **Desktop product card columns**: typically **3** or **4**.
- **Mobile product card columns**: **1** or **2**.

More products and columns increase density but can make titles, pricing, badges, and controls crowded. Shared card appearance is configured under **Theme settings > Product cards**.

## Filtering

- **Enable filtering**
- **Desktop filter layout**, such as **Drawer**
- **Visible filter values before show more**

Available filters come from Shopify's **Search & Discovery** configuration and product data, not from individual blocks in this section. Keep product types, vendors, tags, variants, and metafields consistent. Test applying, combining, clearing, expanding, and returning from filters and verify the result count.

## Sorting

**Enable sorting** shows customer sort controls. Available choices are based on Shopify collection sorting, while the initial order is set on the collection in Shopify admin. Test sorting alone and together with active filters.

## Padding

Use **Padding Top / Bottom** in `px` to control separation from the header and following content.

## Example

| Setting | Example |
| --- | --- |
| Header / Description | Current collection dynamic sources |
| Subtitle size | `XL` |
| Rotate Badge Text / Percent | `Carefully selected materials` / `100%` |
| Products per page | `12` |
| Filtering / layout | On / `Drawer` |
| Visible filter values | `6` |
| Sorting | On |
| Desktop / mobile columns | `4` / `2` |
| Padding | `32 px / 32 px` |

## Before publishing

Confirm the correct template assignment and Online Store publication; check media, titles, prices, and inventory; verify dynamic titles and descriptions across shared templates; test badge wrapping, fewer/equal/more products than the page limit, filters, show-more, clear, counts, sorting, browser back, pagination, every column count, long titles, sale and sold-out states, keyboard access, contrast, and the complete filter-to-product journey after saving.
