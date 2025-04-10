try:
    n=int(input("ENTER NUMBER:"))
    fac=1

    for i in range(1,n+1):
        print(fac)

except ValueError as a:
    print(e)   

else:
    print("try ececuted!!")

finally:
    print("FINALLY EXECUTED!!")

try:
    l=[56,64,42,21]
    n=int(input("ENTER INDEX NUMBER"))
    print("Value is:",l[n])

except ValueError as e:
    print(e)

except IndexError as e:
    print(e)

try:
    n1=int(input("ENTER NUMBER 1:"))
    n2=int(input("ENTER NUMBER 2:"))
    print("Division:",n1/n2)

 
except ValueError as e:
    print(e)

except ZeroDivisionError as e:
    print(e)

try:
    l=[56,64,42,21]
    n=int(input("ENTER INDEX NUMBER:"))
    print("Value is:",l[n])

except:
    print("Invalid input!!")





                



           


