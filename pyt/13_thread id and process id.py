from threading import*
import os

#Ex-1
''' process id :
program is in execution is called process,whenever we will execute a python program then OS will create a process that have some unique number this number is called as process id. By using getpid() we can get process id , which is available inside os module'''

def fun1():
    print('Hi fun1')
fun1()
print(os.getpid()) 

# op:
# Hi fun1
# 13972

''' thread id: 
Every thread have some unique id number,this id number is called thread id.Thread wont get id number at the time of thread object cretion , once a thread started then only it will get id number. We can change thread name,but we cant change thread id number.
By using ident variable, we can get thread id'''
  
def f1():
    print('Jin')

def f2():
    print('Tae')
    
t1=Thread(target=f1)
print('t1 thread id before starting the thread ::',t1.ident)
t1.start()  #after starting the thread ,the thread get its id.
print('t1 thread id after starting the thread ::',t1.ident)

t2=Thread(target=f2)
print('t2 thread id before starting the thread ::',t2.ident)
t2.start()
print('t2 thread id after starting the thread ::',t2.ident)

'''
op:
t1 thread id before starting the thread :: None
Jin
t1 thread id after starting the thread :: 3628
t2 thread id before starting the thread :: None
Tae
t2 thread id after starting the thread :: 4392  '''