#Assignment #8- Library Catalog System
#Catalog_view.py
#Christian Nowak
#OOP

class CatalogView:

    def display_items(self, items):
        if not items:
            print("No items found.")
        else:
            for item in items:
                print(item)

    def display_message(self, message):
        print(message)

    def display_menu(self):
        print()
        print("=============================")
        print("Library Catalog System")
        print("=============================")
        print("1. List all items")
        print("2. Search by title")
        print("3. Search by author")
        print("4. Check out item")
        print("5. Check in item")
        print("6. Add new item")
        print("7. View checked-out items")
        print("8. Save and quit")

    def display_search_results(self, items, query):
        print(f'--- Search Results for "{query}" ---')
        self.display_items(items)