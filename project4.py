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


user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

computer_choice = random.randint(0, 2)

if user_choice == computer_choice:
    print(f"Computer chose {computer_choice}, You won the game")

else:
    print(f"You choose {user_choice} but computer choose {computer_choice}, sorry you lost the game")

