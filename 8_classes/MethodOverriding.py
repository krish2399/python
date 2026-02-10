class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 2

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal constructor")
        self.weight = 4
        super().__init__()

    def walk():
        print("Walk")


m = Mammal()
print(m.age)
print(m.weights4)
