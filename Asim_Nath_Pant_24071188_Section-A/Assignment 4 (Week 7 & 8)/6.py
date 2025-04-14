'''
6. Write a program to input an array of numbers from the user (at least 10 elements in list), sort them and perform slicing operations to get elements between indexes such as 2-5, 5-8, 2-9. 

'''

# Taking input for an array of at least 10 numbers from the user
numbers = []
print("Enter at least 10 numbers:")
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Sorting the array in ascending order
numbers.sort()

# Printing the sorted array
print("\nSorted array:", numbers)

# Performing slicing operations on the sorted array
print("\nSlicing operations:")
print("Elements between index 2 and 5:", numbers[2:6])
print("Elements between index 5 and 8:", numbers[5:9])
print("Elements between index 2 and 9:", numbers[2:10])
