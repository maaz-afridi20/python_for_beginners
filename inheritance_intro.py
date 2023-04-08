print('this is inheritance')


class Employee:
    company = "Google"

    @staticmethod
    def showDetails():
        print('this is Employee')


class Programmer(Employee):  # this is the method to write inheritance we write parent name in bracket
    language = 'python'

    def getLang(self):
        print(f"the language is {self.language}")


e = Employee()
p = Programmer()

e.showDetails()
p.showDetails()
print(p.company)

'''
we can also override the same function through inheritance like for example in above we have
show details method if we want to update the same method we can also change that 
just writing that method in that class in which we want to make in that specific class.
'''
