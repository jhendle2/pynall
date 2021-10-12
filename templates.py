standard_template = '''# Filename: %s
# Author: YOUR_NAME_HERE
# Date Modified: LAST_MODIFIED_DATE

# This is a template Lasso file. Have fun!
# Tutorials can be found at https://github.com/jhendle2/lasso/wiki


layout(title=\'Hello World Page\'):
    block():
        paragraph(style=cool_style):
            \'Hello World!\'
            
        button(onclick=helloWorld())


styles():
    cool_style = Style(align=\'center\', bold=True)


scripts():
    def helloWorld():
        print(\'Hello, World!\')

'''

bare_template = '''layout():
    pass

styles():
    pass

scripts():
    pass
'''