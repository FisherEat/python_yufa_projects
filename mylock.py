# Threading example

import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(2)

def move(func):
    for i in range(5):
        print ("I was at the %s! %s" %(func, ctime()))

def move(func):
    for i in range(2):
        print ("I was at the %s ! %s" %(func, ctime()))
        sleep(4)
threads = []

t1 = threading.Thread(target=music, args=(u'aiqingmaima'))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print ("all over %s" %ctime())