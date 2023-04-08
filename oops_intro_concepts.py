print("POOP(python object oriented programming)")
'''
class dog:
    def barking(self):
        print(" Dog is barking. ")

o = dog()   # this is just the declaring object.
o.barking()
print(type(o))
'''


'''
mean that the __init__ will be automatically call when we initialize object.

'''

'''
class dog:
    def __init__(self, name):  # the __init__ is just like the constructor like in java.
        self.name = name
        print(name)


d1 = dog('kitty party')  # first object
d2 = dog('hellen')  # second object.
'''

# same above class with some changes.

'''
class dog:
    def __init__(self, name):
        self.namee = name


d = dog("he")
print(d.namee)
d2 = dog("she")
print(d2.namee)

so the main difference between the above and this __init__ function is that just in above 
we give the print statement with the self  while here we give the print statement 
when we give the name to the constructor and then print that name. 
'''


# we can also give the get name function just like java.
class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


d = dog('tim', 25)
print(d.get_name(), d.get_age())
d2 = dog('cli', 100)
print(d2.get_name(), d2.get_age())
