""" items = [
    ("product1", 400),
    ("product2", 700),
    ("product3", 900),
    ("product4", 600)
]
items.sort(key= lambda item: item[1])

print(items)
 """


bike = [
    ("bullet", 120000),
    ("splendor", 45000),
    ("GT650", 500000)
]
# bike.sort(key=lambda bike: bike[1], reverse=True)
# print(bike)

print(sorted(bike, key=lambda bike: bike[1]))
