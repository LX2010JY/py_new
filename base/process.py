import os
from multiprocessing import Process,Pool,Queue
import time,random
def unix():
    '''
        只能运行在类unix系统上面
    :return:
    '''
    print('Process (%s) start ...' % os.getpid())
    # fork系统调用，创建了一个新的进程
    pid = os.fork()
    # fork函数调用一次，返回两次，因为操作系统将当前（父进程）进程复制了一份（子进程），分别从两个进程返回，父进程返回子进程id，子进程返回0
    if pid==0:
        print("I am child process (%s) and my parent is %s"%(os.getpid(),os.getppid()))
    else:
        print("I (%s) just create a child process (%s)."%(os.getpid(),pid))


def run_proc(name):
    '''
        子进程执行代码
    :param name: 进程名称
    :return:
    '''
    print('Run child process %s (%s)...'%(name,os.getpid()))

def allos():
    '''
        windows没有fork调用，上面不可用此方法适用于所有系统
        这个方法和多线程简直一毛一样
    :return:
    '''
    print('Parent process %s .'% os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    # join的作用，截断主进程后续代码的运行，必须子进程运行完之后才能继续
    p.join()
    print('Child process end')

def long_time_task(name):
    '''
        一个长时间运行的任务
    :param name: 进程名
    :return:
    '''
    print('Run process %s (%s)...'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s runs %0.2f seconds.'%(name,(end-start)))

def proc_pool(n):
    '''
        进程池
    :param n:
    :return:
    '''
    print('Parent process %s.'%os.getpid())
    # 进程池，最多创建n个进程，当进程池满的时候，新的创建进程请求就会等待，知道进程池中有空闲再继续创建
    p = Pool(n)
    for i in range(n):
        p.apply_async(long_time_task,args=(i,))
    print('waitting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

def write(q):
    '''
        写信息
    :param q: 数据信息队列
    :return:
    '''
    print('Process to write: %s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    '''
        读信息
    :param q:数据信息队列
    :return:
    '''
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)
        # time.sleep(random.random())
def exc_info():
    '''
        进程间通信
    :return:
    '''
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    # 写操作执行完了才能接下去执行，但是读操作没影响
    # 如果写操作执行完了，而读操作还没执行完，那么很有可能被直接中断
    pw.join()
    # pr是死循环，所以必须强行终止
    pr.terminate()

if __name__ == '__main__':
    # proc_pool(10)
    exc_info()