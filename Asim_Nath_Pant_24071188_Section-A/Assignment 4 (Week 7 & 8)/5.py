'''
5. Create a 5x5 matrix with row values ranging from 0 to 4.

'''

import numpy as np

# Creating a 5x5 matrix with row values ranging from 0 to 4
matrix = np.tile(np.arange(5), (5, 1))

# Printing the created matrix
print("Creating a 5x5 matrix with row values ranging from 0 to 4:")
print(matrix)
