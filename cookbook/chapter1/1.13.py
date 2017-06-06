#coding:utf-8
'''
    字典序列 根据字典的某个关键字排序,使用operator模块的itemgetter函数
'''
from operator import itemgetter
rows = [
    {'fname':'Brian','lname':'Jones','uid':1003},
    {'fname':'David','lname':'Beazley','uid':1002},
    {'fname':'John','lname':'Cleese','uid':1001},
    {'fname':'Big','lname':'Jones','uid':1004}
]
rows_by_fname = sorted(rows,key=itemgetter('fname'))
rows_by_uid = sorted(rows,key=itemgetter('uid'))
print(rows_by_fname)
print(rows_by_uid)

#sorted函数接受一个函数参数，所以也可以不用 itemgetter 不过itemgetter更快一点
row_by_uid = sorted(rows,key=lambda x : x['uid'])
print(rows_by_uid[::-1])
