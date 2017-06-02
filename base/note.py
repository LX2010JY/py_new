'''
    一点平时觉得需要记下的细节笔记
'''

arr = []
# insert 在序列指定位置添加元素
arr.insert(1,1)
arr.insert(1,23)
arr.insert(0,122)
arr.insert(1,2333)
print(arr)
arr.clear()
arr = ['第一','第二','第三']

'''
    note 1:
'''
# join 将序列组装成字符串，注意的是：这里和JavaScript有很相似之处，但是js使用的方法是arr.join('>')，刚好相反。
str = '>'.join(arr)
print(str)

'''
    高阶函数：
    note 2:
'''
#map 函数作用于list的每一个变量，返回其值，生成新的数组 map(func,iterable)
#reduce 函数必须接受2个参数，对两个参数进行计算，返回一个值，和数组的下一个变量再次计算，最终返回一个值 reduce(func,iterable) = ...func(func(iterable[0],iterable[1]),iterable[2])...
#filter 过滤 函数参数 对数组元素计算，返回True或者False，False去除，True留下 filter(func,iterable)
arr = [1,2,3,4,5,6,7,8,9,10]
def map_func(x):
    return x*x
def reduce_func(x,y):
    return x+y
def filter_func(x):
    if x%2==0:
        return True
    return False

print(list(x for x in map(map_func,arr)))
from functools import reduce
print(reduce(reduce_func,arr))
print(list(x for x in filter(filter_func,arr)))

'''
    匿名函数 lambda：纳姆达
    lambda 以冒号隔开两部分 冒号前为函数需要的参数  冒号后为函数所做的操作
    note 3:
'''
# x的平方函数
def pingfang() :
    return lambda x:x*x
# 加法
def add():
    x,y=0,1
    return lambda x,y:x+y
# 函数参数带默认值的加法
def add2() :
    x,y = 0,1
    return lambda x=x,y=y:x+y
f = pingfang()
print(f(5))
f = add()
print(f(1,2))
f = add2()
print(f())

# 没有参数的函数
def printf():
    return lambda :print('Hello World')
f = printf()
f()