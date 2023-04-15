class Civilian:
    def __init__(self, name, wealth):
        self.name = name
        self.wealth = wealth


class Robber:
    def __init__(self, name, richness):
        self.name = name
        self.richness = richness


Robert = Civilian("Robert", 50)
Anthony = Robber("Anthony", 3)


def robbery(a, b):
    a.richness += b.wealth
    b.wealth = 0


robbery(Anthony, Robert)
print(Anthony.richness)
