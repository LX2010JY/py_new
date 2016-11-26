'''
    装饰器，在函数执行前，默认给函数添加格外的功能
'''

def log(func):
    '''
        定义了一个装饰器，其本身是一个返回函数的高阶函数
        传入一个函数，添加额外操作以后，又将函数返回
        一切皆对象
    :param func:
    :return:
    '''
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

# 将@log 放在 函数上面，相当于执行了 now = log(now())
@log
def now():
    print('2016-11-26')

def log2(text):
    '''
        如果装饰器需要加上参数，需要三层函数
    :param text:
    :return:
    '''
    def decorator(func):
        def wrapper(*args,**kw):
            print("{0} {1}()".format(text,func.__name__))
            return func(*args,**kw)
        return wrapper
    return decorator

# execute传入第一层函数，那么下面的函数就传入第二层函数。这是为什么装饰器加上参数之后需要三层函数实现
@log2('execute')
def now2():
    print('2016-11-26 23:59')

if __name__ == '__main__':
    now()
    now2()