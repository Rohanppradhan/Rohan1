class Circle:
    r=0
    def __init__(self):
     self.r=int(input("Enter the radius:"))

class Area(Circle):
    A=0
    def __init__(self):
      super().__init__()
      self.A=2*3.14*self.r


    def display(self):
      print("The Area of the circle is",self.A)

a=Area()
a.display()


