from threading import*
import time


print('example----2')
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


print('example--3')

def f1():
    for i in range(3):
        time.sleep(3)
        print('Hi i am priti')
        
t1=Thread(target=f1)
t1.start()

t1.join(5)  #main thread will wair 5 sec 
for i in range(3):
    print('How are you?')
    
    
    '''
    op:
Hi i am priti
How are you?
How are you?
How are you?
Hi i am priti
Hi i am priti  '''



print('example--4')

def f1():
    for i in range(3):
        time.sleep(3) #t1 thread will wait 3 sec
        print('Hi i am priti')
        
t1=Thread(target=f1)
t1.start()

t1.join(5)  #main thread will wait 5 sec 
for i in range(3):
    time.sleep(2)  #main thread  will wait 2 sec
    print('How are you?')
    
    
#     op:
# Hi i am priti
# Hi i am priti
# Hi i am priti
# Hi i am priti
# How are you?
# How are you?
# Hi i am priti
# How are you?