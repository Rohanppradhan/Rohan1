#print a string
"""str="hello to the place"
for i in no:
    if(i==):
        print(str.count(str))"""
#String Slicing
"""a="ram"
print(a[0:-1])"""#the forward numbers start from 0 and the backward numbers start from -1
#Output:"ra"
"""A="Hello World"
print(A[6:],A[:6])"""
#Output=World Hello


#REVERSE OF A STRING
"""a="Rohan Pradhan"
print(a[-1::-1])"""
#Output=nahdarp nahor
#Reverse Of  A String
"""a="Rohan Pradhan"
for i in range((len(a)-1),-1,-1):
    print(a[i],end= " ")"""
#Find Vowel from  a given string
a=input("Enter a String:")
vowels=0
consonants=0
for i in range(0,len(a)):
    if( a[i]=="a" or a [i]=="e" or a[i]=="o" or a[i]=="i" or a[i]=="u"):
        vowels=vowels+1
        consonants=consonants+1
print(vowels,consonants)
