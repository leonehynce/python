class Animal:
    def speak(self):
        print(" Animal Barks")

class Dog(Animal):
    def eats(self):
        print("the dog eats Bones")

class Dogcharacter(Dog):
    def patrols(self):
        print("walks at night")
d=Dog()
d.eats()
d.speak()


