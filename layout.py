import sys
from general_utils import content_is_string


class Argument(dict):
    """
    Arg_Types:
    - value
    - function
    - path
    """

    def __init__(self, arg_keyword, arg_value, arg_type='', args_kwarg=None):
        super().__init__()
        self['arg_keyword'] = arg_keyword
        self['arg_type'] = arg_type
        self['arg_value'] = arg_value
        self['arg_kwargs'] = {}

    @property
    def is_func(self):
        return self['arg_type'] == 'function'

    def __repr__(self):
        arg_type = self['arg_type']
        arg_keyword = self['arg_keyword']
        arg_value = self['arg_value']
        if self.is_func:
            arg_kwargs = self['arg_kwargs']
            return f'[{arg_type}] {arg_keyword} = {arg_value}; kwargs = {arg_kwargs}'
        else:
            return f'[{arg_type}] {arg_keyword} = {arg_value}'


class Node(dict):
    def __init__(self, content=''):
        super().__init__()
        self._parent = None  # pointer to parent Node
        self['tag'] = ''
        self['is_content'] = True
        self['content'] = content
        self['args'] = {}
        self['children'] = []

    @property
    def parent(self):
        return self._parent  # simply return the object at the _parent pointer

    @property
    def has_children(self):
        return len(self['children']) > 0

    @property
    def is_content(self):
        return self['is_content']

    @parent.setter
    def parent(self, node):
        self._parent = node
        # add this node to parent's list of children
        node['children'].append(self)


def build_layout_tree(tups):
    first_tup = tups.pop(0)
    tree, last_level = Node(first_tup[0]), first_tup[1]
    last_node = tree
    for line, level in tups:
        if line == '':
            continue

        if level > last_level:
            child_node = Node(content=line)
            child_node.parent = last_node
            last_node = child_node
            last_level = level
        elif level == last_level:
            child_node = Node(content=line)
            child_node.parent = last_node.parent
            last_node = child_node
            last_level = level
        else:
            while level <= last_level:
                last_node = last_node.parent
                last_level -= 1
            child_node = Node(content=line)
            child_node.parent = last_node
            last_node = child_node
            last_level = level
    return tree


def explode_args_from_string(args_string):
    """
    Takes in a string of arguments and returns
    a list of Argument objects. These objects may
    also have arguments within themselves and
    wouldn't you know it, this function takes
    care of that as well! It was a nightmare...
    :param args_string:
    :return args_dict:
    """
    # args_as_list = [arg.lstrip(' ').rstrip(' ') for arg in args_string.split(',')]
    args_as_list = []

    """
    Okay, so I was gonna use args_as_list.split(',') here,
    but because functions can have arguments with commas
    inside of em...
    ex: block(func=function1(abc, xyz), style=style1):
    ...you'd want those keywords to stay together.
    Soooo, I had to do this monstrosity. Sorry!
    """
    # Build a list of arguments
    temp_string = ''
    paren_depth = 0
    for i in range(len(args_string)):
        c = args_string[i]
        if c == '(':
            temp_string += c
            paren_depth += 1
        elif c == ')':
            temp_string += c
            paren_depth -= 1
        elif c == ',':
            if paren_depth >= 1:
                temp_string += c
            else:
                temp_string = temp_string.lstrip(' ').rstrip(' ')
                args_as_list.append(temp_string)
                temp_string = ''
        else:
            temp_string += c
    if len(temp_string) > 0:
        temp_string = temp_string.lstrip(' ').rstrip(' ')
        args_as_list.append(temp_string)

    # And convert those arguments into Argument objects
    args_dict = {}
    for arg in args_as_list:
        keyword = value = arg.lstrip(' ').rstrip(' ')  # Oh yeah, I just did that.

        # Confirm that we're not finding an equals sign within a function's args
        equals_index = arg.find('=')
        first_paren_index = arg.find('(')
        if equals_index != -1 and equals_index < first_paren_index:
            keyword = arg[:equals_index].lstrip(' ').rstrip(' ')
            value = arg[equals_index+1:].lstrip(' ').rstrip(' ')

        argument = Argument(arg_keyword=keyword, arg_value=value)

        # key1 = func(abc, xyz)
        if '(' and ')' in value:
            argument['arg_type'] = 'function'
            index = value.find('(')
            argument['arg_kwargs'] = value[index+1:-1]
            argument['arg_value'] = value[:index]

        # key2 = 'a/b/c'
        elif '/' in value:
            argument['arg_type'] = 'path'
        else:
            argument['arg_type'] = 'value'

        args_dict[keyword] = argument
    return args_dict


def find_args_from_content(node):
    content = node['content']
    if len(content) > 1 and not(content[0] == "'" or content[0] == '"'):
        if content[-1] == ':':
            content = content[:-1]

        if not content_is_string(content):
            index = content.find('(')
            node['tag'] = content[:index]
            arg_string = content[index+1:-1]
            # print('arg_string=', arg_string)
            args_dict = explode_args_from_string(arg_string)
            # print(args_dict)
            node['args'] = args_dict
            node['content'] = ''
            node['is_content'] = False


def repair_tree_content(tree: Node):
    find_args_from_content(tree)
    if tree.has_children:
        for child in tree['children']:
            repair_tree_content(child)


def dump_tree_as_json(tree):
    import json
    return json.dumps(tree, indent=2)


if __name__ == '__main__':
    # test_line = 'block(word1=value1, word2=value2, function1(x=5, y=abc)):'
    # # test_node = Node(content=test_line)
    # # find_args_from_content(test_node)
    # node1 = Node(content=test_line)
    # find_args_from_content(node1)
    # json_tree = dump_tree_as_json(node1)
    # print(json_tree)

    hellonode = Node(content="'''Hello, World!'''")
    hellonode['is_content'] = True
    hellonode['tag'] = ''
    hellonode['args'] = {}
    hellonode['children'] = []

    test_node = Node(content='paragraph():')
    test_node['is_content'] = True
    test_node['tag'] = ''
    test_node['args'] = {}
    test_node['children'] = [hellonode]

    test_node_json = dump_tree_as_json(test_node)
    print(test_node_json)

    repair_tree_content(test_node)

    test_node_json = dump_tree_as_json(test_node)
    print(test_node_json)

