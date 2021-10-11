
def repair_strings(line):
    line = line.lstrip().rstrip()
    if line[0:3] == "'''" or line[0:3] == '"""':
        line = line[3:]
    elif (line[0] == '\'' and line[-1] == '\'') or \
            (line[0] == '\"' and line[-1] == '\"'):
        line = line[1:-1]
    return line


def args_str_to_dict(args_str):
    args_dict = {}
    if ',' not in args_str:
        args_dict = args_str
        return args_dict

    args_list = args_str.replace(', ', ',').split(',')
    for arg in args_list:
        if '=' in arg:
            name, value = arg.split('=')
            name = name.lstrip().rstrip()
            value = value.lstrip().rstrip()
            args_dict[name] = value
    return args_dict


def line_to_tag_args(line):
    tag = line
    args = {}
    if line[-1] == ':':
        line = line[:-1]
        tag = line

    if '(' in line:
        paren_index = line.find('(')
        tag = line[:paren_index]
        line = line[paren_index:]
        if line[-1] == ')':
            args_str = line[1:-1]
            args = args_str_to_dict(args_str)

    return tag, args


class Node(dict):
    def __init__(self, tag, args, is_content):
        self._parent = None  # pointer to parent Node
        self['tag'] = tag
        self['content'] = ''  # keep reference to id #
        self['children'] = [] # collection of pointers to child Nodes
        self['is_content'] = is_content
        self['args'] = args

    @property
    def parent(self):
        return self._parent  # simply return the object at the _parent pointer

    @property
    def has_children(self):
        return len(self['children']) > 0

    def has(self, key):
        return key in self['args'].keys()

    @parent.setter
    def parent(self, node):
        self._parent = node
        # add this node to parent's list of children
        node['children'].append(self)


def tag_args_to_node(tag_args, is_content):
    temp = Node(tag_args[0], tag_args[1], is_content)
    return temp


def build_layout_tree(tups):
    # parent, last_level = tups.pop(0)
    parent, last_level = Node('pypg', None, False), 0
    if last_level != 0:
        raise Exception('No parent node')

    tree = parent  # tag_args_to_node(line_to_tag_args(parent), False)
    # tree = Node(parent)
    last_node = tree
    for line, level in tups:
        tag, args = line_to_tag_args(line)
        is_content = tag == line
        if is_content:
            tag = repair_strings(tag)
            if tag == '':
                continue

        if level > last_level:
            child_node = Node(tag, args, is_content)
            child_node.parent = last_node
            last_node = child_node
            last_level = level
        elif level == last_level:
            child_node = Node(tag, args, is_content)
            child_node.parent = last_node.parent
            last_node = child_node
            last_level = level
        else:
            while level <= last_level:
                last_node = last_node.parent
                last_level -= 1
            child_node = Node(tag, args, is_content)
            child_node.parent = last_node
            last_node = child_node
            last_level = level
    return tree


def dump_tree_as_json(tree):
    import json
    return json.dumps(tree, indent=4)


if __name__ == '__main__':
    line1 = "block(arg1=test1, arg2=test2):"
    parsed1 = line_to_tag_args(line1)
    print(parsed1)
