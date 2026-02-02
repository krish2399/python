items = [
    ("item1", 10),
    ("item2", 9),
    ("item3", 12),
]

filtered_list = list(filter(lambda item: item[1] <= 10, items))
print(filtered_list)


cars = [
    ("scorpio", 20_00_000),
    ("defender", 84_00_000),
    ("swift", 3_50_000)
]

filtered_car = list(filter(lambda car: car[1] <= 84_00_000, cars))
print(filtered_car)
