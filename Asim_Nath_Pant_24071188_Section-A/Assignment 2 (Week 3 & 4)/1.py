'''
1. Write a function that accepts a string and calculate the number of upper case letters and lower case letters.

'''

# Function to count uppercase and lowercase letters
def count_letters(text):
    upper_count = 0  # Initializing the counter for uppercase letters
    lower_count = 0  # Initializing the counter for lowercase letters

    # Looping through each character in the string
    for char in text:
        if char.isupper():  # Checking if the character is uppercase
            upper_count += 1
        elif char.islower():  # Checking if the character is lowercase
            lower_count += 1

    # Displaying the results to the user
    print("There are", upper_count, "uppercase letters in this string respectively.")
    print("There are", lower_count, "lowercase letters in this string respectively.")

# Main program
str = input("Enter a string: ")  # Taking a string as input from the user
count_letters(str)  # Calling the count_letters() function
