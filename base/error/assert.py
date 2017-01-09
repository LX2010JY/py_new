'''
    断言
'''

def foo(s):
    n = int(s)
    # 断言 如果n!=0为true ,那么继续执行，如果为false 那么执行，后面的内容
    assert n!=0, 'n is zero'
    return 10/n
def main():
    foo('0')

main()