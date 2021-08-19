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
---'    ____)____
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

game_images = [rock, paper, scissors]

users_choice = int(input("what do you want to choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSOR\n"))
if users_choice >= 3 or users_choice < 0:
    print("You typed an invalid number!! YOU LOSE")
else:
    print("users_choice:")
    print(game_images[users_choice])
    computers_choice = random.randint(0, 2)
    print("computer's choice:")
    print(game_images[computers_choice])

    if users_choice == 0 and computers_choice == 1:
        print("SORRY! YOU LOSE")
    elif users_choice == 0 and computers_choice == 2:
        print("YES! YOU WIN")
    elif users_choice == 0 and computers_choice == 0:
        print("MATCH IS DRAW")
    elif users_choice == 1 and computers_choice == 0:
        print("YES! YOU WIN")
    elif users_choice == 1 and computers_choice == 2:
        print("SORRY! YOU LOSE")
    elif users_choice == 1 and computers_choice == 1:
        print("MATCH IS DRAW")
    elif users_choice == 2 and computers_choice == 0:
        print("SORRY! YOU LOSE")
    elif users_choice == 2 and computers_choice == 1:
        print("YES! YOU WIN")
    elif users_choice == 2 and computers_choice == 2:
        print("MATCH IS DRAW")
