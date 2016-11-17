import generator

class Fib:
	'''
		斐波那契数列迭代器
	'''
	# __init__很像构造函数，但是它不是，因为在其调用之前，类对象就已经存在了
	# 每个类里面函数的第一个参数都指向类对象本身
	def __init__(self,max):
		self.max = max

	def __iter__(self):
		'''
			包含__iter__函数的类称为迭代器
			迭代器的类有三种方法   __init__， __iter__， 和 __next__， 起始和结束均为一对下划线（_） 字符。
			这种表示方法一般表示这是“特殊方法”，其特殊之处在于，它不能直接调用,当你使用实例的一些语法的
			时候，python会自动调用它们。
			比如iter(fib)
			比如for循环会调用__iter__,第一次初始化迭代器之后，仅返回执行了__next__之后的类对象，不再赋值初始化
		'''
		self.a = 0
		self.b = 1
		# 返回一个迭代器
		return self

	def __next__(self):
		fib = self.a
		if fib > self.max:
			raise StopIteration
		self.a,self.b = self.b,self.a+self.b
		return fib


# 将一个类实例化，只需要传入__init__中需要的值，就可返回不同的实例
fib = Fib(100)
print(fib.max)

# n 获取的是__next__返回的值
for n in Fib(1000):
	# end=" "的意思大概是输出n之后不换行，而是加上空格结尾
	print(n,end=" ")



class LazyRules:
	'''
		重写 generator.py 中的复数规则生成器
	'''
	# 此变量类的所有实例化对象共享，相当于静态变量
	rules_filename = "generator_rules.txt"
	def __init__(self):
		# 实例化类时，打开文件，但是不读取，初始化缓存，用于存储生成的函数序列
		self.pattern_file = open(self.rules_filename,encoding="utf-8")
		self.cache = []
	def __iter__(self):
		'''
			每一次for循环，都会调用一次__iter__方法，并返回一个迭代器
		'''
		self.cache_index = 0
		return self
	def __next__(self):
		self.cache_index += 1
		if len(self.cache) >=self.cache_index:
			return self.cache[self.cache_index - 1]
		if self.pattern_file.closed:
			raise StopIteration
		line = self.pattern_file.readline()
		if not line:
			self.pattern_file.close()
			raise StopIteration
		pattern,search,replace = line.split(None,3)
		funcs = generator.build_match_and_apply_functions(pattern,search,replace)
		self.cache.append(funcs)
		return funcs


rules = LazyRules()

def plural(noun):
	for match_rule,apply_rule in rules:
		if(match_rule(noun)):
			return apply_rule(noun)
print(plural('physics'))