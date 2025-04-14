'''
4. Write a program to find the Euclidean distance between two coordinates. Take both the coordinates from the user as input.

'''

# Asking the suer to enter the co-ordinates for the first point
print("Enter the co-ordinates for the first point: ")
x1 = float(input("Enter the horizontal co-ordinate (X1): "))
y1 = float(input("Enter the vertical co-ordinate (Y1): "))

# Asking the user to enter the co-ordinates for the first point
print("\nEnter the co-ordinates for the second point: ")
x2 = float(input("Enter the horizontal co-ordinates (X2): "))
y2 = float(input("Enter the vertical co-ordinates (Y2): "))

# Calulating the Euclidean distance based on the co-ordinates given
result = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)

# Displaying the Euclidean distance to the user
print(f"\nThe Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is {result} respectively.")
