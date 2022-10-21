#strong number
i=int(input("enter a number:"))
a=i
sum=0

while(i>0):
    r=i%10
    fact=1
    for f in range(1,r+1):
        fact=fact*f
    sum=sum+fact
    i=i//10
if (sum==a):
    print("It is  a strong number")
else:
    print("It is not a strong number")
