# Love Calc

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true_count = 0
love_count = 0

combined_name_lower = name1.lower() + name2.lower()

t_count = combined_name_lower.count("t")
r_count = combined_name_lower.count("r")
u_count = combined_name_lower.count("u")
e_count = combined_name_lower.count("e")

true_count = t_count + r_count + u_count + e_count

l_count = combined_name_lower.count("l")
o_count = combined_name_lower.count("o")
v_count = combined_name_lower.count("v")
e2_count = combined_name_lower.count("e")

love_count = l_count + o_count + v_count + e2_count

love_score = int(str(true_count) + str(love_count))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")




