# Lists

fruits = ["Apple", "Banana"]
# All data will remain in order set when list was made
states_of_america = ["Delaware", "Pennsylvania"]

print(states_of_america[0])
# Prints first item in list

print(states_of_america[-1])
# Starts counting from end of list

states_of_america.append("New Jersey")
# Adds new item to end of list

states_of_america.extend(["Georgia", "Connecticut", "Massachusetts", "Maryland"])
# Allows you to add a list to end of list

# Other functions: insert(i,x), remove(x), pop([i])

# states_of_america[len(states_of_america)] = "Ben"
# Adds B e n as seperate values to end of list
print(states_of_america)