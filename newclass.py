class Chords:
    def __init__(self, name, function, keys, sound):
        self.name = name
        self.function = function
        self.keys = keys
        self.sound = sound


Gmaj7 = Chords("Gmaj7", 14, "G C D", "maj7")
Dm = Chords("Dm", 145, "C F Bflat", "minor triad")
A7 = Chords("A7", 5, "D", "dominant seventh chord")
Edim = Chords("Edim", 4, "F", "diminished chord")
Caug= Chords("Caug", 5, "occurs in no key naturally, but c major, if you ask me", "augmented chord")

print(Gmaj7.function)
