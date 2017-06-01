#-*-coding:utf-8-*-
'''
列表生成式
1.把要生成的数放在前面
2.循环或者判断等条件放在后面
'''


#很简单，把生成数字的最后一步放到了最前面，其他部分没变化，只是没有换行
type1 = [x*x for x in range(1,101)]
print(type1)
type2 = [x*x for x in range(1,101) if x%2==0]
print(type2)
type3 = [m+n for m in 'ABC' for n in 'XYZ']
print(type3)

import os
type4 = [d for d in os.listdir('.')]
print(type4)