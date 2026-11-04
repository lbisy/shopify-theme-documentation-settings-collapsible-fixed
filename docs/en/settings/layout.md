# Layout

The **Layout** settings control the maximum width of page content and the size of small corner radii, shaping the store's overall spacing and visual style.

## Set Page Width

**Set Page Width** sets the maximum width of the page content area from **1000px to 1600px**. Drag the slider to adjust it. This does not change the browser window; it determines how much horizontal space content can occupy on wide screens.

- **Narrower**: concentrates content and reduces eye movement, which suits text-heavy or compact layouts.
- **Medium**: balances content density and whitespace for most stores.
- **Wider**: shows more content across the page and suits image-led layouts or product grids with many cards.

::: tip Recommendation
After changing the width, check the desktop homepage, collection pages, and product pages to ensure text, images, and cards remain well proportioned.
:::

## Setting Small Border Radius

**Setting Small Border Radius**〔Not declared in package〕 controls small rounded corners across the site:

- **small**: crisp, structured corners.
- **medium**: a balance of clean and soft styling.
- **large**: a noticeably softer and friendlier appearance.

::: warning Note
This setting does not affect fully rounded elements, such as certain buttons and search fields.
:::

Choose a value that fits the brand and coordinates with images, cards, and inputs. Review several pages after making a change to confirm that the result stays consistent.

<!-- latest-layout-note -->
::: warning Update the old range
The current Page width range is 1000–2000 px with a 1600 px default. Small Border Radius is not declared in Layout; Page margin is declared instead.
:::

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `config/settings_schema.json` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → Theme settings → Layout

### Page settings

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Page width<br>`page_width` | range | 1600 | 1000–2000 px; step 100 |
| Page margin<br>`page_margin` | range | 24 | 10–100 px; step 1 |

<!-- latest-schema:end -->
