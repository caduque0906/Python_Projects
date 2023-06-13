
#importing abstract method
from abc import ABC, abstractmethod

#parent class
class Pokemon(ABC):
    def Pikachu(self, move):
        print("Pikachu's strongest attack is ", move)

    #passing argument for child class
    def Raichu(self, move):
        pass

#child class
class Evolution(Pokemon):

    #defining earlier argument from parent class Pokemon
    def Raichu(self, move):
        print("Raichu is the evolution of Pikachu. It's strongest attack is {}".format(move))

obj = Evolution()
obj.Pikachu("Wild Charge")
obj.Raichu("Volt Swtich")
