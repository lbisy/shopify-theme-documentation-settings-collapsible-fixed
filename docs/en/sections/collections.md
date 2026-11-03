# Collection Product List

The **Collection** section is the main content of a collection template. It displays products from the current collection and provides filtering, sorting, pagination, and responsive product-grid controls.

![Collection product list settings and storefront preview](/images/en/collections.png)

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

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/collections.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Collections grid

No presets declared; do not assume this can be added freely through Add section.

`enabled_on`: &#123;"templates": ["list-collections"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Font

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading<br>`heading` | inline_richtext | Latest Brand | — |

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Description<br>`description` | inline_richtext | Introduce the collections customers can browse on this page. | — |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Collections per page<br>`collections_per_page` | range | 12 | 4–24 ; step 4 |
| Show badge<br>`show_badge` | checkbox | true | — |
| Badge text<br>`badge_text` | text | EXPLORE • DISCOVER • SHOP • | — |
| Badge value<br>`badge_value` | text | EXPLORE | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
