# Password Footer

The **Password footer** is the bottom area of the store's password template. Use it to display links to the store's social profiles and to control the footer's color scheme and spacing. The footer also contains Shopify attribution and the store-owner login link.

![Password footer settings and storefront preview](/images/en/password-footer.png)

## Open the Password footer

1. In **Shopify Admin**, go to **Online Store → Themes**.
2. Click **Customize** for the theme you want to edit.
3. Open the template selector at the top of the editor and choose **Password**.
4. Under **Template**, select **Password footer**. Do not confuse it with **Password header** or **Password**.
5. Configure the settings while checking the storefront preview.
6. Click **Save**.

The Password footer is part of the password template structure and normally does not need to be added as a separate section. The brand and password-entry link are configured in **Password header**, while the launch message and email form are configured in **Password**.

## Color scheme

Choose the global color scheme used by the footer. It controls the footer background, social icons, attribution text, owner-login link, and theme-defined hover and focus states.

Click **Edit scheme** to modify the selected global scheme. Because a scheme can be shared by multiple sections, changes may affect other parts of the store. Check the contrast of text, links, icons, and keyboard-focus indicators after editing it.

## Show social media icons

Turn on **Show social media icons** to display icons for the social profile links configured under **Theme Settings**. The screenshot shows the setting enabled and displays Facebook, Instagram, and YouTube icons in the storefront preview.

An icon is shown only when its corresponding profile field contains a value. Leave unused fields blank. Enabling the switch does not validate a link, so incomplete values such as `1`, `2`, and `3` may still produce icons but will not send visitors to a valid profile.

## Padding

- **Padding top** controls the space above the social icons or, when no icons are shown, above the footer information.
- **Padding bottom** controls the space below the store-owner login link.

The screenshot uses `32 px` for both values. Matching values are a balanced starting point. Review the result on mobile, especially when attribution or login text wraps onto another line.

## Theme Settings: social profile links

The fields in the **Theme Settings** group are global social-profile settings shared by every theme area that uses social icons. Enter the full public URL for each account, beginning with `https://`. Changes made here may also affect the main header, footer, or other social sections.

| Platform | Value shown in the screenshot | Publishing note |
| --- | --- | --- |
| **Facebook** | `1` | Incomplete placeholder; replace it with the full Facebook profile URL. |
| **Instagram** | `2` | Incomplete placeholder; replace it with the full Instagram profile URL. |
| **YouTube** | `3` | Incomplete placeholder; replace it with the full YouTube channel URL. |
| **TikTok** | `https://tiktok.com/@shopify` | Replace it with the store's own TikTok profile URL. |
| **X / Twitter** | `https://x.com/shopify` | Replace it with the store's own X profile URL. |
| **Pinterest** | `https://pinterest.com/shopify` | Replace it with the store's own Pinterest profile URL. |
| **Snapchat** | `https://www.snapchat.com/add/shopify` | Replace it with the store's own Snapchat profile URL. |
| **Tumblr** | `https://shopify.tumblr.com` | Replace it with the store's own Tumblr profile URL. |
| **Vimeo** | `https://vimeo.com/shopify` | Replace it with the store's own Vimeo profile URL. |

Open every URL before publishing and confirm that it reaches the intended public brand profile. Remove tracking parameters, temporary login links, and profiles the store no longer maintains.

## Shopify attribution and store-owner login

The footer preview includes **Powered by Shopify** and **Are you the store owner? Log in here**. These labels are normally controlled by the theme's language translations rather than by fields in this section. The login link is intended for the store owner and does not grant storefront access to customers.

If the wording is translated, keep the meaning of the store-owner prompt and login action clear. Test the link in a private browser window and never place an admin password or storefront password in the footer text, social fields, screenshot, or public documentation.

## Example configuration

| Setting | Value shown in the screenshot |
| --- | --- |
| Color scheme | Dark green footer scheme |
| Show social media icons | On |
| Padding top | `32 px` |
| Padding bottom | `32 px` |
| Visible icons in the preview | Facebook, Instagram, YouTube |

The social values in the screenshot are demonstration data. Replace every example or placeholder with the store's own verified profile URL before publishing.

## Before publishing

1. Replace `1`, `2`, `3`, and all Shopify example profiles with the store's own complete URLs.
2. Leave every unused social platform field blank.
3. Open each link and confirm that it reaches the correct public profile.
4. Check the footer background, text, icons, links, hover states, and focus indicators for sufficient contrast.
5. Review spacing and wrapping at desktop and mobile widths.
6. Test every visible icon and the store-owner login link with a pointer, keyboard, and touch input.
7. Confirm that social icons have accessible platform names and visible keyboard focus.
8. Save the theme and complete a final check in a private browser window.
