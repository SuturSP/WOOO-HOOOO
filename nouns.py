import xml.etree.ElementTree as etree

a = str()
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
for token in root.iter("token"):
    if token[0][0][0][0].get("v") == "NOUN":
        for g in token[0][0][0]:
            if g.get("v") == "plur":
                a += token.get("text") + ' ' + '\n'
with open("ooooo.txt", 'w', encoding="utf-8") as f:
    f.write(a)
