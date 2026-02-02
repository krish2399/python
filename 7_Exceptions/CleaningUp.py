try:
    file = open("CleaningUp.py")
    age = int(input("Enter your age "))
    print(age)
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("you didn't enter a vaild age")
else:
    print("no exception were there")
finally:
    file.close()
