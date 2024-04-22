#/usr/bin/python3

"""
Given a Book class and a Solution class, write a MyBook class that does the following:
. Inherits from Book
. Has a parameterized constructor taking these 3 parameters:
    1. string, title
    2. string, author
    3. int price

. Implements the Book class abstruct() method so it prints these 3 lines:
    1. title, a space and then current instance's title.
    2. author, a space then the current instance's author.
    3. price, a space then the current instance's price.

N/B: Because these classes have been written  in the same file, you must not use an access modifiers
(eg. public). when declaring Mybook or your code will not work.
"""

from abc import ABCMeta, abstractmethod

class Book(object, metaClass = ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    @abstractmethod
    def display(): pass        

class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title, author)
        self.price = price

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()