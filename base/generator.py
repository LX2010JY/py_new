import re
'''
	闭合与生成器
'''
def plural(noun):
	'''
		plural : 复数
		noun : 名称
		作用: 返回名词复数形式
	'''
	if(re.search('[syz]$',noun)):
		# re.sub 正则表达式字符串替换，其替换所有匹配的字符，并非单单第一个字符
		return re.sub("$","es",noun)
	elif re.search("[^aeioudgkprt]h$",noun):
		return re.sub("$","es",noun)
	elif re.search("[^aeiou]y$",noun):
		return re.sub("y$","ies",noun)
	else:
		return noun+"s"



'''
	将上面的plural函数，通过迭代的形式生成
	"<------------------开始（进阶第一步）--------------->"
'''
# 将plural函数中的每一个细节判断，返回都写成一个单独的函数
def match_sxz(noun):
    return re.search("[sxz]$", noun)

def apply_sxz(noun):
    return re.sub("$", "es", noun)

def match_h(noun):
    return re.search("[^aeioudgkprt]h$", noun)

def apply_h(noun):
    return re.sub("$", "es", noun)

def match_y(noun):                             
    return re.search("[^aeiou]y$", noun)
        
def apply_y(noun):                             
    return re.sub("y$", "ies", noun)

def match_default(noun):
    return True

def apply_default(noun):
    return noun + "s"

'''
	函数元组类型序列 ， 之所以可以如此，是因为python一切皆对象，函数也是对象，
	所以元组中包含的就是函数本身，而不是单单一个函数名
'''
rules = (
	(match_sxz,apply_sxz),
	(match_h,apply_h),
	(match_y,apply_y),
	(match_default,apply_default)
	)


def plural_new(noun):
	'''
		新的名词复数生成函数,
		因为rules序列中包含的是一个个实际的函数对象，所以match_rule,apply_rule都是一个个可以调用的函数
	'''
	for match_rule,apply_rule in rules:
		if match_rule:
			return apply_rule

'''
<------------------结束（进阶第一步）------------------>
'''

'''
<------------------开始（进阶第二步）------------------>
因为大多数拆分的函数都是很相似的，所以可以将其转化为一个函数处理
'''

def build_match_and_apply_functions(pattern,search,replace):
	# word 变量不需要值，因为返回的只是定义的两个函数，并不是要在这里执行它们，获取返回的函数之后再传值
	def matches_rule(word):
		return re.search(pattern,word)
	def apply_rule(word):
		return re.sub(search,replace,word)
	return (matches_rule,apply_rule)

patterns = (
    ("[sxz]$",           "$",  "es"),
    ("[^aeioudgkprt]h$", "$",  "es"),
    ("(qu|[^aeiou])y$",  "y$", "ies"),
    ("$",                "$",  "s")
)
rules_two = [build_match_and_apply_functions(pattern,search,replace) for pattern,search,replace in patterns]

def plural_two(noun):
	for match_rule,apply_rule in rules_two:
		if(match_rule(noun)):
			return apply_rule(noun)

'''
	<---------------------结束（进阶第二步）----------------------->
'''

'''
	<---------------------开始（进阶第三步）----------------------->
	从文件里面读取rules规则
'''
rules_three = []
with open("generator_rules.txt",encoding="utf-8") as pattern_file:
	# python 可以通过循环读取一行行的内容
	for line in pattern_file:
		# split(None,3) None表示任何空白字符，包括tab，space。3表示拆分成3块
		pattern3,search3,replace3 = line.split(None,3)
		rules_three.append(build_match_and_apply_functions(pattern3,search3,replace3))

def plural_three(noun):
	for match_rule,apply_rule in rules_three:
		if(match_rule(noun)):
			return apply_rule(noun)


'''
	<--------------------开始（最终第四步）----------------->
	生成器方式
'''
def rules_last(rules_filename):
	'''
		这是一个生成器
	'''
	with open(rules_filename,encoding="utf-8") as f:
		for line in f:
			p,s,r = line.split(None,3)
			# yield 相当于暂停函数的执行，但是保存了函数执行到这儿所有的状态，变量值，使用next调用时即可接下去执行
			yield build_match_and_apply_functions(p,s,r)
def plural_last(noun,rules_filename="generator_rules.txt"):
	for matches_rule,apply_rule in rules_last(rules_filename):
		# for循环可以直接调用next函数，执行生成器
		if matches_rule(noun):
			return apply_rule(noun)
	raise ValueError("对于{0},没有合适的匹配规则".format(noun))

if __name__ == "__main__":
	print(plural_last('good'))

