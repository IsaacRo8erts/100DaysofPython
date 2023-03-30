# Rock Paper Scissors
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

# choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# computer_choice = random.randint(0, 2)

# if choice == 0:
#     print(rock)
#     print("Computer chose:\n")
#     if computer_choice == 0:
#         print(rock)
#         print("You draw")
#     elif computer_choice == 1:
#         print(paper)
#         print("You lose")
#     else:
#         print(scissors)
#         print("You win")
# elif choice == 1:
#     print(paper)
#     print("Computer chose:\n")
#     if computer_choice == 0:
#         print(rock)
#         print("You win")
#     elif computer_choice == 1:
#         print(paper)
#         print("You draw")
#     else:
#         print(scissors)
#         print("You lose")
# else:
#     print(scissors)
#     print("Computer chose:\n")
#     if computer_choice == 0:
#         print(rock)
#         print("You lose")
#     elif computer_choice == 1:
#         print(paper)
#         print("You win")
#     else:
#         print(scissors)
#         print("You draw")

# V2

game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >= 3 or choice < 0:
    print("Invalid, you lose")
else:
    print(game_images[choice])

    computer_choice = random.randint(0, 2)
    print("Computer choice:")
    print(game_images[computer_choice])

    if choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and choice == 2:
        print("You lose")
    elif computer_choice > choice:
        print("You lose")
    elif choice > computer_choice:
        print("You win")
    elif computer_choice == choice:
        print("You draw")


