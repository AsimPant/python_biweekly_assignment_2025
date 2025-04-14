'''
5. Develop a program that counts the occurrence of each word in a file.

'''

# Function to count the occurrence of each word in a file
def count_word_occurrences(filename):
    try:
        # Creating an empty dictionary to store word counts
        word_count = {}
        
        # Opening the file in read mode
        with open(filename, 'r') as file:
            # Reading all lines from the file
            content = file.read()
            
            # Converting the content to lowercase and splitting into words
            words = content.lower().split()
            
            # Counting the occurrence of each word
            for word in words:
                # Removing any punctuation attached to words
                word = word.strip(",.!?;:")
                
                # Updating the word count in the dictionary
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        
        # Displaying the word count
        print("Word occurrences in the file:")
        for word, count in word_count.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main Program
filename = input("Enter the name of the file: ")
count_word_occurrences(filename)
