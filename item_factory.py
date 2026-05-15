"""
item_factory.py - Week 8 Starter

ItemFactory uses the FACTORY pattern. The caller passes a string like "Book"
and the factory returns the right concrete subclass.

Tip: a dictionary mapping type strings to classes works well, but a simple
if/elif chain is also fine.

create_item(item_type, title, author, year, *extras)
- item_type: "Book", "DVD", or "Magazine" (case-insensitive)
- For Book, extras are: isbn, page_count
- For DVD, extras are: runtime_minutes, rating
- For Magazine, extras are: issue_number, month
- Raise ValueError for unknown types
"""

from book import Book
from dvd import DVD
from magazine import Magazine


class ItemFactory:

    @classmethod
    def create_item(cls, item_type, title, author, year, *extras):
        # TODO: lowercase item_type for comparison
        # TODO: dispatch on type, unpack extras into the right constructor
        # TODO: raise ValueError for unknown types
        pass
