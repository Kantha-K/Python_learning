
#ROCK PAPER OR SCISSORS
'''computer_choice = "scissors"
user_choice=input("Do you want rock,paper or scissors\n")
if user_choice==computer_choice:
    print("Tie")

elif user_choice == "rock" and computer_choice == "scissors":
    print("Win")
elif user_choice == "paper" and computer_choice == "rock":
    print("Win")
elif user_choice == "Scissors" and computer_choice == "paper":
    print("Win")
else:
    print("Computer_wins")'''

import random
# roll = random.randint(1,10)
# print(roll)
# print(roll)
computer_choice = random.choice(["rock","paper","scissors"])

user_choice=input("Do you want rock,paper or scissors\n")
if user_choice==computer_choice:
    print("Tie")
    print("The computer_choice is"+str(computer_choice))

elif user_choice == "rock" and computer_choice == "scissors":
    print("Win")
    print("The computer_choice is"+str(computer_choice))
elif user_choice == "paper" and computer_choice == "rock":
    print("Win")
    print("The computer_choice is"+str(computer_choice))
elif user_choice == "Scissors" and computer_choice == "paper":
    print("Win")
    print("The computer_choice is"+str(computer_choice))
else:
    print("Computer_wins")
    print("The computer_choice is"+str(computer_choice))
