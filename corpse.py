import xml.etree.ElementTree as etree
import unittest


class Corpus:
    def __init__(self):
        self._sentences = []

    def load(self, path_to_corpus):
        pass

    def pp(self, i):
        return self._sentences[i]


class Sentence:
    def __init__(self, stroka):
        self.stroka = stroka
        self._wordforms = []

    def ps(self, i):
        return self._wordforms[i]


class Wordform:
    def __init__(self, gg):
        self.gg = gg
        self._grammems = []

    def pg(self, i):
        return self._grammems[i]


a = str()
crp = Corpus()
tree = etree.parse('annot.opcorpora.no_ambig.xml')
root = tree.getroot()
for sentence in root.iter("sentence"):
    y = []
    source = sentence.find("source")
    predlog = Sentence(source.text)
    for token in sentence.iter("token"):
        z = []
        if token[0][0][0][0].get("v") != "PNCT":
            slov = Wordform(token.get('text'))
            for gr in token.get('text'):
                z.append(gr)
            slov._grammems = z
            y.append(slov)
    predlog._wordforms = y
    crp._sentences.append(predlog)


class Tests(unittest.TestCase):

    def test_pp(self):
        self.assertIn("Великолепная «Школа злословия» вернулась в эфир после", crp.pp(2).stroka)

    def test_ps(self):
        self.assertEqual(crp._sentences[2].ps(1).gg, "Школа")

    def test_pg(self):
        self.assertEqual(crp._sentences[2]._wordforms[1].pg(3), "л")


if __name__ == '__main__':
    unittest.main()
