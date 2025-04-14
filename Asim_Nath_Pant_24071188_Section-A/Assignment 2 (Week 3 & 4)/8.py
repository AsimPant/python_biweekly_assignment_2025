'''
8. Write a program that prompts the user to enter integer values to populate two lists, then prints messages to determine the following:

(a) Whether the lists are of the same length. 
(b) Whether the elements in each list sum to the same value. 
(c) Whether there are any values that occur in both lists

'''

# Asking user to enter integers for the first list
list1 = []
n1 = int(input("How many numbers in the first list? "))
for i in range(n1):
    num = int(input(f"Enter number {i + 1} for list 1: "))
    list1.append(num)

# Asking user to enter integers for the second list
list2 = []
n2 = int(input("\nHow many numbers in the second list? "))
for i in range(n2):
    num = int(input(f"Enter number {i + 1} for list 2: "))
    list2.append(num)

# (a) Checking if lists are of the same length
if len(list1) == len(list2):
    print("\n(a) The lists are of the same length.")
else:
    print("\n(a) The lists are NOT of the same length.")

# (b) Checking if sum of both lists is the same
if sum(list1) == sum(list2):
    print("(b) The sum of both lists is the same.")
else:
    print("(b) The sum of the lists is NOT the same.")

# (c) Checking for common values in both lists
common = []
for num in list1:
    if num in list2 and num not in common:
        common.append(num)

if common:
    print("(c) The following values occur in both lists:", common)
else:
    print("(c) There are NO common values in the lists.")
