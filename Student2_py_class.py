class Student:
    age=0
    Name=" "
    Address=" "
    gender=" "
    roll=0
    def setStudent(self,age,Name,Address,gender,roll):
        self.age=age
        self.Name=Name
        self.Address=Address
        self.gender=gender
        self.roll=roll
    def getStudent(self):
         print(self.age," ",self.Name," ",self.Address," ",self.gender," ",self.roll)
Std=Student()
Std.setStudent(20,"Rohan","g/323","male",190)
Std.getStudent()


