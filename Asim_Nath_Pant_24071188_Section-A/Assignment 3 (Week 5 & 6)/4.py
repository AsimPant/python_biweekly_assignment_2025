'''
4. Implement a program to read a CSV file and display its contents in a tabular format.

'''

import csv  # Importing the CSV module

# Function to read the CSV file and display its contents in a tabular format
def display_csv_content(filename):
    try:
        # Opening the CSV file in read mode
        with open(filename, 'r') as file:
            # Creating a CSV reader object to read the content
            csv_reader = csv.reader(file)
            
            # Reading and displaying the header
            headers = next(csv_reader)
            print("\t".join(headers))  # Displaying column headers
            
            # Reading and displaying the rows of the CSV
            for row in csv_reader:
                print("\t".join(row))  # Displaying each row
            
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Main Program
filename = input("Enter the name of the CSV file: ")
display_csv_content(filename)
