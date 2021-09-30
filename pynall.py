from layout import Layout
from html_converter import *
from file_opener import *


__author__ = 'PyNaLL Team'
__version__ = '0.0.1'
__date__ = '9/30/2021'

if __name__ == '__main__':
    # layout1 = Layout(tag='page')
    # layout2 = Layout(tag='block')
    # layout3 = Layout(tag='paragraph', content='Hello, World!')
    #
    # layout2.add_child(layout3)
    # layout1.add_child(layout2)
    #
    # html_str = html_str_out(layout1)
    # print(html_str)
    ls = open_file_as_lines('test.pypg')
    print(ls)
