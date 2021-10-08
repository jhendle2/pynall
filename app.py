import sys
from script_manager.script_importer import get_func
from flask import Flask, redirect, url_for, request, render_template

imports = None
app = Flask(__name__)


def func1():
    print('Hello World', file=sys.stderr)


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("test_old.html")


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
        if 'func1' in request.form['button1']:
            local_func1 = get_func(imports, 'func1')
            local_func1()
        elif 'func2' in request.form['button1']:
            local_func2 = get_func(imports, 'func2')
            local_func2()
    return render_template("test_old.html")


def run_flask(global_imports):
    global imports
    imports = global_imports
    app.run(debug=True)

# if __name__ == '__main__':
#     app.run(debug=True)  # Dev
#     # app.run()  # Prod
