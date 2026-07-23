# Search Overlay

The **Search Overlay** is a drawer opened from the header search control. Customers can enter a query, review predictive suggestions, and continue to the full results page without first leaving the current page.

![Search Overlay settings and storefront preview](/images/en/search-overlay.svg)

The overlay shows a limited predictive list; the full Search page provides complete results, result types, and pagination. Their result limits are independent.

## Open and configure

In **Online Store > Themes > Customize**, open **Overlay > Search Overlay** and configure:

- **Color scheme**
- **Drawer position**: Left or Right
- **Predictive search result limit**
- Additional **Template settings**
- Section-scoped **Custom CSS**

This shared overlay must be tested from the homepage, products, collections, blogs, and every other page with a header search control.

## Predictive search

The result limit is only a display maximum. It does not control full-page pagination, searchability, relevance ranking, result types, synonyms, or product boosts.

Enable predictions separately under **Theme settings > Search > Enable predictive search**. When disabled, customers can still enter and submit a query.

Use Shopify **Search & Discovery** to configure supported result types, synonyms, product boosts, and handling of sold-out products. Keep product titles, product types, vendors, variants, page titles, and article titles clear and consistent.

If content does not appear, check publication and searchability, supported attributes and result types, and indexing delay. Increasing the limit cannot make unsearchable content appear.

## Accessibility

On open, focus should enter the search field or first control. `Tab` and `Shift + Tab` must follow a logical order; arrows and `Enter` should select results; `Esc`, close, and supported backdrop clicks should close the drawer; focus must return to the header search button. Prevent background interaction and scrolling, and provide clear input, loading, empty, and error states.

## Before publishing

Open from multiple templates; verify drawer side and RTL languages; test full/partial names, vendors, articles, pages, mixed languages, special characters, long and empty queries; confirm the result limit; open every result type; submit to the full page; test Search & Discovery rules; complete the full keyboard and mobile-soft-keyboard flow; check contrast and Custom CSS isolation; then save and repeat on the storefront.

## Shopify references

- [Predictive search](https://help.shopify.com/en/manual/online-store/storefront-search/predictive-search)
- [Shopify Search & Discovery](https://help.shopify.com/en/manual/online-store/search-and-discovery/settings)
- [Managing searchability](https://help.shopify.com/en/manual/online-store/storefront-search/managing-searchability)
