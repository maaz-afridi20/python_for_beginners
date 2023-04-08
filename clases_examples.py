class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def grade(self):
        return self.grade


s = Students('ali', 35, 4)
print(s.get_name())
print(s.get_age())
print(s.grade)

