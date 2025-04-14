'''
12. Create two sets:

set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

(a) Write code to perform a union of these sets. Print the length of the resulting set.

'''

# Creating the two sets
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

# Performing the union of the two sets
union_set = set1 | set2  # Using the union operator (|)

# Printing the length of the resulting set
print("Length of the union of the two sets:", len(union_set))
