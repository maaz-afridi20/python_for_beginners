#list and tuple.
''' in list we can have many type of things like we can have (diff datatypes)
characters  and we also have integer and also have float.
--> we can change the values in the list form out side
--> we can access indexes just like strings.
'''

a = [2,1,3,4,55,4]
a [0] = 10
# print(a[2]) #indexes.
print(a) # in output this will show 10 instead of 2 

#list slicing.
frndz = ['hary','hehe','ali','jjjj',37,'aqsa','maaz']
print(frndz[0:4]) 
#it has also negative indexes like the stirngs.


# LIST METHODS.(v.imp)

l1 = [1,3,77,44,6,86,90,33]
#these methods will sort the original list directyly.
l1.sort() #this wil sort the list.
# l1.reverse() #this will reverse the list.
print(l1)
l1.append(8) #will add 8 in the end of list.
print(l1) 
l1.insert(2,100) #this will add 100 in 2nd index.
'''in append the next value will add in last while in insert 
we can add the value at any point we want. '''

print(l1) 
l1.remove(90) #this will remove 90 from the list.
l1.pop(2) #this will remove the value form 2nd index.

''' the main differece is that the remove() will remove the specific value
while when we use he pop function we will give the index of the removing
value....   '''

print(l1)


#TUPLES IN PYTH
''' we cannot update tuples. it is immutable
'''
t = (1,2,3,4,5)
print (t[0]) #simple indexds 

t1 = () #empty tuple.
t2 = (1,) #tupel with single element after first element we must
#put , so that the interprator will understand that it is tuple.


# METHODS IN TUPLES
tup = (1,1,1,2,2,55,3,76,3,6,4)
print(tup.count(1)) #this will show how many times 1 repeat.
print(tup.index(3)) #this will show the index of the value.s