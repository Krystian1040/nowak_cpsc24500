##Assignment#3 - Starlight Coffee POS - main
#Christian Nowak
#OOP 

from menu_item import MenuItem
from order import Order

#Drink menu data
drinks = {
    1: ("Americano", 3.50),
    2: ("Cappuccino", 4.25),
    3: ("Espresso", 3.00),
    4: ("Latte", 4.75)
}

#Size options
sizes = {
    1: ("Small", 0.00),
    2: ("Medium", 0.75),
    3: ("Large", 1.25)
}

def main():
    print("*" * 40)
    print("*" + "STARLIGHT COFFEE POS".center(38) + "*")
    print("*" * 40)

    name = input("Enter your name: ")
    order = Order(name)

    #Enters Menu 
    while True:
        print("\n--- Drink Menu ---")
        for num, (drink, price) in drinks.items():
            print(f"{num}. {drink} - ${price:.2f}")

        drink_choice = int(input("Choose a drink (1-4): "))

        #Gets Sizes
        print("\n--- Sizes ---")
        for num, (size, upcharge) in sizes.items():
            print(f"{num}. {size} +${upcharge:.2f}")

        size_choice = int(input("Choose a size (1-3): "))

        drink_name, base_price = drinks[drink_choice]
        size_name, upcharge = sizes[size_choice]

        final_price = base_price + upcharge

        item = MenuItem(drink_name, size_name, final_price)
        order.add_item(item)

        print(f"Added: {item}")


        #Adds 4 choices
        while True:
            print("\n1. Add another drink")
            print("2. Remove a drink")
            print("3. View order")
            print("4. Check out")

            choice = input("Choice: ")

            if choice == "1":
                break

            elif choice == "2":
                print(order)
                index = int(input("Enter item number to remove: ")) - 1
                order.remove_item(index)

            elif choice == "3":
                print(order)

            elif choice == "4":
                print(order)
                print("Thank you! Enjoy your coffee.")
                return

            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
    