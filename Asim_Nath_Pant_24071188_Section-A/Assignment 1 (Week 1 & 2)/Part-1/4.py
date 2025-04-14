'''
4. Program to print 7 factorial minus 5 factorial

'''

# Initializing the first number as '7'
num1 = 7

# Initializing the factorial for '7' to '1'
fact1 = 1

# Looping through each digits of '7'
for k in range(1, num1 + 1):
    fact1 *= k

# Initializing the second number as '5'
num2 = 5

# Initializing the factorial for '5' to '1'
fact2 = 1

# Looping through each digits of '5'
for k in range(1, num2 + 1):
    fact2 *= k

# Calculating the difference in between '7' factorial and '5' factorial
result = fact1 - fact2

# Displaying the difference to the user
print("7 factorial minus 5 factorial is", result, "respectively.")
