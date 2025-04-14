'''
7. Create an array of random integer numbers as a numpy array, sort them and perform operations such as reshaping of the array into matrix of feasible dimensions. (e.g., if we have an array of 1 * 10, then we can reshape it into 2 * 5 or 5 * 2 matrix.) [Hint: Use the array of reshape (row * column)].

'''

import numpy as np

# Creating a random numpy array of 10 integers between 1 and 50
random_array = np.random.randint(1, 51, 10)

# Sorting the array
random_array.sort()

# Printing the sorted array
print("Sorted random array:", random_array)

# Reshaping the array into different feasible dimensions
# Example of reshaping from 1x10 to 2x5 matrix
reshaped_array_2x5 = random_array.reshape(2, 5)
print("\nReshaped to 2x5 matrix:\n", reshaped_array_2x5)

# Example of reshaping from 1x10 to 5x2 matrix
reshaped_array_5x2 = random_array.reshape(5, 2)
print("\nReshaped to 5x2 matrix:\n", reshaped_array_5x2)
