'''
2. Write a program to check whether the given number is prime or not

'''

# Function to check whether the given number is prime or not
def prime(num):
    count = 0    # Counter for counting the no. of factors 

    for i in range(1, num + 1):   # Looping till the number for counting it's no. of factors
        if num % i == 0:    # Using modulus division to whether the given number is the factor of 'num' or not
            count += 1

    # Checking whether the entered number is prime number or not            
    if count == 2:  
        print("\n", num, "is a prime number respectively.")    # Prime numbers have exactly two factors ie. 1 and itself
    elif count > 2:
        print("\n", num, "is a composite number respectively.")   
    else:
        print("\n", num, "is neither prime nor composte number respectively.")


# Main Program
# Taking number from user
num = int(input("Enter a number: "))

# Calling prime() function 
prime(num)