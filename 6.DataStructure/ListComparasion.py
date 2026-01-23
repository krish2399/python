items = [
    ("item1", 10),
    ("item2", 9),
    ("item3", 12),
]

price = list(filter(lambda item: item[1] >= 10, items))

print(price)
