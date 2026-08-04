# Page

The **Page** template displays standard Shopify pages such as About, shipping information, size guides, FAQs, and store policies. Create and save the page resource in Shopify Admin first, then open it from **Pages** in the theme editor's page selector to configure the template layout.

Page content and page layout are managed in different places:

- **Shopify Admin → Online Store → Pages** stores the page title, body content, visibility, search-engine listing, URL handle, and assigned theme template.
- **Online Store → Themes → Customize** controls the layout and presentation of the assigned template, including its sections and theme-provided settings.

## 1. Create the page

1. In **Shopify Admin**, go to **Online Store → Pages**.
2. Click **Add page**.
3. Enter a clear **Title**.
4. Add the page body in the rich-text **Content** editor.
5. Under **Visibility**, choose whether to publish the page immediately, keep it hidden, or schedule publication where available.
6. Under **Online store**, choose a **Theme template**. Use the default page template unless this page needs a separate layout.
7. Review the search-engine listing and URL handle when necessary.
8. Click **Save**.

Creating a visible page does not automatically add it to the storefront navigation. Add the saved page to the appropriate header or footer menu when customers need a navigation link to it.

## 2. Open the page in the theme editor

1. Go to **Online Store → Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Click the page selector at the top of the editor. It displays **Home page** when the editor first opens.
4. Select **Pages**, as shown below.
5. Choose the required page or its assigned page template. Use **Search online store** when the list is long.
6. Confirm that the preview shows the intended page title and content.
7. In the template panel, select **Page** to review the settings supplied by the current theme.
8. Add, remove, hide, or reorder other supported sections when needed, then click **Save**.

![Select Pages from the theme editor page selector](/images/en/page.png)

The page selector changes the resource or template being previewed; it does not move or copy the page content into the theme editor. The Page section reads the current page resource automatically.

## Page content

The main page title and body should be edited on the page record in Shopify Admin. The Page section renders that resource inside the assigned template.

For reliable content:

- Use one descriptive page title and organize long content with meaningful subheadings.
- Keep heading levels in a logical order instead of using heading formatting only for visual size.
- Add descriptive link text rather than labels such as `Click here`.
- Add alt text to informative images and leave it blank only for purely decorative images.
- Avoid pasting unsupported scripts, forms, or complex styling into the rich-text editor.
- Preview tables, embedded media, and long links at mobile widths.

Changes to the page title or body affect only that page. Changes to the assigned template's sections or layout affect every page using that same template.

## Page section and template layout

Select the built-in **Page** section to adjust any presentation controls exposed by the installed theme version. These controls can affect the page container, color scheme, spacing, or section-specific styling, but the page title and body still come from the saved page resource.

Additional theme sections can be placed before or after the Page section to create a richer layout. Keep the Page section enabled when the page's title and rich-text body need to appear. If it is hidden or removed, the page record can still exist while its main content is absent from the storefront template.

Always check whether a setting is global or template-specific. Editing a shared color scheme can affect other templates, while adding or reordering a section affects every page assigned to the current page template.

## Use a separate template for a unique layout

Pages assigned to the same template share the same section structure and template settings. If one page needs a different hero, section order, spacing, or supporting content, create a dedicated page template instead of changing the shared default template.

1. In the theme editor, open the top page selector and choose **Pages**.
2. Click **Create template**.
3. Enter a unique template name and choose an existing page template to use as the starting point.
4. Create the template, arrange its sections, and click **Save**.
5. Return to **Shopify Admin → Online Store → Pages** and open the target page.
6. Under **Online store → Theme template**, assign the new template and save the page.
7. Return to the theme editor and preview that page again.

::: warning Template availability
The **Theme template** list on a page record is based on templates available in the published theme. A template created only in an unpublished theme might not be assignable from the page record until that theme is published. Continue previewing it in the draft theme and verify the assignment during publication.
:::

## Visibility, URL, and navigation

These controls are related but independent:

- **Visibility** determines whether the page is published to the online store.
- The **URL handle** determines the page address, normally under `/pages/`.
- The **Theme template** determines the page layout.
- **Menus** determine whether customers can reach the page from storefront navigation.

A page can therefore be visible and accessible by direct URL but absent from every menu. When changing a URL handle, review inbound links, menus, campaigns, and redirects so existing links do not lead to a 404 page.

## Troubleshooting

- **The page is missing from the selector:** save the page first, search for its title, confirm it belongs to the online store, and reload the theme editor.
- **The wrong content appears:** confirm the preview resource and the template assigned to that page.
- **A layout change affected several pages:** those pages share a template; create and assign a separate template for the page that needs a unique layout.
- **The page exists but customers cannot find it:** confirm it is visible and add it to the appropriate menu.
- **The title or body is missing:** confirm the Page section is enabled and edit the content on the page record, not only in the theme editor.
- **A new template is absent from the page's template list:** confirm that it is a Page template and that it exists in the published theme.

## Before publishing

1. Confirm the correct page resource and theme template are paired.
2. Check the title, body, links, images, alt text, tables, and embedded media.
3. Preview all pages that share the edited template.
4. Review desktop and mobile width, spacing, text contrast, and heading hierarchy.
5. Test the public URL and every menu link that points to the page.
6. Confirm hidden or scheduled pages are not exposed before the intended time.
7. Save the page record, menu changes, and theme customizations.

For more details, see Shopify's guides to [creating pages](https://help.shopify.com/en/manual/online-store/add-edit-pages) and [working with templates](https://help.shopify.com/en/manual/online-store/themes/theme-structure/templates).
