""" numbers = [1, 2, 3, 4, 5, 6, 6, 7]

first, second, third = numbers

first = numbers[0]

print(numbers)
 """

numbers = [1, 2, 3, 4, 5, 6, 7, 9]
first, *others, last = numbers
print(first, last)
print(others)
