# import random
# choices=["rock","paper","scissor"]
# rules={
#     ("rock","paper"):"paper cover you will loose!",
#     ("rock","scissors"):"rock give damage to scissor.You win!",
#     ("paper","scissor"):"scissor cut paper.You lose!",
#     ("paper","rock"):"paper cover rock.You win!",
#     ("scissor","rock"):"rock give damage to scissor.You lose!",
#     ("scissor","paper"):"scissor cut paper.You win!"
# }
# while True:
#     print("Let's play rock-paper-scissor game")
#     player = input("sir ,please enter your choice(or for exit game)::").lower()
#     if player == "quit":
#         print("Thank you for playing sir!!")
#         break
#     if player not in choices:
#         print("Sir ,please enter valid choice:")
#         continue

#     computer = random.choice(choices)
#     print(f"computer choose:{computer}")

#     if player== computer:
#         print("It's tie")
#     else:
#         result = rules.get((player,computer))
#         if result:
#             print(result)
#         else:
#             print("Something went wrong!!")



#OR


import random 
l=["Rock","Paper","Scissor"]
computer = random.choice(l)

while True:
    menu="""
          press r for rock
          press p for paper
          press s for scissor
"""
    print(menu)
    choice = input("Enter your choice:")
    
    if computer=="rock" and choice=="s":
        print("Computer win!!")

    elif computer=="paper" and choice=="r":
        print("Computer win!!")

    elif computer=="scissor" and choice=="p":
        print("Computer win!!")

    else:
        print("User Win!!")            





            


















