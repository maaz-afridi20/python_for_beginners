print('operator Overloading')


class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num2):
        print("sum")
        return self.num + num2.num


nmb1 = Number(10)
nmb2 = Number(20)
sum = nmb2+nmb1
print(sum)