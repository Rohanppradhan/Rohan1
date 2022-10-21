def addition(func):
    def sum_op(x,y):
        func(x,y)
        print(x+y)
    return sum_op
@addition
def sum_num(a,b):
    print("The addition of the numbers are :")
sum_num(1,3)