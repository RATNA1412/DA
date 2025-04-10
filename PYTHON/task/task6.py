n=int(input("enter number : "))

#5-> 1 2 3 4 5
i=1
fac=1

while(i<=n):
    fac*=i
    #1*1=1  1*2=2 

    i=i+1

print("factorial number is:",fac)


n=int(input("enter number : "))

for i in range(1,n+1,1):
    print(i)





"""
*
**
***
****
*****
"""

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")

        print()

for i in range(1,6):
    print("*"*i) 



         
