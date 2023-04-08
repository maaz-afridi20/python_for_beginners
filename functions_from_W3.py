'''
def my_function():
    print('this is my first function')

my_function()  # this is how we can recall the function.

'''

'''
# arguments in function

def my_function(fname):
    print(fname + "\thhaaha\t")

my_function('Email')
my_function('ali')
'''

'''
def my_function(fname, lname):
    print(fname + " " + lname)

my_function('maaz', 'khan')
'''

# we can use * when we donot know that how many parameters will be pass

'''
def my_function(*kids):
    print(kids)

my_function("ali", "khan", "tareen") # so here we can give any number of arguments that we want.
'''

'''
def childs(*child1):
    print("my name is " + child1[0])  # this will print maaz

childs('maaz', 'khan', 'ali')
'''


'''
def childs(child1, child2, child3):
    print('the youngest child is ' + child1)

childs('m', 'r', 'k')  # this will print m
'''


'''
# printing a list or anything through functions

def my_function(food):
    for item in food:
        print(item)


fruits = ['apple', 'banana', 'mango']

my_function(fruits)
'''

'''
# returning values from function

def my_func(x):
    return x*5

print(my_func(5))   # this will return 25
'''

