rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

Draw_list = [rock, paper , scissors]

print("---Welcome to the Rock, Paper, Scissors game.---")
user_choice = int(input("Choose any Number  0 - Rock, 1 - Paper, 2 - Scissors : \n-> "))
computer_choice = random.randint(0,2)

if user_choice >= 0 and user_choice <= 2:
    print("You Choose",Draw_list[user_choice])

print("Computer Choose",Draw_list[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You Choose Invalid Number. You Lose!")

elif user_choice == 2 and computer_choice == 0:
    print("You Lose!")

elif user_choice == 0 and computer_choice == 2:
    print("You Win!")

elif computer_choice < user_choice:
    print("You Win!")

elif computer_choice > user_choice:
    print("You Lose!")

elif computer_choice == user_choice:
    print("Match is Draw")
