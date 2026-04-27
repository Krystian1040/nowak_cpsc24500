#Assignment #5- Pet Simulator
# Dog class
#Christian Nowak
#OOP

from pet import Pet


class Dog(Pet):

    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self._breed = breed 

    #Hunger level
    def feed(self):
        self._hunger = self._hunger - 15

        if self._hunger < 0:
            self._hunger = 0

        return self._name + " eats dog food."

    #Play (energy/happiness)
    def play(self):
        self._happiness = self._happiness + 15
        self._energy = self._energy - 12

        if self._happiness > 100:
            self._happiness = 100

        if self._energy < 0:
            self._energy = 0

        return self._name + " runs around."

    #Dog special instruction
    def fetch(self):
        return self._name + " fetches the ball."