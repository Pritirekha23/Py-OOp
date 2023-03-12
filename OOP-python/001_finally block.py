import os
try:
    print(1)
    print(2)
    os._exit(0)
    print(3)
    
except Exception as e:
    print(e)
finally:
    print('Finally block executed')
    