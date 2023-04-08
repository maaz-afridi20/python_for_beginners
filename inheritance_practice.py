print("inheritance practice")


class Names:
    def __init__(self, Fname, Lname):
        self.Fname = Fname
        self.Lname = Lname


class PrintNames(Names):
    def printingNames(self):
        return self.Fname + self.Lname


n = Names("maaz", "khan")
n2 = PrintNames("k", "m")

print(n2.printingNames())