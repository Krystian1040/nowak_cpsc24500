#Assignment #8- Library Catalog System
#item_factory.py
#Christian Nowak
#OOP

from book import Book
from dvd import DVD
from magazine import Magazine


class ItemFactory:

    @classmethod
    def create_item(cls, item_type, title, author, year, *extras):
        item_type = item_type.lower()

        if item_type == "book":
            if len(extras) != 3:
                raise ValueError("Book requires ISBN, page count, and checked out status.")
            isbn = extras[0]
            page_count = extras[1]
            checked_out = extras[2]
            return Book(title, author, year, isbn, page_count, checked_out)

        elif item_type == "dvd":
            if len(extras) != 3:
                raise ValueError("DVD requires runtime, rating, and checked out status.")
            runtime_minutes = extras[0]
            rating = extras[1]
            checked_out = extras[2]
            return DVD(title, author, year, runtime_minutes, rating, checked_out)

        elif item_type == "magazine":
            if len(extras) != 3:
                raise ValueError("Magazine requires issue number, month, and checked out status.")
            issue_number = extras[0]
            month = extras[1]
            checked_out = extras[2]
            return Magazine(title, author, year, issue_number, month, checked_out)

        else:
            raise ValueError("Unknown item type.")