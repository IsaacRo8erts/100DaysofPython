# For Loop

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)

# For Loop with Range

for number in range(1, 11, 3):
    # third number is the step that the loop counts in
    print(number)
    # 1, 4, 7, 10

# Add all numbers from 1 - 100
total = 0
for number in range(1, 101):
    total += number
print(total)
# 5050