<!-- unlinked-document:start
文档显示状态：未在主页或目录中显示，且未被其他页面有效引用。
核对说明：已注释的目录入口和页面链接不计入有效引用；已排除构建的页面不作为引用来源。
保留正文供后续维护，此标记仅作为源码注释。
unlinked-document:end -->

# Announcement bar

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/announcement-bar.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
:::

Open: Theme editor → relevant template or section group → Announcement bar

Has presets for the Add section picker.

`enabled_on`: &#123;"groups": ["header"]&#125;

`limit`: 1

`max_blocks`: 6

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-1 | — |
| Text<br>`text` | inline_richtext | See More | — |
| Link<br>`link` | url | Not declared | — |

### Public settings

Only displayed on large screens

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Social icon<br>`show_social` | checkbox | false | info: Manage social accounts (`/editor?context=theme&amp;category=social%20icon`) |
| Country/region selector<br>`enable_country_selector` | checkbox | false | info: Manage countries/regions (`/admin/settings/markets`) |
| Language selector<br>`enable_language_selector` | checkbox | false | info: Manage languages (`/admin/settings/languages`) |

### Block: Announcement

`type`: `announcement`

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Text<br>`announcement_text` | inline_richtext | Welcome to our store! | — |

<!-- latest-schema:end -->
