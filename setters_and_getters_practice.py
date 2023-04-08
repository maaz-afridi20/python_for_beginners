print('Getters And Setters')
"""
the getters are use to get data in this method we do not modify any one of the data but we can simply get
that data and read it or what ever we want to print
for example.

while in setter method we do access data and also we modify data as per our choice 
the main function of the setter function is that it set the value like below we change our model name
from one mobile to another

"""

"""

getter example

class Mobile:
    def __init__(self):
        self.model = "REAL ME"

    def get_model(self):
        return self.model


real = Mobile()
m = real.get_model()
print(m)

"""

"""
example of setter method.

class Mobile:
    def __init__(self):
        self.model = "RealMe"

    def set_model(self):
        self.model = "Iphone"


apple = Mobile()
apple.set_model()
print(apple.model)

"""

"""
this is also another method in which we give our own attribute when we call the function and it 
accept and then set the model.


class Mobile:

    def set_model(self, m):
        self.model = m


apple = Mobile()
apple.set_model("Samsung")
print(apple.model)
"""