# Conditional Statements

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

# One = is an assignment, two == is comparing if right value is equal to left value

num = 1
print(num) # prints 1
print(num == 1) # prints True

# Nested if / else

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <=18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

