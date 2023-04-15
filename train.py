class Customer:
    def __init__(self, name, wealth, tickets):
        self.name = name
        self.wealth = wealth
        self.tickets = tickets


class Trip:
    def __init__(self, name, money, seats, seatcost):
        self.name = name
        self.money = money
        self.seats = seats
        self.seatcost = seatcost


Paul = Customer("Paul", 10000, 0)
John = Customer("John", 12000, 0)
MSKtoSPB = Trip("MSKtoSPB", 200000, 2, 2000)


def sale(a, b):
    a.seats = a.seats - 1
    a.money += a.seatcost
    b.wealth = b.wealth - a.seatcost
    b.tickets += 1


def resale(a, b, c):
    a.tickets = a.tickets - 1
    a.wealth += c.seatcost + 1000
    b.wealth = b.wealth - c.seatcost - 1000
    b.tickets += 1


print(Paul.wealth, John.wealth, MSKtoSPB.seats)

sale(MSKtoSPB, Paul)
sale(MSKtoSPB, Paul)
resale(Paul, John, MSKtoSPB)

print(Paul.wealth, John.wealth, MSKtoSPB.seats)
