class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"point: {self.x},{self.y}")


point = Point(1, 2)
point.draw()


class Cars:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def mycar(self):
        print(f"I have a {self.a}, {self.b}, {self.c}")


cars = Cars("Scorpio", "BMW M5", "Defender")
cars.mycar()
