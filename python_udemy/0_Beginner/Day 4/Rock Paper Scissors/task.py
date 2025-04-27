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


user_input = int(input("Select 1/2/3:"))
computer_input = random.randint(1,3)

if user_input == 1 and computer_input == 3 or user_input == 2 and computer_input == 1 or user_input == 3 and computer_input == 2:
    print("You win")
else:
    print("Computer win")

