#(13) Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 
n10 = int(input("enter a first number:"))
n11 = int(input("enter a second number:"))
if n10==n11 or n10+n11==5 or n10-n11==5:
    print("true")
else:
   print("false")