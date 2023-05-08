import time
from threading import*
def fun1():
    print('Jin')
    time.sleep(3)
    print('Jimin')
    
t1=Thread(target=fun1)
print('Before starting t1 thread :',t1.is_alive())
t1.start()
print('After starting t1 thread :',t1.is_alive())