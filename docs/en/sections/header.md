# Header

<!-- latest-schema:start -->
## Latest package settings reference

::: warning Version reference
Generated from the schema in `sections/header.liquid` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.
“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.
[Full audit](/en/version-audit)
:::

Open: Theme editor → relevant template or section group → Header

No presets declared; do not assume this can be added freely through Add section.

`enabled_on`: &#123;"groups": ["header"]&#125;

`limit`: 1

### Header

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Logo position<br>`logo_position` | select | left | Left (`left`); Middle (`middle`); Middle center (`middle-center`)<br>info: Edit your logo in theme settings (`/editor?context=theme&amp;category=logo`) |

### Color

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Color scheme<br>`color_scheme` | color_scheme | scheme-1 | — |
| Menu color scheme<br>`menu_color_scheme` | color_scheme | scheme-1 | — |
| Mobile menu color scheme<br>`mobile_menu_color_scheme` | color_scheme | scheme-1 | — |
| Menu<br>`menu` | link_list | main-menu | — |

### Menu type

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Menu type<br>`menu_type` | select | dropdown | Dropdown menu (`dropdown`); Super menu (`super`) |
| Desktop menu trigger<br>`desktop_menu_trigger` | select | hover | Hover (`hover`); Click (`click`) |
| Super menu watermark<br>`super_menu_watermark_text` | text | Your brand | visible_if: &#123;&#123; section.settings.menu_type == 'super' &#125;&#125; |
| Enable product series tabs<br>`enable_super_menu_series` | checkbox | false | visible_if: &#123;&#123; section.settings.menu_type == 'super' &#125;&#125; |
| Product series layout<br>`super_menu_series_layout` | select | left-right | Left / Right (`left-right`); Top / Bottom (`top-bottom`)<br>visible_if: &#123;&#123; section.settings.menu_type == 'super' and section.settings.enable_super_menu_series &#125;&#125; |
| Super menu left column width<br>`super_menu_primary_width` | range | 42 | 30–70 %; step 1<br>visible_if: &#123;&#123; section.settings.menu_type == 'super' and section.settings.enable_super_menu_series &#125;&#125; |
| Series collection 1<br>`super_collection_1` | collection | Not declared | — |
| Series collection 2<br>`super_collection_2` | collection | Not declared | — |
| Series collection 3<br>`super_collection_3` | collection | Not declared | — |
| Products per series<br>`super_series_products_limit` | range | 6 | 3–12 ; step 1<br>visible_if: &#123;&#123; section.settings.menu_type == 'super' and section.settings.enable_super_menu_series &#125;&#125; |

### Localization

| Editor label / ID | Type and action | Default | Options / range / conditions |
| --- | --- | --- | --- |
| Country/region selector<br>`enable_country_selector` | checkbox | true | info: Manage countries/regions (`/admin/settings/markets`) |
| Language selector<br>`enable_language_selector` | checkbox | true | info: Manage languages (`/admin/settings/languages`) |

<!-- latest-schema:end -->
