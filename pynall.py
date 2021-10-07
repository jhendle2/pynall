from html_converter import *
from css_converter import *
from py_converter import *
from file_opener_2 import *

import sys
import logging

__app__ = 'PyNaLL'
__author__ = 'PyNaLL Team'
__version__ = '0.0.2'
__date__ = '10/06/2021'

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "[%(levelname)s] %(message)s"
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

if __name__ == '__main__':
    logging.info('PyNaLL is starting up...')
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="file to be read in")
    parser.add_argument("-o", "--outfile", help="file to be written to")
    args = parser.parse_args()
    if args.infile:
        infile = args.infile
        outfile = infile.replace('.pypg','')  # + '.html'
        if args.outfile:
            outfile = args.outfile
        logging.info(f'Infile={infile}')

        ls = open_file_as_lines('test.pypg')
        lc = count_levels(ls)
        lt = layout.build_layout_tree(lc)['children']
        lthtml, ltcss, ltscript = None, None, None
        for lti in lt:
            if lti['tag'] == 'page':
                lthtml = lti
            elif lti['tag'] == 'style':
                ltcss = lti
            elif lti['tag'] == 'script':
                ltscript = lti
        # ljson = layout.dump_tree_as_json(lt)
        # with open('test.json', 'w+') as outfile1:
        #     outfile1.write(ljson)
        html_str = dump_tree_as_html(lthtml)
        css_str = dump_tree_as_css(ltcss)
        py_str = dump_tree_as_py(ltscript)

        html_dir = outfile+'.html'
        css_dir = outfile+'.css'
        py_dir = outfile+'.py'

        with open(html_dir, 'w+') as html_out:
            logging.info(f'Outputting html source to {html_dir}')
            html_out.write(html_str)
        # with open(css_dir, 'w+') as css_out:
        # logging.info(f'Outputting css source to {css_dir}')
        #     css_out.write(css_str)
        # with open(py_dir, 'w+') as py_out:
        # logging.info(f'Outputting python source to {py_dir}')
        #     py_out.write(py_str)

    else:
        logging.error('No file found!')
        logging.error('PyNaLL will now exit.')
        sys.exit(1)

