'''
1. Write a program to take a number input from the user and display whether the number is even or odd.

'''

# Take an integer as an input from the user
num = int(input("Enter a number: "))

# Checking whether the entered number is even or odd
if num % 2 == 0:
    print("\n", num, "is an even number respectively.")   # In case the number is even
else:
    print("\n", num, "is an odd number respectively.")    # In case the number is odd
