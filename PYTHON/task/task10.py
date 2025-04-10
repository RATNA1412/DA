def fun1(n):

    usersum=0
    while(n!=0):
        digit = n%10
        usersum = usersum*10+digit
        n //=10

    print("RESERVE NUMBER IS :",usersum)

n= int(input("ENTER NUMBER :"))
fun1(n)     










    






9724