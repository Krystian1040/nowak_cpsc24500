#Assignment #5- Pet Simulator
# Cat class
#Christian Nowak
#OOP

from pet import Pet


class Cat(Pet):

    def __init__(self, name):
        super().__init__(name, "Cat")

    # Cat Hunger 
    def feed(self):
        self._hunger -= 8
        self._happiness += 3

        if self._hunger < 0:
            self._hunger = 0
        if self._happiness > 100:
            self._happiness = 100

        return f"{self._name} eats the cat food."

    #Cat plays => happier
    def play(self):
        self._happiness += 12
        self._energy -= 8

        if self._happiness > 100:
            self._happiness = 100
        if self._energy < 0:
            self._energy = 0

        return f"{self._name} plays with a toy mouse."

    #Unique class
    def purr(self):
        return f"{self._name} purrs softly."