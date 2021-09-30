tag_lookup = {
    'page': 'html',
    'block': 'div',
    'table': 'table',
    'paragraph': 'p',
    'header': 'h',
}


class Tag:

    def __init__(self, name='', bonus=0):
        self.name = name
        self.bonus = bonus  # How changes in level it is from the previous tag

    def __repr__(self):
        return self.name

    def bonus(self):
        return self.bonus

    def get_html_eq(self):
        return tag_lookup[self.name]


class Style:
    def __init__(self, **kwargs):
        self.source = ''  # Could be a source file
        for kw in kwargs:
            setattr(self, kw, kwargs[kw])


class Layout:
    """
    Description: A object which will correspond to
    HTML style tags.
    """

    def __init__(self, **kwargs):
        self.tag : Tag = None
        self.children = []
        self.style : Style = None
        self.lclass = None
        self.content = None  # Usually just a String

        for kw in kwargs:
            setattr(self, kw, kwargs[kw])

    def __repr__(self):
        str_out = ''
        str_out += str(self.tag)
        return str_out

    def props(self):
        return [prop for prop in self.__dict__]

    def add_child(self, child):
        self.children.append(child)


if __name__ == '__main__':
    layout = Layout(tag='test')
    print(layout.props())
    print(layout.tag)