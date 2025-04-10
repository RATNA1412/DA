# print("hello  world")
# print("hello world,end=")



# a=10
# b=20

# print("A:",a)
# print("B:,b")
# print("addition:",a+b)
# print("sub:",a-b)
# print("mul:",a*b)
# print("div:",a/b)





# a=30
# b=60

# print("add",a+b)
# print("sub",a-b)
# print("multi",a*b)
# print("div",a/b)


# a=int(input("enter year:"))
# b=int(input("enter month:"))


# a=int(input("ENTER THE NUMBER:"))
# if a>50:
#     print("THE NUMBER IS POSITIVE!!")
# elif a==50:
#     print("THE NUMBER IS ZERO!!")
# else:
#     print("THE NUMBER IS NEGATIVE!!")  




# a=int(input("ENTER YOUR AGE:"))
# if a>18:
#     print("YOU CAN VOTE!!")
# else:
#     print("YOU ARE MINOR!!")    


# a=int(input("ENTER NUMBER:"))
# if a%2:
#     print("NUMBER IS EVEN!!")
# else:
#     print("NUMBER IS ODD!!")   
# 


# n = 1
# while(n<=10):
#     print(n)
#     n=n+1

# n = 10
# while(n>=1):
#     print(n)
#     n=n-1

# n= int(input("Enter number : "))
# i = 1
# fac = 1
 
# while(i<=n):
#     fac+=i#fac=fac+i
#     i = i+1
# print("fac number is : ",fac)



# for i in range(1,6):
#     print("*"*i)

# for i in range(1,6):
#     print(" "*(6-i)," *"*i)





# n = int(input("enter number : "))
# prime = 0

# for i in range(1,n+1):
#     if n%i==0:
#         prime = prime+1

# if prime==2:
#     print("is prime")

# else:
#     print("is not prime")



# n = int(input("Enter number : "))

# n1 = 0
# n2 = 1
 
# print(n1)
# print(n2)

# for i in range (3,n+1):
#     n3=n1+n2
#     print(n3)
#     n1=n2
#     n2=n3



class A:
    def fun1(self):
        print("this is class A")

        

class B:
    def fun2(self):
        print("this is class B")   

class C(A,B):
    def fun3(self):
        print("this is class C")

obj=C()
obj.fun3()
obj.fun2()
obj.fun1()        
               