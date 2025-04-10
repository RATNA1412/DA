import random

original=random.randint(1,50)
print("*"*10,"WELCOME TO THE GUESS THE NUMBER","*"*10)

while True:
    choice=int(input("ENTER THE NUMBER:"))

    if choice>50:
        print("INVALID CHOICE!!")
        break
    elif choice==original:
        print("YOU WIN")
        break
    elif choice>original:
        print("GREATER THAN ORIGINAL NUMBER!!")
        break
    else:
        print("LESS THAN ORIGINAL NUMBER!!")












































