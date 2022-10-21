class Employee:
    age = 0
    Name = " "
    Address = " "
    gender = " "

    def __init__(self,age,Name,Address,gender):
        self.age = age
        self.Name = Name
        self.Address = Address
        self.gender = gender
    def getEmployee(self):
        print("The Employee is: ",self.age, "----", self.Name, "----", self.Address, "-----", self.gender, "----")
    def __del__(self):
        print("The Employee Constructor is Deleted ")

class Keyboard:
    type = " "
    quality = " "
    brand = " "

    def __init__(self,type,quality,brand):
        self.type = type
        self.quality = quality
        self.brand = brand

    def getKeyboard(self):
        print("the keyboard is :", self.type, "----", self.quality, "---- ", self.brand)
    def __del__(self):
        print("The Keyboard constructor is deleted")

class Mouse:
    type = " "
    quality = " "
    brand = " "

    def __init__(self,type,quality,brand):
        self.type = type
        self.quality = quality
        self.brand = brand

    def getMouse(self):
        print("the mouse is :", self.type, "----", self.quality, "----", self.brand)
    def __del__(self):
        print("The Mouse constructor is deleted")

class Whiteboard:
    type = " "
    quality = " "
    brand = " "
    dimensions = 0

    def __init__(self,type,quality,brand,dimensions):
        self.type = type
        self.quality =quality
        self.brand = brand
        self.dimensions = dimensions

    def getWhiteboard(self):
        print("the whiteboard is :", self.type, "----", self.quality, "----", self.brand, "----", self.dimensions)
    def __del__(self):
        print("the Whiteboard constructor is deleted:")

Emp = Employee(20,"Rohan","cuttack","male")
Emp.getEmployee()

Key = Keyboard("optical","best quality","Logitech")
Key.getKeyboard()

Mou = Mouse("gaming","best quality","logitech")
Mou.getMouse()

Wb = Whiteboard("white","best quality","edu tech",192*177)
Wb.getWhiteboard()
