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
