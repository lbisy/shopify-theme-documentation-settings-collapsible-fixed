# Search

The **Search** setting controls predictive search. When enabled, matching suggestions appear while customers type, helping them reach products and other relevant content before submitting a full search.

## Open the Search settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Open **Theme settings > Search**.

![Search settings and storefront preview](/images/en/settings/search.png)

The example above has **Enable predictive search** turned on.

## Enable predictive search

| Setting | State shown | What it controls |
| --- | ---: | --- |
| **Enable predictive search** | **On** | Shows matching suggestions while a customer types in the storefront search field. |

### When enabled

- Customers can reach a match without typing or submitting the complete query.
- Suggestions can help confirm product names and spelling.
- Large catalogs become faster to explore when products have clear, distinct titles.
- The exact suggestion types and information shown depend on the theme and available store content.

### When disabled

- No live suggestions appear while the customer types.
- Customers submit the query and review the full search results page.
- Regular storefront search remains available.

Disabling predictive search can suit a small catalog or a deliberately simple search interface. Enabling it is generally more useful when customers often search for specific products.

## Improve search suggestions

Predictive search quality depends on the store data available to search. To improve suggestions:

- Use clear, accurate, and distinguishable product titles.
- Include terms customers commonly use in relevant product information.
- Avoid duplicate names that are difficult to tell apart.
- Publish the intended products to the Online Store sales channel.
- Keep product images, prices, and availability current.

Recent product or publication changes may take a short time to appear. Retest after the storefront data has updated.

## Accessibility and interaction

Predictive results must remain usable without a mouse. Check that customers can:

- Open search and reach the input with the keyboard.
- Move through suggestions using the supported keyboard controls.
- See a clear focus indicator on the active suggestion.
- Select a result with `Enter` and close the search interface when needed.
- Understand when suggestions update or when no matches are available.

Also verify that long titles, prices, images, and result groups remain readable at high browser zoom and on narrow mobile screens.

## Recommended test queries

Use several realistic queries rather than testing only one product:

- A partial product title
- A common category, brand, or product feature
- Similar product names that must be distinguished
- A misspelling or incomplete term
- A multilingual term used by customers
- A query with no matches

For each query, compare the predictive suggestions with the full search results and confirm that destinations are correct.

## Save and test

Click **Save**, then test on desktop and mobile:

1. Open search from the header.
2. Type a partial query and inspect the suggestions.
3. Open a suggestion and verify its destination.
4. Submit the query and inspect the full results page.
5. Try a query with no matches and check the empty state.
6. Repeat the flow using only the keyboard.

Confirm that suggestions do not overflow the screen, long text is handled cleanly, and search can be opened and closed without losing focus or blocking page interaction.
