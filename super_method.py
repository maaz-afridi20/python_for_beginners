print("Super method.!")

"""
The super method is use when we want to use the methods that are in father(Parent) class
like if we want to print the takeBreath method of the programmer class but as well as we want also
to print the takeBreath of the Employee class then we will use the super method in the programmer class
so that will print the takeBreath method of the programmer as well as of the Employee class.


we can also use super method to the constructor just like given below.

"""


class Person:
    country = "Pakistan"

    def __init__(self):
        print("initializing Person")

    def takeBreath(self):
        print("i am person and taking breath")


class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("initializing Employee")

    def takeBreath(self):
        super().takeBreath()
        print("i am employee and breathing")


class Programmer(Employee):
    company = "Fiver"

    def __init__(self):
        super().__init__()
        print("initializing Programmer")

    def takeBreath(self):
        super().takeBreath()
        print("I am programmer and breathing")


#p = Person()
#p.takeBreath()


e = Employee()
#e.takeBreath()


#pr = Programmer()
#pr.takeBreath()