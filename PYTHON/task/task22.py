import random

original=random.randint(1001,9999)
d={}
while True:
    menu="""
    prass 1 for Signup
    prass 2  for Login
    prass 3 for Forget-password
    press 4 for Exit
 """
    print(menu)

    choice=int(input("Enter Choice:"))

    if choice==1:
        print("*"*50,"Welcome to Signup Page!!","*"*50)
        name = input("Enter Name:")
        email= input("Enter Email:")
        mobile= int(input("Enter Mobile Number:"))
        password= int(input("Enter Password:"))
        cpassword= int(input("Enter Confirm Password:"))

        if password==cpassword:
            print("Signup Sucessfully!!")

            d['name']=name
            d['email']=email
            d['mobile']=mobile
            d['password']=password 

        else:
            print("Password & confirm password does not match!!")

    elif choice==2:
        print("*"*50,"Welcome to Login Page!!","*"*50)
        email=input("Enter Email:")
        password=int(input("Enter Password:"))  

        
        if email==d['email']:
            if password==d['password']:
                print("Login Successfully!!")
                break
            else:
                print("Password does not match!!")

        else:
            print("Email does not match!!")

    elif choice==3:
        mobile=int(input("Enter Mobile number:"))

        if d['mobile']==mobile:
            print("Your Otp is:" ,original) 

            otp = int(input("Enter New Number"))

            if otp==original:
                password=int(input("Enter New Number:"))

                d['password']=password

            else:
                print("Invalid otp!!")

        else:
            print("Invalid mobile number!!")

    elif choice==4:
        print("Thank You!!")
        break

    else:
        print("Invalid choice!!")
        break               


                     
