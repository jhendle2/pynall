import os
import importlib
import time


def load_script(filename, script_as_lines):
    # Write a file full of the scripts
    with open(filename, 'w+') as file:
        for line in script_as_lines:
            file.write(line + '\n')
        file.write('\n')
        file.close()

    # Try to find file 3 times and import it
    for i in range(3):
        try:
            import_obj = __import__(filename.replace('.py', ''), globals=globals())
            os.remove(filename)
            return import_obj
        except FileNotFoundError:
            time.sleep(1)
    return None


def get_func(import_obj, func_name):
    """
    Gets a function from an import module
    :param import_obj:
    :param func_name:
    :return the function:
    """
    return import_obj.__dict__[func_name]
