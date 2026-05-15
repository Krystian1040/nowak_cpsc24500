"""
catalog.py - Week 8 Starter

The Catalog class uses the SINGLETON pattern. Only one Catalog ever exists.

Singleton pattern in Python: override __new__.
- Use a class variable _instance = None
- The first call to Catalog() creates and stores the instance
- Every later call returns the same instance

IMPORTANT: only initialize the items list inside the `if cls._instance is None` block,
otherwise calling Catalog() a second time will wipe your data.

Methods:
- add_item(item)
- remove_item(title)              case-insensitive
- search_by_title(keyword)        case-insensitive partial match
- search_by_author(keyword)       case-insensitive partial match
- get_all_items()                 sorted by title
- get_checked_out_items()
- get_available_items()
"""


class Catalog:

    _instance = None

    def __new__(cls):
        # TODO: if cls._instance is None: create the instance and initialize ._items = []
        # TODO: return cls._instance
        pass

    def add_item(self, item):
        # TODO
        pass

    def remove_item(self, title):
        # TODO: remove items whose title matches (case-insensitive)
        pass

    def search_by_title(self, keyword):
        # TODO: return items where keyword is in the title (case-insensitive)
        pass

    def search_by_author(self, keyword):
        # TODO: return items where keyword is in the author (case-insensitive)
        pass

    def get_all_items(self):
        # TODO: return a sorted list (uses LibraryItem.__lt__)
        pass

    def get_checked_out_items(self):
        # TODO
        pass

    def get_available_items(self):
        # TODO
        pass
