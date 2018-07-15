#环境
    #- xubuntu 16.04
    #- anaconda
    #- pycharm
    #- python 3.6
#多线程和多进程
    #- 程序：一堆代码以文本的形式存入一个文档
    #- 进程：程序运行的一个状态
        #- 包含地址空间，内存，数据线等
        #- 每个进程由自己完全独立的运行环境，多进程共享数据是一个问题
    #- 线程
        #- 一个进程的独立运行片段，一个进程可以由多个线程
        #- 轻量化的进程
        #- 一个进程的多个现场间共享数据和上下文运行环境
        #- 共享互斥问题
#全局解释器锁（GIL）
    #- Python代码的执行是由python虚拟机进行控制
    #- 在主循环中只能有一个控制线程在执行

#Python 包
    #- thread：有问题，不好用，Python 3改成_thread
    #- threading: 目前用的包


#- 利用 time函数，生成两个函数，顺序调用，计算运行时间
# import time
#
#
# def loop1():
#     #ctime 得到当前时间
#     print('Start loop 1 at:',time.ctime())
#     time.sleep(4)
#     print('End loop 1 at:', time.ctime())
#
#
# def loop2():
#     # ctime 得到当前时间
#     print('Start loop 2 at:', time.ctime())
#     time.sleep(2)
#     print('End loop 2 at:', time.ctime())
#
# def main():
#     print('Starting at:',time.ctime())
#     loop1()
#     loop2()
#     print('all done at:', time.ctime())
#
# if __name__ == '__main__':
#     main()


#threading 的使用
    #- 直接利用threading.Tread（target=xxx，argx= （xxx，））
    #- t.start（）：启动多线程 eg4
    #- t.join）：等待多线程执行完成 eg5
    #- 守护线程-daemo
        #- 如果在程序中将子线程设置成守护线程，则子线程会在主线程结束的时候自动退出
        #- 一般认为，守护线程不重要或不允许离开主线程独立运行
        #- eg6 and eg7
    #- 线程常用属性
        # - threading.currentThread：返回当前线程变量
        # - threading.enumerate：返回一个包含正在运行的线程list，正在运行的线程是指线程启动后，结束前的线程
        # - threading.activeCount：返回正在运行的线程数量，效果跟len（threading.enumerate）相同
        # - thr.setName：给线程设置名字
        # - thr.getName:得到线程名字
        # - eg8
    # - 直接继承自threading.Thread
    #     - 直接继承
    #     - 重写润函数
    #     - 类实例就可以直接运行了
    # eg9
    # eg10 工业风实例


# - 共享变量
    # - 共享变量： 当多个现成同时访问一个变量的时候，会产生共享变量的问题
    # - 案例11
    # - 解决变量：锁，信号灯，
    # - 锁（Lock）：
        # - 是一个标志，表示一个线程在占用一些资源
        # - 使用方法
            # - 上锁
            # - 使用共享资源，放心的用
            # - 取消锁，释放锁
            # - eg12
        # - 锁谁： 哪个资源需要多个线程共享，锁哪个
        # - 理解锁：锁其实不是锁住谁，而是一个令牌
    # - 线程安全问题：
        # - 如果一个资源 / 变量，他对于多线程来讲，不用加锁也不会引起任何问题，则称为线程安全
        # - 线程不安全变量类型： list, set, dict
        # - 线程安全变量类型： queue
    # - 生产者消费者问题
        # - 一个模型，可以用来搭建消息队列，
        # - queue是一个用来存放变量的数据结构，特点是先进先出，内部元素排队，可以理解成一个特殊的list
    # - 死锁问题, eg14
    # - 锁的等待时间问题， eg5
    # - semphore
        # - 允许一个资源最多由几个多线程同时使用
        # - eg16
    # - threading.Timer
        # - eg17
    # - Timer是利用多线程，在指定时间后启动一个功能

    # - 可重入锁
        # - 一个锁，可以被一个线程多次申请
        # - 主要解决递归调用的时候，需要申请锁的情况
        # - 案例18
# 线程替代方案
    # -  subprocess
        # - 完全跳过线程，使用进程
        # - 是派生进程的主要替代方案
        # - python2.4后引入
    # - multiprocessiong
        # - 使用threadiing借口派生，使用子进程
        # - 允许为多核或者多cpu派生进程，接口跟threading非常相似
        # - python2.6后引入
    # - concurrent.futures
        # - 新的异步执行模块
        # - 任务级别的操作
        # - python3.2后引入
# 多进程
    # - 进程间通讯(InterprocessCommunication, IPC)
    # - 进程之间无任何共享状态
    # - 进程的创建
        # - 直接生成Process实例对象， 案例19
        # - 派生子类， 案例20
        #
    # - 在os中查看pid，ppid以及他们的关系
        # - 案例21
    # - 生产者消费者模型
        #    - JoinableQueue
        # - 案例22
        # - 队列中哨兵的使用, 案例23
        # - 哨兵的改进， 案例24


#eg4
# import time
# import threading
#
# def loop1(in1):
#     # ctime 得到当前时间
#     print('Start loop 1 at:', time.ctime())
#     print("我是参数", in1)
#     time.sleep(4)
#     print('End loop 1 at:', time.ctime())
#
# def loop2(in1, in2):
#     # ctime 得到当前时间
#     print('Start loop 2 at:', time.ctime())
#     print("我是参数", in1, "和参数", in2)
#     time.sleep(2)
#     print('End loop 2 at:', time.ctime())
#
# def main():
#     print('Starting at:',time.ctime())
#     t1 = threading.Thread(target=loop1, args=("王老大",))
#     t1.start()
#     t2 = threading.Thread(target=loop2, args=("王大鹏","王晓鹏"))
#     t2.start()
#     print('all done at:', time.ctime())
#
# if __name__ == '__main__':
#     main()
#     #一定要有while语句
#     #因为启动多线程后本程序就作为主线程存在
#     #如果主线程执行完毕，则子线程可能也需要终止
#     while True:
#         time.sleep(10)
#
#eg5
# import time
# import threading
#
# def loop1(in1):
#     # ctime 得到当前时间
#     print('Start loop 1 at:', time.ctime())
#     print("我是参数", in1)
#     time.sleep(4)
#     print('End loop 1 at:', time.ctime())
#
# def loop2(in1, in2):
#     # ctime 得到当前时间
#     print('Start loop 2 at:', time.ctime())
#     print("我是参数", in1, "和参数", in2)
#     time.sleep(2)
#     print('End loop 2 at:', time.ctime())
#
# def main():
#     print('Starting at:',time.ctime())
#     t1 = threading.Thread(target=loop1, args=("王老大",))
#     t1.start()
#     t2 = threading.Thread(target=loop2, args=("王大鹏","王晓鹏"))
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print('all done at:', time.ctime())
#
# if __name__ == '__main__':
#     main()
#     #一定要有while语句
#     #因为启动多线程后本程序就作为主线程存在
#     #如果主线程执行完毕，则子线程可能也需要终止
#     while True:
#         time.sleep(10)


#eg6 无守护线程

# import time
# import threading
#
# def fun():
#     print("Start fun")
#     time.sleep(2)
#     print("end fun")
#
# print("Maub thread")
#
# ti = threading.Thread(target=fun, args=())
# ti.start()
#
# time.sleep(1)
# print("Main thread end")

#eg7 守护线程

# import time
# import threading
#
#
# def fun():
#     print("Start fun")
#     time.sleep(2)
#     print("end fun")#守护线程的存在，使得打印end fun不被执行
#
#
# print("Maub thread")
#
# ti = threading.Thread(target=fun, args=())
#
# ti.setDaemon(True)#守护线程
#
# ti.start()
#
# time.sleep(1)
# print("Main thread end")

#eg8
# import time
# import threading
#
# def loop1():
#     print('Start loop 1 at:',time.ctime())
#     time.sleep(6)
#     print('End loop 1 at:', time.ctime())
#
# def loop2():
#     print('Start loop 2 at:',time.ctime())
#     time.sleep(1)
#     print('End loop 2 at:', time.ctime())
#
# def loop3():
#     print('Start loop 3 at:',time.ctime())
#     time.sleep(5)
#     print('End loop 3 at:', time.ctime())
#
# def main():
#     print('Starting at:',time.ctime())
#     #生成threading.Thread实例
#     t1 = threading.Thread(target=loop1, args=())
#     t1.setName("THR_1")#给子线程设置一个名字
#     t1.start()
#
#     t2 = threading.Thread(target=loop2, args=())
#     t2.setName("THR_2")
#     t2.start()
#
#     t3 = threading.Thread(target=loop3, args=())
#     t3.setName("THR_3")
#     t3.start()
#     #预期三秒后t2结束
#     time.sleep(3)
#     #enumerate 得到正在的运行的t1t3
#     for thr in threading.enumerate():
#         #getName得到名字
#         print("现在正在运行的线程名字为：{0}".format(thr.getName()))
#
#     print("现在运行的子线程数量为：{0}".format(threading.activeCount()))
#
#     print('all done at:', time.ctime())
#
# if __name__ == '__main__':
#     main()
#     #一定要有while语句
#     #因为启动多线程后本程序就作为主线程存在
#     #如果主线程执行完毕，则子线程可能也需要终止
#     while True:
#         time.sleep(10)


#eg 9
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def __init__(self,arg):
#         super(MyThread,self).__init__()
#         self.arg = arg
#
#     def run(self):
#         time.sleep(2)
#         print("The args for this class is {0}".format(self.arg))
#
# for i in range(5):
#     t = MyThread(i)
#     t.start()
#     t.join()
#
# print("Main thread is done !!!!!!")

#eg10
# import threading
# from time import sleep, ctime
#
#
# loop = [4,2]
#
# class ThreadFunc():
#
#     def __init__(self, name):
#         self.name = name
#
#     def loop(self, nloop, nsec):
#         '''
#         :param nloop: loop函数的名称
#         :param nsec: 系统休眠时间
#         :return:
#         '''
#         print('Start loop ', nloop, 'at ', ctime())
#         sleep(nsec)
#         print('Done loop ', nloop, ' at ', ctime())
#
# def main():
#     print("Starting at: ", ctime())
#
#     # ThreadFunc("loop").loop 跟一下两个式子相等：
#     # t = ThreadFunc("loop")
#     # t.loop
#     # 以下t1 和  t2的定义方式相等
#     t = ThreadFunc("loop")
#     t1 = threading.Thread( target = t.loop, args=("LOOP1", 4))
#     # 下面这种写法更西方人，工业化一点
#     t2 = threading.Thread( target = ThreadFunc('loop').loop, args=("LOOP2", 2))
#
#     # 常见错误写法
#     #t1 = threading.Thread(target=ThreadFunc('loop').loop(100,4))
#     #t2 = threading.Thread(target=ThreadFunc('loop').loop(100,2))
#
#     t1.start()
#     t2.start()
#
#     t1.join( )
#     t2.join()
#
#
#     print("ALL done at: ", ctime())
#
#
# if __name__ == '__main__':
#     main()
#


#eg11
# import threading
#
# sum = 0
# loopSum = 1000000
#
#
# lock = threading.Lock()
#
#
# def myAdd():
#     global  sum, loopSum
#
#     for i in range(1, loopSum):
#         # 上锁，申请锁
#         lock.acquire()
#         sum += 1
#         # 释放锁
#         lock.release()
#
#
# def myMinu():
#     global  sum, loopSum
#     for i in range(1, loopSum):
#         lock.acquire()
#         sum -= 1
#         lock.release()
#
# if __name__ == '__main__':
#     print("Starting ....{0}".format(sum))
#
#     # 开始多线程的实例，看执行结果是否一样
#     t1 = threading.Thread(target=myAdd, args=())
#     t2 = threading.Thread(target=myMinu, args=())
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("Done .... {0}".format(sum))


#eg12

# import threading
#
# sum = 0
# loopSum = 1000000
#
#
# lock = threading.Lock()
#
#
# def myAdd():
#     global  sum, loopSum
#
#     for i in range(1, loopSum):
#         # 上锁，申请锁
#         lock.acquire()
#         sum += 1
#         # 释放锁
#         lock.release()
#
#
# def myMinu():
#     global  sum, loopSum
#     for i in range(1, loopSum):
#         lock.acquire()
#         sum -= 1
#         lock.release()
#
# if __name__ == '__main__':
#     print("Starting ....{0}".format(sum))
#
#     # 开始多线程的实例，看执行结果是否一样
#     t1 = threading.Thread(target=myAdd, args=())
#     t2 = threading.Thread(target=myMinu, args=())
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("Done .... {0}".format(sum))


# eg13
#
# #encoding=utf-8
# import threading
# import time
#
# # Python2
# # from Queue import Queue
#
# # Python3
# import queue
#
#
# class Producer(threading.Thread):
#     def run(self):
#         global queue
#         count = 0
#         while True:
#             # qsize返回queue内容长度
#             if queue.qsize() < 1000:
#                 for i in range(100):
#                     count = count +1
#                     msg = '生成产品'+str(count)
#                     # put是网queue中放入一个值
#                     queue.put(msg)
#                     print(msg)
#             time.sleep(0.5)
#
#
# class Consumer(threading.Thread):
#     def run(self):
#         global queue
#         while True:
#             if queue.qsize() > 100:
#                 for i in range(3):
#                     # get是从queue中取出一个值
#                     msg = self.name + '消费了 '+queue.get()
#                     print(msg)
#             time.sleep(1)
#
#
# if __name__ == '__main__':
#     queue = queue.Queue()
#
#     for i in range(500):
#         queue.put('初始产品'+str(i))
#     for i in range(2):
#         p = Producer()
#         p.start()
#     for i in range(5):
#         c = Consumer()
#         c.start()

# eg14
# import threading
# import time
#
# lock_1 = threading.Lock()
# lock_2 = threading.Lock()
#
#
#
#
# def func_1():
#    print("func_1 starting.........")
#    lock_1.acquire()
#    print("func_1 申请了 lock_1....")
#    time.sleep(2)
#    print("func_1 等待 lock_2.......")
#    lock_2.acquire()
#    print("func_1 申请了 lock_2.......")
#
#    lock_2.release()
#    print("func_1 释放了 lock_2")
#
#    lock_1.release()
#    print("func_1 释放了 lock_1")
#
#    print("func_1 done..........")
#
#
# def func_2():
#    print("func_2 starting.........")
#    lock_2.acquire()
#    print("func_2 申请了 lock_2....")
#    time.sleep(4)
#    print("func_2 等待 lock_1.......")
#    lock_1.acquire()
#    print("func_2 申请了 lock_1.......")
#
#    lock_1.release()
#    print("func_2 释放了 lock_1")
#
#    lock_2.release()
#    print("func_2 释放了 lock_2")
#
#    print("func_2 done..........")
#
# if __name__ == "__main__":
#
#    print("主程序启动..............")
#    t1 = threading.Thread(target=func_1, args=())
#    t2 = threading.Thread(target=func_2, args=())
#
#    t1.start()
#    t2.start()
#
#    t1.join()
#    t2.join()
#
#    print("主程序启动..............")


# eg15
# import threading
# import time
#
# lock_1 = threading.Lock()
# lock_2 = threading.Lock()
#
# def func_1():
#     print("func_1 starting.........")
#     lock_1.acquire(timeout=4)
#     print("func_1 申请了 lock_1....")
#     time.sleep(2)
#     print("func_1 等待 lock_2.......")
#
#     rst = lock_2.acquire(timeout=2)
#     if rst:
#         print("func_1 已经得到锁 lock_2")
#         lock_2.release()
#         print("func_1 释放了锁 lock_2")
#     else:
#         print("func_1 注定没申请到lock_2.....")
#
#     lock_1.release()
#     print("func_1 释放了 lock_1")
#
#     print("func_1 done..........")
#
#
# def func_2():
#     print("func_2 starting.........")
#     lock_2.acquire()
#     print("func_2 申请了 lock_2....")
#     time.sleep(4)
#     print("func_2 等待 lock_1.......")
#     lock_1.acquire()
#     print("func_2 申请了 lock_1.......")
#
#     lock_1.release()
#     print("func_2 释放了 lock_1")
#
#     lock_2.release()
#     print("func_2 释放了 lock_2")
#
#     print("func_2 done..........")
#
# if __name__ == "__main__":
#
#     print("主程序启动..............")
#     t1 = threading.Thread(target=func_1, args=())
#     t2 = threading.Thread(target=func_2, args=())
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#     print("主程序结束..............")

# eg16
# import threading
# import time
#
# # 参数定义最多几个线程同时使用资源
# semaphore = threading.Semaphore(3)
#
# def func():
#     if semaphore.acquire():
#         for i in range(5):
#             print(threading.currentThread().getName() + ' get semaphore')
#         time.sleep(15)
#         semaphore.release()
#         print(threading.currentThread().getName() + ' release semaphore')
#
#
# for i in range(8):
#     t1 = threading.Thread(target=func)
#     t1.start()

# eg17
# import threading
# import time
#
# def func():
#     print("I am running.........")
#     time.sleep(4)
#     print("I am done......")
#
#
#
# if __name__ == "__main__":
#     t = threading.Timer(6, func)
#     t.start()
#
#     i = 0
#     while True:
#         print("{0}***************".format(i))
#         time.sleep(3)
#         i += 1
#
#
# eg18
#
# import threading
# import time
#
# class MyThread(threading.Thread):
#     def run(self):
#         global num
#         time.sleep(1)
#
#         if mutex.acquire(1):
#             num = num+1
#             msg = self.name+' set num to '+str(num)
#             print(msg)
#             mutex.acquire()
#             mutex.release()
#             mutex.release()
#
# num = 0
#
# mutex = threading.RLock()
#
#
# def testTh():
#     for i in range(5):
#         t = MyThread()
#         t.start()
#
#
#
# if __name__ == '__main__':
#     testTh()
#
#
# eg19
# import multiprocessing
# from time import sleep, ctime
#
#
# def clock(interval):
#     while True:
#         print("The time is %s" % ctime())
#         sleep(interval)
#
#
#
# if __name__ == '__main__':
#     p = multiprocessing.Process(target = clock, args = (5,))
#     p.start()
#
#     while True:
#         print('sleeping.......')
#         sleep(1)
#
#
#
# eg20
# import multiprocessing
# from time import sleep, ctime
#
#
# class ClockProcess(multiprocessing.Process):
#     '''
#     两个函数比较重要
#     1. init构造函数
#     2. run
#     '''
#
#     def __init__(self, interval):
#         super().__init__()
#         self.interval = interval
#
#     def run(self):
#         while True:
#             print("The time is %s" % ctime())
#             sleep(self.interval)
#
#
# if __name__ == '__main__':
#     p = ClockProcess(3)
#     p.start()
#
#     while True:
#         print('sleeping.......')
#         sleep(1)
#
#
#
# eg21
# from multiprocessing import Process
# import os
#
#
# def info(title):
#     print(title)
#     print('module name:', __name__)
#     # 得到父亲进程的id
#     print('parent process:', os.getppid())
#     # 得到本身进程的id
#     print('process id:', os.getpid())
#
#
# def f(name):
#     info('function f')
#     print('hello', name)
#
#
# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()
#
#
# eg22
# import multiprocessing
# from time import ctime
#
#
# def consumer(input_q):
#     print("Into consumer:", ctime())
#     while True:
#         # 处理项
#         item = input_q.get()
#         print ("pull", item, "out of q") # 此处替换为有用的工作
#         input_q.task_done() # 发出信号通知任务完成
#     print ("Out of consumer:", ctime()) ##此句未执行，因为q.join()收集到四个task_done()信号后，主进程启动，未等到print此句完成，程序就结束了
#
#
# def producer(sequence, output_q):
#     print ("Into procuder:", ctime())
#     for item in sequence:
#         output_q.put(item)
#         print ("put", item, "into q")
#     print ("Out of procuder:", ctime())
#
#
#
# # 建立进程
# if __name__ == '__main__':
#     q = multiprocessing.JoinableQueue()
#     # 运行消费者进程
#     cons_p = multiprocessing.Process (target = consumer, args = (q,))
#     cons_p.daemon = True
#     cons_p.start()
#
#     # 生产多个项，sequence代表要发送给消费者的项序列
#     # 在实践中，这可能是生成器的输出或通过一些其他方式生产出来
#     sequence = [1,2,3,4]
#     producer(sequence, q)
#     # 等待所有项被处理
#     q.join()
#
# eg23
# import multiprocessing
# from time import ctime
#
# # 设置哨兵问题
# def consumer(input_q):
#     print("Into consumer:", ctime())
#     while True:
#         item = input_q.get()
#         if item is None:
#             break
#         print("pull", item, "out of q")
#     print ("Out of consumer:", ctime()) ## 此句执行完成，再转入主进程
#
#
# def producer(sequence, output_q):
#     print ("Into procuder:", ctime())
#     for item in sequence:
#         output_q.put(item)
#         print ("put", item, "into q")
#     print ("Out of procuder:", ctime())
#
# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#     cons_p = multiprocessing.Process(target = consumer, args = (q,))
#     cons_p.start()
#
#     sequence = [1,2,3,4]
#     producer(sequence, q)
#
#     q.put(None)
#     cons_p.join()
#
#
# eg24
#
# import multiprocessing
# from time import ctime
#
# def consumer(input_q):
#     print ("Into consumer:", ctime())
#     while True:
#         item = input_q.get()
#         if item is None:
#             break
#         print("pull", item, "out of q")
#     print ("Out of consumer:", ctime())
#
# def producer(sequence, output_q):
#     for item in sequence:
#         print ("Into procuder:", ctime())
#         output_q.put(item)
#         print ("Out of procuder:", ctime())
#
# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#     cons_p1 = multiprocessing.Process (target = consumer, args = (q,))
#     cons_p1.start()
#
#     cons_p2 = multiprocessing.Process (target = consumer, args = (q,))
#     cons_p2.start()
#
#     sequence = [1,2,3,4]
#     producer(sequence, q)
#
#     q.put(None)
#     q.put(None)
#
#     cons_p1.join()
#     cons_p2.join()














