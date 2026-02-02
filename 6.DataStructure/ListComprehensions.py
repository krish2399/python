items = [
    ("item1", 10),
    ("item2", 9),
    ("item3", 12),
]

# prices = list(map(lambda item: item[1], items))
prieces = [item[1] for item in items]
print(prieces)


# filtered = list(filter(lambda item: item[1] <= 10, items))
filterd = [item for item in items if item[1] <= 10]
print(filterd)
