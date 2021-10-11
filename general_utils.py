def line():
    print('-----------------------------------------------------')


def print_header(*args):
    line()
    for a in args:
        print(a, end='')
    print()

