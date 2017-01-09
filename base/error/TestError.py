'''
    所有的错误异常都是类，每抛出一个异常都是对应类的对象
'''
class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s'% s)
foo(0)
