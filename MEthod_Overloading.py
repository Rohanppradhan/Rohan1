from multipledispatch import dispatch
@dispatch(int,int)
def sum(a,b):
    print("the sum is ",a+b)
@dispatch(int,int,int)
def sum(a,b,c):
    print(a+b+c)
@dispatch(int,int,int)
def sum(a,b,c,d):
    print(a+b+c+d)
sum(1,2,3)