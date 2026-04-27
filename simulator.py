#Assignment #5- Pet Simulator
#Simulator
#Christian Nowak
#OOP

from cat import Cat
from dog import Dog
from fish import Fish

#Pet Type
def adopt_pet(pets):
    print("1. Cat")
    print("2. Dog")
    print("3. Fish")

    choice = input("Choose a pet: ")

    if choice == "1":
        name = input("Enter cat name: ")
        pet = Cat(name)

    elif choice == "2":
        name = input("Enter dog name: ")
        breed = input("Enter dog breed: ")
        pet = Dog(name, breed)

    elif choice == "3":
        name = input("Enter fish name: ")
        pet = Fish(name)

    else:
        print("Invalid choice.")
        return

    pets.append(pet)
    print("Pet adopted.")

#Pet selection
def select_pet(pets):
    if len(pets) == 0:
        print("No pets adopted yet.")
        return None

    for i in range(len(pets)):
        print(str(i + 1) + ". " + str(pets[i]))

    choice = int(input("Choose pet number: "))

    if choice < 1 or choice > len(pets):
        print("Invalid pet.")
        return None

    return pets[choice - 1]


def main():
    pets = []

    #Main Menu
    while True:
        print("\nPet Simulator")
        print("1. Adopt a pet")
        print("2. Feed a pet")
        print("3. Play with a pet")
        print("4. Put a pet to sleep")
        print("5. View all pets")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            adopt_pet(pets)

        elif choice == "2":
            pet = select_pet(pets)
            if pet != None:
                print(pet.feed())  # polymorphism

        elif choice == "3":
            pet = select_pet(pets)
            if pet != None:
                print(pet.play())

        elif choice == "4":
            pet = select_pet(pets)
            if pet != None:
                print(pet.sleep())

        elif choice == "5":
            # show all pets
            for pet in pets:
                print()
                print(pet.status())

        elif choice == "6":
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()