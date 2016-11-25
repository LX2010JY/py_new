import threading,time
'''
    多线程

    每个进程都默认带有一个主线程，线程才是程序执行的基本单位，主线程可以创建多个新的线程
    多进程之间互相数据不会影响，但是每个进程的数据只有一份，多线程同时访问，改动的是同一个变量
'''
def loop():
    print("thread {0} is running...".format(threading.current_thread().name))
    n = 0
    while n<5:
        n = n+1
        print("thread {0} >>> {1}".format(threading.current_thread().name,n))
        time.sleep(1)
    print("thread {0} is running...".format(threading.current_thread().name))

print("thread {0} is running...".format(threading.current_thread().name))
# t = threading.Thread(target=loop)
# t.start()
# t.join()
print('thread {0} is end'.format(threading.current_thread().name))

# 线程锁
lock = threading.Lock()

balance = 0
def change_it(n):
    global balance
    balance = balance+n
    time.sleep(0.1)
    balance = balance-n
def run_thread(n):
    global balance
    for i in range(1000):
        # 由于多个线程操作同一个数（全局变量），万一某个线程崩溃了，对于其他线程将会影响，结果肯定错误，所以需要给change_it函数一把线程锁
        # 表示一个线程只能执行完了函数的内容，锁才能打开，其他线程才能够执行
        # 第一步，获取锁
        lock.acquire()
        try:
            change_it(n)
        except:
            print("thread {0} 执行第{1}次时出现错误".format(threading.current_thread().name,i))
        finally:
            # 执行完毕，释放锁，如果不用try finally 那么一旦一个线程出错，将会死锁，所有线程都不能执行
            lock.release()

        print("thread {0} 第{1}次执行 {2} 结果:{3}".format(threading.current_thread().name,i,n,balance))

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()

print('thread {0} 报最终balance={1}'.format(threading.current_thread().name,balance))



