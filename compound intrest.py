import math
t=int(input("the time taken is:"))
P= int(input("principal(original balance):"))
r=int(input("rate per period:"))
n=int(input("no of periods:"))
C=(1+(r/n))
D=(t*n)
res=math.pow(C,D)
amt=P*res



print("the Compound Intrest is=",amt)
