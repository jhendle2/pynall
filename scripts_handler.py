import importlib

# from general_utils import print_header
from file_handler import shift_left_one_tab
from inspect import getmembers, isfunction


def isolate_scripts_section(lines):
    scripts_lines = []
    scripts_switch = False
    for line in lines:
        if line in ['layout():', 'layout:', 'styles():', 'style:']:
            scripts_switch = False
        if scripts_switch:
            line = shift_left_one_tab(line)
            scripts_lines.append(line)
        if line in ['scripts():', 'scripts:']:
            scripts_switch = True
    return scripts_lines


def create_temporary_scripts_file(filename, lines, project_directory_name):
    scripts_filename = project_directory_name + filename.replace('src', '').replace('.pypg', '_scripts.py')
    with open(scripts_filename, 'w+') as scripts_file:
        print(f'Creating temporary scripts file \"{scripts_filename}\"...')
        for line in lines:
            scripts_file.write(line + '\n')
        scripts_file.close()
        print(f'Finished creating temporary scripts file \"{scripts_filename}\"')
        return scripts_filename


def load_scripts_as_functions(scripts_path):
    """
    Imports a Python script as a module, then returns
    a dictionary of each function's name and a pointer
    to the address of the function itself.
    :param scripts_path:
    :return dict of functions:
    """
    scripts_path_fixed = scripts_path.replace('.py', '').replace('/', '.')
    scripts_import_module = importlib.import_module(scripts_path_fixed)
    scripts_functions = dict((func[0], func[1]) for func in getmembers(scripts_import_module, isfunction))
    return scripts_functions


def process_scripts(filename, lines, project_directory_name):
    print('Processing scripts section...')
    script_lines = isolate_scripts_section(lines)
    scripts_filename = create_temporary_scripts_file(filename, script_lines, project_directory_name)
    script_functions = load_scripts_as_functions(scripts_filename)
    return script_functions

