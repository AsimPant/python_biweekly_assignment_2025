'''
10. Create three dictionaries: 

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

(f) Write code to multiply all the items in the dictionary nums.

'''

# Creating the three dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Merging all dictionaries into one called nums
nums = {}

for key in dic1:
    nums[key] = dic1[key]

for key in dic2:
    nums[key] = dic2[key]

for key in dic3:
    nums[key] = dic3[key]

# Adding a new key-value pair
nums[7] = 70

# Updating the value of key 3
nums[3] = 80

# Removing the third item from nums
third_key = list(nums.keys())[2]
del nums[third_key]

# Multiplying all values in the dictionary
product = 1
for value in nums.values():
    product *= value

# Displaying the product
print("Product of all values in the dictionary:")
print(product)
