'''
5. Write a program to find the simple interest when the value of principle, rate of interest and time period is provided by the user.[

'''

# Taking Principal, Time, and Rate as input from the user
principal = float(input("Enter Principal: "))
time = float(input("Enter Time (in years): "))
rate = float(input("Enter Rate: "))

# Calculating the Simple Interest using the formula
si = (principal * time * rate) / 100

# Displaying the Simple Interest to the user
print("\nThe simple interest is", si, "respectively.")
