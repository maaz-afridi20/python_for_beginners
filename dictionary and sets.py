# SYNTAX 
#in dictrionary we have the key and its value 
my_dict = {
    "fast" : "quick",
    "me" : "a studend",
    "marks" : "[3,23,4,22]",
    "anotherdict" :  { 'kust': 'university' } 
}
print(type(my_dict))
print(my_dict["me"])
print(my_dict['fast']) #this will show the value of the fast which is quick
print(my_dict['marks']) # will show list of the numbers.
print(my_dict['anotherdict']) #this will show whole nested dictionary
''' we can also make a nested dictionary in the one dictionary.
and if we then acess it. can be access. just like the other key values.
like above 
we can also acess the valuse in the nested dictionary like below.

--> it is unordered
--> it is mutable (we can chang the value of dictionry later on.)
'''
print(my_dict['anotherdict']['kust'])        #this will show only the value of kust in dictionary.
my_dict['marks'] = [1,2,3,4,5]               #now the value of tthe marks will change here.
print(my_dict['marks'])



# METHOD IN DICTIONARY /

print(my_dict.keys())   #will show only keys of the dictionary.
print(my_dict.values()) #show only values of dictionary
print(my_dict.items()) # print all key and values of all content.
print(my_dict)
update_dict = { # update the dictionary with key value content
    "love" : "forever",
    "fake" : "friends"
}
my_dict.update(update_dict) #this will add love forever key value in the dictionary
print(my_dict)


print(my_dict['fake'])      #one way
print(my_dict.get('fake'))  # 2nd way

''' both of the ways will return the same value but when we put the simple way and that element 
is not present in that dictionary then it will through error 
while if we put .get() method  then if the value is not present in the dictionaryy then it will
only show none and will not through the error. (this is the only difference.) '''

#END OF DICTIONARY