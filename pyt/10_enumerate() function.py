#enumerate():
#   It will return a list of all active thread object.

from threading import*
import time

#ex-1
print(enumerate())

# op:[<_MainThread(MainThread, started 2672)>]

#ex-2
# print('ex----2')
# def fun1():
#     time.sleep(3)
#     print('Hi fun1')
# t1=Thread(target=fun1)
# t1.start()
# print(enumerate())

# op:[<_MainThread(MainThread, started 8372)>, <Thread(Thread-1 (fun1), started 6608)>]
# Hi fun1


# print('ex----3')

# def fun1():
#     time.sleep(3)
#     print('Hi fun1')
    

# def fun2():
#     time.sleep(3)
#     print('Hello fun2')
    
    
# t1=Thread(target=fun1)
# t1.start()
  
# t2=Thread(target=fun2)
# t2.start()
# print(enumerate())


# op:[<_MainThread(MainThread, started 7560)>, <Thread(Thread-1 (fun1), started 15408)>, <Thread(Thread-2 (fun2), started 1612)>]
# Hello fun2
# Hi fun1


# print('example-4')
# def fun1():
#     time.sleep(3)
#     print('Hi fun1')
    

# def fun2():
#     time.sleep(3)
#     print('Hello fun2')
    
    
# t1=Thread(target=fun1)
# t1.start()
  
# t2=Thread(target=fun2)
# t2.start()
# list=enumerate()
# for i in list:
#     print(i.name)
#     print(i.ident)
    
# op:
# MainThread
# 11040
# Thread-1 (fun1)
# 6308
# Thread-2 (fun2)
# 3944
# Hi fun1
# Hello fun2

print('example-6')
def fun1():
    time.sleep(3)
    print('Hi fun1')
    

def fun2():
    time.sleep(3)
    print('Hello fun2')
    
    
t1=Thread(target=fun1)
t1.start()
  
t2=Thread(target=fun2)
t2.start()
print(enumerate())
time.sleep(5)
print('---------')
print(enumerate())


# op:
#     [<_MainThread(MainThread, started 8024)>, <Thread(Thread-1 (fun1), started 10004)>, <Thread(Thread-2 (fun2), started 16192)>]
# Hello fun2
# Hi fun1
# ---------
# [<_MainThread(MainThread, started 8024)>]