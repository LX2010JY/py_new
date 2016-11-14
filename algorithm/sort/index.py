#-*-coding:utf-8 -*-

'''
	调用当前路径下所有的文件，使用其中方法
'''


# 引用本地的文件当做模块
import bubble_sort

li = [123,123,123,123,12,33,4,324,3,5,34,32]
bubble_sort.bubble(li)
# 显示bubble 函数中定义的docstring，也就是注释
print(bubble_sort.bubble.__doc__)
print(bubble_sort.__doc__)
