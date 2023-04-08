"""
the multiple inheritance means that one child is getting inherit from
2 or more parents
"""


class Employee:
    company = "visa"


class Freelancing:
    company = "fiver"
    level = 0


class Programmer(Employee, Freelancing):  # this is multiple inheritance in bracket we always write
    # the parent classes here we have two parent classes so we have two parents
    name = "Rohit"


p = Programmer()
print(p.level)
