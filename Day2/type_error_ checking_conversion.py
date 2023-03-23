# Type Error, Type Checking, and Type Conversion

# TypeError 
# Example: len(1234) returns TypeError as this function requires strings

# Type Checking
print(type(len(input("What is your name?"))))
# Use type function to figure out the type if unsure

# Type Conversion
num_char = len("Hello")
new_num_char = str(num_char)
# str converts num_char variable for an int to a string
print("Hello has " + new_num_char + " characters.")
# Can use float() to convert to float, int() to convert to int