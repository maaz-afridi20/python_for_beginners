print("practice class method!")

"""
like in below example if we want to change salary then we make a def method but that will change the
instance method means that it will not change the salary of the whole class salary variable
it will change the salary of that instance variable that we created in the def method that we created.

so if we want to change the salary of the whole class then we can write the class method and the syntax
will be         like      


def changeSalary(self, sal):
    self.__class__.Salary = sal
    
here the name may be any thing but the self.__class__  will remain same for all the things
the self.__class__ will refer to that class that we are changing the value.
"""


class Employee:
    company = "Camel"
    salary = 100
    location = "Lahore"

#    def changeSalary(self, sal):
#        self.__class__.salary = sal

# another way of doing the above thing is
    @classmethod
    def changeSalary(cls, loc):
        cls.location = loc  # will change location from Lahore to another any thing we give,

# this is the same method of the above method.


e = Employee()
print(e.salary)

print(Employee.salary)
e.changeSalary("pindi")
print(e.salary)
print(Employee.salary)
# print(Employee.location)
