'''
1. Write a program to count the number of lines, words, and characters in a text file.

'''

# Function to count lines, words, and characters in a file
def count_file_contents(filename):
    # Initializing counters
    lines = 0
    words = 0
    characters = 0
    
    try:
        # Opening the file in read mode
        with open(filename, 'r') as file:
            for line in file:
                lines += 1  # Incrementing line counter
                words_in_line = line.split()  # Spliting the line into words
                words += len(words_in_line)  # Adding the number of words
                characters += len(line)  # Adding the number of characters (including spaces)

        # Displaying the counts
        print(f"Number of lines: {lines}")
        print(f"Number of words: {words}")
        print(f"Number of characters: {characters}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")

# Main Program
filename = input("Enter the name of the text file: ")
count_file_contents(filename)
