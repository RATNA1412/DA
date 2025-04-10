#(9) Write python program that swap two number with temp variable and without temp variable.
#with temp
n3 = int(input("enter a number a:"))
n4 = int(input("enter a number b:"))

temp = n3 
n3=n4
n4= temp
print("number after swapping are:" "a = ",n3 ,"b=",n4)
#with out temp
print("number before swapping are :" "a = ",n3 ,"b=",n4)
n3,n4= n4,n3
print("number after swapping are :" "a = ",n3 ,"b=",n4)