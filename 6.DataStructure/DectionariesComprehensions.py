value = []
for x in range(5):
    value.append(x*2)


print(value)

# [expression for item in items]

""" values = [x*2 for x in range(5)]
print(values) """

""" value = {x*2 for x in range(5)}
print(value) """

""" values = {x: x*2 for x in range(5)}
print(values) """

value = (x*2 for x in range(5))
print(value)
