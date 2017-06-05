#coding:utf-8
'''
    实现一个优先级队列，每次pop都返回优先级最高的那个元素，利用heapq实现,没搞懂
'''
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

