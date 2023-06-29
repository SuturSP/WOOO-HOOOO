class Figure:
    def __init__(self, w="white"):
        self.color = w

    def changecolor(self, ch):
        self.color = ch

    def out(self):
        pass


class Oval(Figure):
    def __init__(self, r, x, y):
        self.radius = r
        self.ox = x
        self.oy = y
        super().__init__()

    def out(self):
        print(self.radius, self.ox, self.oy, self.color)


class Square(Figure):
    def __init__(self, w, h):
        self.widht = w
        self.height = h
        super().__init__()

    def out(self):
        print(self.widht, self.height, self.color)


x = Figure("red")
print(x.color)

o = Oval(5, 0, 0)
o.out()
o.changecolor("black")
o.out()

s = Square("8", 8)
s.out()
s.changecolor("grey")
s.out()
