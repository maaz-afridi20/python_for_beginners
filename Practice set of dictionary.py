# q1
my_dict = {
    "maiz" : "table",
    "chappal" : "shoes",
    "dabba" : "box",
    "aam" : "mango"
}
print("the option are given as : " , my_dict.keys())
a = input("Enter the word.\n")
#print("the meaning of the word is. : " ,my_dict[a]) 
# [] --> method may give error when the value is not present so we will use
#.get() method.
print("meaning of the word is : " , my_dict.get(a))



# q2

#create empty dictionary and input from user.

fav_lang = {}
a = input("enter your language. : maaz\n ")
b = input("enter your language. : khan\n ")
c = input("enter your language. : ali\n ")
d = input("enter your language. : dani\n ")
fav_lang['maaz'] = a
fav_lang['khan'] =b
fav_lang['ali'] = c
fav_lang['dani'] = d
print(fav_lang)