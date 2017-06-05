#-*-coding:utf-8-*-
'''
字典的键映射多个值，主要是介绍一个方法
'''
#一般字典键值要想对于 多个值，只能这样,这样的字典怎么生成，在这里就不写了，传统的方法应该懂
d = {
    'one' : [1,2,3,4],
    'two' : [33,54,23]
}
#主要是介绍不传统的方法
from collections import defaultdict

d = defaultdict(list)  #在此处确定了键对应的值的结构类型
d['a'].append(1)       # 所以在这里可以直接用list的方法
d['a'].append(2)
d['b'].append(12)

print(d)
d = defaultdict(set) #键值类型为set
d['a'].add(1)
d['a'].add(2)
d['b'].add(12)
print(d)