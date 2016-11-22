# ORM 技术 :Object-Relational Mapping ,将关系数据库的表结构映射到对象上
# ORM 添加一行记录可视为添加一个对象

from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__='user'

    id = Column(String(20),primary_key=True)
    name = Column(String)

# create_engine 初始化数据库
engine = create_engine('mysql+pymysql://root:@localhost:3306/test')
# DBSession可视为当前数据库的连接
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='5',name='Bob')
session.add(new_user)
session.commit()
session.close()


