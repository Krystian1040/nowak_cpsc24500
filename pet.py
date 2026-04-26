#Assignment #5- Pet Simulator
# Pet class
#Christian Nowak
#OOP


class Pet:

    #Pet info 
    def __init__(self, name, species):
        self._name = name
        self._species = species
        self._hunger = 50
        self._happiness = 50
        self._energy = 50

    # Hunger level
    def feed(self):
        self._hunger -= 10
        if self._hunger < 0:
            self._hunger = 0
        return f"{self._name} has been fed."

    #Happiness/enegry usage
    def play(self):
        self._happiness += 10
        self._energy -= 10

        if self._happiness > 100:
            self._happiness = 100
        if self._energy < 0:
            self._energy = 0

        return f"You played with {self._name}."

    #Restores energy
    def sleep(self):
        self._energy += 15
        if self._energy > 100:
            self._energy = 100
        return f"{self._name} took a nap."

    #Pet Status
    def status(self):
        return (
            f"{self}\n"
            f"Hunger: {self._hunger}\n"
            f"Happiness: {self._happiness}\n"
            f"Energy: {self._energy}"
        )

    def __str__(self):
        return f"{self._name} the {self._species}"
    

