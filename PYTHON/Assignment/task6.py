#(6) Write a Python program to get the Fibonacci series of given range. 
n1 = int(input("enter a number:"))
p,q = 0,1
for i in range(n1):
    print(p, end=" ")
    p,q = q,p+q