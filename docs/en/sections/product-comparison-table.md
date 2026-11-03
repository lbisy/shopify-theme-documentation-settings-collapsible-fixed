# Comparison Table

The **Comparison Table** places product images, names, prices, ratings, custom attributes, and availability side by side to help customers compare related products or models.

![Comparison Table settings and storefront preview](/images/en/product-comparison-table.png)

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

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/product-comparison-table.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Comparison table

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Section heading<br>`heading` | inline_richtext | Similar Comparison Products | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Select products<br>`products` | product_list | Not declared | limit: 8 |
| Highlight column index<br>`highlight_index` | range | 0 | 0–8 ; step 1<br>info: 1 = first product column; 0 = no highlight |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Product info

`type`: `header`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

### Block: Price

`type`: `price`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

### Block: Rating

`type`: `rating`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

### Block: Ingredients / metafield

`type`: `metafield_text`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Row title<br>`row_title` | inline_richtext | Ingredients | — |
| Metafield key (namespace.key)<br>`metafield_key` | text | custom.ingredients | info: e.g. custom.ingredients |

### Block: Availability

`type`: `availability`; `limit`: 1

No local settings declared here; app/theme blocks define their own controls.

<!-- latest-schema:end -->
