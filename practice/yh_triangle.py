#-*-coding:utf-8-*-
'''
    使用生成器生成杨辉三角，一次返回一行
'''
def trangle():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [L[i-1]+L[i] for i in range(len(L))]

index , max = 0,20
for line in trangle() :
    print(line)
    index = index + 1
    if index>max:
        break


