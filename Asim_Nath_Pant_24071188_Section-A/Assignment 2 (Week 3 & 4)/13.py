'''
12. Create a function called word_intersection that prompts the user for two English words, and displays which letters the two words have in common.

'''

# Function to find and show common letters between two words
def word_intersection():
    # Asking the user to enter the first word
    word1 = input("Enter the first word: ")
    
    # Asking the user to enter the second word
    word2 = input("Enter the second word: ")

    # Creating an empty list to store common letters
    common_letters = []

    # Looping through each letter in the first word
    for letter in word1:
        # Checking if the letter is in the second word and not already added
        if letter in word2 and letter not in common_letters:
            # Adding the letter to the list of common letters
            common_letters.append(letter)

    # Printing the list of common letters
    print("Common letters:", common_letters)

# Main program
word_intersection()
