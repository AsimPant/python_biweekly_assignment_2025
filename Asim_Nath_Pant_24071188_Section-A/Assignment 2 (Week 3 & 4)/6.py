'''
6. Write a program that prompts the user for a series of integers and stores in a list only the values between 1-100, and displays the resulting list.

'''

# Empty list to store valid numbers
valid_numbers = []

# Asking the users how many numbers they want to enter
n = int(input("How many numbers do you want to enter? "))

# Looping to take input for the integer numbers
for i in range(n):
    num = int(input("Enter a number: "))
    if 1 <= num <= 100:
        valid_numbers.append(num)

# Displaying the list containing integers between 1 and 100
print("The list containing intergers between 1 and 100 is", valid_numbers, "respectively.")
