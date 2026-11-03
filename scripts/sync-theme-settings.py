"""Document schema declarations without executing anything from a theme archive."""
import argparse
import hashlib
import html
import json
import re
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- latest-schema:start -->'
END = '<!-- latest-schema:end -->'


def parse(text):
    return json.loads(re.sub(r'^\s*/\*.*?\*/', '', text, flags=re.S))


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('archive', type=Path)
    args = parser.parse_args()
    archive_bytes = args.archive.read_bytes()
    records = []
    with zipfile.ZipFile(args.archive) as archive:
        locale = parse(archive.read('locales/en.default.schema.json').decode('utf-8-sig'))

        missing_translations = set()

        def translate(value):
            if not isinstance(value, str) or not value.startswith('t:'):
                return value
            found = locale
            for key in value[2:].split('.'):
                found = found.get(key, {}) if isinstance(found, dict) else {}
            if isinstance(found, str):
                return found
            missing_translations.add(value)
            return value

        def cell(value):
            if isinstance(value, str):
                value = translate(value)
            else:
                value = json.dumps(value, ensure_ascii=False)
            # Shopify admin-relative links are not routes in this documentation site.
            value = re.sub(r'\[([^\]]+)\]\((/[^)]+)\)', r'\1 (`\2`)', value)
            return (html.escape(value, quote=False).replace('|', '&#124;').replace('\n', '<br>')
                    .replace('{', '&#123;').replace('}', '&#125;'))

        groups = parse(archive.read('config/settings_schema.json').decode('utf-8-sig'))
        metadata = groups[0]
        for group in groups:
            if group.get('name') == 'theme_info':
                continue
            name = translate(group['name'])
            records.append(dict(kind='settings', slug=slug(name), name=name,
                                source='config/settings_schema.json', schema=group))
        for filename in sorted(archive.namelist()):
            if not filename.startswith('sections/') or not filename.endswith('.liquid'):
                continue
            source = archive.read(filename).decode('utf-8-sig')
            match = re.search(r'{%\s*-?\s*schema\s*-?\s*%}(.*?){%\s*-?\s*endschema\s*-?\s*%}', source, re.S)
            if not match:
                raise ValueError(f'Missing schema: {filename}')
            schema = parse(match[1])
            records.append(dict(kind='sections', slug=Path(filename).stem,
                                name=translate(schema.get('name', Path(filename).stem)),
                                source=filename, schema=schema))

        def table(settings, zh, level=3):
            lines = []
            rows = []

            def flush():
                if rows:
                    lines.extend((['| 设置项（后台名称） / ID | 类型与操作 | 默认值 | 可选值 / 范围 / 条件 |',
                                   '| --- | --- | --- | --- |'] if zh else
                                  ['| Editor label / ID | Type and action | Default | Options / range / conditions |',
                                   '| --- | --- | --- | --- |']))
                    lines.extend(rows)
                    lines.append('')
                    rows.clear()

            actions = {
                'checkbox': '勾选开启，取消关闭', 'select': '从选项中选择', 'radio': '选择一项',
                'range': '拖动滑块调整数值', 'text': '输入文字', 'textarea': '输入多行文字',
                'richtext': '编辑格式化文字', 'inline_richtext': '编辑行内格式化文字',
                'image_picker': '选择或上传图片', 'video': '选择视频', 'video_url': '填写视频地址',
                'url': '选择或填写链接', 'color': '选择颜色', 'color_background': '设置背景颜色或渐变',
                'color_scheme': '选择全局配色方案', 'font_picker': '选择字体',
                'product': '选择商品', 'product_list': '选择多个商品', 'collection': '选择商品系列',
                'collection_list': '选择多个商品系列', 'link_list': '选择菜单', 'page': '选择页面',
                'blog': '选择博客', 'article': '选择文章', 'liquid': '编辑 Liquid 内容',
                'color_scheme_group': '添加或编辑配色方案', 'number': '输入数值',
            }
            for setting in settings:
                typ = setting['type']
                if typ in ('header', 'paragraph'):
                    flush()
                    content = cell(setting.get('content', ''))
                    lines.extend(([f'{"#" * level} {content}', ''] if typ == 'header' else [content, '']))
                    continue
                details = []
                if 'options' in setting:
                    details.append('; '.join(f'{cell(o["label"])} (`{cell(o["value"])}`)' for o in setting['options']))
                if 'min' in setting or 'max' in setting:
                    details.append(f'{setting.get("min", "—")}–{setting.get("max", "—")} {cell(setting.get("unit", ""))}; ' +
                                   ('步长 ' if zh else 'step ') + str(setting.get('step', '—')))
                for key in ('info', 'placeholder', 'visible_if', 'limit', 'accept'):
                    if key in setting:
                        details.append(f'{key}: {cell(setting[key])}')
                label = cell(setting.get('label', setting.get('id', typ)))
                identifier = cell(setting.get('id', ''))
                default = cell(setting['default']) if 'default' in setting else ('未声明' if zh else 'Not declared')
                action = f'{typ}：{actions.get(typ, "按后台控件配置")}' if zh else typ
                rows.append(f'| {label}<br>`{identifier}` | {action} | {default} | {"<br>".join(details) or "—"} |')
                if 'definition' in setting:
                    flush()
                    lines.extend([f'{"#" * level} {label} / ' + ('方案内设置' if zh else 'Scheme fields'), ''])
                    lines.extend(table(setting['definition'], zh, level + 1))
                    if 'role' in setting:
                        lines.extend([('角色映射：' if zh else 'Role mapping: ') + cell(setting['role']), ''])
            flush()
            return lines

        report = []
        stats = {'global_groups': 0, 'sections': 0, 'settings': 0, 'block_types': 0}
        known_404 = {'Form background color', 'Form text color', 'Image', 'Image alt text', 'Button text', 'Success message'}
        for rec in records:
            stats['global_groups' if rec['kind'] == 'settings' else 'sections'] += 1
            schema = rec['schema']
            def count_fields(items):
                return sum((1 if 'id' in s else 0) + count_fields(s.get('definition', [])) for s in items)
            stats['settings'] += count_fields(schema.get('settings', []))
            stats['block_types'] += len(schema.get('blocks', []))
            stats['settings'] += sum(count_fields(b.get('settings', [])) for b in schema.get('blocks', []))
            for lang in ('zh', 'en'):
                zh = lang == 'zh'
                path = ROOT / 'docs' / lang / rec['kind'] / (rec['slug'] + '.md')
                existed = path.exists()
                original = path.read_text(encoding='utf-8') if existed else f'# {rec["name"]}\n'
                original = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', original, flags=re.S).rstrip()
                if original.strip() == f'# {rec["name"]}':
                    existed = False
                if rec['slug'] == '404' and rec['kind'] == 'sections':
                    for heading in known_404:
                        marker = ('安装包无此设置' if zh else 'Not declared in package')
                        original = re.sub(r'^(### ' + re.escape(heading) + r')(?:〔[^\n]*〕)?$',
                                          r'\1〔' + marker + '〕', original, flags=re.M)
                if rec['kind'] == 'settings' and rec['slug'] == 'animations':
                    for label in ('Content reveal style', 'Media reveal style', 'Motion speed', 'Reveal behavior'):
                        original = original.replace('**' + label + '**', '**' + label + '**' +
                                                    ('〔安装包无此设置〕' if zh else '〔Not declared in package〕'))
                    original = original.replace('**Enable motion**', '**Enable motion**' +
                                                ('〔新版名称：Scroll and reveal animations〕' if zh else '〔Current label: Scroll and reveal animations〕'))
                    # Keep repeat runs from duplicating inline annotations.
                    original = re.sub(r'(〔[^〕]+〕)(?:\1)+', r'\1', original)
                if rec['kind'] == 'settings' and rec['slug'] == 'layout':
                    original = original.replace('**Setting Small Border Radius**', '**Setting Small Border Radius**' +
                                                ('〔安装包无此设置〕' if zh else '〔Not declared in package〕'))
                    original = re.sub(r'(〔[^〕]+〕)(?:\1)+', r'\1', original)
                    if '<!-- latest-layout-note -->' not in original:
                        original += '\n\n<!-- latest-layout-note -->\n' + ('::: warning 旧版范围需更新\n上方 1000–1600 px 是旧说明；新版 Page width 范围为 1000–2000 px，默认 1600 px。Small Border Radius 未在新版 Layout 中声明；Page margin 是新版包实际提供的另一个设置项。\n:::' if zh else
                            '::: warning Update the old range\nThe current Page width range is 1000–2000 px with a 1600 px default. Small Border Radius is not declared in Layout; Page margin is declared instead.\n:::')
                lines = [START, '## ' + ('新版安装包设置项（核对清单）' if zh else 'Latest package settings reference'), '',
                         '::: warning ' + ('版本核对说明' if zh else 'Version reference'),
                         (f'依据 `latest.zip` 内 `{rec["source"]}` 的 schema 整理。后台名称保留安装包的英文原文；以下清单是本页设置范围的核对依据。上方旧说明和截图尚未逐项实机验证。' if zh else
                          f'Generated from the schema in `{rec["source"]}` inside `latest.zip`. This list defines the declared editor settings for this page. Earlier prose and screenshots have not been verified in a running store.'),
                         ('“未声明”表示 schema 没有指定默认值，不等于关闭。模板或已保存店铺的值可能与默认值不同。' if zh else
                          '“Not declared” means the schema supplies no default; it does not mean disabled. Templates and saved store values can differ.'),
                         f'[完整核对报告](/zh/version-audit)' if zh else '[Full audit](/en/version-audit)', ':::', '']
                if rec['kind'] == 'settings':
                    lines.extend([('入口：主题编辑器 → 主题设置 → ' if zh else 'Open: Theme editor → Theme settings → ') + rec['name'], ''])
                else:
                    lines.extend([('入口：主题编辑器 → 对应页面模板或分区组 → ' if zh else 'Open: Theme editor → relevant template or section group → ') + rec['name'], '',
                                  ('可通过“添加分区”添加（声明了 presets）。' if schema.get('presets') else '未声明 presets；不要据此假定可在任意页面通过“添加分区”添加。') if zh else
                                  ('Has presets for the Add section picker.' if schema.get('presets') else 'No presets declared; do not assume this can be added freely through Add section.'), ''])
                    for key in ('enabled_on', 'disabled_on', 'limit', 'max_blocks'):
                        if key in schema:
                            lines.extend([f'`{key}`: {cell(schema[key])}', ''])
                lines.extend(table(schema.get('settings', []), zh))
                if not schema.get('settings'):
                    lines.extend(['未声明分区级设置。' if zh else 'No section-level settings declared.', ''])
                for block in schema.get('blocks', []):
                    lines.extend([f'### ' + ('内容块：' if zh else 'Block: ') + cell(translate(block.get('name', block['type']))), '',
                                  f'`type`: `{cell(block["type"])}`' + (f'; `limit`: {block["limit"]}' if 'limit' in block else ''), ''])
                    lines.extend(table(block.get('settings', []), zh, 4))
                    if not block.get('settings'):
                        lines.extend(['此处未声明本地设置（应用或主题区块需查看其自身定义）。' if zh else 'No local settings declared here; app/theme blocks define their own controls.', ''])
                lines.append(END)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(original + '\n\n' + '\n'.join(lines) + '\n', encoding='utf-8')
                if lang == 'zh':
                    report.append((rec, existed))

        for lang in ('zh', 'en'):
            zh = lang == 'zh'
            lines = ['# ' + ('新版安装包与文档核对报告' if zh else 'Latest package documentation audit'), '',
                     f'`latest.zip` · {metadata.get("theme_name")} {metadata.get("theme_version")} · SHA-256: `{hashlib.sha256(archive_bytes).hexdigest()}`', '',
                     ('本次只读取压缩包中的设置定义、语言和源码，不执行其中的文件。未删除或注释旧文档，原说明保留供人工处理。' if zh else
                      'The archive was read as data only. Existing documentation is preserved for manual review.'), '',
                     ('## 范围与标记' if zh else '## Scope and labels'), '',
                     (f'共 {stats["global_groups"]} 组全局设置、{stats["sections"]} 个分区、{stats["block_types"]} 个分区内区块类型声明、{stats["settings"]} 个设置字段声明（包含配色子字段及区块字段；不同位置同名 ID 分别统计）。' if zh else
                      f'{stats["global_groups"]} global groups, {stats["sections"]} sections, {stats["block_types"]} local block type declarations, {stats["settings"]} setting declarations including nested color fields and block fields.'), '',
                     ('- **安装包无此设置**：对应分区 schema 未声明该编辑器设置；不等于整个主题没有此功能。\n- **待核对**：仅凭名称或旧说明无法确认对应关系。\n- **补充页面**：当前文档原先没有独立页面；不能据此认定该功能是本版本首次新增。\n- 本次没有旧版安装包，无法判定哪些字段是版本间新增或删除；本报告比较的是当前文档与这份新版包。\n- 安装包仅提供英文 schema 语言文件，中文页面保留英文后台名称以便对照。' if zh else
                      '- **Not declared in package**: absent from the relevant section schema, not necessarily absent as a theme feature.\n- **Needs review**: no reliable equivalence established.\n- **Added page**: documentation was missing; this does not prove the feature is newly introduced.\n- No previous archive was supplied, so this is a documentation-to-package audit, not a version-to-version diff.\n- The archive provides English schema labels only.'), '',
                     '## ' + ('安装包无此设置：404 页面旧说明' if zh else 'Not declared: old 404 page instructions'), '',
                     ('404 页面原文混入了联系表单设置；以下六个独立控件未在 `sections/404.liquid` schema 中声明，已在中英文原文标题旁标注。标题、描述等共享名称不能证明其联系表单用途，相关原文也应人工修改。' if zh else
                      'The old 404 guide describes a contact form. These six controls are not declared in the 404 section schema and are marked beside the original headings. Shared names such as Heading and Description do not establish a contact-form purpose; review the surrounding prose too.'), '',
                     '| ' + ('原文项目 | 核对结果 |' if zh else 'Original item | Result |'), '| --- | --- |']
            for heading in sorted(known_404):
                lines.append(f'| {heading} | ' + ('安装包无此设置（404 分区范围） |' if zh else 'Not declared in the 404 schema |'))
            lines.extend(['', f'[404 ' + ('原文及完整设置清单' if zh else 'guide and complete reference') + f'](/{lang}/sections/404)', '',
                          '## ' + ('其他不匹配的旧设置' if zh else 'Other legacy setting mismatches'), '',
                          ('| 页面 | 旧设置 | 标记 / 新版依据 |\n| --- | --- | --- |\n'
                           '| [Animations](/zh/settings/animations) | Content reveal style、Media reveal style、Motion speed、Reveal behavior | 安装包未声明这四个独立控件，原文已逐处标注 |\n'
                           '| [Animations](/zh/settings/animations) | Enable motion | 名称已改为 Scroll and reveal animations，ID 为 `motion_enabled`；保留开关说明，核对其具体作用范围 |\n'
                           '| [Layout](/zh/settings/layout) | Setting Small Border Radius | Layout 中未声明此设置，已标注 |\n'
                           '| [Layout](/zh/settings/layout) | Page width：1000–1600 px | 范围不一致；新版为 1000–2000 px，默认 1600 px |' if zh else
                           '| Page | Old setting | Current evidence |\n| --- | --- | --- |\n'
                           '| [Animations](/en/settings/animations) | Content reveal style, Media reveal style, Motion speed, Reveal behavior | Four independent controls not declared; marked inline |\n'
                           '| [Animations](/en/settings/animations) | Enable motion | Current label: Scroll and reveal animations; ID: `motion_enabled` |\n'
                           '| [Layout](/en/settings/layout) | Setting Small Border Radius | Not declared in Layout; marked inline |\n'
                           '| [Layout](/en/settings/layout) | Page width 1000–1600 px | Current range: 1000–2000 px; default: 1600 px |'), '',
                          '## ' + ('全局设置清单' if zh else 'Global settings'), '', '| ' + ('页面 | 文档状态 | 来源 |' if zh else 'Page | Documentation status | Source |'), '| --- | --- | --- |'])
            for kind in ('settings', 'sections'):
                if kind == 'sections':
                    lines.extend(['', '## ' + ('分区与内容块清单' if zh else 'Sections and blocks'), '', '| ' + ('页面 | 文档状态 | 来源 |' if zh else 'Page | Documentation status | Source |'), '| --- | --- | --- |'])
                for rec, existed in report:
                    if rec['kind'] == kind:
                        status = ('原页面补充完整清单' if existed else '补充页面') if zh else ('Reference appended' if existed else 'Added page')
                        lines.append(f'| [{rec["name"]}](/{lang}/{kind}/{rec["slug"]}) | {status} | `{rec["source"]}` |')
            missing = []
            for kind in ('settings', 'sections'):
                expected = {r['slug'] for r in records if r['kind'] == kind}
                for path in sorted((ROOT / 'docs' / lang / kind).glob('*.md')):
                    if path.stem not in expected:
                        missing.append(path)
                        warning = ('::: warning 安装包未找到对应定义\n新版安装包未找到与本页同名的 schema。可能已改名或合并，旧内容保留，请人工核对。\n:::' if zh else
                                   '::: warning No matching schema\nNo schema with the same name was found. It may have been renamed or merged. Review manually.\n:::')
                        old = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', path.read_text(encoding='utf-8'), flags=re.S).rstrip()
                        path.write_text(old + '\n\n' + START + '\n' + warning + '\n' + END + '\n', encoding='utf-8')
            lines.extend(['', '## ' + ('未找到对应定义的原页面' if zh else 'Existing pages without a matching schema'), ''])
            lines.extend([f'- [{p.stem}](/{lang}/{p.parent.name}/{p.stem})' for p in missing] or
                         ['现有全局设置和分区独立页面均找到对应定义。' if zh else 'All existing settings and section pages have matching definitions.'])
            lines.extend(['', '## ' + ('待核对与人工处理' if zh else 'Manual review'), '',
                          ('- 历史截图与正文未进行 Shopify 实机验证；各页末尾新版 schema 清单优先作为字段依据。\n- `custom-liquid` 的 Simple text、Product vendor、Existing snippet 是示例标题，不是编辑器设置，不标为缺失。\n- `newsletter-overlay` 的 Audience and timing 是说明标题，不是单独的控件。\n- 404 页关于联系表单、提交成功和图片的旧说明应一起检查，再手动删除或注释。\n- 颜色子字段、内容块设置与分区设置分开列出；不要因为在分区顶层找不到就删除。\n- 这里只确认 schema 声明，不保证前台代码使用了每个字段，也不把没有默认值的字段判为不支持。' if zh else
                           '- Screenshots and legacy prose require Shopify verification; use the appended schemas as the field reference.\n- Simple text, Product vendor and Existing snippet in Custom Liquid are examples, not missing controls.\n- Audience and timing in Newsletter Overlay is an explanatory heading.\n- Review the old contact-form, submission and image prose on the 404 page before manually removing it.\n- Nested color fields and block settings are listed separately.\n- Schema presence alone does not verify storefront behavior.'), ''])
            lines.extend(['## ' + ('安装包缺少的后台翻译' if zh else 'Missing schema translations'), '',
                          ('下列翻译键在安装包英文 schema 语言文件中未找到。文档保留原键作为证据；这是安装包翻译缺失，不代表设置项缺失。' if zh else
                           'These keys are missing from the English schema locale. Raw keys are preserved as evidence; missing translations do not imply missing controls.'), ''])
            lines.extend(f'- `{key}`' for key in sorted(missing_translations))
            (ROOT / 'docs' / lang / 'version-audit.md').write_text('\n'.join(lines), encoding='utf-8')

        output = ROOT / 'scripts' / 'latest-schema-inventory.json'
        output.write_text(json.dumps(dict(archive_sha256=hashlib.sha256(archive_bytes).hexdigest(),
                                         metadata=metadata, counts=stats, records=records), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(stats, ensure_ascii=False))


if __name__ == '__main__':
    main()
