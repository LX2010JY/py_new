# coding:utf-8
'''
    将0001生成的激活码 保存到数据库里面
'''
from sqlalchemy import Column,String,create_engine,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random
base = declarative_base()
class code(base):
    __tablename__ = 'code'
    id = Column(Integer,primary_key=True)
    code = Column(String)

def create_coupons(count,len=10):
    '''
        生成优惠券激活码
    :param count: 生成数量
    :param len:  码长度
    :return: 生成结果数组
    '''
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    coupons = []
    for i in range(0,count):
        coupon = ''
        for j in range(0,len):
            coupon += random.choice(str)
        if coupon not in coupons:
            coupons.append(coupon)
        else:
            i -= 1
    return coupons
def save_coupons(session,coupons):
    for coupon in coupons:
        c = code(code=coupon)
        session.add(c)
    session.commit()
if __name__ == '__main__':
    engine = create_engine('mysql+pymysql://root:@localhost:3306/test')
    DBsession = sessionmaker(bind=engine)
    session = DBsession()
    coupons = create_coupons(20,20)
    save_coupons(session,coupons)
    session.close()