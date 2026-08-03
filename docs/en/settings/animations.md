# Animations

The **Animations** settings control how content and media appear as they enter the viewport. Thoughtful motion can guide attention and add rhythm, while excessive or repeated motion can distract visitors or reduce perceived performance.

## Open the Animations settings

1. In Shopify admin, go to **Online Store > Themes**.
2. Find the theme you want to edit and click **Customize**.
3. Open **Theme settings > Animations**.

![Animations settings and storefront preview](/images/en/settings/animations.png)

The example above enables motion, reveals content with **Rise**, reveals media with **Zoom**, uses **Normal** speed, and replays animations when elements re-enter the viewport.

## Animation settings

| Setting | Value shown | What it controls |
| --- | ---: | --- |
| **Enable motion** | **On** | Master switch for page reveal animations. When off, content appears immediately. |
| **Content reveal style** | **Rise** | How headings, text, buttons, and other content appear. **Rise** combines a fade with slight upward movement. |
| **Media reveal style** | **Zoom** | How images, video, and other media appear. **Zoom** combines a fade with subtle scaling. |
| **Motion speed** | **Normal** | Overall reveal timing. Available speed choices are **Slow**, **Normal**, and **Fast**. |
| **Reveal behavior** | **Replay on re-enter** | Replays a reveal whenever an element leaves and later re-enters the viewport. |

Disabling **Enable motion** prevents reveal animation from delaying content; it does not hide the content.

## Content and media reveal styles

Content and media are configured separately so the page can use different levels of emphasis.

- **None** displays the element immediately without a reveal effect.
- **Fade** changes opacity gradually and is usually the least distracting animated option.
- **Rise** adds slight upward movement to content as it fades in.
- **Zoom** adds subtle scaling to media as it fades in.

The screenshot combination—**Rise** for content and **Zoom** for media—creates a more expressive presentation. Preview image-heavy sections, product grids, slideshows, and large banners carefully because many simultaneous zoom effects can compete for attention.

## Speed and reveal behavior

- **Slow** creates a relaxed, atmospheric pace but delays the final state longer.
- **Normal** balances motion with responsiveness for most storefronts.
- **Fast** completes reveals quickly and can suit content-dense pages.

For **Reveal behavior**:

- **Once** plays each reveal the first time the element enters the viewport.
- **Replay on re-enter** plays it again whenever the element re-enters the viewport.

Use **Once** for long pages, product grids, and reading-focused layouts. Use **Replay on re-enter** only when repeated movement remains intentional and does not interfere with browsing.

## Reduced motion and performance

Visitors who request reduced motion through their device or browser should see content immediately. Content should also appear immediately when page motion is disabled.

Test animation performance on real mobile devices and image-heavy pages. Look for delayed first content, scrolling stutter, layout shifts, and several sections animating at the same time. Motion should support the content rather than make the interface feel slower.

## Recommended adjustment order

1. Enable motion and choose the content reveal style.
2. Choose a separate media reveal style.
3. Set a speed that feels responsive.
4. Decide whether reveals should play once or replay on re-entry.
5. Preview long pages, dense product grids, and mobile layouts.
6. Test with reduced-motion preferences enabled.

The screenshot values (**Rise**, **Zoom**, **Normal**, and **Replay on re-enter**) create a noticeable, repeatable motion style. For a quieter storefront, switch the behavior to **Once** or use **Fade** for one or both reveal styles.

## Save and test

Click **Save**, then check:

- Above-the-fold content appears promptly.
- Text, buttons, images, and videos reveal smoothly.
- Product grids do not stutter while scrolling.
- Replayed animations do not distract when scrolling back and forth.
- Mobile scrolling remains responsive.
- Keyboard focus is not moved or obscured by animation.
- Reduced-motion mode and disabled motion show all content immediately.
