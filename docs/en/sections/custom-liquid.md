# Custom Liquid

Use **Custom Liquid** to add small amounts of HTML, Liquid output, or existing theme snippets in the editor. It suits simple dynamic content that existing sections cannot provide, but it is not a replacement for full theme development or an app.

![Custom Liquid settings and storefront preview](/images/en/custom-liquid.svg)

::: warning Back up first
Invalid Liquid can hide the section or break the page layout. Duplicate the theme and keep a working copy of the code before editing.
:::

## Add the section

Open the required template in **Online Store > Themes > Customize**, click **Add section > Custom Liquid**, choose its width, enter the code, set colors and spacing, test desktop and mobile, then click **Save**.

## Color scheme and width

**Color scheme** controls the background and theme-aware text and links. Hard-coded colors may not follow the scheme, so prefer theme classes and CSS variables and test light and dark variants.

- **Fixed width** keeps content inside the theme page container.
- **Full width** extends the outer section across the available page width.

Internal fixed widths, maximum widths, and margins can still prevent custom content from filling a full-width section.

## Custom liquid

Liquid executes while Shopify renders the storefront and outputs HTML:

- <code v-pre>{{ ... }}</code> outputs an object property or expression.
- `{% ... %}` performs conditions, loops, assignments, and snippet rendering.
- `| filter` formats, escapes, or transforms output.

### Simple text

```liquid
<div class="rte">
  <p>Add your supporting information here.</p>
</div>
```

### Product vendor

```liquid
{% if product %}
  <p>Brand: {{ product.vendor | escape }}</p>
{% endif %}
```

### Existing snippet

```liquid
{% render 'snippet-name' %}
```

The named file must exist under `snippets`, and any object it requires must be available on the current template.

## Template context

Available objects depend on placement: product templates usually provide `product`, collections provide `collection`, article templates provide `article` and `blog`, and standard pages provide `page`. Guard template-specific objects with conditions and test every template where the section appears.

## Appropriate uses

- Small static HTML or supporting copy.
- Simple content based on the current template object.
- Tested snippets already included in the theme.
- Basic conditions, loops, and formatted output.
- Compatible code explicitly supplied by an app developer.

Do not use it for a complete section architecture, `{% schema %}`, unknown or obfuscated scripts, secrets or tokens, large repeated CSS/JavaScript, or features already supplied as an App block or App embed.

## Output safety

Escape variable data when it should appear as plain text:

```liquid
{{ product.title | escape }}
```

Do not place untrusted content directly into executable HTML, attributes, URLs, CSS, or JavaScript. Review the source, performance, privacy policy, and consent requirements of any third-party resource.

## Padding and Custom CSS

**Padding Top / Bottom** control section spacing in `px`. Check the custom markup for its own margins and padding to avoid duplicated whitespace.

Use the section's **Custom CSS** field for small local styling changes instead of repeatedly adding `<style>` tags. Scope rules with a unique class:

```css
.custom-note {
  max-width: 48rem;
  margin-inline: auto;
}
```

## Troubleshooting

- **No output**: check conditions, object availability, tag syntax, and snippet names; replace the code temporarily with plain HTML.
- **Broken layout**: check closing tags, fixed widths, negative margins, absolute positioning, and Full width conflicts.
- **Works on only some pages**: add existence checks for template-specific objects.
- **Editor differs from storefront**: test the saved storefront across markets, languages, sign-in states, privacy consent, and device widths.

## Before publishing

Back up the theme; validate Liquid, HTML, and quotes; guard template objects; escape text output; remove secrets and unknown scripts; test both widths, color schemes, keyboard interaction, spacing, languages, markets, resource data, privacy behavior, and performance. Save, then repeat the complete test on the actual storefront.

## Shopify references

- [Liquid reference](https://shopify.dev/docs/api/liquid)
- [Theme architecture](https://shopify.dev/docs/storefronts/themes/architecture)
- [Snippets](https://shopify.dev/docs/storefronts/themes/architecture/snippets)
- [Customizing sections](https://help.shopify.com/en/manual/online-store/themes/customizing-themes/theme-editor/customizing-sections)
