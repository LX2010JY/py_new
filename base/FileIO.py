'''
    使用IO模块
'''

import io
a_string = "hello this is string in memory"
# 将存在内存的字符串当做文件读取出来 把字符串当做文本文件处理（虽然不知道这么做有啥用）
a_file = io.StringIO(a_string)
print(a_file.read())
# 类型不是string 也不是 bytes 而是StringIOhuxa
print(type(a_file))
a_file.seek(0)
print(a_file.read(10))

b_byte = b'abcdefg'
b_file = io.BytesIO(b_byte)
print(b_file.read())
print(b_file.seek(2))
print(b_file.tell())
print(b_file.read())
print(b_file.tell())

# 操作压缩文件，import gzip ，不用解压文件，可像操作普通文件一样直接处理
import gzip
# out.txt.gz .gz 是后缀，压缩方式；out.txt是压缩文件的名称
with gzip.open('../file/out.txt.gz',mode="wb") as z_file:
    z_file.write("A nine mile walk is no joke,especially. in the rain.".encode("utf-8"))