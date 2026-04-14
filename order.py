#Assignment#3 - Starlight Coffee POS - order
#Christian Nowak
#OOP 

#Order class
class Order:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    #Add item
    def add_item(self, item):
        self.items.append(item)

    #Remove item
    def remove_item(self, index):
        if index >= 0 and index < len(self.items):
            self.items.pop(index)
        else:
            print("Invalid item number.")

    #Get subtotal
    def subtotal(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    #Get tax
    def tax(self):
        return self.subtotal() * 0.0875

    #Get total
    def total(self):
        return self.subtotal() + self.tax()

    #Print receipt
    def __str__(self):
        output = "\n" + "=" * 40 + "\n"
        output += "STARLIGHT COFFEE RECEIPT".center(40) + "\n"
        output += "=" * 40 + "\n"
        output += f"Customer: {self.customer_name}\n"
        output += "-" * 40 + "\n"

        count = 1
        for item in self.items:
            output += f"{count}. {item.name} ({item.size}) - ${item.price:.2f}\n"
            count += 1

        output += "-" * 40 + "\n"
        output += f"Subtotal: ${self.subtotal():.2f}\n"
        output += f"Tax (8.75%): ${self.tax():.2f}\n"
        output += f"Total: ${self.total():.2f}\n"
        output += "=" * 40 + "\n"

        return output