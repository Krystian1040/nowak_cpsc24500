#Assignment#3 - Starlight Coffee POS - menu_item
#Christian Nowak
#OOP 


#Menu item class
class MenuItem:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    #Prints menu item
    def __str__(self):
        return f"{self.name} ({self.size}) - ${self.price:.2f}"
    