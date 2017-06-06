#-*-coding:utf-8-*-
'''
    1.9 查找两个字典的相同点 （set可以直接减？）
'''
a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' :2
}
#查找键值集合的交集 （一样的键）
print(a.keys() & b.keys())
#在a 但是不在b的键值
print(a.keys()-b.keys())
#键和值都一样的
print(a.items()&b.items())
#列表生成器？字典生成器？生成器？
#字典q 键值去除 z 和 w的item
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)