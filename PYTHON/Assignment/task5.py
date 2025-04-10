#(5) Write a Python program to get the Factorial number of given numbers. 
n= int(input("enter a number:"))
if n<0 :
    print("write a positive number")
else:
    factorial = 1
    for  i in range (1,n+1):
        factorial*= i
    print("factorial of  given number is :",factorial)