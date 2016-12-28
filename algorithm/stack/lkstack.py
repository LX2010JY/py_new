#coding : utf-8
'''
    链式存储结构的栈
'''
class Node(object):
    def __init__(self,data=None):
        self.data = data
        self.next = None




class LkStack(object):
    def __init__(self):
        self.top = Node()
        self.count = 0
    def length(self):
        '''
            栈的长度
        :return:
        '''
        return self.count
    def top(self):
        '''
            栈首元素
        :return:
        '''
        return self.top.data
    def is_empty(self):
        '''
            是否为空
        :return:
        '''
        return self.count == 0
    def push(self,val):
        '''
            插入一个新节点
        :param val:
        :return:
        '''
        tmp = Node(val)
        if self.is_empty():
            self.top=tmp
        else:
            tmp.next = self.top
            self.top = tmp
        self.count += 1

    def pop(self):
        '''
            去除栈尾元素
        :return:
        '''
        if self.is_empty():
            raise IndexError('栈已空')
        else:
            tmp = self.top
            self.top = self.top.next
            self.count -= 1
            return tmp.data
    def show_stack(self):
        '''
            打印栈
        :return:
        '''
        if self.is_empty():
            raise IndexError('栈已空')
        else:
            i = self.count
            tmp = self.top
            while i>0:
                print(tmp.data,end=' ')
                tmp = tmp.next
                i -= 1

if __name__ == '__main__':
    stack = LkStack()
    for i in range(10):
        stack.push(i)
    stack.show_stack()
    print(stack.pop())
    stack.show_stack()


