# Video Banner

The **Video Banner** displays Shopify-hosted video or a YouTube/Vimeo video with optional subheading, heading, and supporting text. Use it for brand stories, demonstrations, event previews, and product use cases.

![Video Banner settings and storefront preview](/images/en/video-banner.png)

## Add the section

Open a template in the theme editor, click **Add section > Video Banner**, choose a hosted or external video, configure mobile media, cover image, ratio and playback, add overlay copy, set spacing, and click **Save**.

## Video sources

### Shopify-hosted video

Choose the primary desktop video or connect a dynamic source. Trim and compress it before uploading, and never include confidential or personal material in a storefront-accessible file.

### Mobile video

Optionally provide a smaller, narrow-screen composition. When set, it replaces the desktop hosted video on mobile. Keep key products, people, and text inside a safe central area.

### External video URL

Enter a public YouTube or Vimeo URL. It is used only when no Shopify-hosted video is selected. Confirm embedding, region, age, thumbnail, caption, and privacy settings.

The source priority is: Mobile video on mobile → Shopify-hosted video → External URL → cover image or empty state.

## Cover image and layout

Use a representative **Cover image** with the same ratio as the container. It remains important when autoplay is blocked, data saving is enabled, loading is slow, or playback fails.

**Aspect ratio** options:

- **16:9** for common landscape video.
- **4:3** for a taller landscape composition.
- **1:1** for square and mobile-oriented content.

Use **Page width** for the normal page container or **Full width** for an edge-to-edge presentation. Check cropping, quality, rounded edges, and text safe areas on mobile.

## Playback

- **Autoplay**: may be blocked by the browser and must start muted.
- **Loop**: best for short, seamless background clips.
- **Muted**: initial sound state; provide captions for important audio.
- **Show controls**: play, pause, progress, and volume controls as supported by the source.
- **Show play button**: keep this visible when autoplay is off.
- **Show mute button**: a separate control for Shopify-hosted video only.

Never disable autoplay, controls, and the play button together, or visitors may have no discoverable way to start the video.

## Content

- **Subheading**: a short category, duration, or prompt.
- **Heading**: the main description of the video.
- **Text**: brief supporting information or the key meaning when watched without sound.
- **Text alignment**: left, center, or right.

Keep copy away from important imagery and captions. Avoid long paragraphs or complex lists over video, and test all store languages.

## Color, spacing, and CSS

**Color scheme** affects background, overlay text, and controls. Check contrast against changing video brightness, the cover image, and failure states.

Use **Padding top / bottom** in `px`; full-width video usually needs less additional whitespace. Scope any **Custom CSS** to this section and retest every ratio, width, and playback state after theme updates.

## Accessibility and performance

- Provide accurate captions and a transcript when needed.
- Do not communicate essential information through sound alone.
- Avoid rapid flashes.
- Keep play, pause, and volume keyboard accessible with visible focus.
- Prevent overlay copy from covering captions.
- Compress short videos and provide a lighter mobile version.
- Review third-party requests, cookies, and consent.

## Example

| Setting | Example |
| --- | --- |
| Aspect ratio | `16:9` |
| Container width | `Page width` |
| Autoplay / Loop | Off / Off |
| Muted | On |
| Controls / Play / Mute buttons | On |
| Subheading | `Product demonstration` |
| Heading | `See how it is designed and used` |
| Text | `Play the video to explore the main features.` |
| Text alignment | Center |
| Padding | `32 px / 32 px` |

## Before publishing

Test source priority, actual mobile replacement, every ratio and width, allowed and blocked autoplay, cover and play states, all playback switches, keyboard controls, captions, text contrast, slow networks, YouTube/Vimeo embedding and privacy, custom CSS isolation, and the complete desktop/mobile playback flow.

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/video-banner.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Video banner

Has presets for the Add section picker.

`disabled_on`: &#123;"groups": ["header", "footer", "custom.overlay"]&#125;

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-2 | — |
| Section height<br>`section_height` | select | adapt | Adapt to media (`adapt`); Small (`small`); Medium (`medium`); Large (`large`); Full screen (`full`) |

### Video

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Shopify-hosted video<br>`video` | video | Not declared | — |
| Mobile video<br>`video_mobile` | video | Not declared | info: Optional. If set, this video replaces the desktop video on mobile screens. |
| External video URL<br>`external_video_url` | video_url | https://www.youtube.com/watch?v=_9VUPq3SxOc | info: YouTube or Vimeo URL. Only shown when no Shopify-hosted video is selected above.<br>accept: ["youtube", "vimeo"] |
| Cover image<br>`poster` | image_picker | Not declared | — |
| Aspect ratio<br>`aspect_ratio` | select | 16/9 | 16:9 (`16/9`); 4:3 (`4/3`); 1:1 (`1/1`) |
| Container width<br>`container_width` | select | page | Page width (`page`); Full width (`full`) |

### Playback

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Autoplay<br>`autoplay` | checkbox | false | — |
| Loop<br>`loop` | checkbox | false | — |
| Muted<br>`muted` | checkbox | true | info: Autoplay videos are always muted to comply with browser policies. |
| Show controls<br>`controls` | checkbox | true | — |
| Show play button<br>`show_play_button` | checkbox | true | — |
| Show mute button (Shopify-hosted video only)<br>`show_mute_button` | checkbox | false | — |

### Padding

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Padding top<br>`padding_top` | range | 32 | 0–100 px; step 4 |
| Padding bottom<br>`padding_bottom` | range | 32 | 0–100 px; step 4 |

<!-- latest-schema:end -->
