'''
    对于进程来说，每一个进程都会复制一份数据，所以不用关心进程间数据的影响
    但是对于线程，其多个线程公用的事同一个数据，所以数据很容易混乱，在处理数据的时候加上锁，让多个线程之间互不影响
'''
import time,threading

# 定义一个线程锁
lock = threading.Lock()
balance = 0

def change_it(n):
    # 返回0
    global balance
    balance = balance + n
    balance = balance - n
    # print(balance)

def run_thread(n):
    global lock
    for i in range(10000):
        # 加上线程锁，不释放其他的线程不可用
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 线程锁释放
            lock.release()

if __name__ == '__main__':
    t1 = threading.Thread(target=run_thread,args=(5,))
    t2 = threading.Thread(target=run_thread,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)