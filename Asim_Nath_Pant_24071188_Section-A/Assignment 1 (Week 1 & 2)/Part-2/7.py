'''
7. Write a Python program that accepts a string and calculates the number of digits and letters.

'''

# Taking string as the input from the user
text = input("Enter a string: ")

# Initializing the counters for letters and digits
letters = 0
digits = 0

# Looping through each character in the string
for char in text:
    if char.isalpha():  # Checking if the character is a letter
        letters += 1
    elif char.isdigit():  # Checking if the character is a digit
        digits += 1

# Displaying the results to the user
print("\nThe number of letters is", letters, "respectively.")
print("The number of digits is", digits, "respectively.")
