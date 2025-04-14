'''
4. Can you create a identity matrix of shape (3,4). If yes write code for it.

'''

import numpy as np

# Creating an identity matrix of shape (3, 4) using np.eye()
# Note: An identity matrix is a square matrix, so for a non-square matrix like (3, 4),
# it will create a matrix with 1s on the diagonal and 0s elsewhere.
identity_matrix = np.eye(3, 4)

# Printing the created identity matrix
print("Creating an identity matrix of shape (3, 4):")
print(identity_matrix)
