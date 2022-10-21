class Student:
    Name=" "
    Roll=0
    Class=" "
    Gender=" "
    def setStudent(self):
        self.Name=str(input("enter the name of the student:"))
        self.Roll=int(input("Enter the roll no:"))
        self.Class=str(input("enter the class of the student:"))
        self.Gender=str(input("enter the gender of the student:"))
    def getStudent(self):
        print(self.Name,"---",self.Roll,"---",self.Class,"---",self.Gender,"---")
class Teacher(Student):
    TeacherName=" "
    TeacherId=0
    TeachingSubject=" "
    def setTeacher(self):
        self.TeacherName=str(input("enter the name of the teacher:"))
        self.TeacherId=int(input("enter the Teacher id:"))
        self.TeachingSubject=str(input("Enter the Subject taught:"))
    def getTeacher(self):
        print(self.TeacherName,"---",self.TeacherId,"---",self.TeachingSubject,"---")
T=Teacher()
T.setStudent()
T.setTeacher()
T.getStudent()
T.getTeacher()