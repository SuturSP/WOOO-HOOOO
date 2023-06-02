import unittest
from ddff import subtract, add, isbigger, inclusion, exclusion, equality


class Tests(unittest.TestCase):
    def test_subtract(self):
        self.assertGreater(15, subtract(5, 15))
        """self.assertGreater(8, subtract(8, -1))"""

    def test_add(self):
        self.assertLess(15, add(5, 15))
        """self.assertLess(8, add(8, -1))"""

    def test_isbigger(self):
        self.assertTrue(isbigger(15, 5))
        self.assertFalse(isbigger(5, 15))

    def test_inclusion(self):
        self.assertIn(5, inclusion([], 5))

    def test_exclusion(self):
        self.assertNotIn(5, exclusion([15, 5], 5))
        self.assertNotIn(8, exclusion([15, 5], 8))

    def test_equality(self):
        self.assertCountEqual([len("123")], [len(equality("12", "123"))])


if __name__ == "__main__":
    unittest.main()
