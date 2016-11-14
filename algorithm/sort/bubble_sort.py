#!/usr/bin/env python
# -*- coding:utf-8 -*-
def bubble(li):
	'''
		从小到大冒泡排序
	'''
	length = len(li)
	for i in range(length):
		for j in range(0,length-i-1):
			if li[j]>li[j+1]:
				li[j],li[j+1] = li[j+1],li[j]
	print(li)
if __name__ == '__main__':
	list1 = [23,34,35,34,564,6,54,6,5,7,56,7,56]
	bubble(list1)


