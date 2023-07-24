def my_name():
    print("My name is Ghadeer")


my_name()


def my_meal(food, drink):
    print(f"I like to eat {food} while drinking {drink}")


my_meal("fatayer", "chocolate milk")


def cube(number):
    return number ** 3


def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


print(cube(2))
print(by_three(3))
