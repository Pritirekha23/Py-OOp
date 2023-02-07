n=int(input("Enter a number::"))
for i in range(n):
    for j in range(n):
        if j>i or i==j:
               print("*",end=" ")
        else:
          
          print(" ",end=" ")
    print()