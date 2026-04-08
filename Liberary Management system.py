# Add a method search_book(title)
#
# If book exists → print details
# If not → print “Book not found”

#Liberary Management system

class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._isborrowed = False
    def borrow(self):
        if not self._isborrowed:
            self._isborrowed = True
            return True
        return False
    def return_book(self):
        if self._isborrowed:
            self._isborrowed = False
            return True
        return False
    def __str__(self):
        status="Avilable" if not self._isborrowed else "borrowed"
        return f"{self._title} by {self._author} {status}"
class Library:
    def __init__(self):
        self._books = []
    def add_book(self,title,author):
        book = Book(title,author)
        self._books.append(book)
    def show_books(self):
        if not self._books:
            print("No books in library")
            return
        for i,book in enumerate(self._books,1):
            print(f"{i}. {book}")
    def borrow(self,title):
        for book in self._books:
            if book._title.lower() == title.lower():
                if book.borrow():
                    print(f"{book._title} borrowed")
                else:
                    print(f"sorry{book._title}is not avilable")
                return
        print("book not found")
    def return_book(self,title):
        for book in self._books:
            if book._title.lower() == title.lower():
                if book.return_book():
                    print(f"you returned{book._title} ")
                else:
                    print(f"{book._title} is not borrowed")
                return
        print("book not found")
    def search_book(self,title):
        for book in self._books:
            if book._title.lower() == title.lower():
                print(f"{book._title} is avilable")
            else:
                print(f"{book._title} is not avilable")
            return
lib=Library()
title=input("enter book title: ")
author=input("enter book author: ")
lib.add_book(title, author)
lib.add_book("Atomic Habits", "James Clear")
lib.add_book("Python Basics", "John Doe")
print("all Books:")
lib.show_books()
print("borrw Harry Potter")
lib.borrow("Harry Potter")
print("after borrowing Harry Potter")
lib.show_books()
print("return Harry Potter")
lib.return_book("Harry Potter")
lib.show_books()
print("search python Basics")
lib.search_book("Python Basics")







