'''
2. Write a program to copy the contents of one file to another.

'''

# Function to copy the contents of one file to another
def copy_file_contents(source_filename, destination_filename):
    try:
        # Opening the source file in read mode
        with open(source_filename, 'r') as source_file:
            # Reading the contents of the source file
            content = source_file.read()
        
        # Opening the destination file in write mode
        with open(destination_filename, 'w') as destination_file:
            # Writing the content to the destination file
            destination_file.write(content)
        
        print(f"Contents of '{source_filename}' have been copied to '{destination_filename}'.")
    
    except FileNotFoundError:
        print(f"One of the files '{source_filename}' or '{destination_filename}' was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main Program
source_filename = input("Enter the name of the source file: ")
destination_filename = input("Enter the name of the destination file: ")
copy_file_contents(source_filename, destination_filename)
