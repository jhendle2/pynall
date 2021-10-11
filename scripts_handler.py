from general_utils import print_header
from file_handler import shift_left_one_tab


def isolate_scripts_section(lines):
    scripts_lines = []
    scripts_switch = False
    for line in lines:
        if line in ['layout():','layout:','styles():','style:']:
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


def process_scripts(filename, lines, project_directory_name):
    print('Processing scripts section...')
    script_lines = isolate_scripts_section(lines)
    create_temporary_scripts_file(filename, script_lines, project_directory_name)
    # print(script_lines)

