#ex-3(thread informations)
from threading import *
print('line-2:', current_thread().name)
def fun1():
    print('line-5:', current_thread().name)
    for i in range(5):
        print('priti')
 
      
def fun2():
    print('line-11:', current_thread().name)
    for i in range(5):
        print('smruti')
        
# create thread
t1=Thread(target=fun1)
print('line-17:', current_thread().name)
t1.start()
print('line-19:', current_thread().name)

t2=Thread(target=fun2)
print('line-22:', current_thread().name)
t2.start()
print('line-24:', current_thread().name)