try:
    with open("TheWithStatement.py") as file:
        print("file opended")
    age = int(input("Enter your age "))
    print(age)
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a vaild age")
else:
    print("no exception were there")
finally:
    file.close()
