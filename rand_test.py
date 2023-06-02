import unittest
from rand import gen


class Tests(unittest.TestCase):
    def test_gen(self):
        for i in range(10):
            with self.subTest(i = i):
                self.assertGreater(gen(10)[i], 0.5)
