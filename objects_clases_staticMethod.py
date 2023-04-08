class Employee:
    company = "Google"

    def salary(self):
        print(f"the salary is {self.salary}")

    @staticmethod
    def greet():
        print('good morning')
'''
@staticmethod is use when we donot want to give self parameter if we do not give the self
parameter in def then it will give error. but if we do not want to give self parameter then we must 
use the @staticmethod.
'''

meme = Employee()
meme.salary = 100000
meme.greet()  # this will print good morning.
