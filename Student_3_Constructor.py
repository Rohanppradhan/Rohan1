class Student:
    age=0
    Name=" "
    Address=" "
    gender=" "
    roll=0
    def __init__(self,age,Name,Address,gender,roll):
        self.age=age
        self.Name=Name
        self.Address=Address
        self.gender=gender
        self.roll=roll
    def getStudent(self):
         print(self.age," ",self.Name," ",self.Address," ",self.gender," ",self.roll)
    def __del__(self):
        print("the Student Constructor is deleted ")
Std=Student(20,"rohan","fdskjhfskd","male",2409)
Std.roll=43894393#updation of roll number outside the class
Std.getStudent()
print(Std)