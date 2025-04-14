'''
2. Write a program that prompts the user for two integer values and displays the results of the first number divided by the second, with exactly two decimal places displayed. 

'''

# Prompting the user to enter any two numbers
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

# Checking in case both the numbers are zero or not
if num1 != 0 and num2 != 0:
    result = num1 / num2    # Dividing the first number by second number
elif num1 == 0 and num2 != 0:
    result = 0    # If zero is divided by any number, the result is zero itself
else:    # In case both the numbers are zero
    print("\nDivision is not possible since the second number is zero respectively.")

# Displaying the results with exactly two decimal places
print(f"\n{num1} divided by {num2} is {result:.2f} respectively.")
