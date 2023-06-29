class Civilian:
    def __init__(self, name, wealth):
        self.name = name
        self.wealth = wealth


class Robber:

    def __init__(self, name, richness):
        self.name = name
        self.richness = richness

    def robbery(self, b):
        self.richness += b.wealth
        b.wealth = 0


Robert = Civilian("Robert", 50)
Anthony = Robber("Anthony", 3)

Anthony.robbery(Robert)
print(Anthony.richness)
