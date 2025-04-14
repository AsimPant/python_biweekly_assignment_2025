'''
10. Create three dictionaries: 

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

(a) Write code to concatenate these dictionaries to create a new one. Create a variable called nums to store the resulting dictionary.

'''

# Creating the three dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenating the dictionaries into one
nums = {}

# Adding all key-value pairs from dic1
for key in dic1:
    nums[key] = dic1[key]

# Adding all key-value pairs from dic2
for key in dic2:
    nums[key] = dic2[key]

# Adding all key-value pairs from dic3
for key in dic3:
    nums[key] = dic3[key]

# Display the final combined dictionary
print("Combined dictionary:")
print(nums)
