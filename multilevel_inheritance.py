"""
multi level inheritance means that when we are inheriting the property of one class in second
class and then we again inherit some properties in 3rd class but from 2nd class then it is called
the multi level inheritance and so on....
"""


class Person:
    country = "Pakistan"

    def takeBreath(self):
        print(" I am taking breath")


class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f" my salary is {self.sarary}")

    def takeBreath(self):
        print("I am employee and taking breath")


class Programmer(Employee):
    company = "Fiver"


    def takeBreath(self):
        print("i am progammer and breathing")

    def getSalary(self):
        print("No salary to me..")


p = Person()  # grand father
p.takeBreath()
e = Employee()  # father
e.takeBreath()
pr = Programmer()  # last child
pr.takeBreath()
