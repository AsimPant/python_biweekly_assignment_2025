'''
4. Write a function to accept a list of names and return the sorted order of names back.

'''

# Function to sort the names from the list
def sort_names(names):
    names.sort()  # Sort the elements in 'names' list
    return names


# Main program 

myList = []  # Initializng the list for storing the names
n = int(input("Enter the number of names for the list: "))

# Prompting the user to input numbers for the list 'n' times
for k in range(n):
    name = input("Enter a name: ")
    myList.append(name)

print("\nInitial List of Names:", myList)

# Calling remove_duplicates() for the list by assigning the return value to 'myUniqueList'
sortedList = sort_names(myList)  

# Displaying the sorted names to the user
print("\nList after sorting the names:", sortedList)
