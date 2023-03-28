import xml.etree.ElementTree as etree

a = 0
b = 0
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
for text in root.findall('text'):
    paragraphs = text.find("paragraphs")
    for paragraph in paragraphs.findall("paragraph"):
        for sentence in paragraph.findall("sentence"):
            tokens = sentence.find("tokens")
            for token in tokens.findall("token"):
                if token.get("text") == "может":
                    if token[0][0][0][0].get("v") =="CONJ":
                        a += 1
                    if token[0][0][0][0].get("v") =="VERB":
                        b += 1
print (a,b)
