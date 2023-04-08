# q1
#making table.



num = int(input("enter number : "))
for i in range(1,11):
    #print(str(num) + " X " + str(i) + " = " + str(num*i))
    print(f" {str(num)} X {str(i)} = {str (num * i)} ") 
#this is the same of doing the above statement.but in easy manner.





#F STRING 
''' it is the easy way to put many variables 
above we have put + in between the variables if we put f in front
of that line then we donot use + like
'''

# q2
#finding a name starting with specific character.
'''
l1 = [ "maaz," "ali","alyan","aliullah","abdul","khan"]

for name in l1:
    if name.startswith('a'):
        print("hello " , name)
startswith function will chek the starting character of the name
and will print that which character is starting from specific character
'''

'''

list = ["maaz," "ali","alyan","aliullah","abdul","khan"]
for names in list:
    if names.startswith('a'):
        print("hi! " , names)
'''



#making table using while loop.
'''
numb =int (input("enter nmbr."))
tb = 1
while tb < 11:
    print(f" {numb} * {tb} = {numb * tb} ")
    tb = tb+1
'''

#printing steric.

n= 4
for i in range(4):
    print("*" * (i+1)) #the (i+1) will add i and then multiply with * so we will get
# that much of star 


# END OF PRACTICE