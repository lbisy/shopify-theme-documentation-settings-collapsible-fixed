# Frequently Asked Questions

Save your work and confirm that you are editing the correct theme and template before troubleshooting.

## Pages and sections

### Why does the homepage differ from the demo?

Theme packages normally do not include demo products, images, menus, or brand content. Add sections to the homepage and assign your own resources.

### Why can I not find a section?

Check the selected template. Some sections are page-specific, and an existing section may simply be hidden.

### Why is an added section empty?

Select its product, collection, blog, or page; add and complete required blocks; publish the selected resources to Online Store; then click **Save**.

### Why did another page change too?

Both pages probably use the same template. Create and assign a separate template when a product, collection, or page needs a different layout.

### Why is a section misaligned on mobile?

Check mobile columns, spacing, image ratio, and copy length. Temporarily disable custom Liquid or app code to isolate conflicts.

## Global styling

### A section did not change after editing colors

Sections can use different color schemes. Select the scheme you edited and remember that buttons, inputs, badges, and feedback messages have dedicated colors.

### A custom font does not appear

Enable **Use custom font URL**, provide the family name and a public `.woff2` URL, and verify that the font includes all required language glyphs.

### Product cards have different heights

Source images probably use different ratios. Change **Theme settings > Product cards > Image ratio** or upload consistent primary images.

### Buttons, inputs, or dialogs did not change

Edit the matching global settings, refresh the correct theme preview, and check whether a section or app overrides the styles. Test in a private window to rule out caching.

### Keyboard focus is invisible

Set a nonzero width under **Theme settings > Focus** and a contrasting **Focus ring color** in the active color scheme. Test with `Tab`.

## Images and media

### Images are blurry or cropped

Upload sufficiently large originals, check image-ratio settings, keep important subjects away from edges, and review desktop and mobile crops.

### A video banner does not play

Verify the file or URL and browser-compatible format. Browsers can block autoplay with sound, so use muted video and provide a cover image. Test desktop and mobile browsers.

### Google Map does not appear

Check the address or embed code, use code from a trusted map-sharing source, and verify that cookie, privacy, or content blockers are not preventing it from loading.

## Animation and overlays

### Animations do not play

Enable **Enable motion**, choose a reveal style other than **None**, and check the device's reduced-motion preference. With **Once**, an element will not animate repeatedly.

### Toast messages do not appear

Toasts appear only after relevant actions. Use **Toast > Preview**, check that other fixed elements do not cover them, and verify Feedback-message contrast.

### Newsletter Overlay does not open automatically

Check its enabled state and display conditions. Clear site data or leave private mode when retesting; the theme may remember that a visitor dismissed or submitted the popup. Disable competing popup apps.

## Products, cart, and search

### Featured or recommended products are empty

Select valid products, ensure recommendation data exists, publish products to Online Store, and check count and display conditions.

### The cart does not open after adding

Check **Theme settings > Cart > Cart type** and the Cart Overlay. **Drawer** opens a panel; **Page** opens the cart page. Temporarily disable apps that alter cart behavior.

### Predictive search has no results

Enable it under **Theme settings > Search**, publish the products, test terms from product titles, enter more characters, and temporarily disable search apps.

### Badge, price, or button colors are wrong

In the active scheme, review Badges, Primary button, Secondary button, and Text color. Price and sale states come from product data.

## Navigation and social links

### Header or footer menu is empty

Create the menu in Shopify admin, select it in Header or Footer, and ensure every destination is published.

### Social icons are missing or wrong

Enter complete `https://` profile URLs under **Theme settings > Social icon**, leave unused platforms blank, save, and test every icon.

### Logo or favicon still shows the old image

Save the theme, verify file format and size, adjust logo width if needed, and use a private window or clear browser cache for favicon updates.

## Custom code and apps

### Custom Liquid breaks the layout

Check for unclosed HTML, remove recent Liquid/CSS/JavaScript to isolate the cause, avoid duplicate scripts, keep a backup, and test on an unpublished theme.

### An app conflicts with the template

Disable its theme embed, check whether it modifies cart, search, product forms, or popups, compare on a theme copy, and send the app developer a URL, screenshot, and reproduction steps.

### Customizations disappeared after a theme update

A new version is normally a separate theme copy and does not merge all code or settings. Back up the old theme and manually migrate custom Liquid, CSS, JavaScript, template settings, and app embeds.

## Still need help?

Provide support with the store URL, theme version, affected page, exact reproduction steps, desktop or mobile screenshots, browser/device details, and recent apps or custom code. Complete information makes it easier to distinguish theme settings, store data, custom code, and third-party conflicts.
