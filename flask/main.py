#coding:utf-8
from flask_script import Manager
from flask import Flask,redirect,abort,render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
manager = Manager(app)
@app.route("/")
def hello():
    comments = [
        '你好','去死','再见','python','spider','machine learning','physics'
    ]
    # return "Hello World!"
    return render_template('index.html',comments = comments)

@app.route('/user/<name>')
def user(name):
    '''
        含参数变量
    :param name:
    :return:
    '''
    # return '<h1>Hello,%s!</h1>' % name
    return render_template('user.html',name=name)
@app.route('/user/<int:id>')
def get_user(id):
    user = load_user(id)

@app.route('/redirect')
def redit():
    '''
        跳转
    :return:
    '''
    return redirect('http://www.baidu.com')

if __name__ == "__main__":
    manager.run()