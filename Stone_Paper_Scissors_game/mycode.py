import random
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
# User Side
print("What do you choose? \n\t0 for Rock,\n\t1 for Paper,\n\t2 for Scissors.")
user_choice = int(input("Input --> "))
# print (f"Your Choice is: {user_choice}")
if user_choice == 0:
    print("Your Choice is: Rock")
    print(rock)
elif user_choice == 1:
    print("Your Choice is: Paper")
    print(paper)
elif user_choice == 2:
    print("Your Choice is: Scissors")
    print(scissors)
else:
    print("Please, Enter Valid Input!")

# Pc side
pc_choice = random.randint(0,2)
if pc_choice == 0:
    print("Pc Choice is: Rock")
    print(rock)
elif pc_choice == 1:
    print("Pc Choice is: Paper")
    print(paper)
elif pc_choice == 2:
    print("Pc Choice is: Scissors")
    print(scissors)
else:
    print("Sorry, Something is Wrong with the System!")

# Game Result
if user_choice == 0:
    if pc_choice == 0:
        print ("---Match Draw---.")
    elif pc_choice == 1:
        print ("---You Lose---.")
    else:
        print ("---You Win.---")

if user_choice == 1:
    if pc_choice == 0:
        print("---You Win.---")
    elif pc_choice == 1:
        print("---Match Draw.---")
    else:
        print("---You Lose.---")

if user_choice == 2:
    if pc_choice == 0:
        print("---You Lose.---")
    elif pc_choice == 1:
        print("---You Win.---")
    else:
        print("---Match Draw.---")