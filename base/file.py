'''
	字节即字节，字符即字符
	字符串是Unicode编码的字符序列构成，但是在磁盘文件上，文件不是unicode编码的字符序列。文件是字节序列。
	读取一个文件，首先要把文件的字节序列转为字符序列
'''
'''
    f = open('../file/?',r) 获取打开文件的二进制流对象，想象一个指针指向二进制流的首位，通过移动指针读取所有的二进制内容，
    f.tell(),返回指针当前的位置,0表示在首位，f.seek(0)选择指针指向的位置，f.read(),读取从指针当前为到末尾内容，之后指针会指向内容末尾
    read()中可以添加参数，指定读取的长度，不指定参数就直接读到末尾
    
'''
# python 打开文件，如果没有指定encoding，那么python就会使用默认编码格式，而默认编码格式与使用电脑平台有关，
# 所以一个文件在自己电脑可能可以打开一个文件，但是换到其他电脑就不行了，所以一定要指定encoding

file = open("class.py")
try:
	print(file.read())
except:
	print('不加encoding错误')

f = open("class.py",encoding="utf-8")
print("fllename:{0}".format(f.name))
print("encoding:{0}".format(f.encoding))

line_number = 0


# open的encoding参数，写入文件的时候，因为文件不能存储字符序列，只能存字节序列，所以必须告知python使用何种编码格式将字符序列转为字节序列存入文件，否则读取文件时，由于不清楚编码格式，字节序列转字符序列将会出错
with(open('class.py','r',encoding='utf-8')) as wf:
	# 循环获取可以获取分行内容
	for item in wf:
		line_number +=1
		# 可以省略{1}中的数字
		print("{:>4} {}".format(line_number,item.rstrip()))

# 写入方式 w：覆盖 a: 追加
with(open('../file/write.txt','w',encoding="utf-8")) as ww:
	ww.write('你好')

# 打开非文本文件  需要file文件夹里添加一张图片
with(open("../file/180.jpg",mode="rb")) as pic:
    print("name:",pic.name)
    print("mode:",pic.mode)
    # 二进制的流对象没有encoding，因为图片不是字符，不需要将字节序列转化为字符序列，
    print("encoding:",pic.encoding)
