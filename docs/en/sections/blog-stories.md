# Blog Stories

The **Blog Stories** section presents selected articles on a standard page or homepage. It can include a heading, introduction, and multiple Article cards for product stories, guides, brand news, or industry content.

![Blog Stories settings and storefront preview](/images/en/blog-stories.png)

## Prepare articles

Under **Shopify admin > Content > Blog posts**, complete each article's title, body, excerpt, featured image, author, tags, search information, blog assignment, visibility, and publication date. Use consistent image ratios and reasonably similar title and excerpt lengths.

## Add the section

Open a template, click **Add section > Blog Stories**, choose the Blog, add the section heading and description, then add and configure **Article** blocks.

## Section settings

- **Color Scheme**: background, heading, description, article information, and reading links.
- **Heading size** and **Heading**
- **Subtitle size** and **Description**
- **Blog**: the Shopify blog associated with the section.
- **Padding Top / Bottom**

Use one or two sentences to explain what readers will find. If expected articles are missing, verify the blog assignment, visibility, publication date, and block configuration.

## Article blocks

Each block represents an article card, usually including a featured image, supporting information, title, and reading link. Reorder, hide, duplicate, or remove blocks in the left panel.

- Use a different article in each block.
- Put the newest or most important first.
- Use clear, consistently proportioned images.
- Write accurate, non-clickbait titles.
- Keep reading-link labels consistent.
- Keep categories and supporting copy brief.

If placeholders remain, complete both the Shopify article and its Article block before publishing.

## Content guidance

Keep card image ratios consistent and important subjects in safe crop areas. Preserve a real text title rather than embedding the only title in the image. Excerpts should explain the value without duplicating the full opening. Image, title, and link must lead to the same article. Add accurate alt text and support any product, environmental, or customer claims.

## Example

| Setting | Example |
| --- | --- |
| Heading size | `2XL` |
| Heading | `Product stories and practical guides` |
| Subtitle size | `Large` |
| Description | `Explore new designs, useful tips, and brand updates.` |
| Articles | Design story; Daily-use guide; Materials and craft |
| Padding | `32 px / 32 px` |

## Before publishing

Verify the Blog and article visibility; remove default copy; confirm unique article blocks; review image quality, ratio, crop, and alt text; compare card information with article content; test every image, title, and reading link; test different card counts and responsive layouts; check keyboard focus, contrast, and spacing; then save and browse the actual storefront.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/blog-stories.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Blog stories

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |

### Font

### Heading

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`heading_size` | select | title-2xl | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |
| Heading<br>`heading` | inline_richtext | Product stories, updates, and useful insights. | — |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Description<br>`description` | richtext | &lt;p&gt;Introduce the stories, guides, or updates featured in this section.&lt;/p&gt; | — |
| Blog<br>`blog` | blog | Not declared | — |
| Articles to show<br>`articles_limit` | range | 3 | 1–12 ; step 1<br>visible_if: &#123;&#123; section.settings.blog &#125;&#125; |
| Link text<br>`link_text` | text | Read more | visible_if: &#123;&#123; section.settings.blog &#125;&#125; |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

### Block: Article

`type`: `article`

#### Font

#### Title

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Heading size<br>`card_title_size` | select | title-m | 4X large (`title-4xl`); 3X large (`title-3xl`); 2X large (`title-2xl`); Extra large (`title-xl`); Large (`title-l`); Medium (`title-m`); Small (`title-s`); Extra small (`title-xs`) |

#### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`card_subtitle_size` | select | copy-l | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Image<br>`image` | image_picker | Not declared | — |
| Subtitle<br>`subtitle` | inline_richtext | Article category | — |
| Title<br>`title` | inline_richtext | Article title | — |
| Link<br>`link` | url | Not declared | — |
| Link text<br>`article_link_text` | text | Read more | — |

<!-- latest-schema:end -->
