# Pickup Availability

The **Pickup availability** section shows whether the currently selected product variant can be collected at the store's pickup locations. It is a data-driven product-page component: location names, availability, pickup times, addresses, and phone numbers come from Shopify rather than editable section fields.

::: warning No section settings
The schema contains an empty `settings` array and no preset. There are no content or layout controls in the theme editor, and this section is not intended to be added like a regular customizable section. Its placement and variant-refresh behavior are handled by the product template and theme code.
:::

## What customers see

When at least one location has pickup enabled for the current variant, the section displays:

- A status icon and an **available at** or **unavailable at** message for the first returned location.
- The estimated pickup time when that first location is available and a pickup time is provided.
- An expandable **View store info** link when there is one pickup location.
- An expandable **Check other stores** link when there are multiple pickup locations.
- A list of every pickup-enabled location, including its name, current status, formatted address, optional pickup time, and optional phone number.

Available locations use a check icon. Unavailable locations use a close icon. The icon is hidden from assistive technology because the same status is also provided as text.

## Display conditions

The code reads `product_variant.store_availabilities` and keeps only records where `pick_up_enabled` is `true`.

| Condition | Result |
| --- | --- |
| No pickup-enabled availability records | No visible pickup card is rendered; the content wrapper has `data-empty="true"`. |
| One or more pickup-enabled records | The pickup card is rendered and the wrapper has `data-empty="false"`. |
| First location is available | Shows the available message and, when present, its pickup time. |
| First location is unavailable | Shows the unavailable message and omits its pickup time. |
| One location | The disclosure label uses the `view_store_info` translation. |
| Multiple locations | The disclosure label uses the `check_other_stores` translation. |

Filtering is based on whether pickup is enabled, not whether the variant is currently available. An unavailable location therefore remains in the expanded list. The summary always uses the first returned record; this section does not calculate or reorder locations itself. A later location can still be available when the summary location is unavailable.

## Information shown for each location

The expanded list renders the following data for every pickup-enabled availability record:

- **Location name** from `availability.location.name`.
- **Available** or **Unavailable** from `availability.available`.
- **Pickup time** from `availability.pick_up_time`, but only when the location is available and the value is not blank.
- **Address** from `availability.location.address`, formatted with Shopify's `format_address` filter.
- **Phone number** from `address.phone` when it is not blank.

The phone number is displayed as text; this code does not create a `tel:` link or a map link. Keep each location's public name, address, phone number, pickup status, and processing time accurate in Shopify Admin.

Pickup availability and pickup time can account for inventory supplied through a store transfer. A location may therefore be shown as available even when the item is not physically on hand there yet; the displayed pickup time should reflect the additional preparation or transfer time supplied by Shopify.

## Variant changes and dynamic refresh

Pickup availability belongs to a specific variant, not the product as a whole. A color or size change can produce a different location list and status.

The attributes `data-pickup-availability-fragment`, `data-pickup-availability-content`, and `data-empty` provide hooks for the theme's JavaScript. The Liquid file itself does not listen for variant changes or make network requests. The surrounding product-page code must:

1. Detect the newly selected variant.
2. Request the Pickup availability section in that variant's rendering context.
3. Replace the existing fragment with the returned content.
4. Handle an empty response or request failure without leaving stale availability on the page.

If the status does not change after choosing another variant, inspect the product form's variant-change event, section-rendering request, returned HTML, and fragment replacement logic. Also confirm that the requested variant is selected or is the first available variant, because Shopify only defines `variant.store_availabilities` in those contexts.

## Theme styling and interaction

There are no section-specific color or spacing settings. The component inherits theme tokens and utility classes for its border, background, text, spacing, focus ring, and opening animation.

The store list uses native `<details>` and `<summary>` elements. Customers can open it with a pointer or keyboard, and the arrow rotates when the disclosure is open. Test the disclosure with `Enter`, `Space`, touch input, and a screen reader. Make sure status text, borders, and focus indicators remain visible in every color scheme used by the product page.

## Translations

Customer-facing labels come from the following locale keys:

- `products.product.pickup_availability.available_at_html`
- `products.product.pickup_availability.unavailable_at_html`
- `products.product.pickup_availability.view_store_info`
- `products.product.pickup_availability.check_other_stores`
- `products.product.pickup_availability.available`
- `products.product.pickup_availability.unavailable`

The first two keys receive `location_name` and may contain HTML. Check every published language for missing keys, correct grammar around the inserted location name, and clear available/unavailable wording. Pickup-time text is supplied by Shopify and should also be reviewed in each storefront language.

## Store setup checklist

Before testing the section, confirm that:

1. Local pickup is enabled for at least one Shopify location.
2. The location is associated with the product variant's inventory.
3. Pickup availability and preparation time are configured for the location.
4. The public location name, address, and optional phone number are correct.
5. The product template includes the pickup-availability container and refresh script expected by this section.

The section only presents Shopify's pickup data. It cannot enable local pickup, assign inventory, change preparation times, or edit location contact details.

## Before publishing

1. Test a product with one pickup location and another with multiple locations.
2. Test variants that are available, unavailable, and have no pickup-enabled records.
3. Switch every variant without reloading the page and confirm the content refreshes without showing stale data.
4. Verify the summary location, status icon, pickup time, and disclosure label.
5. Expand the list and confirm every location's status, address, and optional phone number.
6. Check the empty state: no blank bordered card or outdated location should remain visible.
7. Test long location names, multi-line addresses, missing phone numbers, and missing pickup times.
8. Review desktop and mobile wrapping, contrast, focus visibility, and disclosure animation.
9. Test mouse, keyboard, touch, and screen-reader interaction.
10. Repeat the checks in every published storefront language.

For implementation details, see Shopify's [pickup availability guide](https://shopify.dev/docs/storefronts/themes/delivery-fulfillment/pickup-availability).
