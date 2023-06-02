import os

def fold(s):
    os.makedirs(s)
    fg = open(s + r"\fgfg.txt", "w+", encoding="utf-8")
    fg.write("Fgfgfgfg")
    fg.close()
