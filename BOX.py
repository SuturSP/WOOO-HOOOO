class Shapes:
    def __init__(self, name, color, size, angles):
        self.name = name
        self.color = color
        self.size = size
        self.angles = angles


class Box:
    def __init__(self, name, amount, insides):
        self.name = name
        self.amount = amount
        self.insides = insides


x = []
box = Box("box", 0, x)
triangle = Shapes("triangle", "red", 10, 3)
square = Shapes("square", "yellow", 12, 4)
pentagon = Shapes("pentagon", "blue", 14, 5)
circle = Shapes("circle", "green", 10, 1000)


def putin(a, b):
    a.amount += 1
    a.insides += b.name


putin(box,triangle)
print(box.amount)