try:
    age = int(input("Enter Your Age: "))
    print(age)
    xfac = 10/age
except (ValueError, ZeroDivisionError):
    print("You didn't enter the valid age.")
else:
    print("No excaption were thrwon")
