#Assignment #5- Pet Simulator
#Fish class
#Christian Nowak
#OOP

from pet import Pet


class Fish(Pet):

    def __init__(self, name):
        super().__init__(name, "Fish")

    #Fish Hunger Level
    def feed(self):
        self._hunger -= 5

        if self._hunger < 0:
            self._hunger = 0

        return f"{self._name} eats fish flakes."

    #Fish plays(Happiness/Energy)
    def play(self):
        self._happiness += 6
        self._energy -= 3

        if self._happiness > 100:
            self._happiness = 100
        if self._energy < 0:
            self._energy = 0

        return f"{self._name} swims through the bubbles."

    #Overrides sleep (rest)
    def sleep(self):
        self._energy += 8

        if self._energy > 100:
            self._energy = 100

        return f"{self._name} rests in the water."