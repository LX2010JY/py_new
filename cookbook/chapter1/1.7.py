#coding:utf-8
'''
字典元素排序  OrderedDict  其内部维护这一个双向链表，记录着插入顺序，一般这种方式比普通字典会大2倍
'''
from collections import OrderedDict
import json

#按顺序排序
def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    with(open("../../file/dict_order.json","w")) as f:
        f.write(json.dumps(d))

def normal_dict():
    d = {}
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    with(open("../../file/dict_normal.json","w")) as f:
        f.write(json.dumps(d))
if __name__ == '__main__':
    ordered_dict()
    normal_dict()
    with(open("../../file/dict_order.json","r")) as f:
        tmp = f.read()
    #重新从json中读取出来 之后 字典的顺序已经没有了
    d = json.loads(tmp)
    for i in d:
        print(i,d[i])