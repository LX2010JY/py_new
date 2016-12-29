#coding: utf-8
'''
    十进制转二进制，十六进制
'''
def translate(num,type=16):
    if type == 16:
        sixteen = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        prefix = '0x'
        out = ''
        while num >0:
            yushu = num%16
            out = sixteen[yushu] + out
            num = int(num/16)
        return prefix+out
    else:
        out = ''
        while num >0:
            yushu = num%2
            if len(out)%5 == 0:
                out = ' ' + out
            out = str(yushu)+out
            num = int(num/2)
        return out

if __name__ == '__main__':
    num = input('输入需要转换的十进制数字：')
    try:
        print('十六进制：'+translate(int(num)))
        print('二进制：'+translate(int(num),2))
    except:
        raise ValueError('输入类型错误')