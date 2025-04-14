'''
6. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2000 (both included).

'''

found = False # Initializing the Boolean value for found as 'False'

print("Numbers between 1500 and 2000 that are divisible by 7 and a multiple of 5:\n")

# Finding numbers in the given range between 1500 and 2000
for num in range(1500, 2000 + 1):
    if num % 7 == 0 and num % 5 == 0:
        print(num, "\t")   # Displaying the numbers that meet the criteria
        found = True

# In case no numbers are found in this range 
if not found:
    print("No numbers found in this range that meet the criteria.")
