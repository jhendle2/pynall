from std_layout import button

page:
    block:
        title:
            'Test Page' # with a comment
        header(2):
            'Welcome to my test page!'
        paragraph:
            '''
            This is a test page to
            test my PyPg interpreter.
            '''
        link(text='Click here for more info!', path='test_out.html')
        image(source='src/images/cat.png', hover='a fluffy cat!', height=default, width=default)

style:
    pass

script:
    def func1():
        print('Hello World')