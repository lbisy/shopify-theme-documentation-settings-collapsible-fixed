# Related Products

The **Related products** section dynamically recommends products based on the current product. Place it after product details or comparison content to offer alternatives or complementary purchases.

![Related products settings and storefront preview](/images/en/product-recommendations.png)

## Add the section

Open a product template, add **Related products**, configure recommendation type, heading, description, count, and spacing, then click **Save**. Products are generated from the current product context; no manual product blocks are needed.

## Recommendation type

- **Related products**: similar alternatives for continued browsing.
- **Complementary products**: accessories or products suited to buying together.

Some products may have fewer or no recommendations for a selected type. Preview several different products.

## Content and layout

- **Color scheme**
- **Heading** and **Heading size**
- **Description**
- **Subtitle size** for card supporting text
- **Products limit**
- **Padding Top / Bottom**

Match the heading to the logic: `You may also like` for related items, or `Complete the look` for complementary products. Keep description concise and do not imply that recommendations are included with the current product.

Large heading or subtitle sizes and long copy can crowd mobile layouts. The limit is only a maximum; actual results depend on available recommendations.

## Product data

Images, titles, prices, links, vendor text, and card behavior come from Shopify product data and global product-card styling. If results are missing, verify that the template has product context, recommended products are published, the selected recommendation type has results, and the limit is greater than zero.

## Before publishing

Test both recommendation types and several source products; align heading and copy with the type; review responsive type sizes; verify product media, name, price, link, and availability; test fewer results than the limit; operate cards and navigation with mouse, touch, and keyboard; check contrast and spacing; then save and complete product visits on desktop and mobile.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/product-recommendations.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Product recommendations

Has presets for the Add section picker.

`enabled_on`: &#123;"templates": ["product"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Recommendation type<br>`recommendation_type` | select | related | Related products (`related`); Complementary products (`complementary`) |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Heading<br>`heading` | inline_richtext | Related products | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Description<br>`description` | richtext | &lt;p&gt;Introduce products that complement the item customers are viewing.&lt;/p&gt; | — |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Products limit<br>`limit` | range | 4 | 2–12 ; step 1 |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
