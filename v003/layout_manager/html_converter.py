
TAGS = {
    'pypg': '',
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
    if tag == 'pypg':
        # print('here')
        return ''

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
    elif tag == 'button':
        # print('args=', args)
        button_type, button_id, button_path, button_text = 'submit', 'button1', '', ''
        if 'type' in args.keys():
            button_type = args['type'].replace('\'', '').replace('"', '')

        if 'id' in args.keys():
            button_id = args['id'].replace('\'', '').replace('"', '')

        if 'path' in args.keys():
            button_path = args['path'].replace('\'', '').replace('"', '')

        if 'text' in args.keys():
            button_text = args['text'].replace('\'', '').replace('"', '')

        if '(' in button_path and ')' in button_path:
            button_path = button_path.replace('(', '').replace(')', '')

        # print(button_path, button_text, button_id, button_type)
        str_out = '<form action="/index_data" method="POST">'
        str_out += f'<input type="{button_type}" name="{button_id}" value="{button_path}">'
        str_out += '</form>'
        return str_out
    else:
        if tag not in TAGS:
            return tag
        else:
            html_tag = tag_to_html(tag)
            content = tree['content']
            return f'<{html_tag}>{content}</{html_tag}>'
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
        if tag != 'pypg':
            str_out += open_tag + '\n'
        for child in tree['children']:
            tree_dump = dump_tree_as_html(child)
            if tree_dump is not None:
                str_out += tree_dump + '\n'
        if tag != 'pypg':
            str_out += close_tag
    else:
        single_line = build_single_line(tree)
        str_out += single_line
    if '\\n' in str_out:
        str_out = str_out.replace('\\n', '<br>')
    return str_out
