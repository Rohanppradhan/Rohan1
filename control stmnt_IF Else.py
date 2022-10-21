#find the greater among the 4 nos using nested if
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
d=int(input("enter the fourth number:"))
if(a>b):
  if (a>c):
      if(a>d):
          print("the greatest number is a")
      if(c>d):
         print("c is greater")
     else:
         print("d is greater")
     else:
       if (b>c):
         if(b>d):
             print("b is greatest")
         else:
             print("the greatest number d")
     else:
         print("the greatest number c")
     if(c>d):
         print("print the greatest number c")
     else:
         print("the greatest number is d")
    else:
      if(a>d):
        print("a is greater")
    else:
        print("d is gtreater")






























