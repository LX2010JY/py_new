# coding:utf-8
'''
    二分查找算法
'''
def binary_search(find,list1):
    '''
        将有序的列表折半查找
    :param find:
    :param list1:
    :return:
    '''
    low = 0
    high = len(list1)
    while low <= high:
        # / 除得到的是小数，//得到的是整数
        mid = (low+high) // 2
        if list1[mid]==find:
            return mid
        elif list1[mid]>find:
            high = mid - 1
        else:
            low = mid+1

    return -1

if __name__ == '__main__':
    list1 = [1,2,3,7,8,9,10,5,13]
    list1.sort()
    print('原有序列为：',list1)
    try:
        find = int(input('请输入要查找的数字：'))
    except:
        print('请输入整数！！！')
        exit()

    result = binary_search(find,list1)
    if result == -1:
        print('未找到')
    else:
        print('数字{0}在列表{1}中的第{2}位.'.format(find,list1,result+1))

