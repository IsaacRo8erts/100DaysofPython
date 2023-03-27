print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇


left_or_right = input('Would you like to go "left" or "right"? ').lower()
# Can add to lower at end instead of doing OR
# Can do single quotes so that left and right can be in double quotes
if left_or_right == "left":
    print("You chose left.")
    swim_or_wait = input("Would you like to swim or wait? ")
    if (swim_or_wait == "Wait" or swim_or_wait == "wait"):
        which_door = input("What colour door will you go through? ")
        if (which_door == "Yellow" or which_door == "yellow"):
            print("YOU WIN!")
        elif (which_door == "Red" or which_door == "red"):
            print("Burned by fire! GAME OVER.")
        elif (which_door == "Blue" or which_door == "blue"):
            print("Eaten by beasts! GAME OVER.")
        else:
            print("GAME OVER.")
    else:
        print("Attacked by sharks! GAME OVER.")
else:
    print("You have fallen into a hole! GAME OVER.")