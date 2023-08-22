def add(*args):
    print(args[0])
    total = 0
    for number in args:
        total += number
    return total


print(add(1, 2, 3))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Honda", colour="Blue")
print(my_car.colour)
