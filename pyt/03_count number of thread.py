#ex-4 count number of thread
from threading import *
def fun1():
    for i in range(5):
        print('priti')
def fun2():
    for i in range(5):
        print('smruti')
# create thread
t1=Thread(target=fun1)
print('line 11:',active_count())
t1.start()
print('line 13:',active_count())
t2=Thread(target=fun2)
print('line 15:',active_count())
t2.start()
print('line 17:',active_count())