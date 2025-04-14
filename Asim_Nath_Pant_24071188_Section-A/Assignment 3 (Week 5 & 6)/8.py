'''
8. Write a program to implement a basic library book management with the functionalities such as issue the book, return the book and search the book. Use the concept of OOP to create the necessary classes on your own and implement the concept of other OOP features. For the storage of book details, use the file handling along with the exception handling. 

'''

import os

# Class to represent a Book in the library
class Book:
    def __init__(self, title, author, book_id, is_issued=False):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_issued = is_issued
    
    def __str__(self):
        status = "Issued" if self.is_issued else "Available"
        return f"ID: {self.book_id} | Title: {self.title} | Author: {self.author} | Status: {status}"

# Class to represent the Library
class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        """Load books from the file into the list"""
        books = []
        try:
            if os.path.exists("library_books.txt"):
                with open("library_books.txt", "r") as file:
                    for line in file:
                        title, author, book_id, is_issued = line.strip().split(",")
                        book = Book(title, author, book_id, is_issued == 'True')
                        books.append(book)
        except Exception as e:
            print(f"Error loading books from file: {e}")
        return books
    
    def save_books(self):
        """Save the current list of books back to the file"""
        try:
            with open("library_books.txt", "w") as file:
                for book in self.books:
                    file.write(f"{book.title},{book.author},{book.book_id},{book.is_issued}\n")
        except Exception as e:
            print(f"Error saving books to file: {e}")

    def issue_book(self, book_id):
        """Issue a book if it's available"""
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' has been issued.")
                    self.save_books()
                    return
                else:
                    print(f"Sorry, the book '{book.title}' is already issued.")
                    return
        print("Book with the given ID not found.")

    def return_book(self, book_id):
        """Return a book to the library"""
        for book in self.books:
            if book.book_id == book_id:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' has been returned.")
                    self.save_books()
                    return
                else:
                    print(f"The book '{book.title}' is not issued.")
                    return
        print("Book with the given ID not found.")

    def search_book(self, search_query):
        """Search for a book by title or author"""
        found_books = [book for book in self.books if search_query.lower() in book.title.lower() or search_query.lower() in book.author.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"No books found matching '{search_query}'.")


# Main program to demonstrate library management system
def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Issue a Book")
        print("2. Return a Book")
        print("3. Search a Book")
        print("4. Exit")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                book_id = input("Enter Book ID to issue: ")
                library.issue_book(book_id)
            elif choice == 2:
                book_id = input("Enter Book ID to return: ")
                library.return_book(book_id)
            elif choice == 3:
                search_query = input("Enter book title or author to search: ")
                library.search_book(search_query)
            elif choice == 4:
                print("Exiting the library management system.")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
