# import math
# def check(num):
#     c_digit=len(str(num))
    
#     sum=0
#     flg=num
#     while(flg!=0):
#         r=flg%10
        
#         sum=(int) (sum + math.pow(r,c_digit))
#         c_digit=c_digit-1
#         flg=flg//10
#     # if sum==num:
#     #     return 1
#     # else:
#     #     return 0
        
        

      
# num=int(input("Enter a number::"))
# if(check(num)==1):
#      print('The number is a Disarium number')
# else:
#       print('The number is not a Disarium number')


#calculateLength() will count the digits present in a number    
def calculateLength(n):    
    length = 0;    
    while(n != 0):    
        length = length + 1;    
        n = n//10;    
    return length;    
     
num = 89;    
rem = sum = 0;    
len = calculateLength(num);    
     
#Makes a copy of the original number num    
n = num;    
     
#Calculates the sum of digits powered with their respective position    
while(num > 0):    
    rem = num%10;    
    sum = sum + int(rem**len);    
    num = num//10;    
    len = len - 1;    
     
#Checks whether the sum is equal to the number itself    
if(sum == n):    
    print(str(n) + " is a disarium number");    
else:    
    print(str(n) + " is not a disarium number");    