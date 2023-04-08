# strings is the sequence of characters.
#there are 3 type of strings.
#single auote double and tripple quote. all can be use.


#STRING SLICING. 
# myname = "maazullah , "
# myadress = "razgir banda"
# add = myname+myadress (concatinationg 2 strings.)
# print("my name and adress is  " , add)
# print(len(myname))
# arr = "2,3,3,4,6,7,8,8,6"
# print(max(arr))

h = "goodmorning"
print(len(h))
print(h[0:12]) #this will show all (good morning)
               #if we also let this palce blank then this will not 
               #through error. it will assume that it is 0
print(h[3:11]) #starting from  (d morning)
# we can also use negative indexes.

#print(h[0:]) --> # same as (h[0:12])

print(h[:-1]) # this will start the index from negative side.



#SLICING WITH SKIP VALUES.

WORD =  "salampakistan"
print(len(WORD))
print(WORD[0:13:2]) #ye aik k bad doosra letter skip krdega. or agy jayega.
#ya hm kah saktya hain k hr doosray character ko print kro.
print(WORD[0::2]) #this is same as (word[0:13:2])

