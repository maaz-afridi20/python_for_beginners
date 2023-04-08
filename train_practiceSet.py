class Train:
    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getStatus(self):
        print(f" The name of the train is {self.name}")
        print(f" The seats available are {self.seats }")

    def fareInfo(self):
        print(f"The price of ticket is Rs s: {self.fare}")

    def bookTicket(self):
        if (self.seats>0):
            print('Your ticket has been boocked.!')
            self.seats = self.seats-1
        else:
            print('The train if full')

people = Train("Gaggar Shah express ",2 , "Rs : 300")
people.fareInfo()
people.getStatus()
people.bookTicket()
people.getStatus()
people.bookTicket()
people.getStatus()
people.bookTicket()
people.getStatus()