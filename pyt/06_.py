#ex-2

from threading import*
import time
def fun1():
    time.sleep(3)
    print('Jimin')
    
def fun2():
    print('Jin')
    
t1=Thread(target=fun1)
t2=Thread(target=fun2)
print('Before starting t1 thread :',t1.is_alive())
print('Before starting t2 thread :',t2.is_alive())
t1.start()
t2.start()
print('After starting t1 thread :',t1.is_alive())
print('After starting t2 thread :',t2.is_alive())