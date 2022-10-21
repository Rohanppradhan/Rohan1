# electricity unit bill
units=float(input("Enter units:"))
a:int(0)
if units<=50:
    a=units*1
elif units<=100:
    a=(50*1)+(units-50)*1.5
elif units<=200:
    a=(100*1.5)+(units-100)*2
elif units<=300:
    a=(200*2)+(units-200)*2.5
elif units<=400:
    a=(300*2.5)+(units-300)*3
else:
     a=(400*3)+(units-400)*4

a+=300
print("units consumed:",units)
print("bill amount",a)



