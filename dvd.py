#Assignment #8- Library Catalog System
#Dvd.py
#Christian Nowak
#OOP

from library_item import LibraryItem


class DVD(LibraryItem):

    def __init__(self, title, author, year, runtime_minutes, rating, checked_out=False):
        super().__init__(title, author, year, checked_out)
        self._runtime_minutes = int(runtime_minutes)
        self._rating = rating

    @property
    def runtime_minutes(self):
        return self._runtime_minutes

    @property
    def rating(self):
        return self._rating

    def get_item_type(self):
        return "DVD"

    def __str__(self):
        return super().__str__() + f" | Runtime: {self.runtime_minutes} min, Rating: {self.rating}"