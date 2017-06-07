#coding:utf-8
from flask_script import Manager
from flask import Flask,redirect,abort,render_template,url_for,session,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

from datetime import datetime

app = Flask(__name__)
#CSRF 防止跨站攻击
app.config['SECRET_KEY'] = 'no key'

#flask扩展一般在创建程序的时候都需要初始化
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[DataRequired()])
    submit = SubmitField('Submit')
#页面未发现
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),400

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500



@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and form.name.data != old_name:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),current_time = datetime.utcnow())
    # return render_template('index.html',form=form,name=name,current_time = datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    '''
        含参数变量
    :param name:
    :return:
    '''
    # return '<h1>Hello,%s!</h1>' % name
    return render_template('user.html',name=name)

@app.route('/redirect')
def redit():
    '''
        跳转
    :return:
    '''
    return redirect('http://www.baidu.com')


if __name__ == "__main__":
    app.run(debug=True)