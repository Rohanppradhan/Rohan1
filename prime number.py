#wap to find out wether the entered number is prime or not
a=int(input("enter a number:"))
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print(a,"the given number is not an prime number")
            break
    else:
     print(a,"the given number is a prime number")
else:
    print(a,"it is not a prime number")
