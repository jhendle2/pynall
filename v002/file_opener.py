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
            line = remove_comments(line)
            line = remove_newlines(line)
            if line != '':
                file_lines.append(line)
        return file_lines
    # raise Exception(f'File {filename} not found!')


def line_to_layout_prototype(line):
    level = 0
    tag = ''
    params = []
    tab_length = len(TAB_CHAR)

    while line[:tab_length] == TAB_CHAR:
        level += 1
        line = line[tab_length:]

    if line[-1] == ':': line = line[:-1]

    if ', ' in line:
        line = line.replace(', ',',')
    if '(' in line and line[-1] == ')':
        paren_index = line.find('(')
        tag = line[:paren_index]
        line = line[paren_index+1:-1]
        params = line.split(',')
    else:
        tag = line

    return {
        'tag': tag,
        'level': level,
        'params': params,
    }


if __name__ == '__main__':
    # ls = open_file_as_lines('test.pypg')
    # for l in ls:
    #     print(l)
    line_ex1 = '    block(x=1, y=2):'
    line_ex2 = 'page:'
    r1 = line_to_layout_prototype(line_ex1)
    r2 = line_to_layout_prototype(line_ex2)
    print(r1)
    print(r2)