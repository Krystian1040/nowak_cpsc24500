#Assignment #8- Library Catalog System
#Magazine.py
#Christian Nowak
#OOP

from library_item import LibraryItem


class Magazine(LibraryItem):

    def __init__(self, title, author, year, issue_number, month, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self._issue_number = int(issue_number)
        self._month = month

    @property
    def issue_number(self):
        return self._issue_number

    @property
    def month(self):
        return self._month

    def get_item_type(self):
        return "Magazine"

    def __str__(self):
        return super().__str__() + f" | Issue: {self.issue_number}, Month: {self.month}"