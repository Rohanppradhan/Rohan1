class Employee:
    age=0
    Name=" "
    Address=" "
    gender=" "
    def getEmployee(self):
        self.age=int(input("enter the age of the employee:"))
        self.Name=input("Enter the Employee's Name:")
        self.Address=input("Enter the adddress of the employee:")
        self.gender=input("Enter the gender of the employee:")
    def setEmployee(self):
        print(self.age,"----" ,self.Name,"----",self.Address,"-----",self.gender,"----")

class Keyboard:
    type=" "
    quality=" "
    brand=" "
    def getKeyboard(self):
        self.type = str(input("enter the type of the keyboard:"))
        self.quality = str(input("enter the quality of the keyboard:"))
        self.brand = str(input("enter the brand:"))
    def setKeyboard(self):
        print("the keyboard is :",self.type,"----",self.quality,"---- ",self.brand)

class Mouse:
    type=" "
    quality=" "
    brand=" "
    def getMouse(self):
        self.type = str(input("enter the type of the mouse:"))
        self.quality = str(input("enter the quality of the mouse:"))
        self.brand = str(input("enter the brand:"))
    def setMouse(self):
        print("the mouse is :",self.type,"----",self.quality,"----",self.brand)

class Whiteboard:
    type =" "
    quality =" "
    brand =" "
    dimensions=0
    def getWhiteboard(self):
        self.type = str(input("enter tthe type of whiteboard:"))
        self.quality = str(input("enter the quality of the whiteboard:"))
        self.brand = str(input("enter the brand:"))
        self.dimensions = int(input("enter the dimensions of the whiteboard:"))
    def setWhiteboard(self):
        print("the whiteboard is :",self.type,"----",self.quality,"----",self.brand,"----",self.dimensions)
Emp=Employee()
Emp.setEmployee()
Emp.getEmployee()

Key=Keyboard()
Key.setKeyboard()
Key.getKeyboard()

Mou=Mouse()
Mou.setMouse()
Mou.getMouse()

Wb=Whiteboard()
Wb.setWhiteboard()
Wb.getWhiteboard()