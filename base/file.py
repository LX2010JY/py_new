'''
	字节即字节，字符即字符
	字符串是Unicode编码的字符序列构成，但是在磁盘文件上，文件不是unicode编码的字符序列。文件是字节序列。
	读取一个文件，首先要把文件的字节序列转为字符序列
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