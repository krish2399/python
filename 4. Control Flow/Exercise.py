# count = 0

# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"Total even number {count}")


even = 0
odd = 0

for number in range(1, 100):
    if number % 2 == 0:
        even += 1
        print(number)
print(f"total even number is {even}")

for number in range(1, 100):
    if number % 2 != 0:
        odd += 1
        print(number)
print(f"total odd number is {odd}")
