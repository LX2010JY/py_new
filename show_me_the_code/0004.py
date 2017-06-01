# coding:utf-8
import re
from collections import Counter
def word_count(txt):
    pattern = r'[a-zA-z]+'
    words = re.findall(pattern,txt)
    return Counter(words).items()

if __name__ == '__main__':
    txt = open('file/test.txt','r').read()
    print(word_count(txt))