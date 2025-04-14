'''
3. Write a program to find and replace a specific word in a file with another word.

'''

# Function to find and replace a specific word in a file
def find_and_replace_word(filename, old_word, new_word):
    try:
        # Opening the file in read mode
        with open(filename, 'r') as file:
            # Reading the content of the file
            content = file.read()
        
        # Replacing the old word with the new word
        content = content.replace(old_word, new_word)
        
        # Opening the file in write mode to save the changes
        with open(filename, 'w') as file:
            # Writing the modified content back to the file
            file.write(content)
        
        print(f"The word '{old_word}' has been replaced with '{new_word}' in the file.")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main Program
filename = input("Enter the name of the file: ")
old_word = input("Enter the word to find: ")
new_word = input("Enter the word to replace with: ")

find_and_replace_word(filename, old_word, new_word)
