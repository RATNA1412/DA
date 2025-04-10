print("press 1 for manager")
print("press 2 for customer")

choice =int(input("enter choice : "))

ch1 =int(input("enter choice :"))

if ch1==1:
    print("welcome to manager department!!")

    choice1 =int(input("press 1 for add product)"))
    if choice1==1:
        name = input("enter product name : ")
        price = int(input("enter price : "))
        qty = int(input("enter qty :"))

        print("product added successfully!!")

        choice3 = int(input("press 3 for purchase product"))

        if  choice3==3:
            qty1 = int(input("enter quantity :"))

            if qty1<qty:
                print("price for product is : ",price)

                print("total bill is : ",price*qty1)

            else:
                print("out of stock!!")

        else:
            print("invalid choice!!")

    else:
        print("invalid choice!!")

else:
    print("invalid choice")



            


                
    

    


