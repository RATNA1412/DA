def fun3():
    n=int(input("enter number:"))
    fac = 1

    for i in range(1,n+1):
        fac*=i
    return fac
    
print("factorial number is:",fun3())    
          
    
