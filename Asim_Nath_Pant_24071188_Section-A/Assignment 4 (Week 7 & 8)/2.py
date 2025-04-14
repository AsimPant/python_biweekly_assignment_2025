'''
2. Ask user to input two numbers a, b. Write a program to generate a random array of shape (a, b) and print the array and avg of the array.

'''

import numpy as np

# Asking user to input two numbers a and b
a = int(input("Enter the number of rows (a): "))
b = int(input("Enter the number of columns (b): "))

# Generating a random array of shape (a, b)
random_array = np.random.rand(a, b)

# Calculating the average of the array
array_avg = np.mean(random_array)

# Printing the array and its average
print("\nGenerated random array:")
print(random_array)
print("\nAverage of the array:", array_avg)
