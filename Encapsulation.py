#Start Encapsulation
class Protected:

    def __init__(self):
        #protected. Note the single underscore
        self._protectedVar = 0

#End Encapsulation

obj = Protected()
obj._protectedVar = 100
print(obj._protectedVar)

class Private:

    #private. Note the double underscore
    __privateVar = 6
    print (__privateVar)
