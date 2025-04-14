'''
7. Write a program that prompts the user to enter a list of names and store them in a list. The program should display how many times the letter 'a' appears within the list.

'''

# Empty list to store names
names = []

# Asking the user how many names they want to enter
n = int(input("How many names do you want to enter? "))

# Adding the names to the list by taking them as an input from the user
for i in range(n):
    name = input("Enter name: ")
    names.append(name)

# Counting the number of times 'a' appears in all of the names combined
count_a = 0
for name in names:
    count_a += name.lower().count('a')  # converting to lowercase to count both 'a' and 'A' and add them

# Displaying the result to the user
print("The letter 'a' appears", count_a, "times in the list of entered names respectively.")
