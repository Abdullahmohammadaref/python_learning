"""
Scenario: Building a Simple Library System
Imagine you’re tasked with creating a simple library system to manage books and members.
Using OOP principles, you can create a structured and efficient solution.

Step 1: Define the Classes
Book Class: Represents a book in the library.
Member Class: Represents a library member.
Library Class: Manages the collection of books and members.

Problem Description
You need to create a simple library system to manage books and members. 
The system should allow members to borrow and return books,
and the library should keep track of which books are available and which are checked out.

Requirements:
------------------
Book Management:
    Add new books to the library.
    Check out books to members.
    Return books to the library.
Member Management:
    Add new members to the library.
    Allow members to borrow and return books.
Library Management:
    Maintain a collection of books.
    Maintain a list of members.
    
UML Design
Here's a UML class diagram to illustrate the design:

+------------------------------------+
|                Library             |
+------------------------------------+
|         - books:   List<Book>      |
|         - members: List<Member>    |
+------------------------------------+
|  + add_book(book: Book): str       |
|  + add_member(member: Member): str |
+------------------------------------+

+-------------------------+
|           Book          |
+-------------------------+
|  - title: str           |
|  - author: str          |
|  - isbn: str            |
|  - is_checked_out: bool |
+-------------------------+
|  + check_out(): str     |
| + return_book(): str    |
+-------------------------+

+--------------------------------+
|           Member               |
+--------------------------------+
| - name: str                    |
| - member_id: str               |
| - borrowed_books: List<Book>   |
+--------------------------------+
| + borrow_book(book: Book): str |
| + return_book(book: Book): str |
+--------------------------------+

Explanation of the UML
----------------------
Library Class:
    Attributes: books (a list of Book objects), members (a list of Member objects).
    Methods: add_book to add a new book, add_member to add a new member.
Book Class:
    Attributes: title, author, isbn, is_checked_out (a boolean indicating if the book is checked out).
    Methods: check_out to mark the book as checked out, return_book to mark the book as returned.
Member Class:
    Attributes: name, member_id, borrowed_books (a list of Book objects the member has borrowed).
    Methods: borrow_book to borrow a book, return_book to return a book.    
"""
import sys #impoting sys library to allow the user to exit the program by typing exit program in the main menu.

class Library:

    def __init__(self):
        self.books = [] # a list of Book objects owned by the library.
        self.members = [] # a list of member objects of the library.

    def add_book(self, book):
        self.books.append(book) # adds a new book to the list of books owned by the library.
        for book in self.books: # prints the updated list of books owned by the library.
            print(f"- {book.title} {book.isbn} {book.author}")

    def add_member(self, member):
        self.members.append(member) # adds a new member to the list of member of the library.
        for member in self.members: # prints the updated list of the members of the library.
            print(f"- {member.name} {member.member_id} ")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False #a boolean indicating if the book is checked out

    def check_out(self):
        self.is_checked_out = True # labels the book as checked out from the library.
        print("book is checked out")

    def return_book(self):
        self.is_checked_out = False # labels the book as returned to the library.
        print("book returned")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = [] # a unique list for each member showing each book he is currently borrowing.

    def borrow_book(self, library, isbn):
        for book in library.books:
            if book.isbn == isbn: # check if the input isbn exists in one of the books owned by the library
                if book.is_checked_out: # checks weather the book is already checked out
                    print("book is already checked out")
                    return
                self.borrowed_books.append(book) # adds the book to the list of books that the member is currently borrowing
                book.check_out() # calls the check_out method in the Book class to label this book as checked out from the library.
                for borrowed_book in self.borrowed_books: # print the updated list of books that the member is currently borrowing.
                    print(f"- {borrowed_book.title}")
                return
        print("Book dont exist.")

    def return_book(self, library, isbn):
        for book in library.books:
            if book.isbn == isbn: # check if the input isbn exists in one of the books owned by the library
                if book.is_checked_out == False: # checks if the book is not checked out
                    print("book is not checked out")
                    return
                self.borrowed_books.remove(book) # removes the book from the list of books that the member is currently borrowing
                book.return_book() # calls the return_book method in the Book class to label this book as returned to the library.
                for borrowed_book in self.borrowed_books: # print the updated list of books that the member is currently borrowing.
                    print(f"- {borrowed_book.title}")
                return
        print("Book dont exist.")

def main():
    library = Library() # creates a library object from the Library class
    while True:
        user_options = ["add new", "borrow/return", "exit program"]
        add_new_options = ["book", "member"]
        borrow_or_return_options = ["borrow", "return"]
        user_request = user_prompt(user_options) # calls the user_prompt function to as the user for an option
        if user_request == user_options[0]: # if the user chooses the first option (add new) in the user_options list
            add_new_request = user_prompt(add_new_options) # calls the user_prompt function to as the user for an option
            if add_new_request == add_new_options[0]: # if the user chooses the first option (book) in the add_new_options list
                new_book_title = input("Enter the new books' title: ")
                new_book_author = input("Enter the new books' author: ")
                new_book_isbn = input("Enter the new books' isbn: ")
                new_book = Book(new_book_title, new_book_author, new_book_isbn) # creating a new_book object from the Book class
                library.add_book(new_book) # calls the add_book method from the Library class to add a new book to the list of books owned by the library
            elif add_new_request == add_new_options[1]: # if the user chooses the second option (member) in the add_new_options list
                new_member_name = input("Enter the new members' name: ")
                new_member_id = input("Enter the new members' ID: ")
                new_member = Member(new_member_name, new_member_id) # creating a new_member object from the Member class
                library.add_member(new_member) # calls the add_member method from the Library class to add a new member to the list of the library members
        elif user_request == user_options[1]: # if the user chooses the second option (borrow/return) in the user_options list
            borrow_or_return_request = user_prompt(borrow_or_return_options) # calls the user_prompt function to as the user for an option
            if borrow_or_return_request == borrow_or_return_options[0]: # if the user chooses the first option (borrow) in the borrow_or_return_options list
                member_id = input("Enter the members' ID: ")
                isbn = input("Enter the members' ISBN: ")
                for member in library.members:
                    if member.member_id == member_id: # check if the input member_id exists in one of the members of the library
                        member.borrow_book(library, isbn) # calls the borrow_book method from the Member class to add the book to the list of books that the member is currently borrowing
                    else:
                        print("Member dont exist")
            elif borrow_or_return_request == borrow_or_return_options[1]: # if the user chooses the second option (return) in the borrow_or_return_options list
                member_id = input("Enter the members' ID: ")
                isbn = input("Enter the members' ISBN: ")
                for member in library.members:
                    if member.member_id == member_id: # check if the input member_id exists in one of the members of the library
                        member.return_book(library, isbn) # calls the borrow_book method from the Member class to remove the book to the list of books that the member is currently borrowing
                    else:
                        print("Member dont exist")
        elif user_request == user_options[2]: # if the user chooses the third option (exit program) in the user_options list
            sys.exit() # exists the program

def user_prompt(list_options):

    """
    This function asks the user which option he wants and checks weather that option exists in the list of available options or not.
    If the option exists: the selected option will be returned and the function will end
    If the option doesn't exist: a value error will be raised and the user will be asked to input the option he wants again.
    """
    while True:
        try:
            selected_option = input(f"Select an option: {' '.join(f'{k} ' for k in list_options)} ")
            if selected_option in list_options:
                return selected_option
            else:
                raise ValueError
        except ValueError:
            print("select one of the available options")

if __name__ == '__main__':
    main()