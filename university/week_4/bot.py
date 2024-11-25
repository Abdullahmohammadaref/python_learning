class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_out(self):
        if self.is_checked_out:
            return "Book is already checked out."
        self.is_checked_out = True
        return "Book checked out successfully."

    def return_book(self):
        if not self.is_checked_out:
            return "Book is not checked out."
        self.is_checked_out = False
        return "Book returned successfully."

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_checked_out:
            return "Book is not available."
        self.borrowed_books.append(book)
        book.check_out()
        return "Book borrowed successfully."

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.return_book()
            return "Book returned successfully."
        return "Book not found in borrowed books."

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")
        print("Current books:")
        for book in self.books:
            print(f"- {book.title} by {book.author} (ISBN: {book.isbn})")

    def add_member(self, member):
        self.members.append(member)
        print("Member added successfully.")
        print("Current members:")
        for member in self.members:
            print(f"- {member.name} (ID: {member.member_id})")

    def borrow_book(self, member_id, isbn):
        for member in self.members:
            if member.member_id == member_id:
                for book in self.books:
                    if book.isbn == isbn:
                        if book.is_checked_out:
                            print("Book is already checked out.")
                            return
                        member.borrow_book(book)
                        print("Book borrowed successfully.")
                        print(f"{member.name}'s borrowed books:")
                        for borrowed_book in member.borrowed_books:
                            print(f"- {borrowed_book.title}")
                        return
        print("Member or book not found.")

    def return_book(self, member_id, isbn):
        for member in self.members:
            if member.member_id == member_id:
                for book in member.borrowed_books:
                    if book.isbn == isbn:
                        member.return_book(book)
                        print("Book returned successfully.")
                        print(f"{member.name}'s borrowed books:")
                        for borrowed_book in member.borrowed_books:
                            print(f"- {borrowed_book.title}")
                        return
        print("Book not found in member's borrowed books.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        while True:
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            isbn = input("Enter ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
        elif choice == 2:
            name = input("Enter member name: ")
            member_id = input("Enter member ID: ")
            member = Member(name, member_id)
            library.add_member(member)
        elif choice == 3:
            member_id = input("Enter member ID: ")
            isbn = input("Enter ISBN of book to borrow: ")
            library.borrow_book(member_id, isbn)
        elif choice == 4:
            member_id = input("Enter member ID: ")
            isbn = input("Enter ISBN of book to return: ")
            library.return_book(member_id, isbn)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
