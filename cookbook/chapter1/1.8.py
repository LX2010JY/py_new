#-*-coding:utf-8-*-
'''
    字典的运算，zip方法，将字典的键值反转
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM' : 205.55,
    'HPQ' : 37.20,
    'FB'  : 10.75
}
#比较价格大小
#用zip反转字典的键值,zip创建的是一个只能访问一次的迭代器
print(dict(zip(prices.values(),prices.keys())))
min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))

print('max:',max_price,'min',min_price)