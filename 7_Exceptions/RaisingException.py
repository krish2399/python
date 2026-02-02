def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("age cannot be 0 or less")
    return 10/age


try:
    result = calculate_xfactor(10)
except ValueError as error:
    print(error)
else:
    print(result)
