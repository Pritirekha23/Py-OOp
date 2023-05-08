from threading import*
import time

# It is used to count the number of active threads.
# Active thread mean the thread which is in active mode not dead.
#ex-1
def fun1():
    print('I am fun1')

def fun2():
    print('I am fun2')
    
t1=Thread(target=fun1)
t2=Thread(target=fun2)
print('number of active threads:',active_count())
t1.start()
t2.start()

# output-
# number of active threads: 1
# I am fun1
# I am fun2

#ex-2
print('Example-2')
def fun1():
    time.sleep(5)
    print('I am fun1')

def fun2():
    print('I am fun2')
    
t1=Thread(target=fun1)
t2=Thread(target=fun2)

t1.start()
t2.start()
time.sleep(3)
print('number of active threads:',active_count())

# output:
# I am fun2
# number of active threads: 2
# I am fun1

