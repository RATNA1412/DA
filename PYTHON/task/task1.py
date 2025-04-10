print("hello ,end=") #show the statement in terminal
print("welcome")

a=10
b=20

print("A:",a)
print("B:,b")
print("addition:",a+b)
print("sub:",a-b)
print("mul:",a*b)
print("div:",a/b)



a=int(input("enter year:"))
print("year are:",a/12)


a=int(input("enter number 1:"))
b=int(input("enter number1:"))

print("before swapping A;",a)
print("before swapping B:",b)


#a=50,b=40

temp=a #temp=50 a=blank
a=b #a=40 b=blank
b=temp #b=50 temp=blank


a= a+b #50+40=90=a
b= a-b #90-40=b
a= a-b #90-50=40

a,b = b,a

print("after swapping a:",a)
print("afterswapping b:",b)
