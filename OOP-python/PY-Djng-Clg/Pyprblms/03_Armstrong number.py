
n=int(input("Enter a numbers::"))
sum=0
ord=len(str(n))

temp=n
while temp>0:
    r=temp%10
    sum+=r**ord
    temp//=10
if n==sum:
    print(f'{n} is an armstrong number')
else:
    print(f'{n} is not an armstrong number')
