#coding:utf-8
# 保留最后的N条记录
# 程序作用：按行读取一个文件，每行查找符合要求的行，找到之后，输出该行，并且输出此行之前的5行数据
from collections import deque
def search(lines,pattern,history=5):
    # deque是一个队列，设置了maxlen，则队列只能存储设置的大小，如果超过，则前面的数据则会出队(使用 append前提下) appendleft 出队和入队相反
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)


def createfile():
    with(open('../file/lines.txt','w',encoding='utf-8')) as f:
        f.write('ls -l in the world\n')
        f.write('lift is short , I use python \n')
        f.write('this is a pen \n')
        f.write('炼金狂士地方将卡萨丁很快就我还打开\n')
        f.write('爱上即可打开老实交代\n')
        f.write('aksjdklajdklasjdkasdjasldjasld\n')
        f.write('aklsdjl的卢卡斯加大快乐圣诞节爱上了肯德基阿里\n')
        f.write('1+2=122;and 09*192=12\n')
        f.write('this is python last one\n')
if __name__ == '__main__':
    createfile()

    with(open('../file/lines.txt','r',encoding='utf-8')) as f:
        for line,prevlines in search(f,'python',5):
            for pline in prevlines:
                # end=''，输出结尾不换行，而是'';
                print(pline,end='')
            print(line,end='')
            print('-'*20)


