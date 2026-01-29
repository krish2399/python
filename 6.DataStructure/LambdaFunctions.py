item = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12)
]

item.sort(key=lambda item: item[1])
print(item)


bike = [
    ("bullet", 1_20_000),
    ("splendor", 1_00_000),
    ("GT650", 5_00_000)
]
print(bike[0])

""" bike.sort(key=lambda bike: bike[1])
print(bike) """
