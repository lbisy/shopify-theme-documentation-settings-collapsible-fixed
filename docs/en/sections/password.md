# Password

The **Password** section is the main content area of the store's password template. Use it to announce an upcoming launch and collect email sign-ups while storefront access is restricted. This section controls the central heading, message, and subscription form; it does not set or change the store password.

![Password section settings and storefront preview](/images/en/password.png)

## Open the Password section

1. In **Shopify Admin**, go to **Online Store → Themes**.
2. Click **Customize** for the theme you want to edit.
3. Open the template selector at the top of the editor and choose **Password**.
4. Under **Template**, select **Password**. Do not confuse it with **Password header** or **Password footer**.
5. Configure the settings while checking the storefront preview.
6. Click **Save**.

The password template is normally available only while password protection is enabled or while previewing that template in the theme editor.

## Color scheme

Select the global color scheme used by the section. It controls the section background, heading and message colors, form styling, button colors, borders, and other theme-defined states.

Click **Edit scheme** to change the selected global scheme. Because a color scheme can be shared by multiple sections, editing it may affect other areas of the store. Check the contrast of normal text, placeholder text, input borders, buttons, focus rings, and validation messages after making changes.

## Heading

Enter the main launch message, such as `Opening soon`. Keep it short so it remains readable on mobile and does not push the subscription form too far down the page.

The dynamic-source icon can be used when a compatible source is available. If the store supports multiple languages, translate the heading instead of placing several languages in the same field.

## Message

Add supporting copy that explains what visitors can expect and why they should subscribe. The rich-text editor supports basic formatting such as bold, italic, links, and lists, and it can use a compatible dynamic source.

Use concise, specific wording. Do not promise a launch date, discount, or exclusive offer unless the store can honor it. If subscribing has legal or promotional conditions, link to the relevant privacy or terms page.

## Email placeholder

Set the hint shown inside the email field, for example `Email` or `Enter your email address`. A placeholder should be brief and should not contain important consent information because it disappears after the visitor starts typing.

This setting changes only the field placeholder. The subscribe button label and form success or error messages are normally managed through the theme's language translations.

## Padding

- **Padding top** controls the space above the heading and form.
- **Padding bottom** controls the space below the form before the password footer.

The screenshot uses `32 px` for both values. Matching values are a reliable starting point, but the final spacing should be checked on desktop and mobile, especially when the message wraps onto multiple lines.

## Custom CSS

Use **Custom CSS** for small, section-specific adjustments that are not available through the built-in settings. Prefer the section controls and global theme settings first. Keep selectors scoped to this section, avoid hiding labels or validation messages, and verify the result after theme updates.

## Subscription form behavior

- Test the form with valid, invalid, and duplicate email addresses.
- Confirm successful submissions are recorded in the expected Shopify customer or email-marketing records.
- Check that loading, success, and error feedback remain visible and understandable.
- Verify keyboard focus order and submit the form with the `Enter` key.
- Review the mobile soft keyboard, field width, and button layout.
- Keep privacy and consent language appropriate for every region where the store operates.

The **Enter using password** link shown at the top of the preview belongs to the **Password header** section. Social links, Shopify attribution, and the store-owner login link belong to the **Password footer** section.

## Example configuration

| Setting | Value shown in the screenshot |
| --- | --- |
| Color scheme | Light section scheme |
| Heading | `Opening soon` |
| Message | `Be the first to know about new collections and exclusive offers.` |
| Email placeholder | `Email` |
| Padding top | `32 px` |
| Padding bottom | `32 px` |

## Before publishing

1. Replace all default copy and translate the heading, message, placeholder, button, and form feedback.
2. Check text, input, button, border, and focus-ring contrast in the selected color scheme.
3. Test the subscription form with real validation and confirm the resulting record in Shopify Admin.
4. Review the layout at desktop and mobile widths, including long translated text.
5. Test the page using only a keyboard and confirm the email field has an accessible name.
6. Verify privacy links, consent wording, and promotional claims.
7. Confirm the password-entry link works and that the password header and footer are configured consistently.
8. Save the theme, open the password page in a private browser window, and complete one final end-to-end test.
