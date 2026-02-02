""" numbers = [3, 2, 23, 423, 423]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)
 """


""" items = [
    ("product1", 1200),
    ("product2", 700),
    ("product3", 800),
    ("product4", 200)
]


def sort_item(items):
    return items[1]


items.sort(key=sort_item)
print(items)
 """


bike = [
    ("bullet", 120000),
    ("splendor", 45000),
    ("GT650", 500000)
]


def bike_price(bike):
    return bike[1]


# bike.sort(key=bike_price)
# print(bike)


print(sorted(bike, key=bike_price))
