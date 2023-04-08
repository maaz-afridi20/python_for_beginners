class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"the square of number is {self.num **2} ")

    def cube(self):
        print(f"the cube of number is {self.num **3}")

    def Root(self):
        print(f"the root of the number  is {self.num **0.5}")

a = Calculator(9)
a.square()
a.cube()
a.Root()
