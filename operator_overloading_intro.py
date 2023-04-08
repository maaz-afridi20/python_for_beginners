print("operator overloading")
# print(int.__add__(10, 20)) behind the scene when we just simply put + then this type of method runs
# int.__sub__(self, other) for subtraction
# __mul__(self, other)

"""
so the main idea of the operator overloading is that just like above when we simply add something
there is some method like above which perform its work and then we get + but if we want to
add two object of the classes then we will use the __add__(self, other) to add them
so this is the main function of the operator overloading. 
so the main idea is that we put our own logic here to add something that cannot be add simply
we can also use it for subtraction, multiplication, division, and many other.
like for example..
"""


class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x


class B:
    def __init__(self, x):
        self.x = x


a = A(100)
b = B(200)
print(a+b)  # so it will run like A.__add__(a, b)
