class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point1 = Point(21, 34)
point2 = Point(32, 23)

sum = point1 + point2
print(sum.x)
