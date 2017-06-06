#coding:utf-8
'''
    命名切片，清理固定下标的硬编码
'''

record = '....................100.......513.25...........'
#此处切片的位置是固定的，为硬编码
print(int(record[20:23])*float(record[30:36]))

SHARES = slice(20,23)
PRICE = slice(30,36)
#此处下标为变量，非硬编码
print(int(record[SHARES]) * float(record[PRICE]))