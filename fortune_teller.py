#Assignment 2 fortune_teller
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
        print_banner()

    name = input("Enter your full name: ").strip()
    age = get_valid_age()
    color = input("Enter your favorite color: ").strip()

    lucky_number = random.randint(1, 10)
    category = get_fortune_category(lucky_number, color)

    fortunes = [
        "Your mind is your greatest asset.",
        "The best prediction of future is the past.",
        "Miles are covered one step at a time.",
        "Happiness will bring you good luck.",
        "Fear and desire. Two sides of the same coin.",
        "An inch of time is an inch of gold.",
        "A friend is a present you give yourself.",
        "A light heart carries you through all the hard times."
    ]
    selected_fortune = random.choice(fortunes)
    lucky_percentage = (lucky_number / age) * 100

    print("\n" + "=" * 50)
    print("YOUR FORTUNE READING")
    print("=" * 50)
    print(f"Name: {name.upper()}")
    print(f"Name length: {len(name.strip())} characters")
    print(f"Age: {age}")
    print(f"Favorite color: {color.lower()}")
    print(f"Lucky number: {lucky_number}")
    print(f"Fortune category: {category}")
    print(f"Lucky percentage: {lucky_percentage:.3f}%")
    print(f'Your fortune: "{selected_fortune}"')
    print("=" * 50)
    