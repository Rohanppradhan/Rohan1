# Armstrong number
i=int(input("enter a number:"))
#a is a variable declared for keeping the original number as the number is been cutted out
a=i
#here a new variable order is declared for calculating the lenth of the given int number
order=len(str(i))
sum=0
while(i>0):
    #it will show the first value that would be calculated below ex:153%10=3 so first 3 will be calculated then following as follows
    digit=i%10
    sum=sum+digit**order#here the ** represents pow function
    i=i//10#it will also count the latest number from the backside and again the loop will follow
if a==sum:
    print("number is armstrong")
else:
    print("number is not armstrong")
