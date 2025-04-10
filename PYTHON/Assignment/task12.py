#(12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
n7 = int(input("enter a first number:"))
n8 = int(input("enter a second number:"))
n9 = int(input("enter a third number:"))

if n7==n8 or n8==n9 or n9==n7:
    print("sum is zero")
else:
    print("the sum of the numbers is :",n7+n8+n9)