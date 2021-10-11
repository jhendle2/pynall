import sys
from v003.script_manager.script_importer import get_func, get_funcs
from flask import Flask, request, render_template

imports = None
app = Flask(__name__)

index_page = None


def func1():
    print('Hello World', file=sys.stderr)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template(index_page)


@app.route("/index_data", methods=['GET', 'POST'])
def index_data():
    # if request.method == 'POST':
    #     # if request.form['button1'].value == 'Run Func1':
    #     #     imports.func1()
    #     # elif request.form['submit_button'] == 'Do Something Else':
    #     #     pass  # do something else
    #     else:
    #         pass  # unknown
    if request.method == 'POST':
        funcs = get_funcs(imports)
        # print(funcs, file=sys.stderr)
        for func in funcs:
            # print('on=',func, file=sys.stderr)
            # print(request.form)
            if func in request.form['button1']:
                # print('found=', func, file=sys.stderr)
                local_func = get_func(imports, func)
                local_func()
        # if 'func1' in request.form['button1']:
        #     # print('hello world', file=sys.stderr)
        #     local_func1 = get_func(imports, 'func1')
        #     local_func1()
        # elif 'func2' in request.form['button1']:
        #     local_func2 = get_func(imports, 'func2')
        #     local_func2()
    return render_template(index_page)


def run_flask(pages, global_imports):
    global imports, index_page
    index_page = pages['index']
    imports = global_imports
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(debug=True)  # Dev
#     # app.run()  # Prod
