"""
main.py - Week 8 Starter (Controller)

This is the controller. It coordinates the Catalog (model), CatalogView (view),
and ItemFactory (creation).

Flow:
1. Load data/catalog.tsv at startup (use ItemFactory.create_item for each row)
2. Show the menu and read the user's choice
3. Dispatch to the right action; delegate display to CatalogView
4. On "Save and quit", write the catalog back to the file in the same format
5. Wrap risky operations in try/except so the program never crashes

Menu:
1. List all items
2. Search by title
3. Search by author
4. Check out item
5. Check in item
6. Add new item
7. View checked-out items
8. Save and quit
"""

import os
from catalog import Catalog
from catalog_view import CatalogView
from item_factory import ItemFactory

DATA_FILE = os.path.join("data", "catalog.tsv")


def load_catalog(catalog, filename):
    # TODO: open the file (catch FileNotFoundError -- start with empty catalog)
    # TODO: for each line, split on tab
    # TODO: parse fields and call ItemFactory.create_item(...)
    # TODO: set the checked_out flag if the last field is "true"
    # TODO: catalog.add_item(item)
    pass


def save_catalog(catalog, filename):
    # TODO: open in write mode
    # TODO: for each item in catalog.get_all_items(), write a tab-delimited line
    #       in the same format as the input file
    pass


def add_item_interactive(catalog, view):
    # TODO: ask for type, title, author, year, then the type-specific fields
    # TODO: use ItemFactory.create_item(...) and catalog.add_item(item)
    # TODO: catch ValueError and show a friendly message via the view
    pass


def main():
    catalog = Catalog()
    view = CatalogView()

    load_catalog(catalog, DATA_FILE)
    view.display_message(f"Catalog loaded.")

    # TODO: menu loop
    pass


if __name__ == "__main__":
    main()
