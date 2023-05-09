from threading import*
import time

def fun1():
    for i in range(3):
        print('fun1')
        
def fun2():
    t1.join() #this thread will execute after completion of t1 thread
    for i in range(3):
        print('fun2')
        
def fun3():
    for i in range(3):
        print('fun3')
        
t1=Thread(target=fun1)
t2=Thread(target=fun2)
t3=Thread(target=fun3)

t1.start()
t2.start()
t3.start()


'''
op:
fun1
fun1
fun1
fun2
fun2
fun3
fun2
fun3
fun3  '''