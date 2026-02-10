from collections import namedtuple

Point = namedtuple("point", ['x', 'y'])
p1 = Point(x=2, y=3)
p1 = Point(x=20, y=30)
p2 = Point(x=2, y=3)

print(p1 == p2)
