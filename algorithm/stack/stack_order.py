# coding:utf-8
'''
    顺序存储栈
'''
class stack(object):
    def __init__(self,size):
        if isinstance(size,int) and size>0:
            self.data = list(None for _ in range(size))
            self.top = -1
            self.size = size
        else:
            raise ValueError('栈的大小必须是大于0的整数')

    def  length(self):
        '''
            获取栈的长度
        :return:
        '''
        return self.top+1

    def push(self,val):
        '''
            加入一个元素
        :param val:
        :return:
        '''
        if self.top+1==self.size:
            raise IndexError('栈已满')
        else:
            self.top+=1
            self.data[self.top] = val

    def pop(self):
        if self.top == -1:
            raise IndexError('栈已空')
        else:
            self.top -= 1
            return self.data[self.top + 1]

    def top(self):
        if self.top == -1:
            raise IndexError('栈已空')
        else:
            return self.data[self.top + 1]
    def show_stack(self):
        i = self.top
        while i>=0:
            print(self.data[i],end=' ')
            i -= 1

    def is_empty(self):
        return self.top == -1

if __name__ == '__main__':
    stack = stack(10)
    stack.push('asdasd')
    for i in range(9):
        stack.push(i)
    stack.show_stack()
    print(stack.pop())
    stack.show_stack()




