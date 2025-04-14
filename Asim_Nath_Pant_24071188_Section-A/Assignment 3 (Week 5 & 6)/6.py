'''
6. Create a class Student with the attributes such as id, name, address, admission year, level, section. Instantiate the object of class to take input for all the attributes and display the output.

'''

# Defining the Student class
class Student:
    def __init__(self, student_id, name, address, admission_year, level, section):
        # Initializing the attributes
        self.student_id = student_id
        self.name = name
        self.address = address
        self.admission_year = admission_year
        self.level = level
        self.section = section

    # Method to display student details
    def display_details(self):
        print("\nStudent Details:")
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Admission Year: {self.admission_year}")
        print(f"Level: {self.level}")
        print(f"Section: {self.section}")

# Main Program
def main():
    # Taking input from the user for each attribute
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    address = input("Enter Student Address: ")
    admission_year = input("Enter Admission Year: ")
    level = input("Enter Level (e.g., Undergraduate, Graduate): ")
    section = input("Enter Section: ")

    # Creating an object of the Student class
    student = Student(student_id, name, address, admission_year, level, section)

    # Displaying the student details
    student.display_details()

# Running the main program
main()
