#Assignment #8- Library Catalog System
#Library_item.py
#Christian Nowak
#OOP

from abc import ABC, abstractmethod


class LibraryItem(ABC):

    def __init__(self, title, author, year, checked_out=False):
        self._title = title
        self._author = author
        self._year = int(year)
        self._checked_out = checked_out

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @property
    def checked_out(self):
        return self._checked_out

    @abstractmethod
    def get_item_type(self):
        pass

    def check_out(self):
        if self._checked_out:
            raise RuntimeError("Item is already checked out")
        self._checked_out = True

    def check_in(self):
        if not self._checked_out:
            raise RuntimeError("Item is already available")
        self._checked_out = False

    def __lt__(self, other):
        return self.title.lower() < other.title.lower()

    def __str__(self):
        if self.checked_out:
            status = "CHECKED OUT"
        else:
            status = "AVAILABLE"

        return f"[{self.get_item_type()}] {self.title} by {self.author} ({self.year}) - {status}"
    