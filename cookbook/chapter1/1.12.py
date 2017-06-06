#-*-coding:utf-8-*-
'''
统计序列中出现次数最多的元素
'''
import heapq
from collections import Counter
def count_word(items):
    '''
    这是我的解法
    :param items:
    :return:
    '''
    count = {}
    for word in items:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return heapq.nlargest(1,zip(count.values(),count.keys()))

def cookbook(words):
    '''
        cookbook的做法
    :param words:
    :return:
    '''
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)

if __name__ == '__main__':
    a = ['woed','sad','one','two','woed','three','one','woed']
    print(count_word(a))
    cookbook(a)