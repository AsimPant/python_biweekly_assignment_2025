'''
7. Write a program to implement a class called employee with attributes such as empid, name, address, contact_number, spouse name, number_of_child, salary. Instantiate this class to input the values for multiple employees and write it in a file “employees.csv”. Allow the user of your program to see the list of employees and their details as well. Try to use the concept of try/except too in the program.

'''

import csv

# Defining the Employee class
class Employee:
    def __init__(self, empid, name, address, contact_number, spouse_name, number_of_children, salary):
        # Initializing the attributes
        self.empid = empid
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.spouse_name = spouse_name
        self.number_of_children = number_of_children
        self.salary = salary

    # Method to return employee details as a dictionary
    def to_dict(self):
        return {
            "empid": self.empid,
            "name": self.name,
            "address": self.address,
            "contact_number": self.contact_number,
            "spouse_name": self.spouse_name,
            "number_of_children": self.number_of_children,
            "salary": self.salary
        }

# Function to write employee data to a CSV file
def write_to_file(employee_list):
    try:
        # Opening the file in write mode, create a CSV writer object
        with open("employees.csv", mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["empid", "name", "address", "contact_number", "spouse_name", "number_of_children", "salary"])
            
            # Writing the header
            writer.writeheader()

            # Writing employee data to the file
            for employee in employee_list:
                writer.writerow(employee.to_dict())

        print("Employee data has been written to 'employees.csv'.")

    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

# Function to display employee data from the file
def display_employee_data():
    try:
        # Opening the file in read mode
        with open("employees.csv", mode="r") as file:
            reader = csv.DictReader(file)
            
            # Displaying employee details
            print("\nEmployee Details:")
            for row in reader:
                print(row)
                
    except FileNotFoundError:
        print("No employee data found. Please add some employee details first.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Main Program
def main():
    employee_list = []

    # Loop to allow adding multiple employees
    while True:
        try:
            empid = input("\nEnter Employee ID: ")
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            contact_number = input("Enter Contact Number: ")
            spouse_name = input("Enter Spouse Name: ")
            number_of_children = int(input("Enter Number of Children: "))
            salary = float(input("Enter Salary: "))

            # Creating an employee object and adding it to the list
            employee = Employee(empid, name, address, contact_number, spouse_name, number_of_children, salary)
            employee_list.append(employee)

            # Asking if the user wants to add another employee
            another = input("Do you want to add another employee? (yes/no): ").strip().lower()
            if another != "yes":
                break
        
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please enter valid data.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # Writing employee data to file
    write_to_file(employee_list)
    
    # Option to view employee data
    view_data = input("\nDo you want to see the list of employees? (yes/no): ").strip().lower()
    if view_data == "yes":
        display_employee_data()

# Running the main program
if __name__ == "__main__":
    main()
