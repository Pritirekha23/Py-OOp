from threading import *
import time
print('example-4')
def fun1():
    time.sleep(3)
    print('Hi fun1')
    

def fun2():
    time.sleep(3)
    print('Hello fun2')
    
    
t1=Thread(target=fun1)
t2=Thread(target=fun2)
t1.start()
t2.start()
list=enumerate()
for i in list:
    print(i.name)
    print(i.ident)