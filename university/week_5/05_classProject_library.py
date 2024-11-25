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
import sys

class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        for book in self.books:
            print(f"- {book.title} {book.isbn} {book.author}")

    def add_member(self, member):
        self.members.append(member)
        for member in self.members:
            print(f"- {member.name} {member.member_id} ")

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True
        print("book is checked out")

    def return_book(self):
        self.is_checked_out = False
        print("book returned")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, library, isbn):
        for book in library.books:
            if book.isbn == isbn:
                if book.is_checked_out:
                    print("book is already checked out")
                    return
                self.borrowed_books.append(book)
                book.check_out()
                for borrowed_book in self.borrowed_books:
                    print(f"- {borrowed_book.title}")
                return
        print("Book dont exist.")

    def return_book(self, library, isbn):
        for book in library.books:
            if book.isbn == isbn:
                if book.is_checked_out == False:
                    print("book is not checked out")
                    return
                self.borrowed_books.remove(book)
                book.return_book()
                for borrowed_book in self.borrowed_books:
                    print(f"- {borrowed_book.title}")
                return
        print("Book dont exist.")

def main():
    library = Library()
    while True:
        user_options = ["add new", "borrow/return", "exit program"]
        add_new_options = ["book", "member"]
        borrow_or_return_options = ["borrow", "return"]
        user_request = user_prompt(user_options)
        if user_request == user_options[0]:
            add_new_request = user_prompt(add_new_options)
            if add_new_request == add_new_options[0]:
                new_book_title = input("Enter the new books' title: ")
                new_book_author = input("Enter the new books' author: ")
                new_book_isbn = input("Enter the new books' isbn: ")
                new_book = Book(new_book_title, new_book_author, new_book_isbn)
                library.add_book(new_book)
            elif add_new_request == add_new_options[1]:
                new_member_name = input("Enter the new members' name: ")
                new_member_id = input("Enter the new members' ID: ")
                new_member = Member(new_member_name, new_member_id)
                library.add_member(new_member)
        elif user_request == user_options[1]:
            borrow_or_return_request = user_prompt(borrow_or_return_options)
            if borrow_or_return_request == borrow_or_return_options[0]:
                member_id = input("Enter the members' ID: ")
                isbn = input("Enter the members' ISBN: ")
                for member in library.members:
                    if member.member_id == member_id:
                        member.borrow_book(library, isbn)
                    else:
                        print("Member dont exist")
            elif borrow_or_return_request == borrow_or_return_options[1]:
                member_id = input("Enter the members' ID: ")
                isbn = input("Enter the members' ISBN: ")
                for member in library.members:
                    if member.member_id == member_id:
                        member.return_book(library, isbn)
                    else:
                        print("Member dont exist")
        elif user_request == user_options[2]:
            sys.exit()

def user_prompt(list_options):
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