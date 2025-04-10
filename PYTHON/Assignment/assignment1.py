# (1) What are the types of Applications?
# '''
# cloud application, desktop application,mobile application,web application,gaming application,database application, server application'''

#(2)What is programing? 
# ''' programing is a one type of term in which we can write a diffrent diffrent computer langugages code like pytjon , c ,c++,java to perform  
#     a task and make an application ,software and system in computer.'''
#(3) What is Python? 
# ''' python is a simple programming language which is  easy and have a wide range of framwork and libraries,which is find by guido van rossum in 1991 .
#     it is use for application  devlopment ,software devlopment ,artificial intelligence, robotics.
# '''
# (4) Write a Python program to check if a number is positive, negative or zero. 
#  a = int(input("enter a number"))
#  if a>0:
#      print("number is positive")
#  elif a==0:
#       print("number is zero")
#  else:
# 
#     print("number is negative")
# (5) Write a Python program to get the Factorial number of given numbers. 
#  n= int(input("enter a number"))
#  if n<0 :
#         print("write a positive number")
#  else:
#         factorial = 1
#         for  i in range (1,n+1):
#             factorial*= i
#         print("factorial of  given number is :",factorial)

# (6) Write a Python program to get the Fibonacci series of given range. 
#  n1 = int(input("enter a number:"))
#  p,q = 0,1
#  for i in range(n1):
#      print(p, end=" ")
#      p,q = q,p+q

# (7) How memory is managed in Python?
#  '''In Python memory allocation and deallocation method is automatic as the Python developers created a garbage collector for Python so that
#    the user does not have to do manual garbage collection.
   
#    Garbage Collection:
#                       Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for 
#                       other objects.
#    Reference Counting:
#                       Reference counting works by counting the number of times an object is referenced by other objects in the system. When 
#                       references to an object are removed, the reference count for an object is decremented. When the reference count becomes 
#                       zero, the object is deallocated.
# '''
# #(8) What is the purpose continuing statement in python?
# # '''Continue statement is a loop control statement that forces to execute the next iteration of the loop while skipping the rest of the code 
#    inside the loop for the current iteration only.
# '''
# for i in range(1,9):
#    if i == 6:
#     continue
#    print(i)
#(9) Write python program that swap two number with temp variable and without temp variable.
# ''' with temp'''
# n3 = int(input("enter a number a"))
# n4 = int(input("enter a number b"))

# temp = n3 
# n3=n4
# n4= temp
# print("number after swapping are:" "a = ",n3 ,"b=",n4)
# ''' with out temp'''
# print("number before swapping are :" "a = ",n3 ,"b=",n4)
# n3,n4= n4,n3
# print("number after swapping are :" "a = ",n3 ,"b=",n4)
#(10) Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 
# n5= int(input("enter a number:"))
# if n5 %2 == 0:
#     print("number is even")
# else:
#     print("number is odd")
#(11) Write a Python program to test whether a passed letter is a vowel or not. 
# n6 = input("enter a letter ")
# if n6 in 'AEIOUaeiou':
#     print("letter is vowel")
# else:
#     print("letter is not vowel")
#(12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.
# n7 = int(input("enter a first number:"))
# n8 = int(input("enter a second number:"))
# n9 = int(input("enter a third number:"))

# if n7==n8 or n8==n9 or n9==n7:
#     print("sum is zero")
# else:
#     print("the sum of the numbers is :",n7+n8+n9)
#(13) Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 
# n10 = int(input("enter a first number:"))
# n11 = int(input("enter a second number:"))
# if n10==n11 or n10+n11==5 or n10-n11==5:
#     print("true")
# else:
#     print("false")
#(14) Write a python program to sum of the first n positive integers. 
# n = int(input("enter a number:"))
# sum = 0
# for i in range(1,n+1):
#     sum += i
# print(sum)
    
#(15) Write a Python program to calculate the length of a string. 
# n12 = input("enter a string:")
# print("length of string is ",len(n12))
#(16) Write a Python program to count the number of characters (character frequency) in a string 
# n13 = input("enter a string:")

#(17) What are negative indexes and why are they used? 
# '''Negative indexes in the context of list basics refer to the ability to access elements in a list by specifying a negative number
#    as the index. This allows you to count backwards from the end of the list, providing an alternative way to reference the same 
#    elements.

#    for example:'''
# n14= "singh"
# print(n14[-3:-1])



#(18) Write a Python program to count occurrences of a substring in a string.
# n15=input("enter a string:")
# n16=input("enter a sub string:")
# count = n15.count(n16)
# print("the total occcurrenece of substring is :",count)
#(19 Write a Python program to count the occurrences of each word in a given sentence 
# '''(pending)'''
# n17=input("enter a sentances:")
# n18=input("enter a word:")
# count = n17.count(n18)
# print("the word occurrence in santances  is :",count)

#(20) Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
# n19=input("enter a 1st string:")
# n20=input("enter a 2nd string:")

# p= n20[:2] + n19[2:]
# q= n19[:2] + n20[2:]
# n21= p + " "+ q
# n21

#(21) Write a Python program to add 'in' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then
# add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. '''

# n21=input("enter a word :")
# if len(n21)<3:
#     result = n21
# elif n21.endswith("ing"):
#     result = n21+"ly"
# else:
#     result = n21+"ing"
# print(result)
    

#(22) Write a Python function to reverses a string if its length is a multiple of 4. 
# n22=input("enter a  string:")
# if len(n22) %4 == 0:
#     n22= n22[::-1]
# n22
#(23) Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return
# instead of the empty string. 
# n23=input("enter a string:")
# if len(n23)<2:
#     print("")
# else:
#     n24 = n23[:2]+n23[-2:]
# n24
#(24) Write a Python function to insert a string in the middle of a string.
# n25=input("enter a 1st string:")
# n26=input("enter a 2nd string:")

# n27 = len(n25)//2
# n28 = n25[:n27]+ " " + n26 +n25[n27:]
# n28
#(25) What is List? How will you reverse a list? 
# '''There are many built-in types in Python that allow us to group and store multiple items. Python lists are the most versatile among them.
#    A list is a collection of ordered, mutable elements '''
# l1= [1,2,3,4,5,6,7,8,9]
# l1.reverse()
# l1
#(26) How will you remove last object from a list?
# l1= [1,2,3,4,5,6,7,8,9]
# l1.pop()
# l1
#(27) Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]? 
# '''25'''
#(28) Differentiate between append () and extend () methods?
# ''' the key diffrence between two method is
#     append() Adds a single element to the end of the list.extend()Adds multiple elements from an iterable to the end of the list.
# 	append() Accepts a single element (any data type).extend()Accepts an iterable (e.g., list, tuple).'''
   #example
# l2 = [1,2,3,4,5,6]
# l2.append([7,8])
# l2
# l2.extend([7,8])
# l2
#(29) Write a Python function to get the largest number, smallest num and sum of all from a list. 
# l3=[5,6,7,11,9,11,13,20,28,30]
# large = max(l3)
# small = min(l3)
# sum = sum(l3)
# print("large number is :",large)
# print("small number is :",small)
# print("sum number is :",sum)
#(30)How will you compare two lists?
# l4=[1,2,3,4,5]
# l5=[6,7,8,9,10]
# if l4 == l5:
#     print("list are equal")
# else:
#     print("list are not equal")
#(31) Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a
#given list of strings.
# '''pending'''
# count= 0
# n29 = ['abc','vfe','gfgfd','asd']
# if len(n29)>=2 or n29[0]==n29[-1]:
#     count+=1
#     print(count)
 
#(32)Write a Python program to remove duplicates from a list.

# l4=[1,2,3,3,4,,5,6,6,7,8,9]
# l5=set(l4)
# print(l5)
#(33)Write a Python program to check a list is empty or not
# l6 = []
# if len(l6) == 0:
#     print("list is empty")
# else:
#     print("list is not empty")
#(34) Write a Python function that takes two lists and returns true if they have at least one common member. 
# l7 = [1,2,3,4]
# l8 = [4,5,6,7]


# for i in l7:
#     if i in l8:
#         n = "true"
#         break
#     else:
#         n= "false"
# print(n)

#(35) Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.
# l9=[i**2  for i in range (1,31)]
# print(l9[:5]+l9[-5:])
#(36) Write a Python function that takes a list and returns a new list with unique elements of the first list.
# l10 = [1,2,3,4,3,2,4,5,6,'a','b']
# l11 = set(l10)
# print(l11)
#(37)Write a Python program to convert a list of characters into a string. 
# l12 = ["a","m","a","n"]
# l13 = "".join(l12)
# print(l13)
#(38)Write a Python program to select an item randomly from a list. 
# import random
# l14= [1,2,3,4,5,"a","b"]
# print(random.choice(l14))

#(39)Write a Python program to find the second smallest number in a list. 
# l15 = [1,2,3,5,6,7]
# l15.remove(min(l15))
# l16= min(l15)
# print(l16)
#(40)Write a Python program to get unique values from a list 

# l17=[1,2,,3,5,5,6,"a","b","z"]
# l18 = set(l17)
# print("Unique List=", l18)
#(41)Write a Python program to check whether a list contains a sub list 

# l19 = [1,2,3,4,5,6,7]
# l20 = [9,7]

# for i in l20:
#     if i in l19:
#         print("sub list")
        
#     else:
#         print("not sub list")

#(42)Write a Python program to split a list into different variables. 
# l21 = [(1,2,3),(4,5,6)]
# l23,l22 = l21
# print(l22)
# print(l23)


#(43)What is tuple? Difference between list and tuple. 
#'''Tuples are used to store multiple items in a single variable.
   #Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary,
   #all with different qualities and usage.
   #A tuple is a collection which is ordered and unchangeable.

   #Diffrences:
   #Lists and Tuples in Python are two classes of Python Data Structures. The list structure is dynamic, and readily changed whereas 
   #the tuple structure is static and cannot be changed. This means that the tuple is generally faster than the list. Lists are denoted
   #by square brackets and tuples are denoted with parenthesis.
#(44)Write a Python program to create a tuple with different data types. 
#n32 = ( 7,"rs",4.5,[1,2,3,4],('a','b'))
#n32
#type(n32)
#(45)Write a Python program to unzip a list of tuples into individual lists. 
#n33 = ('1','a','c','7',(1,2))
#n34 = tuple(zip(*n33))
#n34
#(46)Write a Python program to convert a list of tuples into a dictionary. 
#n35 = [("a",1),("b",2),("c",3)]
#dic2 = dict(n35)
#print(dic2)
#(47)How will you create a dictionary using tuples in python? 
#dic = {1,2,("rs","pq")}
#print(dic)

#(48)Write a Python script to sort (ascending and descending) a dictionary by value. 
#dic1= {1,2,6,4,8,3,5}
#set(dic)
#(49)Write a Python script to concatenate following dictionaries to create a new one. 
#dic3 = {'a':1,'b':2}
#dic4 = {'g':3,'h':4}
#dic5 = {'m':5,'n':6}

#dic6 = dic3.copy()
#dic6.update(dic4)
#dic6.update(dic5)

#print(dic6)

#(50)Write a Python script to check if a given key already exists in a dictionary. 
#dic7 = { 'ram':1,'shyam':2,'gita':3}
#key = input("enter a key:")
#if key in dic7:
    #print("key is in dictionary")
#else:
    #print("key is  not in dictionary")
#(51)How Do You Traverse Through a Dictionary Object in Python? 
#dic8 = {'animal':'lion','id':1,'rs':3}
#n38=dic8.keys()
# n39=dic8.values()
# n40=dic8.items()
# print(n38)
# print(n39)
# print(n40)
#(52)How Do You Check the Presence of a Key in A Dictionary? 
# dic8 = { 'ayushi':1,'shradha':2,'preeti':3}
# key = input("enter a key:")
# if key in dic8:
#     print("key is in dictionary")
# else:
#     print("key is  not in dictionary")
# #(53)Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 
# dict1 = {}

# for key in range(1,16):
#     dict1[key] = '*'
# print(dict1)

#(54)Write a Python program to check multiple keys exists in a dictionary
# dic8 = { 'ram':1,'shyam':2,'gita':3}
# key = ['ram','shyam','gita']
# if all(i in dic8 for i in key):
#     print(" all key are in dictionary")
# else:
#     pint(" all key  are not in dictionary")
#(55)Write a Python script to merge two Python dictionaries 
# def merge(dic9,dic10):
#     return(dic9.update(dic10))
# dic9 = {1,2,3,4,5}
# dic10={'a','b','c'}
# merge(dic9,dic10)
#print(dic9)
#(56)Write a Python program to map two lists into a dictionary 
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}). 
# key = ['a','b','c']
# value = [1,2,3]
# dic11 = {}
# for  i in range(len(key)):
#     dic11[key[i]] = value[i]
# dic11
# #(57)Write a Python program to find the highest 3 values in a dictionary 
# dic12= {300,500,600,700,800,900}
# lst = list(dic12)
# lst.sort()
# print("the highest three value is:",lst[3:])
#(58)Write a Python program to combine values in python list of dictionaries.
#Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]
#Expected Output: Counter ({'item1': 1150, 'item2': 300})
# ndp = [
#     {'item': 'item1', 'amount': 400},
#     {'item': 'item2', 'amount': 300},
#     {'item': 'item1', 'amount': 750}]
# dictnn={}
# for i in ndp:
#     items = i["item"]
#     amount = i["amount"]
#     if items in dictnn:
#         dictnn[items] += amount
#     else:
#         dictnn[items] = amount
# print(dictnn)
#(59)Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string. 

# str = input("enter a string")
# char_count = {}
# for  i in str:
#     if  i in char_count:
#         char_count[i] += 1
#     else:
#         char_count[i] = 1
# print(char_count)
#(60)Sample string:
# 'w3resource' Expected output: • {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
# str2 = "w3resource"
# char_count2 = {}
# for  j in str2:
#     if  j in char_count2:
#         char_count2[j] += 1
#     else:
#         char_count2[j] = 1
# print(char_count2)
# print
#(61)Write a Python function to calculate the factorial of a number (anonnegative integer) 
# import math
# n41 = int(input("enter a number:"))
# n42 = math.factorial(n41)
# print(n42)
#(62)Write a Python function to check whether a number is in a given range 
# def r1(start,n43,end,):
#     return start <= n43 <= end
# start=int(input("enter start a number"))
# end = int(input("enter end number"))
# n43 = int(input("enter a number"))
# print(r1(start,n43,end))
#(63)Write a Python function to check whether a number is perfect or not. 
# def is_perfect(number):
#     if number <= 0:
#         return False 
    
#     divisors_sum = 0
#     for i in range(1, number):
#         if number % i == 0:
#             divisors_sum += i
    
#     return divisors_sum == number
# print(is_perfect(6))   
# print(is_perfect(28))  
# print(is_perfect(12))  
#(64)Write a Python function that checks whether a passed string is palindrome or not 
# def pal(n):
#     return n == n[::-1]
# n44 = input("enter a string:")
# if pal(n44):
#     print("it is palindrome:")
# else:
#     print("it is bot palindrome")
#(65)How Many Basic Types of Functions Are Available in Python? 
# """
# There are many functions  available in python.
# a)user defind functions : functions we create.
# b)Recursive functions : Functions that call themselsves.
# c) lambada function : small, anonymous functions. 
# """
#(66)How can you pick a random item from a list or tuple?
# import random
# lstx = [1,2,3,4,5]
# print(random.choice(lstx))

#(67)How can you pick a random item from a range?
# import random 
# print(random.randrange(1,10))
#(68)How can you get a random number in python?
#import random
# random.seed()
# print(random.random())
#(69)How will you set the starting value in generating random numbers?
# nn = int(input("Enter the strating number :"))
#import random
# ny = random.randrange(nn,50)
# print(nm)
#(70) How will you randomize the items of a list in place?
# import random 
# list20 = [2,4,6,8,5]
# print("old",list20)
# random.shuffle(list20)
# print(list20)
#(71)What is File function in python? What are keywords to create and write file. 
# """
# In python file function is part of a web application.
# there are several keywords to create and write a file . To create a file keyword is 'x' and for write file is 'w'.
# """
#(72)Write a Python program to read an entire text file.
# aa = open("example.txt")
# print(aa.read())
#(73)Write a Python program to append text to a file and display the text.

# aa = open("example.txt", "a")
# aa.write("txt")
# aa.close()
# aa = open("example.txt", "r")
# print(aa.read())
#(74)Write a Python program to read first n lines of a file. 
# ab = open("example.txt","r")
# print(ab.readline())
#(75)Write a Python program to read last n lines of a file.
# ac = open("example.txt","a")
# ac.write("\n hello my name is ratna singh")
# ac.close()
# ac = open("example.txt","r")
# p = list(ac.readlines())
# print(p[-1])

#(76)Write a Python program to read a file line by line and store it into a list 
# ad = open("example.txt","r")
# q = list(ad.readlines())
# print(q)


#(77)Write a Python program to read a file line by line store it into a variable. 
# ad = open("example.txt","r")
# q = str(ad.readlines())
# print(q)
#(78)Write a python program to find the longest words. 
# ae = open("example.txt","r")
# x = ae.read()
# y=x.split()
# y
# max_word=max(y,key=len)
# print(max_word)
#(79)Write a Python program to count the number of lines in a text file. 
# af= open("example.txt","r")
# a = len(af.readlines())
# a
#(80)Write a Python program to count the frequency of words in a file. 
# def fun(ag):
#     char_count = {}

#     for char in ag:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
        
#     return char_count

# print(countt(y))
# y
#(81)Write a Python program to write a list to a file. 
# lst = ['a','b','c','rs']
# ah= open("example1.txt","w")
# for i in lst:
#     ah.write(i)
# ah.close()
# ai= open("example1.txt","r")
# print(ai.read())



#(82)Write a Python program to copy the contents of a file to another file
# aj= open("example1.txt","a")
# ak = open("example.txt","r")
# x = aj.write(ak.read())

#(83)Explain Exception handling? What is an Error in Python? 
# """ In Python, when an error occurs, Python will generate an error message , exceptions are assigned by try statement.  
# In Python, Errors are problems in a program that causes the program to stop its execution."""
#(84)How many except statements can a try-except block have? Name Some built-in exception classes:
# """
# A try-except block can have multiple except statements. 
# You can use different except clauses to handle various exceptions, or combine them in one except statement using a tuple.

# Python has many built-in exception classes, including:

# Exception – The base class for all exceptions.
# ValueError – Raised when a function gets a valid type but an incorrect value.
# IndexError – Raised when an invalid index is used in a list or tuple.
# KeyError – Raised when a dictionary key doesn't exist.
# TypeError – Raised when an operation is applied to an incorrect type.
# FileNotFoundError – Raised when a file cannot be found.
# AttributeError – Raised when an attribute reference fails.
# IOError – Raised for input/output issues (e.g., file reading errors).
# ImportError – Raised when an import fails.
# MemoryError – Raised when there is not enough memory to continue."""
#(85)When will the else part of try-except-else be executed?
# """
# when the code inside the try block will run without giving any errors than Else part of the code will executed (run). If an exception occurs in
# try block than except bolck will be executed without touching the else part.
# """
#(86)Can one block of except statements handle multiple exception?
# """
# Yes, one block of except statements can handle multiple exception in a tuple .
# """
#(87)When is the finally block executed? 
# """
# In Python language, the finally block is always executed, whether or not an exception is raised. 
# It runs after the except and try blocks which is commonly used for cleanup tasks.
# """
#(88)What happens when "1"== 1 is executed?
# """
# It will returns output as False.
#  1 assigns as a integar value and "1" will assigned as  a string.
#  """
# print("1" == 1) 
#(89)How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets. 
# """
#  The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.
# """
# try:
#     print(x1)
# except:
#     print("hello world")
# finally:
#     print("hey everyone")
#(90)Write python program that user to enter only odd numbers, else will raise an exception. 
# try:
#     rs = int(input("Enter odd number: "))
#     if rs % 2 == 0:
#         raise (ValueError("Error: The number is not odd number!"))
#     print(f"odd number: {rs}")
# except ValueError:
#     print(ValueError)
