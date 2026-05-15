#Assignment #8- Library Catalog System
#Main.py
#Christian Nowak
#OOP

from catalog import Catalog
from catalog_view import CatalogView
from item_factory import ItemFactory


DATA_FILE = "data/catalog.tsv"


def string_to_bool(value):
    return value.strip().lower() == "true"


def bool_to_string(value):
    if value:
        return "true"
    return "false"


def load_catalog(filename, catalog):
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("\t")

                if len(parts) != 7:
                    print(f"Skipping bad line: {line}")
                    continue

                item_type = parts[0]
                title = parts[1]
                author = parts[2]
                year = parts[3]
                extra1 = parts[4]
                extra2 = parts[5]
                checked_out = string_to_bool(parts[6])

                item = ItemFactory.create_item(
                    item_type,
                    title,
                    author,
                    year,
                    extra1,
                    extra2,
                    checked_out
                )

                catalog.add_item(item)

        print(f"Catalog loaded: {len(catalog.get_all_items())} items.")

    except FileNotFoundError:
        print("Catalog file was not found. Starting with an empty catalog.")

    except Exception as error:
        print(f"Error loading catalog: {error}")


def save_catalog(filename, catalog):
    try:
        with open(filename, "w") as file:
            for item in catalog.get_all_items():
                item_type = item.get_item_type()

                if item_type == "Book":
                    line = [
                        item_type,
                        item.title,
                        item.author,
                        str(item.year),
                        item.isbn,
                        str(item.page_count),
                        bool_to_string(item.checked_out)
                    ]

                elif item_type == "DVD":
                    line = [
                        item_type,
                        item.title,
                        item.author,
                        str(item.year),
                        str(item.runtime_minutes),
                        item.rating,
                        bool_to_string(item.checked_out)
                    ]

                elif item_type == "Magazine":
                    line = [
                        item_type,
                        item.title,
                        item.author,
                        str(item.year),
                        str(item.issue_number),
                        item.month,
                        bool_to_string(item.checked_out)
                    ]

                else:
                    continue

                file.write("\t".join(line) + "\n")

        print("Catalog saved. Goodbye!")

    except Exception as error:
        print(f"Error saving catalog: {error}")


def find_exact_title(catalog, title):
    for item in catalog.get_all_items():
        if item.title.lower() == title.lower():
            return item

    return None


def add_new_item(catalog):
    item_type = input("Item type (Book/DVD/Magazine): ")
    title = input("Title: ")
    author = input("Author: ")

    try:
        year = int(input("Year: "))

        if item_type.lower() == "book":
            isbn = input("ISBN: ")
            page_count = int(input("Page count: "))

            item = ItemFactory.create_item(
                item_type,
                title,
                author,
                year,
                isbn,
                page_count,
                False
            )

        elif item_type.lower() == "dvd":
            runtime_minutes = int(input("Runtime minutes: "))
            rating = input("Rating: ")

            item = ItemFactory.create_item(
                item_type,
                title,
                author,
                year,
                runtime_minutes,
                rating,
                False
            )

        elif item_type.lower() == "magazine":
            issue_number = int(input("Issue number: "))
            month = input("Month: ")

            item = ItemFactory.create_item(
                item_type,
                title,
                author,
                year,
                issue_number,
                month,
                False
            )

        else:
            print("Invalid item type.")
            return

        catalog.add_item(item)
        print(f"Added: {title}")

    except ValueError:
        print("Invalid number entered. Item was not added.")

    except Exception as error:
        print(f"Error adding item: {error}")


def main():
    catalog = Catalog()
    view = CatalogView()

    load_catalog(DATA_FILE, catalog)

    running = True

    while running:
        view.display_menu()
        choice = input("Enter choice: ")

        try:
            if choice == "1":
                print("--- All Items (sorted by title) ---")
                view.display_items(catalog.get_all_items())

            elif choice == "2":
                query = input("Enter title to search: ")
                results = catalog.search_by_title(query)
                view.display_search_results(results, query)

            elif choice == "3":
                query = input("Enter author to search: ")
                results = catalog.search_by_author(query)
                view.display_search_results(results, query)

            elif choice == "4":
                title = input("Enter the exact title to check out: ")
                item = find_exact_title(catalog, title)

                if item is None:
                    print("Item not found.")
                else:
                    item.check_out()
                    print(f"Successfully checked out: {item.title}")

            elif choice == "5":
                title = input("Enter the exact title to check in: ")
                item = find_exact_title(catalog, title)

                if item is None:
                    print("Item not found.")
                else:
                    item.check_in()
                    print(f"Successfully checked in: {item.title}")

            elif choice == "6":
                add_new_item(catalog)

            elif choice == "7":
                print("--- Checked-Out Items ---")
                view.display_items(catalog.get_checked_out_items())

            elif choice == "8":
                save_catalog(DATA_FILE, catalog)
                running = False

            else:
                print("Invalid choice. Please enter a number from 1 to 8.")

        except RuntimeError as error:
            print(error)

        except Exception as error:
            print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()

