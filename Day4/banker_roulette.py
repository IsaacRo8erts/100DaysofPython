import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Length of array
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
# -1 because we start counting from 0 remember, so fifth name is actually at index 4

person_who_will_pay = names[random_choice]

print(f"{person_who_will_pay} is going to buy the meal today!")
