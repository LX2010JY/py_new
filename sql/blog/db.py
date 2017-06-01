# coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer

engine = create_engine('mysql+pymysql://root@localhost:3306/blog?charset=utf8')
print(engine)
Base = declarative_base() #将数据表结构用ORM语言描述出来
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    username = Column(String(64),nullable=False,index=True)
    password = Column(String(64),nullable=False)
    email = Column(String(64),nullable=False,index=True)

    def __repr__(self):
        return "{0}({1})".format(self.__class__.__name__,self.username)
luoxiao = User(username='luoxiao',password='asdasd',email='asdas@1223.cn')
