# Before After Comparison

The **Before After Comparison** section overlays two images and reveals the difference with a draggable divider. Use it for product results, renovations, repairs, material treatments, or design comparisons.

![Before After Comparison settings and storefront preview](/images/en/before-after-comparison.png)

## Add the section

Open a template, click **Add section > Before After Comparison**, upload the Before and After images, configure headings, labels, image ratio, and spacing, then click **Save**.

## Text and color

**Color Scheme** affects the background, headings, image labels, and comparison control. Make every control and label visible over both light and dark parts of the images.

- **Heading size** and **Heading**: the primary comparison title.
- **Subtitle size** and **Sub Heading**: optional supporting title.

Both text fields support rich text, links, and dynamic sources. Keep them concise, remove unused defaults, and check wrapping on mobile.

## Images

**Image ratio** controls the shared container. **Wide (16:9)** suits landscapes, interiors, and wide products. Fixed ratios can crop edges.

Use the same dimensions, ratio, camera position, focal length, lighting, background, and subject placement for **Before Image** and **After Image**. Do not pre-apply labels or borders that conflict with the section controls.

::: tip Image preparation
The more consistent the two source images are, the easier it is to judge the actual change and the smoother the divider feels.
:::

## Labels and interaction

Set **Before Label** and **After Label** to a clear pair such as `BEFORE / AFTER` or `Before treatment / After treatment`.

The handle must contrast with both images, avoid covering important subjects or labels, remain large enough to touch, and move continuously without scaling or shifting the sources. Horizontal dragging should not seriously interfere with vertical page scrolling.

## Padding and compliance

Use **Padding Top / Bottom** in `px`. Revisit mobile spacing when headings wrap onto more lines.

Use real, verifiable comparisons and do not exaggerate results through different lighting, angles, or editing. Beauty, health, and performance claims must comply with local rules and may require a results disclaimer. Obtain permission for people and copyrighted images, and write descriptive alt text for both states rather than only “Before” and “After.”

## Before publishing

Confirm image order and alignment; drag fully from edge to edge; test mouse, touch, and keyboard controls; verify focus and contrast; check cropping in every ratio; test long, absent, and translated headings/labels; then save and repeat desktop and mobile tests on the live storefront.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/before-after-comparison.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Before/after comparison

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
| Heading<br>`heading` | inline_richtext | Compare every detail | — |

### Subtitle

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Subtitle size<br>`subtitle_size` | select | copy-xl | Extra large (`copy-xl`); Large (`copy-l`); Default (`copy-m`); Small (`copy-s`) |
| Subheading<br>`sub_heading` | inline_richtext | Before and after | — |
| Image ratio<br>`image_ratio` | select | 16/9 | Adapt to image (`auto`); Wide (16:9) (`16/9`); Landscape (4:3) (`4/3`); Square (1:1) (`1/1`) |
| Before image<br>`before_img` | image_picker | Not declared | — |
| After image<br>`after_img` | image_picker | Not declared | — |
| Before label<br>`before_label` | text | Before | — |
| After label<br>`after_label` | text | After | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
