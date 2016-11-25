# -*-coding:utf-8-*-
'''
    @property 装饰器 将一个函数变为一个属性调用
    @变为属性的函数名.setter 是@property 创建的另一个装饰器，为当做属性的函数提供设置值的功能
'''
class Student:
    def func_get_score(self):
        return self._score
    def func_set_score(self,value):
        if not isinstance(value,int):
            raise ValueError("成绩必须是整数！")
        if value<0 or value>100:
            raise ValueError("成绩必须在0~100之间。")
        self._score = value
    '''
        以上是普通设置值的方法，
        以下是使用装饰器设置属性
    '''

    @property
    def score(self):
        return self._score
    # 此处装饰器的名称 score 不是由self._score 决定的，而是它装饰的这个函数的名字
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("成绩必须是整数！")
        if value<0 or value>100:
            raise ValueError("成绩必须在0~100之间。")
        self._score = value



if __name__ == '__main__':
    stu = Student()
    # 函数score被当做属性直接赋值，但是同时可以做此函数应该执行的操作（判断输入值是否合理）
    stu.score = 100
    print(stu.score)
