'''
5. Create a program called calculator with functions to perform the following arithmetic calculations, each should take two decimal parameters and return the result of the arithmetic calculation in question.[7]

A. Addition
B. Subtraction
C. Multiplication
D. Division
E. Truncated division
F. Modulus
G. Exponentiation

'''

# Function definition for 'add()'
def add(a, b):
    sum = a + b
    print("\nSum of", a, "and", b, "is", sum, "respectively.")

# Function definition for 'substarct()'
def substract(a, b):
    if a > b:
        difference = a - b
        print("\nThe difference of", a, "and", b, "is", difference, "respectively.")
    else:
        difference = b - a
        print("\nThe difference of", b, "and", a, "is", difference, "respectively.")

# Function definition for 'multiply()'
def multiply(a, b):
    product = a * b
    print("\nThe product of", a, "and", b, "is", product, "respectively.")

# Function definition for 'divide()'
def divide(a, b):
    if a != 0 and b != 0:
        if a > b:
            quotient = a / b
            print("\nThe quotient of", a, "and", b, "is", quotient, "respectively.")
        else:
            remainder = b / a
            print("\nThe quotient of", b, "and", a, "is", quotient, "respectively.")
    else:
        print("\nModular Division not possible since one of the entered numbers is zero respectively.")

# Function definition for 'truncate_divide()'
def truncate_divide(a, b):
    if a != 0 and b != 0:
        if a > b:
            truncate = int(a / b)
            print("\nWhole number nearest to zero for the quotient of", a, "and", b, "is", truncate, "respectively.")
        else:
            truncate = int(b / a)
            print("\nWhole number nearest to zero for the quotient of", b, "and", a, "is", truncate, "respectively.")
    else:
        print("\nTruncate Division is not possible since one of the two numbers is zero respectively.")

# Function definition for 'modular_divide()'
def modular_divide(a, b):
    if a != 0 and b != 0:
        if a > b:
            remainder = a % b
            print("\nThe remainder of", a, "and", b, "is", remainder, "respectively.")
        else:
            remainder = b % a
            print("\nThe remainder of", b, "and", a, "is", remainder, "respectively.")
    else:
        print("\nModular Division not possible since one of the entered numbers is zero respectively.")

# Function definition for 'exponent()'
def exponent(a, b):
    if a != 0 and b != 0:
        if a > b:
            num = a ** b
            print("\n", a, "raised to the power", b, "is", num, "respectively.")
        else:
            num = b ** a
            print("\n", b, "raised to the power", a, "is", num, "respectively.")
    elif (a == 0 and b != 0) or (a != 0 and b == 0):
        if a == 0:
            num = 0
            print("\n", a, "raised to the power", b, "is", num, "respectively.")
        elif b == 0:
            num = 0
            print("\n", b, "rasied to the power", a, "is", num, "respectively.")
    else:
        print("Since both the numbers are zero, exponentation is not possible respectively.")

# Main Program
# Taking numbers as input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Prompting the user to choose one of the operations
print("\nChoose one of the operations below: \n")
print("1. Addition \n2. Substraction \n3. Multiplication \n4. Division \n5. Truncated Division \n6. Modular Division \n7. Exponentation \n")
choice = int(input("Enter your choice (1-7): "))

# Choice '1' for addition of the numbers
if choice == 1:
    add(a, b)

# Choice '2' for substraction of the numbers
elif choice == 2:
    substract(a, b)

# Choice '3' for multiplication of the numbers
elif choice == 3:
    multiply(a, b)

# Choice '4' for division of the numbers
elif choice == 4:
    divide(a, b)

# Choice '5' for truncate division of the numbers
elif choice == 5:
    truncate_divide(a, b)

# Choice '6' for modular division of the numbers
elif choice == 6:
    modular_divide(a, b)

# Choice '7' for exponentation of the numbers
elif choice == 7:
    exponent(a, b)

# In case of Invalid Choice Entry
else:
    print("\nError!! Invalid Choice Entry !!")