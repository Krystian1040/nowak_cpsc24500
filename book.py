#Assignment #8- Library Catalog System
#Book.py
#Christian Nowak
#OOP

from library_item import LibraryItem


class Book(LibraryItem):

    def __init__(self, title, author, year, isbn, page_count, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self._isbn = isbn
        self._page_count = int(page_count)

    @property
    def isbn(self):
        return self._isbn

    @property
    def page_count(self):
        return self._page_count

    def get_item_type(self):
        return "Book"

    def __str__(self):
        return super().__str__() + f" | ISBN: {self.isbn}, Pages: {self.page_count}"