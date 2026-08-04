# Password Header

The **Password header** is the top branding and access area of the store's password template. It can display the selected logo or the store name and provides the **Enter using password** link for visitors who already have the storefront password.

![Password header settings and storefront preview](/images/en/password-header.png)

## Open the Password header

1. In **Shopify Admin**, go to **Online Store → Themes**.
2. Click **Customize** for the theme you want to edit.
3. Open the template selector at the top of the editor and choose **Password**.
4. Under **Template**, select **Password header**.
5. Configure the settings while checking the storefront preview.
6. Click **Save**.

The Password header is part of the password template structure. The launch message and email form are configured in **Password**, while social links and store-owner information are configured in **Password footer**.

## Color scheme

Choose the global color scheme used by the header. It controls the header background, store name or logo context, password-entry link, borders, focus state, and other colors defined by the theme.

Click **Edit scheme** to modify the selected global scheme. A scheme can be shared with other sections, so review every area that uses it after making changes. The password-entry link must remain easy to identify in its normal, hover, and keyboard-focus states.

## Padding

- **Padding top** controls the space above the logo or store name and the password-entry link.
- **Padding bottom** controls the space below the header content before the main Password section.

The screenshot uses `32 px` for both values. Matching values provide a balanced starting point. Reduce them only if the header feels too tall on mobile, and verify that the content does not touch the viewport edges.

## Theme Settings: Logo

Use **Logo** in the **Theme Settings** group to select the branding image shown in the Password header. The image picker can use an uploaded asset, a free image where available, or a compatible dynamic source.

If no logo is selected, the theme can display the store name as text, as shown in the screenshot. This is a useful fallback, but the store name, spelling, and capitalization should be checked in Shopify Admin.

For a selected logo:

- Use a clean image with enough resolution for high-density screens.
- Prefer a transparent background when the header color may change.
- Keep important details legible at the compact header size.
- Avoid embedding a slogan or small text that becomes unreadable on mobile.
- Check that the logo has an appropriate accessible name or text fallback.

## Enter using password link

The **Enter using password** link opens the password-entry interface for authorized visitors. Its label is normally controlled by the theme's language translations rather than by a field in this panel.

This section does not create or change the storefront password. Password protection is managed in Shopify's store preferences. Test the link with an incorrect password, the correct password, keyboard-only navigation, and a mobile device. Do not expose the password in page text, Custom CSS, screenshots, or public documentation.

## Custom CSS

Use **Custom CSS** only for small, section-specific styling adjustments not covered by the built-in controls. Prefer the color scheme, padding, and logo settings first. Keep selectors scoped to this section, and do not hide the password link, its focus indicator, or any dialog controls.

## Example configuration

| Setting | Value shown in the screenshot |
| --- | --- |
| Color scheme | Dark green header scheme |
| Padding top | `32 px` |
| Padding bottom | `32 px` |
| Logo | Not selected; store name displayed as text |

## Before publishing

1. Confirm the correct logo or store name is visible and links or branding behave as expected.
2. Check the header background, text, link, hover, and focus-state contrast.
3. Review the header at desktop and mobile widths, including long translated link labels.
4. Verify the password-entry label and related dialog messages are translated.
5. Open the password-entry interface using a mouse, keyboard, and touch input.
6. Test both rejected and accepted passwords without exposing the password to unauthorized users.
7. Confirm the header spacing aligns with the main Password section and does not create excessive empty space.
8. Save the theme and complete a final test in a private browser window.
