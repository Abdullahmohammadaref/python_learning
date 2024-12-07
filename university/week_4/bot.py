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

    def borrow_book(self, library, book_isbn):
        for book in library.books:
            if book.isbn == book_isbn:
                if book.is_checked_out:
                    print("book is already checked out")
                    return
                self.borrowed_books.append(book)
                book.check_out()
                for borrowed_book in self.borrowed_books:
                    print(f"- {borrowed_book.title}")
                return
        print("Book or member dont exist.")

    def return_book(self, library, book_isbn):
        for book in library.books:
            if book.isbn == book_isbn:
                self.borrowed_books.remove(book)
                book.return_book()
                for borrowed_book in self.borrowed_books:
                    print(f"- {borrowed_book.title}")
                return
        print("Book or member dont exist.")

def user_prompt(list_options):
    while True:
        try:
            selected_option = input(f"Select an option: {' '.join(f'{k} ' for k in list_options)} ")
            for option in list_options:
                if selected_option in list_options:
                    return selected_option
                elif selected_option in option:
                    return option
                else:
                    raise ValueError
        except ValueError:
            print("select one of the available options")

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
                member_id = input("Enter the new members' ID: ")
                isbn = input("Enter the new members' ISBN: ")
                for member in library.members:
                    if member.member_id == member_id:
                        member.borrow_book(library, isbn)
            elif borrow_or_return_request == borrow_or_return_options[1]:
                member_id = input("Enter the new members' ID: ")
                isbn = input("Enter the new members' ISBN: ")
                for member in library.members:
                    if member.member_id == member_id:
                        member.return_book(library, isbn)
        elif user_request == user_options[2]:
            sys.exit()
if __name__ == '__main__':
    main()

"""

"""
import sys

num = 2
if num <= 1:
    print("Not prime")
    sys.exit()
for i in range(2, num):
    if num % i == 0:
        print("Not prime")
        sys.exit()
print("prime")
"""
"""
// C Program to check for prime number using
//  Simple Trial Division
#include <stdbool.h>
#include <stdio.h>

int main() {
    int n = 29;

    int cnt = 0;

    // If number is less than/equal to 1,
    // it is not prime
    if (n <= 1)
        printf("%d is NOT prime\n", n);
    else {

        // Check for divisors from 1 to n
        for (int i = 1; i <= n; i++) {

            // Check how many number is divisible
            // by n
            if (n % i == 0)
                cnt++;
        }

        // If n is divisible by more than 2 numbers
        // then it is not prime
        if (cnt > 2)
            printf("%d is NOT prime\n", n);

        // else it is prime
        else
            printf("%d is prime", n);
    }

    return 0;
}
"""
"""
import time

def main():
    time_start = time.time()
    hallo()
    time_end = time.time()
    time_elapsed = time_end - time_start
    print(time_elapsed)

def hallo():
    time.sleep(10)

if __name__ == "__main__":
    main()
"""
import numpy as np
import cv2
import matplotlib.pyplot as plt

original_array = np.array([9,5,2,4,2,8,5])
cumlative_array = np.zeros(len(max(original_array)))
print(cumlative_array)

