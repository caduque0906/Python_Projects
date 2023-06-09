# Parent class
class Vehicle:

    brand = ""
    model = ""

    def __init__ (self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print(self.brand + " " + self.model)

#child class
class Car(Vehicle):

    # Attributes for child class
    commuteStyle = "ground"
    doorNum = "4"

    # adding string value to attribute
    def move(self):
        print("This vehicle is a car. It is a " + self.model + ", " + self.brand + ". \nNumber of door: " + self.doorNum + "\nIt can only travel in the " + self.commuteStyle + ".")

#child class
class Plane(Vehicle):

    commuteStyle = "sky"
    wingNum = "2"
    
    def move(self):
        print("This vehicle is a plane. It is a " + self.model + ", " + self.brand + ". \nNumber of wings: " + self.wingNum + "\nIt can only travel in the " + self.commuteStyle + ".")


car1 = Car("Ford", "Mustang")
plane1 = Plane("Boeing", "747")


print(car1.move())
print(plane1.move())


