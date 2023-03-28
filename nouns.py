import xml.etree.ElementTree as etree

a = str()
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
for text in root.findall('text'):
    paragraphs = text.find("paragraphs")
    for paragraph in paragraphs.findall("paragraph"):
        for sentence in paragraph.findall("sentence"):
            tokens = sentence.find("tokens")
            for token in tokens.findall("token"):
                if token[0][0][0][0].get("v") == "NOUN":
                    for g in token[0][0][0]:
                        if g.get("v") == "plur":
                            a += token.get("text") + ' ' + '\n'
with open("ooooo.txt", 'w', encoding="utf-8") as f:
    f.write(a)