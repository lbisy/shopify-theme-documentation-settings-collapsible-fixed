# Comparison Table

The **Comparison Table** places product images, names, prices, ratings, custom attributes, and availability side by side to help customers compare related products or models.

![Comparison Table settings and storefront preview](/images/en/product-comparison-table.svg)

## Prepare product data

Publish each product and complete its image, title, price, and inventory. For ratings, use a compatible review app or standard rating metafield. For materials, dimensions, or other custom rows, create the same product metafield definition and type for every compared product and fill all values consistently.

## Configure the section

Open a template, add **Comparison Table**, choose **Select Products**, add and order comparison-row blocks, configure highlighting, colors, and padding, then click **Save**.

## Appearance and products

- **Color scheme**
- **Section heading** and **Heading size**
- **Highlight column background**
- **Availability in stock color**
- **Availability out of stock color**
- **Select Products**
- **Highlight Column Index**: `0` for none, `1` for the first product, `2` for the second, and so on.

Keep the number of products manageable and compare similar purposes or price ranges. Check market availability and currency. When product order changes, update the highlight index. Do not communicate “recommended” by color alone; provide explanatory text.

## Comparison-row blocks

- **Product Info**: primary image and title.
- **Price**: Shopify and market pricing.
- **Rating**: compatible rating data; test rated and unrated products.
- **Ingredients / Metafield**: material, specification, or other consistent product metafield.
- **Availability**: inventory status using the configured colors.

A useful order is Product Info → Price → Rating → Metafield → Availability, but move the attributes most important to the decision upward.

Inventory must be tested for in-stock, sold-out, partially unavailable variants, and continue-selling states. Status must include clear text as well as color.

## Responsive behavior

Many columns require horizontal browsing, especially on mobile. Ensure customers can discover and operate it and can keep row labels aligned with each product. Use section-scoped Custom CSS cautiously and test long titles, values, widths, and row heights.

## Before publishing

Verify publication and market availability; product order and highlight index; images, titles, prices, currencies, and sale states; ratings and empty ratings; every metafield name, unit, format, and missing value; all inventory states; contrast; desktop/mobile horizontal navigation; keyboard product links; long content and different column counts; and Custom CSS isolation. Save, compare products, and open a product detail page.
