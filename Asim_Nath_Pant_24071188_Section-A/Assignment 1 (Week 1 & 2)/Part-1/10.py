'''
10. Program to print the Unicode encoding for your name

'''

# Initialing the name
name = "Asim Nath Pant"

# Empty 'unicode' list for storing the unicode value of each characters
unicode = []

# Looping through each characters of the name
for char in name:
    unicode.append(ord(char))     # Adding the unicode value of each characters to the list

# Displaying the list storing all the unicode values for each characters in the name
print("The Unicode encoding for", name, "is", unicode)
