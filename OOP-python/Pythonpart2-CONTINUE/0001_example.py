#Ex-18
import os
try:
    print(10/0)
except Exception as e:
    print(e)
    try:
        print(23+'surendra')
    except Exception as e:
        print(e)
        os._exit(0) #PVM stop forcefully so 
    print('2')
else:
    print('I am else block')
finally:
    print('end')