#-*-coding:utf-8-*-
'''
基本雷同与 1.1 ，当可迭代对象的数量超过N时，怎么从可迭代对象中同时复制N个变量，如果不做任何处理，将会抛出一个ValueError
'''
from functools import reduce
def avg(nums):
    all = reduce(lambda x,y:x+y,nums)
    return all/len(nums)

def drop_first_last(grades):
    '''
    去掉一个最低分，再去掉一个最高分
    使用星号来代替无限不可知的变量
    :param grades: 分数列表
    :return:
    '''
    grades.sort()
    first,*middle,last = grades
    return avg(middle)

if __name__ =='__main__':
    grades = [85,91,98,134,94,39]
    avg_grade = drop_first_last(grades)
    print(avg_grade)

    url = 'http://www.lexue100.com/student.php?do=index&randstr=14966364902'
    #split 切割字符串 类似php的explode
    protocol ,*center,last_path =  url.split('/')
    php,val = last_path.split('?')
    print(protocol,val)
