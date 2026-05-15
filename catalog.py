#Assignment #8- Library Catalog System
#Catalog.py
#Christian Nowak
#OOP

from library_item import LibraryItem


class Catalog:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Catalog, cls).__new__(cls)
            cls._instance._items = []
        return cls._instance

    def add_item(self, item):
        if not isinstance(item, LibraryItem):
            raise TypeError("Only LibraryItem objects can be added to the catalog.")
        self._items.append(item)

    def remove_item(self, title):
        original_count = len(self._items)

        self._items = [
            item for item in self._items
            if item.title.lower() != title.lower()
        ]

        return original_count - len(self._items)

    def search_by_title(self, keyword):
        return [
            item for item in self._items
            if keyword.lower() in item.title.lower()
        ]

    def search_by_author(self, keyword):
        return [
            item for item in self._items
            if keyword.lower() in item.author.lower()
        ]

    def get_all_items(self):
        return sorted(self._items)

    def get_checked_out_items(self):
        return [
            item for item in self._items
            if item.checked_out
        ]

    def get_available_items(self):
        return [
            item for item in self._items
            if not item.checked_out
        ]