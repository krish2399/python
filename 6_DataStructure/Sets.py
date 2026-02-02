number = [1, 2, 3, 3, 2, 1]
first = set(number)
second = {1, 4, 5, 6}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)


# second = {1, 4}
# second.add(5)
# print(second)


if 1 in first:
    print("yes")
