import random

def create_coupons(count,len=10):
    '''
        生成优惠券激活码
    :param count: 生成数量
    :param len:  码长度
    :return: 生成结果数组
    '''
    str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    coupons = []
    for i in range(0,count):
        coupon = ''
        for j in range(0,len):
            coupon += random.choice(str)
        if coupon not in coupons:
            coupons.append(coupon)
        else:
            i -= 1
    return coupons

def show_code(coupons):
    '''
        显示码
    :param coupons:
    :return:
    '''
    for coupon in coupons:
        print(coupon)

if __name__ == '__main__':
    coupons = create_coupons(20,20)
    show_code(coupons)