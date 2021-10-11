import sys, os
# import logging

from templates import standard_template

from file_handler import read_file_as_lines
from layout_handler import process_layout
from styles_handler import process_styles
from scripts_handler import process_scripts

from general_utils import line, print_header

__app__ = 'Lasso'
__author__ = 'The Lasso Team'
__version__ = '0.0.4'
__date__ = '10/11/2021'

# LOG_LEVEL = logging.DEBUG
# LOG_FORMAT = "[%(levelname)s] %(message)s"
# logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)


def create_empty_project(filename):
    print('Creating new empty project...')
    with open(filename, 'w') as empty_project:
        empty_project.write(standard_template % filename)
        empty_project.close()
    print('Finished creating empty project')


def get_source_name():
    print('No source file detected. Please enter it here: ', end='')
    source_name = 'src/'+str(input())

    if os.path.exists(source_name):
        print(f'Successfully located source file "{source_name}"')
        return source_name
    else:
        print(f'Could not locate source file "{source_name}"!')

        def create_new_source_file():
            print('Would you like to create it? (Y)es/(N)o: ', end='')
            choice = str(input())
            if 'y' in choice:
                create_empty_project(source_name)
                print(f'Created new source file "{source_name}"')
                print('Happy coding :)')
            print('Goodbye!')
            sys.exit(0)

        create_new_source_file()


def create_project_directory(filename):
    print_header('Create project directory...')

    def new_directory_name():
        print('Directory name: ', end='')
        dir_name = str(input())
        print(f'Is "{dir_name}/" correct?', end=' ')
        print('(Y)es/(N)o: ', end='')
        choice2 = str(input()).lower()
        if 'y' in choice2:
            return dir_name
        else:
            return new_directory_name()

    print('No directory name selected. Would you like to pick the default?', end=' ')
    print('(Y)es/(N)o: ', end='')
    choice = str(input()).lower()
    if 'y' in choice:
        return filename
    else:
        return new_directory_name()


def process_file(filename):
    print_header(f'Processing "{filename}"')

    # scripts_data = process_scripts(filename)
    # styles_data = process_styles(filename)
    # layout_data = process_layout(filename, scripts_data, styles_data)


if __name__ == '__main__':
    print_header('Lasso is starting up...')
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

    infile = ''
    try:
        if not args.infile:
            infile = get_source_name()
        if args.infile:

            # Parse the infile/outfile name
            infile = args.infile
            print(f'Source file selected: "{infile}"')
            # outfile = infile.replace('.pypg', '') if not args.outfile else args.outfile

            project_directory_name = ''
            if args.outfile:
                project_directory_name = args.outfile
            else:
                project_directory_name = create_project_directory(infile)

            try:
                os.mkdir('src/'+project_directory_name)
                print(f'Created directory "{project_directory_name}/"')
            except FileExistsError:
                print(f'Directory "{project_directory_name}/" already exists!')

            process_file(infile)
    except KeyboardInterrupt:
        print()
        line()
        print('Setup interruption. Goodbye!')
        # logging.info(f'Created directory {project_directory_name}.')
        # logging.info(f'Infile={infile}, Outfile={outfile}')
        #
        # layout_switch = args.layout or args.all
        # layout_outfile = outfile + '.html'
        # styles_switch = args.styles or args.all
        # styles_outfile = outfile + '.css'
        # scripts_switch = args.scripts or args.all
        # scripts_outfile = outfile + '.py'
        #
        # file_as_lines = read_file_as_lines(infile)
        # print(file_as_lines)


