from file_handler import TAB
from layout import *
from html_converter import build_html_from_node

from debugs import DEBUG_JSON_INTERIM


def isolate_layout_section(lines):
    layout_lines = []
    layout_switch = False
    string_switch = False
    string_line = ''
    for line in lines:
        if line in ['scripts():', 'scripts:', 'styles():', 'style:']:
            layout_switch = False
        if line in ['layout():', 'layout:']:
            layout_switch = True
        if layout_switch:
            if "'''" in line or '"""' in line:
                if string_switch:
                    string_line += line.lstrip(TAB)
                    layout_lines.append(string_line)
                    string_line = ''
                else:
                    string_line = line
                string_switch = not string_switch
            else:
                if string_switch:
                    string_line += line.lstrip(TAB)
                else:
                    layout_lines.append(line)
    return layout_lines


def build_level_list(lines):
    level_list = []
    tab_length = len(TAB)
    for line in lines:
        if len(line) == 0:
            continue

        level = 0
        while TAB in line[0:tab_length]:
            level += 1
            line = line[tab_length:]
        pair = line, level
        level_list.append(pair)
    return level_list


def process_layout(filename, file_as_lines, project_directory):
    print('Processing layouts section...')
    layout_selection = isolate_layout_section(file_as_lines)
    # print(layout_selection)
    level_list = build_level_list(layout_selection)
    # print(level_list)

    layout_tree = build_layout_tree(level_list)
    layout_json = dump_tree_as_json(layout_tree)
    print(layout_json)

    repair_tree_content(layout_tree)
    layout_json = dump_tree_as_json(layout_tree)
    new_filename = project_directory + '/' + filename.replace('src/', '').replace('.pypg', '')
    if DEBUG_HTML_JSON_INTERIM:
        dump_directory = new_filename + '.json'
        print(f'DEBUG: Printing JSON dump to \"{dump_directory}\"')
        with open(dump_directory, 'w+') as json_out:
            json_out.write(layout_json)
            json_out.close()

    html_str = build_html_from_node(layout_tree)
    html_filename = new_filename + '.html'
    print(f'Outputting HTML source to \"{html_filename}\"')
    with open(html_filename, 'w+') as html_out:
        html_out.write(html_str)
        html_out.close()

    print(f'Finished outputting HTML source to \"{html_filename}\"')

