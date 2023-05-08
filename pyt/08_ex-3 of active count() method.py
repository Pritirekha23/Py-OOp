#ex-3
from threading import*
import time
print('Example-3')
def fun1():
    time.sleep(5)
    print('I am fun1')

def fun2():
    time.sleep(5)
    print('I am fun2')
    
t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()
time.sleep(3)
print('number of active threads:',active_count())


# output:
# number of active threads: 3
# I am fun1
# I am fun2