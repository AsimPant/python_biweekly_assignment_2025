'''
10. Create three dictionaries: 

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

(c) Write code to update the value of the item with key 3 in nums to 80.

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

# (c) Updating the value of key 3 to 80
nums[3] = 80

# Displaying the updated dictionary
print("Updated dictionary after changing the value of key 3 to 80:")
print(nums)
