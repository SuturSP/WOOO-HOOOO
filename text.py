import xml.etree.ElementTree as etree

a = str()
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
for text in root.findall('text'):
    paragraphs = text.find("paragraphs")
    for paragraph in paragraphs.findall("paragraph"):
        for sentence in paragraph.findall("sentence"):
            source = sentence.find("source")
            a+=source.text + ' ' + '\n'
with open("ooooo.txt", 'w', encoding="utf-8") as f:
    f.write(a)