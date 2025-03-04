import datetime
from prettytable import PrettyTable

# Represents each book with attributes and methods to borrow and return the book.
class Book:      
    def __init__(self, title, author, isbn, status="available", borrow_date=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status
        self.borrow_date = borrow_date

    def borrow(self):
        self.status = "borrowed"
        self.borrow_date = datetime.datetime.now()

    def return_book(self):
        self.status = "available"
        self.borrow_date = None

# Manages a collection of books and provides methods to add, borrow, return, and view books.
class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    # Add a new book to the library.
    def add_new_book(self, title, author, isbn):
        # Check if the book already exists in the library
        for book in self.books:
            if book.isbn == isbn:
                print(f"A book with ISBN {isbn} already exists.")
                return
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        print(f"Book '{title}' by {author} has been added to the library.")

    # Borrow a book from the library.
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "available":
                    book.borrow()
                    print(f"You have borrowed '{book.title}' by {book.author}.")
                    return
                else:
                    print(f"The book '{book.title}' is already borrowed.")
                    return
        print(f"No book found with ISBN {isbn}.")

    # Return a book to the library.
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "borrowed":
                    book.return_book()
                    print(f"You have returned '{book.title}'. Thank you!")
                    return
                else:
                    print(f"'{book.title}' is already available in the library.")
                    return
        print(f"No book found with ISBN {isbn}.")

    # Displays all books that are available.
    def view_available_books(self):
        table = PrettyTable()
        table.field_names = ["Title", "Author", "ISBN", "Status"]
        any_available = False
        for book in self.books:
            if book.status == "available":
                table.add_row([book.title, book.author, book.isbn, book.status])
                any_available = True
        if any_available:
            print("We have the following books available in our library:")
            print(table)
        else:
            print("No books available in the library at the moment.")

    # Displays all books that are borrowed along with the date and time of borrowing.
    def view_borrowed_books(self):
        table = PrettyTable()
        table.field_names = ["Title", "Author", "ISBN", "Status", "Borrow Date"]
        any_borrowed = False
        for book in self.books:
            if book.status == "borrowed":
                table.add_row([book.title, book.author, book.isbn, book.status, book.borrow_date.strftime("%Y-%m-%d %H:%M:%S")])
                any_borrowed = True
        if any_borrowed:
            print("The following books are currently borrowed:")
            print(table)
        else:
            print("No books are currently borrowed.")

# Main Function: Provides a user interface to interact with the library system.
def main():
    library = Library("Sherin's Library")

    while True:
        print(f"\nWelcome to {library.name}. Enter your choice to continue:")
        print("Press 1 to add a new book")
        print("Press 2 to borrow a book")
        print("Press 3 to return a book")
        print("Press 4 to view currently available books in our library")
        print("Press 5 to view currently borrowed books from our library")
        print("Press 'q' to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_new_book(title, author, isbn)

        elif choice == '2':
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)

        elif choice == '3':
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)

        elif choice == '4':
            library.view_available_books()

        elif choice == '5':
            library.view_borrowed_books()

        elif choice == 'q':
            print("Exiting the program.")
            break

        else:
            print("Not a valid option.")

        print("Press 'q' to exit or 'c' to continue")
        user_choice = ""
        while user_choice not in ["c", "q"]:
            user_choice = input()
            if user_choice == "q":
                print("Thank you! Feel free to come again.")
                exit()
            elif user_choice == "c":
                continue

if __name__ == "__main__":
    main()
