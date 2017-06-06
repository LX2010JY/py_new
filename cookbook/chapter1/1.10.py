#coding:utf-8
'''
    怎么在一个序列上面保持元素顺序的同时删除重复的值
'''
#如果序列的值都是hashable? 所谓可哈希，指的是对象不可修改，比如字符串，数字，tuple等，如果是list，dict即使不可哈希的
#此方法只适用于items元素是可哈希的，如果items是dict，试想还可以用吗？
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

#可用于不可哈希的
def dedupe2(items,key=None):
    '''
    :param items: 序列
    :param key: 一个函数，将不可哈希的元素转为hashable的元素
    :return:
    '''
    seen = set()
    for item in items:
        #这是什么鬼格式
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == '__main__':
    a = (12,32,2,324,3,1,23,3,43,2,334)
    print(list(dedupe(a)))
    #如果仅仅是想要去除重复，不用保留顺序的话，可以用set
    print(set(a))

    a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
    #将字典转为 tuple，只有可哈希的元素才能用 if item in items ?
    print(list(dedupe2(a,lambda b:(b['x'],b['y']))))

