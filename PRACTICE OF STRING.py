#Q1
# name = input("enter your name :\n ")
# print("hello " , name)

#Q2
letter = '''

 Dear <|name|>, you are selected ! 
date : <|date|>

'''
# print(letter)

# name = input("name: ")
# date = int (input("date: "))
# print("Dear " , name , "you are selected!!  \n" , "on date : " , date)

#this is also 2nd methond to do this below.
name = input("enter your name : ")
date = input ("enter your date : ")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)

#FINDING DOUBLE SPACES IN STRING.

st = "this is the stirng with double    space"
dsp = st.find("  ")
print(dsp) # this wil show the place where the white spaces is present.