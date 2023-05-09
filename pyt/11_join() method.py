''' join():
    In multithreading, multiple thread can execute simultaneously but there are some situations where a thread wants to wait until completion of another thread execution then we should go for join() method. '''

from threading import*
import time 
'''
#ex-1
def fun1():
    for i in range(3):
        print('fun1')

t1=Thread(target=fun1)
t1.start()

for i in range(3):
    print('Jimin')
    
    
  op:
fun1
Jimin
fun1
Jimin
fun1
Jimin  '''


#apply join
# 
'''
def fun1():
    for i in range(3):
        print('fun1')
        

t1=Thread(target=fun1)
t1.start()
t1.join()   #mainThread will execute thus line and here mainthread will execute after fully execution of t1 thread.
for i in range(3):
    print('Jimin')
    
op:
fun1
fun1
fun1
Jimin
Jimin
Jimin '''