"""
Problem Statement Found At: https://www.hackerrank.com/challenges/30-abstract-classes/problem
"""

# ####Begin Auto generated problem code.####
from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    @abstractmethod
    def display(self): pass
# ####End Auto generated problem code.####


# Write MyBook class
class MyBook(Book):
    def __init__(self, title: str, author: str, price: int) -> None:
        super().__init__(title, author)
        self.price = price

    def display(self) -> None:
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Price: {self.price}')
