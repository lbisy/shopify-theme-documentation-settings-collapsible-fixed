# Cart

The **Cart** setting determines how customers view and edit their cart after adding a product or selecting the cart icon. It changes the presentation of the cart, not the cart contents.

## Open the Cart settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Open **Theme settings > Cart**.

![Cart settings and storefront preview](/images/en/settings/cart.png)

The example above sets **Cart type** to **Drawer**, so the cart opens over the current page.

## Cart type

| Setting | Value shown | Available options | What it controls |
| --- | ---: | --- | --- |
| **Cart type** | **Drawer** | **Drawer**, **Page** | Whether the cart opens as an overlay panel or as a dedicated page. |

Changing this setting does not remove products or alter quantities. It changes how customers access and review the same cart data.

### Drawer

With **Drawer**, the cart opens as a panel over the current page.

- Customers can review or edit the cart without leaving the product or collection page.
- It supports a quick add-and-continue-shopping flow.
- It is well suited to simple purchases and customers who add several products in succession.
- On mobile, the drawer must leave enough room for item details, quantity controls, totals, and checkout actions.

### Page

With **Page**, customers are taken to a dedicated cart page.

- It provides more room for cart items, quantity controls, totals, notes, and additional information.
- It is useful for larger or more complex carts that need careful review.
- Customers can refresh or return to a clear cart URL.
- It adds a page transition before customers continue shopping or proceed to checkout.

## Choose the appropriate type

| Consideration | Drawer | Page |
| --- | --- | --- |
| Shopping flow | Keeps customers on the current page | Moves customers to a dedicated cart page |
| Best suited to | Fast purchases and continued browsing | Detailed review and larger carts |
| Available space | Limited by the overlay width and height | Uses the full page |
| Mobile testing | Check panel width, scrolling, and fixed actions | Check page spacing and checkout visibility |

Choose **Drawer** when speed and continued browsing are the priority. Choose **Page** when customers need more room to verify products, quantities, messages, or order details.

## Related behavior

Dynamic checkout buttons such as **Buy now** may go directly to checkout and bypass the cart display. **Cart type** primarily affects regular **Add to cart** actions and the cart icon.

Also verify any cart upsells, discount messages, free-shipping progress, notes, and app blocks. These elements may fit differently in a narrow drawer and on a full cart page.

## Save and test

Click **Save**, then test on desktop and mobile:

1. Add a product from a product page and a product grid.
2. Open the cart from the header icon.
3. Change quantities and remove an item.
4. Check prices, discounts, totals, and cart messages.
5. Continue to checkout.
6. Return to the store and add another product.

Confirm that the selected cart type opens consistently, content can scroll when necessary, and the checkout action remains fully visible and usable.
