#Assignment 2 Fortune_Teller
#Christian Nowak
#OOP

import random

#Welcome banner
def print_banner():
    print("*" * 50)
    print("*        CHRIS'S FORTUNE TELLER       *")
    print("*     Discover what the stars hold!   *")
    print("*" * 50)

#age function
def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                return age
            else:
                print("Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")

#fortune category #/color
def get_fortune_category(lucky_number, favorite_color):
    if 1 <= lucky_number <= 3:
        return f"Patience with a touch of {favorite_color.lower()}"
    elif 4 <= lucky_number <= 6:
        return f"Adventure guided by {favorite_color.lower()}"
    else:
        return f"Prosperity shining in {favorite_color.lower()}"

def main():
    