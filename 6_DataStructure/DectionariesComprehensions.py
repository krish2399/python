value = []
for x in range(5):
    value.append(x*2)


print(value)

# [expression for item in items]

""" values = [x*2 for x in range(5)] #list
print(values) """

""" value = {x*2 for x in range(5)}  #set
print(value) """

values = {x: x*2 for x in range(5)}  # dectionarie have a key pair
print(values)

value = (x*2 for x in range(5))  # touple
print(value)
