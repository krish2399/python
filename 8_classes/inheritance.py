class Animal():
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")
# Animal : parent base
# mammal :child base


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)
