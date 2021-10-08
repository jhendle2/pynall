from utils.file_opener import *
from script_manager import script_importer
from layout_manager.layout import build_layout_tree
from layout_manager.html_converter import dump_tree_as_html

import sys
import logging

import app

__app__ = 'PyNaLL'
__author__ = 'PyNaLL Team'
__version__ = '0.0.3'
__date__ = '10/07/2021'

LOG_LEVEL = logging.DEBUG
LOG_FORMAT = "[%(levelname)s] %(message)s"
logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

if __name__ == '__main__':
    logging.info('PyNaLL is starting up...')
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--infile", help="file to be read in")
    parser.add_argument("-o", "--outfile", help="file to be written to")
    parser.add_argument("-l", "--live", help="live reload files upon update")
    parser.add_argument("-a", "--all", help="output layout, styles, and scripts sections", action='store_true')
    parser.add_argument("-L", "--layout", help="output layout (.html)", action='store_true')
    parser.add_argument("-S", "--styles", help="output styles (.css)", action='store_true')
    parser.add_argument("-P", "--scripts", help="output scripts (.py)", action='store_true')
    args = parser.parse_args()

    if args.infile:
        # Parse the infile/outfile name
        infile = args.infile
        outfile = infile.replace('.pypg','') if not args.outfile else args.outfile
        logging.info(f'Infile={infile}, Outfile={outfile}')

        layout_switch = args.layout or args.all
        layout_outfile = outfile + '.html'
        styles_switch = args.styles or args.all
        styles_outfile = outfile + '.css'
        scripts_switch = args.scripts or args.all
        scripts_outfile = outfile + '.py'

        file_as_lines = open_file_as_lines(infile)

        if scripts_switch:
            scripts_section = isolate_scripts(file_as_lines)
            scripts_section = remove_one_tab(scripts_section)
            # scripts_section = count_levels(file_as_lines)
            script_obj = script_importer.load_script(scripts_outfile, scripts_section)
            # if script_obj is not None:
            #     script_obj.func1()

        # if styles_switch:
        #     styles_section = isolate_styles(file_as_lines)
        #     styles_levels = count_levels(styles_section)
        #     print(styles_levels)

        #TODO: FIX
        # if layout_switch:
        #     layout_section = isolate_layout(file_as_lines)
        #     print(layout_section)
        #     layout_levels = count_levels(layout_section)
        #     layout_tree = build_layout_tree(layout_levels)
        #
        #     print(layout_tree)
        #
        #     html_str = dump_tree_as_html(layout_tree)
        #     html_dir = 'templates/' + outfile + '.html'
        #
        #     with open(html_dir, 'w+') as html_out:
        #         logging.info(f'Outputting html source to {html_dir}')
        #         html_out.write(html_str)

        app.run_flask(script_obj)


    else:
        logging.error('No file found!')
        logging.error('PyNaLL will now exit.')
        sys.exit(1)

