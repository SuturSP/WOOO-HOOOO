import unittest
from corpusss import Calculator
import os
import shutil


class Tests(unittest.TestCase):
    def setUp(self):
        text1 = "Я Серёжа. Сегодня мне исполняется двадцать годиков. Пока что, лучший мой др. Ах, питон, питон..."
        text2 = "Я Диана. Сегодня мне не исполняется двадцать годиков. Пока что, лучший мой не др. Ах, питон, питон..."
        os.makedirs('C:\\Users\\79137\\PycharmProjects\\WOOO-HOOOO\\corpus2')
        fg = open('C:\\Users\\79137\\PycharmProjects\\WOOO-HOOOO\\corpus2' + r"\Text1.txt", "w+")
        fg.write(text1)
        fg.close()
        fg = open('C:\\Users\\79137\\PycharmProjects\\WOOO-HOOOO\\corpus2' + r"\Text2.txt", "w+")
        fg.write(text2)
        fg.close()
        self.mycalcul = Calculator('C:\\Users\\79137\\PycharmProjects\\WOOO-HOOOO\\corpus2', idf_file='idfochki.pickle')
        self.mycalcul.imblind()

    def test_calculate_tf(self):
        txt = "Я Диана. Сегодня мне не исполняется двадцать годиков. Пока что, лучший мой не др. Ах, питон, питон..."
        rezzultat = self.mycalcul.calculate_tf(txt)
        self.assertGreater(len(rezzultat), 0)
        self.assertIsInstance(rezzultat[0], tuple)
        self.assertIsInstance(rezzultat[0][0], str)
        self.assertIsInstance(rezzultat[0][1], float)

    def test_calculate_idf(self):
        idfochki = self.mycalcul.idf_values
        self.assertEqual(len(idfochki), 17)
        self.assertIsInstance(idfochki, dict)

    def tearDown(self) -> None:
        shutil.rmtree(r"C:\\Users\\79137\\PycharmProjects\\WOOO-HOOOO\\corpus2")


if __name__ == '__main__':
    unittest.main()
