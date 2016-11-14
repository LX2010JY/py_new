# -*-coding:utf-8-*-
'''
	集合set 和 字典 dict的操作方法
	集合，同其名，和数学上的集合一样有各种关系
	集合的内容和list不一样，其中的顺序是不规律的，不是后加的就排在后面
'''

# 初始化一个集合
set_one = set()
# 初始化一个字典
dict_one = {}

set_one.add(4)
set_one.add(5)
print('*'*10+"第一次添加集合"+"*"*10)
print(set_one)

# update 和 add区别在 update参数必须是一个集合
#集合不会添加重复的内容
set_one.update({5,7,9})
print("*"*10+"第二次update集合"+"*"*10)
print(set_one)


'''
	删除集合的一个数值
	1. discard 和 remove的区别 ，删除不存在的数据是，discard会忽略，remove会报错
	2. pop() 删除数据 ，list是删除最后一个，但是 集合因为内容排序无规律，所以pop删除数据也是随机的(其实是有规律的，看起来随机)
	若set_one 为空，则pop会报错
	3. clear() 清空集合
'''

try:
	set_one.discard(5)
	set_one.discard(18)
except:
	print('discard 删除错误')

print("*"*10+"第一次discard数据"+"*"*10)
print(set_one)

set_one.add(5)


try:
	set_one.remove(5)
	set_one.remove(18)
except:
	print('remove 删除错误')


print("*"*10+"第二次remove数据"+"*"*10)
print(set_one)


'''
	集合之间的数学运算
	set_one.issubset(set_two) 子集
	set_one.issuperset(set_two) 超集
'''

set_two = {1,5,6,7,8,9,0}

# 获取两个集合中所有出现过的元素
set_union = set_one.union(set_two)
print("*"*10+"两个集合union<交集>的结果"+"*"*10)
print('set_one:',set_one)
print('set_two:',set_two)
print('union:',set_union)

# 获取两个集合都存在的元素

set_bing = set_one.intersection(set_two)

print("*"*10+"两个集合<并集>的结果"+"*"*10)
print('bing:',set_bing)

set_diff = set_one.difference(set_two)
print("*"*10+"前一个集合存在，后一个不存在的元素"+"*"*10)
print('diff:',set_diff)

set_alldiff = set_one.symmetric_difference(set_two)
print("*"*10+"交集减去并集"+"*"*10)
print('alldiff:',set_alldiff)


'''
	字典（键值对） 其中的键就是集合
'''

dict_one = {'one':[12,3,454,564],'two':(23,234,345,3456,4,123)}
dict_one['three'] = {123,234,2345,3,54,5,34,5,123}
print("*"*10+"字典添加"+"*"*10)
print(dict_one)