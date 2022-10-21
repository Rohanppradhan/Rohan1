#student class
class Student:
    age=0
    Name=" "
    Address=" "
    gender=" "
    roll=0
    def setStudent(self):
        self.age=int(input("enter the Student's age:"))
        self.Name=input("Enter the Student's Name:")
        self.Address=input("Enter the adddress: ")
        self.gender=input("Enter the gender: ")
        self.roll=int(input("Enter the roll no:"))
    def getStudent(self):
         print(self.age," ",self.Name," ",self.Address," ",self.gender," ",self.roll)
Std=Student()
Std.setStudent()
Std.getStudent()



