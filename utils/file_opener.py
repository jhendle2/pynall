"""
Description: This file reads and nicely formats a
.pypg file for later processing.
"""

COMMENT_CHAR = '#'
NEWLINE_CHAR = '\n'
# NEWLINE_CHAR = '\n\r'
TAB_CHAR = '    '
# TAB_CHAR = '  '
# TAB_CHAR = '\t'


def remove_comments(line):
    if COMMENT_CHAR in line:
        line = line[:line.find(COMMENT_CHAR)]
    return line


def remove_newlines(line):
    if len(line) > 0 and line[-1] == NEWLINE_CHAR:
        line = line[:-1]
    return line


def open_file_as_lines(filename):
    with open(filename) as file:
        file_lines = []
        for line in file:
            if 'import' in line or 'from' in line:
                continue

            line = remove_comments(line)
            line = remove_newlines(line)
            if line != '':
                file_lines.append(line)
        return file_lines
    # raise Exception(f'File {filename} not found!')


def count_levels(lines_in):
    lines_out = []
    for line in lines_in:
        level = 1
        while TAB_CHAR in line:
            line = line[len(TAB_CHAR):]
            level += 1
        lines_out.append((line, level))
    return lines_out


def isolate(lines, switch_on, switch_off):
    switch_on = switch_on + ':'
    switch_off = [s + ':' for s in switch_off]
    isolated_lines = [switch_on]
    switch = False
    for line in lines:
        if switch:
            isolated_lines.append(line)
        if line.replace('()', '') == switch_on:
            switch = True
        elif line.replace('()', '') in switch_off:
            switch = False
    return isolated_lines


def isolate_layout(lines):
    layout_lines = isolate(lines,'page', ['styles', 'scripts'])
    if layout_lines[-1] == 'styles():' or layout_lines[-1] == 'styles:':
        layout_lines = layout_lines[:-1]
    return layout_lines


def isolate_styles(lines):
    return isolate(lines, 'styles', ['page', 'scripts'])


def isolate_scripts(lines):
    return isolate(lines, 'scripts', ['styles', 'page'])


def remove_one_tab(lines):
    """
    .pypg files are automatically tabbed one line in.
    This file removes that.
    :param lines:
    :return new_lines:
    """
    if 'scripts' in lines[0]:
        lines.pop(0)

    new_lines = []
    tab_length = len(TAB_CHAR)
    for line in lines:
        if len(line) > tab_length and line[:tab_length] == TAB_CHAR:
            new_lines.append(line[tab_length:])
    return new_lines

