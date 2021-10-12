from layout import Node

TAGS = {
    'layout': 'html',
    'block': 'div',
    'paragraph': 'p',
    'header': 'h',
    'header1': 'h1',
    'header2': 'h2',
    'header3': 'h3',
    'header4': 'h4',
    'title': 'h',
}


def valid_tag(tag):
    return tag in TAGS.keys()


def htmlize_content(content):
    if "'''" in content:
        content = content.replace("'''", '"')
    elif '"""' in content:
        content = content.replace('"""', '"')
    elif content[0] == "'" and content[-1] == "'":
        content = '"' + content[1:-1] + '"'

    if content[0] == '"' and content[-1] == '"':
        content = content[1:-1]
    return content


def build_html_from_node(node: Node):
    if node.is_content:
        return htmlize_content(node['content'])

    if node['tag'] != '':
        tag = node['tag']

        if valid_tag(tag):
            tag = TAGS[tag]

        html_out = ''
        if node.has_children:
            html_out = f'<{tag}>\n'
            for child in node['children']:
                html_out += build_html_from_node(child) + '\n'
            html_out += f'</{tag}>'
        else:
            html_out = f'<{tag}/>'
        return html_out
    return ''

