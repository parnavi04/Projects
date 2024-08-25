"""Rock  Paper annd Scissors"""
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
scissor =  '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = [rock,paper,scissor]
random_choice = random.randint(0,2)
players_choice = int(input("What do you want to choose. Type 0 for Rock, 1 for Paper,2 for scissor: "))
print("Your  choice:")
print(choice[players_choice])

print("Computer's choice:")
print(choice[random_choice])

"""
rock and scissor - rock won
rock and paper - paper won
paper and scissor - scissor won"""

if random_choice==0:
    if players_choice==0:
        print("It's a tie..")
    if players_choice==1:
        print("You Won!")
    if players_choice==2:
        print("You Lose..")
        
if random_choice==1:
    if players_choice==0:
        print("You Lose..")
    if players_choice==1:
        print("It's a tie..")
    if players_choice==2:
        print("You Won!")

if random_choice==2:
    if players_choice==0:
        print("You Won!")
    if players_choice==1:
        print('You Lose..')
    if players_choice==2:
        print("It's a tie..")