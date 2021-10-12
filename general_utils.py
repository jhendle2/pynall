def line():
    print('-----------------------------------------------------')


def nline():
    print()
    line()


def print_header(*args):
    print()
    for a in args:
        print(a, end='')
    print()
    line()


def content_is_string(content):
    content_len = len(content)
    if content_len > 3:
        if content[0:3] == "'''" or content[0:3] == '"""':
            return True
    elif content_len > 0:
        if content[0] == "'" or content[0] == '"':
            return True
    return False