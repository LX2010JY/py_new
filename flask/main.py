#coding:utf-8
from flask_script import Manager
from flask import Flask,redirect,abort,render_template,url_for,session,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand

from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

from datetime import datetime
import os
app = Flask(__name__)
#CSRF 防止跨站攻击
app.config['SECRET_KEY'] = 'no key'
basedir = os.path.dirname(__file__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data/data.sqlite')
app.config['SQLACHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


#flask扩展一般在创建程序的时候都需要初始化
manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

#定义数据表模型 （难）
class Role(db.Model):
    '''
        定义数据表roles的模型Role(注意：一个是复数，一个是单数，不要混了)
    '''
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    #这里定义user和role的关系，调用users可以获取在这个角色下所有相关的user信息
    #话说外键不是不能用的吗
    users = db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %r' % self.name

class User(db.Model):
    '''
        定义users表的模型User
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    #定义外键 ，话说外键也是 数据表的一个字段，别特殊化了
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username

#定义表单
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
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'),current_time = datetime.utcnow(),known=session.get('known'))

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
    # app.run(debug=True)
    manager.run()