# Video Banner

The **Video Banner** displays Shopify-hosted video or a YouTube/Vimeo video with optional subheading, heading, and supporting text. Use it for brand stories, demonstrations, event previews, and product use cases.

![Video Banner settings and storefront preview](/images/en/video-banner.svg)

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
