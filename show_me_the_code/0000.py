'''
   问题0000 图片右上角加上数字
'''
from PIL import Image,ImageFont,ImageDraw

im = Image.open("./file/180.jpg")
# 设置字体，大小
font = ImageFont.truetype('../file/MONACO.TTF',16,encoding='utf-8')
w,h = im.size
draw = ImageDraw.Draw(im)
draw.text((w-30,0),u'180',fill=(255,4,9),font=font)
im.show()
try:
    im.save('./file/result.jpg')
    print('保存成功')
except:
    print('保存失败')