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
            output = ROOT / 'scripts' / 'latest-schema-inventory.json'
        output.write_text(json.dumps(dict(archive_sha256=hashlib.sha256(archive_bytes).hexdigest(),
                                         metadata=metadata, counts=stats, records=records), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(stats, ensure_ascii=False))


if __name__ == '__main__':
    main()
