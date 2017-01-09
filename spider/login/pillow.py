# coding:utf-8

from PIL import Image

im = Image.open('captcha.jpg')

w,h = im.size
print('当前图片的大小为：%s %s'%(w,h))

im.thumbnail((w//2,h//2))
print('缩小一般图片大小为:%s %s'%(w//2,h//2))
im.save('thumbnail.jpg',im.format)
