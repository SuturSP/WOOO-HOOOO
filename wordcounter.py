import xml.etree.ElementTree as etree

a = 0
b = 0
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
for token in root.iter("token"):
    if token.get("text") == "может" or token.get("text") == "Может":
        if token[0][0][0][0].get("v") == "CONJ":
            a += 1
        if token[0][0][0][0].get("v") == "VERB":
            b += 1
print(a, b)
