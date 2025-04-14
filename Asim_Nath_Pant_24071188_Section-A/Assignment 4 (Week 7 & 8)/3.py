'''
3. Create a vector of size 10 with values ranging from 0 to 1, both excluded.

'''

import numpy as np

# Creating a vector of size 10 with values ranging from 0 to 1 (both excluded)
vector = np.linspace(0, 1, 11)[1:-1]

# Printing the vector
print("Vector of size 10 with values ranging from 0 to 1 (both excluded):")
print(vector)
