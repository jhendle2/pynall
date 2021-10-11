NEWLINE = '\n'
# NEWLINE = '\n\r'
def remove_newline(line):
    if len(line) > 0 and line[-1] == NEWLINE:
        return line[:-1]
    if len(line) > 1 and NEWLINE in line[-2:]:
        return line[:-2]
    return line


def remove_comments(line):
    if '#' in line:
        comment_index = line.find('#')
        line = line[:comment_index]
    return line


# TAB = '  ' # two spaces
TAB = '    '  # four spaces
# TAB = '\t'  # tab char
def replace_tabs(line):
    """
    Replaces unexpected tab chars with standard 4-spaces tab
    """
    if len(line) > 0 and line[0] == '\t':
        line = line.replace('\t', TAB)
    return line


def repair_strings(lines):
    return lines


def read_file_as_lines(filename):
    with open(filename) as file:
        file_as_lines = []
        for line in file:
            line = remove_newline(line)
            line = remove_comments(line)
            line = replace_tabs(line)

            if len(line) > 0:
                file_as_lines.append(line)
        return file_as_lines

