# to check whether a number is perfet number or not
i=int(input("enter a number:"))
sum=0
for a in range (1,i):
    if (i%a)==0:
        sum=sum+a
if sum==i:
    print("number is perfect",i)
else:
    print("number is not perfect",i)