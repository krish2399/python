def mul(*number):
    total = 1
    for number in number:
        total *= number
    return total


print("start")
print(mul(2, 3, 4))
