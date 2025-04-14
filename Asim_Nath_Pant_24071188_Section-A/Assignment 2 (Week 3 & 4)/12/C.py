'''
12. Create two sets:

set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

(c) Write code to compute the symmetric difference between set1 and set2.

'''

# Creating the two sets
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

# Computing the symmetric difference between the two sets
symmetric_diff = set1 ^ set2  # Using the symmetric difference operator (^)

# Printing the resulting symmetric difference
print("Symmetric difference between set1 and set2:", symmetric_diff)
