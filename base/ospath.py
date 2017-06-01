# -*-coding:utf-8-*-

import os

print(os.path)
#当前工作目录
print(os.getcwd())
# 修改工作目录
os.chdir('/')
print(os.getcwd())

dict_one = {1000:['KB','MB','GB','TB']}
'''
	格式化 format
'''

'''
	{0} 表示format()里面的第一个参数，类推{1}表示第二个
'''
print('100000byte=100{0[0]}'.format(dict_one[1000]))
# :表示后面的都是格式说明.1f 表示四舍五入保留一位小数
print('{0:.1f}GB={1}MB'.format(681.34,680000))

s = """Finish your code
women doushi haohaizi1
zuihounatian womne """
#已三个引号开头结尾的字符串，可以呀splitlines转换为列表，一行作为一个元素
print(s.splitlines())
# upper 大写，lower 转小写
print(s.upper());
# 统计字符串中d的个数
print(s.count('d'))
'''
	字符是字节的一种抽象，根本不存在字符，字符串可以看做是不可变的unicode编码的字符序列 字符串可以看做元组
	string 是字符序列 ， bytes是一串0-255之间数字组成的序列。
'''

# 定义byte类型 

by = b"asdasda" #python 默认定义编码格式为ascii，中文没法这样定义 
by = "我打瞌睡道具卡蝴蝶结款".encode('utf-8')
print(type(by))
print(by)