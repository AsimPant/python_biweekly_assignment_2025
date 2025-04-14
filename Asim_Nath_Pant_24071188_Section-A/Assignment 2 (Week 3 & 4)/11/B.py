'''
10. Create three dictionaries: 

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

(b) Write code to add a new key/value pair to the dictionary nums: (7, 70).

'''

# Creating the three dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Creating an empty dictionary to store combined values
nums = {}

# Adding contents of dic1 to nums
for key in dic1:
    nums[key] = dic1[key]

# Adding contents of dic2 to nums
for key in dic2:
    nums[key] = dic2[key]

# Adding contents of dic3 to nums
for key in dic3:
    nums[key] = dic3[key]

# Adding new key/value pair (7, 70) to nums
nums[7] = 70

# Displaying the updated dictionary
print("Updated dictionary after adding (7, 70):")
print(nums)
