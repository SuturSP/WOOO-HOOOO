class Customer:
    def __init__(self, name, wealth, tickets):
        self.name = name
        self.wealth = wealth
        self.tickets = tickets

    def resale(a, b, c):
        a.tickets = a.tickets - 1
        a.wealth += c.seatcost + 1000
        b.wealth = b.wealth - c.seatcost - 1000
        b.tickets += 1


class Trip:
    def __init__(self, name, money, seats, seatcost):
        self.name = name
        self.money = money
        self.seats = seats
        self.seatcost = seatcost

    def sale(a, b):
        a.seats = a.seats - 1
        a.money += a.seatcost
        b.wealth = b.wealth - a.seatcost
        b.tickets += 1


Paul = Customer("Paul", 10000, 0)
John = Customer("John", 12000, 0)
MSKtoSPB = Trip("MSKtoSPB", 200000, 2, 2000)


print(Paul.wealth, John.wealth, MSKtoSPB.seats)

MSKtoSPB.sale(Paul)
MSKtoSPB.sale(Paul)
Paul.resale(John, MSKtoSPB)

print(Paul.wealth, John.wealth, MSKtoSPB.seats)
