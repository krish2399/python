""" numbers = [1, 2, 3]
print(*numbers) """


""" values = list(range(5))
values = [*range(5), *"Hello"]
print(values) """

""" import math
first = {"x": 1}
second = {"x": 10, "y": 20}
combind = {**first, **second, "z": 1}
print(combind) """

cars = {"swift": 3_50_000, "scorpio": 20_000_000}
bikes = {"bullet": 1_20_000, "gt650": 5_00_000}

combine = {**cars, **bikes, "Defender": 15_000_000}
print(combine)
