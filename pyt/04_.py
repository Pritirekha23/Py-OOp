from threading import*
def fun1():
    for i in range(5):
        print('priti')
def fun2():
    print('line-6',current_thread().name)
    for i in range(5):
        print('Arun') 
        
t1=Thread(target=fun1)
t1.start()
print('line-12',current_thread().name)

print(t1.name)
t2=Thread(target=fun2)
t2.start()

print('line-18',current_thread().name)