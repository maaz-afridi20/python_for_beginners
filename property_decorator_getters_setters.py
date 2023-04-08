print("property decorator and setters and getters.")
"""
the property decorator is use if some thing is changing and we cannot hard code it
so we will use the property decorator so this will do that we will write a method but 
it will act as a property not as method like example given below.
"""

class Employee:
    company = "CNG"
    salary = 5600
    salaryBonus = 500


    @property  # so this looks like method but will act as property
    def totalSalary(self):
        return self.salary + self.salaryBonus


e = Employee()
print(e.totalSalary)