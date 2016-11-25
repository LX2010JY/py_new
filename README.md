# py_new
新建一个，之前那个太多没用的东西了


>## 一切皆对象
>1. 在 Python 里面所有东西都是对象。字符串是对象，列表是对象，函数是对象，类是对象，类的实例是对象，甚至模块也是对象。

>2. 对象有一个内置的属性__doc__,访问它用来返回 对象里面定义的 docstring(也就是注释)

>'''
>	这是注释你信吗？
>'''

>3. 一切变量名 函数名，类名都是严格区分大小写的

>### if \_\_name\_\_ == "\_\_main\_\_"的含义

>我们写的一个py文件可以作为一个模块，而模块是对象，其内置了一个 \_\_name\_\_属性，如果通过import 你写的这个文件，那么 其\_\_name\_\_就是文件名，如果通过python直接执行的文件，那么\_\_name\_\_就等于 \_\_main\_\_.

# python包含的数据类型

	1. Booleans(布尔型)
	>python2 遗留问题 布尔值可以当做数字使用 True = 1 False = 0
	2. Numbers(数值型 包含integers,floats,complex,fractions)
	3. Strings(字符串型)
	4. Bytes(字节型) Byte Arrays(字节数组型) 
	5. Lists(列表 有序)
	6. Tuples(元组 有序 不可变)
	7. Sets(无序序列)
	8. Dictionaries(字典 键值对)
	
	>判断变量类型 isinstance(1,int) True 

###range(n)创建一个整数序列，但是它不是列表也不是元组，它是一个迭代器

# None
>None 是python特殊常量，它不等于0、空字符串、False，它不和任何非None相等，它有自己的数据类型 NoneType ，判断时 None 为 False ,not None 为 True

## 字符串前面的 r,u
>1. 经常在字符串前面加r ,如 `print(r'dfhajsd')` r代表其中的字符串都是普通字符，哪怕里面有`/\*&^%$`等待的特殊字符，都会直接输出，经常在正则表达式中使用
>2. u 代表Unicode编码格式，写非英文字符