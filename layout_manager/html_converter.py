
TAGS = {
    'pypg': 'html',
    'page': 'html',
    'block': 'div',
    'paragraph': 'p',
    'header': 'h',
    'title': 'h1',
    'style_manager': 'css',
    'image': 'img',
    'link': 'a',
    'bold': 'strong',
    'italic': 'italic',
}


def tag_to_html(tag):
    if tag in TAGS.keys():
        return TAGS[tag]
    else:
        return tag


def build_single_line(tree):
    tag = tree['tag']
    args = tree['args']
    if tag == 'link':
        text = args['text'] if tree.has('text') else ''
        path = args['path'] if tree.has('path') else ''
        return f'<a href={path}>{text}</a>'
    elif tag == 'image':
        source = args['source'] if tree.has('source') else ''
        # if source[0]=='/':
        #     source = source[1:]
        hover = args['hover'] if tree.has('hover') else ''
        height = str(args['height']) if tree.has('height') else ''
        width = str(args['width']) if tree.has('width') else ''
        height = 'height='+height if height != 'default' or '' else ''
        width = 'width='+width if width != 'default' or '' else ''
        # height = 'height='+str(args['height']) if tree.has('height') else ''
        # width = 'width='+str(args['width']) if tree.has('width') else ''
        return f'<img src={source} alt={hover} {height} {width}/>'

    return ''


def dump_tree_as_html(tree):
    str_out = ''
    # if tree['is_content']:
    #     return tree['tag']

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
            tree_dump = dump_tree_as_html(child)
            if tree_dump is not None:
                str_out += tree_dump + '\n'
        str_out += close_tag
    else:
        single_line = build_single_line(tree)
        str_out += single_line
    if '\\n' in str_out:
        str_out = str_out.replace('\\n', '<br>')
    return str_out
