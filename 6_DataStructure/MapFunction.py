""" items = [
    ("item1", 10),
    ("item2", 9),
    ("item3", 12),
]

x = map(lambda item: item[1], items)
for item in x:
    print(item) """


cars = [
    ("scorpio", 20_00_000),
    ("defender", 84_00_000),
    ("swift", 3_50_000)
]

prices = list(map(lambda car: car[1], cars))
print(prices)
