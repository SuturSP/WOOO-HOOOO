class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):
    def __init__(self, l, w, h):
        super().__init__(l, w, h)
        self.places = None

    def howplaces(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def outplases(self):
        print(self.places)


class Worker(Table):
    def __init__(self, l, w, h):
        super().__init__(l, w, h)
        self.total = None

    def total(self, m):
        if m == 1:
            self.total = self.long + self.width + self.height
        elif m == 2:
            self.total = self.long * self.width * self.height
        else:
            print('Input 1 for sum params or 2 for multiplication')

    def get_total(self):
        print(self.total)


t_room1 = Kitchen(2, 1, 0.5)
t_room1.outing()
t_room1.howplaces(5)
t_room1.outplases()
t_2 = Table(1, 3, 0.7)
t_2.outing()
t_room1 = Worker(2, 4, 8)
t_room1.outing()
t_room1.total(1)
t_room1.get_total()
t_room1 = Worker(2, 4, 8)
t_room1.total(2)
t_room1.get_total()
t_room1 = Worker(2, 4, 8)
t_room1.total(3)
t_room1.get_total()
