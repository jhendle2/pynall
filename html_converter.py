from layout import Layout, Tag


def html_str_out(layout_hierarchy : Layout) -> str:
    my_tag = layout_hierarchy.tag
    open_tag, close_tag = f'<{my_tag}>', f'</{my_tag}>'
    str_out = open_tag + '\n'
    layout_children = layout_hierarchy.children
    for child in layout_children:
        str_out += html_str_out(child) + '\n'
    str_out += close_tag
    return str_out

