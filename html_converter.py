# from layout import Layout, Tag
#
#
# def html_str_out(layout_hierarchy : Layout) -> str:
#     my_tag = layout_hierarchy.tag
#     open_tag, close_tag = f'<{my_tag}>', f'</{my_tag}>'
#     str_out = open_tag + '\n'
#     layout_children = layout_hierarchy.children
#     for child in layout_children:
#         str_out += html_str_out(child) + '\n'
#     str_out += close_tag
#     return str_out
#

TAGS = {
    'pypg': 'html',
    'page': 'html',
    'block': 'div',
    'paragraph': 'p',
    'header': 'h',
    'style': 'css',
}


def tag_to_html(tag):
    if tag in TAGS.keys():
        return TAGS[tag]
    else:
        return tag


def dump_tree_as_html(tree):
    str_out = ''
    if tree['is_content']:
        return tree['tag']

    tag = tree['tag']
    args = tree['args']
    level = ''
    if type(args) is str:
        level = args

    html_tag = tag_to_html(tag)

    if tree.has_children:
        open_tag = '<' + html_tag + level + '>'
        close_tag = '</' + html_tag + level + '>'
        str_out += open_tag + '\n'
        for child in tree['children']:
            str_out += dump_tree_as_html(child) + '\n'
        str_out += close_tag
    else:
        open_tag = '<' + html_tag + level + '/>'
        str_out = open_tag + '\n'
    return str_out
