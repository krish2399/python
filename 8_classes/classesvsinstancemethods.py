# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls): # for the pass value
#         return cls(0, 0)

#     def draw(self):   #for print
#         print(f"Point {self.x},{self.y}")


# point = Point.zero()
# point.draw()


# class MyName:
#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname

#     @classmethod
#     def value(cls):
#         return cls("Krish", "gujarati")

#     def pri(self):
#         print(f"{self.firstname} {self.lastname}")


# name = MyName.value()
# name.pri()


class MyCars:
    def __init__(self, firstcar, secondcar, thirdcar):
        self.firstcar = firstcar
        self.secondcar = secondcar
        self.thirdcar = thirdcar

    @classmethod
    def valuecar(cls):
        return cls("Scoripo Classic S11", "BMW M5 Compititon ", "Defender Octa")

    def showcar(self):
        print(
            f"My first car is {self.firstcar}\nMy Second car is {self.secondcar} \nMy Third car is {self.thirdcar} ")


allcars = MyCars.valuecar()
allcars.showcar()
