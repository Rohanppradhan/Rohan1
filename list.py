#syntax is l=[]
"""l=[1,2,3,4,5]
print(len(l))"""

#how to copy one index of all list into another list without using blank list
"""l=[1,2,3,3,4,5]
l[0:2]=["add","sub",3,4]
print(l)"""

#insert a element inside the list
'''l=[1,2,3,4,5,67,7,8,8,9]
l.insert(2,"asdhgd")
print(l)'''

# inserting element without using insert function
"""l=[1,2,3,4,5,67,7,8,8,9]
l[3:3]=["sdasda"]
print(l)"""

#append function
'''l=[1,2,3,4,5,67,7,8,8,9]
l.append('true')
print(l)'''#the value is added in the last of the index

#extend function
"""l=[1,2,3,4,5,67,7,8,8,9]
l.extend('asasdasffsdfsdfsdffdsf')
print(l)"""

#remove function
'''l=[1,2,3,4,5,67,7,8,8,9]
l.remove(l[5])
print(l)'''#there is no error

#pop method
"""l=[1,2,3,4,5,67,7,8,8,9]
l.pop()
print(l)"""#index if not given it will delete the last index

#delete method
'''l=[1,2,3,4,5,67,7,8,8,9]
del l[4]
print(l)'''#if del() is given a null value then the index will be totlly deleted

#how to remove multiple elements from list
'''l=[1,2,3,4,5,67,7,8,8,9]
del l[0:6]
print(l)'''

#index number and what is stored in the index
'''l=[1,2,3,4,5,67,7,8,8,9]
for i in range(len(l)):
    print(l[i],"=>",i,"\n")'''






