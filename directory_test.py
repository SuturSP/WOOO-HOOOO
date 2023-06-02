import unittest
from directory import fold
import shutil

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        fold(r"C:\Users\79137\Desktop\Fhfhfh")
    def test_fold(self):
        fg = open(r"C:\Users\79137\Desktop\Fhfhfh\fgfg.txt", "r", encoding="utf-8")
        self.assertGreater(len(fg.read()), 0)
        fg.close()
    def tearDown(self) -> None:
        shutil.rmtree(r"C:\Users\79137\Desktop\Fhfhfh")