import unittest
from corpse import Corpus

crp = Corpus()


class Tests(unittest.TestCase):

    def test_pp(self):
        self.assertIn("Великолепная «Школа злословия» вернулась в эфир после", crp.pp(2))

    def test_ps(self):
        self.assertIn(crp._sentences[2].ps(1), "Школа")

    def test_pg(self):
        self.assertEqual(crp._sentences[2]._wordforms[1].pg(3), "л")


if __name__ == '__main__':
    unittest.main()
