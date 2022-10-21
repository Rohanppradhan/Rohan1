class Student:
    Name = " "
    Roll = 0
    Class = " "
    Gender = " "

    def setStudent(self):
        self.Name = str(input("enter the name of the student:"))
        self.Roll = int(input("Enter the roll no:"))
        self.Class = str(input("enter the class of the student:"))
        self.Gender = str(input("enter the gender of the student:"))

    def getStudent(self):
        print(self.Name, "---", self.Roll, "---", self.Class, "---", self.Gender, "---")


class Teacher(Student):
    TeacherName = " "
    TeacherId = 0
    TeachingSubject = " "

    def setTeacher(self):
        self.TeacherName = str(input("enter the name of the teacher:"))
        self.TeacherId = int(input("enter the Teacher id:"))
        self.TeachingSubject = str(input("Enter the Subject taught:"))

    def getTeacher(self):
        print(self.TeacherName, "---", self.TeacherId, "---", self.TeachingSubject, "---")


class School( Student):
    SchoolName = " "
    Established = 0
    def setSchool(self):
        self.SchoolName = str(input("Enter the school name:"))
        self.Established = int(input("enter the establishment date:"))

    def getSchool(self):
        print("The school is", self.SchoolName, "---", self.Established, "---")
class Games(School,Teacher):
    GamesName=" "
    def setGames(self):
        self.GamesName=str(input("enter the Games:"))
    def getGames(self):
        print("The games played are",self.GamesName)
g=Games()
g.setGames()
g.setSchool()
g.setStudent()
g.setTeacher()
g.getGames()
g.getSchool()
g.getTeacher()
g.getStudent()