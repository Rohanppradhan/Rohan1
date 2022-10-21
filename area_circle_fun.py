r=2#global
def area_of_circle():#called
    global r
    r=3
    print("area of circle: ",(3.14*r*r))

area_of_circle()#calling

def perimeter_of_circle():
    print("perimeter of circle: ",(2*3.14*r))

perimeter_of_circle()