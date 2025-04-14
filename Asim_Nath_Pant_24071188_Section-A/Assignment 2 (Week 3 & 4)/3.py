'''
3. Write a program to check whether the given number is armstrong or not

'''

# Function to check whether the given number is armstrong or not
def armstrong(num):
    num_str  =str(num)  # Converting the number to string for counting digits

    # Calculating the sum of each digit raised to the power of digit
    total = 0
    for digit in num_str:
        total += int(digit) ** len(num_str)

    # Checking whether the number is armstrong or not            
    if total == num:
        print(num, "is an armstrong number respectively.")
    else:
        print(num, "is not an armstrong number respectively.")


# Main Program
# Taking number from user
num = int(input("Enter a number: "))

# Calling armstrong() function 
armstrong(num)