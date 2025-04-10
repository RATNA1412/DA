#(20) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
n19=input("enter a 1st string:")
n20=input("enter a 2nd string:")

p= n20[:2] + n19[2:]
q= n19[:2] + n20[2:]
n21= p + " "+ q
n21
