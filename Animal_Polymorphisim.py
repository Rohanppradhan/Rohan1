class Animal:
    def getNameoftheanimal(self):
        return 0
class Dog(Animal):
    def getNameoftheanimal(self):
        print("The animal is a  dog")
class Lion(Animal):
    def getNameoftheanimal(self):
        print("The animal is a lion")
class Cat(Animal):
    def getNameoftheanimal(self):
        print("The animal is a cat")
class Cow(Animal):
    def getNameoftheanimal(self):
        print("The animal is cow")

A=Animal()
A=Dog()
A.getNameoftheanimal()
A=Lion()
A.getNameoftheanimal()
A=Cat()
A.getNameoftheanimal()
A=Cow()
A.getNameoftheanimal()



