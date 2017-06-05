#-*-coding:utf-8-*-
'''
将一个包含N个元素的可迭代对象 同时赋值给N个变量
'''

#list
a,b,c = [1,2,3]
print('list:',a,b,c)
#tuple
a,b,c = (1,2,3)
print('tuple:',a,b,c)
#dict 只会赋值键值
a,b,c = {'one':1,'two':2,'three':3}
print('dict:',a,b,c)
#set
a,b,c = set({1,2,3})
print('set:',a,b,c)
#string 字符串也是可迭代对象
a,b,c = '123'
print('string:',a,b,c)
