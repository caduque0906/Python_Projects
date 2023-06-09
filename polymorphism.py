# Parent class
class Vehicle:

    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

#child class
class Car(Vehicle):
    def move(self):
        commuteStyle = "Ground"
        doorNum = 4

#child class
class Plane(Vehicle):
    def move(self):
        commuteStyle = "Sky"
        doorNum = 6

car1 = Car("Ford", "Mustang")
plane1 = Plane("Boeing", "747")

for x in (car1, plane1):
    print(x.brand)
    print(x.model)
    x.move()


