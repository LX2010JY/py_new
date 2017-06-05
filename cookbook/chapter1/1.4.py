#-*-coding:utf-8-*-
'''
从数组中提取最大的N个数，或者最小的N个数                       此处堆排序
'''
import heapq

nums = [1,8,23,4,5,-1,-4,42,4,2]
print('largest:',heapq.nlargest(3,nums))
print('smallest:',heapq.nsmallest(3,nums))
#如果是字典，nlargest 和 nsmallest可接受第三个参数，指定比较的内容（是个函数，输入应该是可迭代对象的其中一个子项，输出是比较的内容）

dicts = [
    {'name':'IBM','famous':1,'price':98.2},
    {'name':'lenovo','famous':0.2,'price':60.5},
    {'name':'Apple','famous':1,'price':99.5}
]

#s.price dict has no attribute 'price' 字典不能用.的形式获取属性吗？只能用['price']?
print('dict largest:',heapq.nlargest(1,dicts,lambda s:s['price']))
print('dict smallest:',heapq.nsmallest(1,dicts,lambda s:s['famous']))


#heapq 的实现底层是以堆排序实现的，堆排序每一次第一个元素必然是最小的
heapq.heapify(nums)
print('smallest:',nums[0]) #堆排序最重要的特征，第一个元素一定是最小的

print(heapq.heappop(nums)) #弹出第一个元素，并且用剩下的元素中最小的元素替代,必须让第一个元素最小才能使用，否则它只是简单的弹出第一个元素
print(heapq.heappop(nums)) #这样可以连续获取最小的元素
print(heapq.heappop(nums))