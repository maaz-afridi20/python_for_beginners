print('this is the intro of the classes')
'''
class myClass:
    x = 5

p1 = myClass()
print(p1.x)
'''

class myClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = myClass('maaz', 23)

print(p1.name)
print(p1.age)