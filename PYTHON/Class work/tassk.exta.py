class A:
    def fun1(self):
        print("THIS IS FUNCTION 1!!")
class B:
    def fun2(self):
        print("THIS IS FUNCTION 2!!")

class C(A,B):
    def fun3(self):
        print("THIS IS FUNCTION 3!!")

obj = C()
obj.fun1()
obj.fun2()
obj.fun3()                
            






            

class A:
    def fun1(self):
        print("CLASS A")
class B(A):
    def fun2(self):
        print("CLASS B")

class C:
    def fun3(self):
        print("CLASS C")

class D(B,C): 
    def fun4(self):
        print("CLASS D")   

obj = D()
obj.fun1()
obj.fun2()
obj.fun3()
obj.fun4()        