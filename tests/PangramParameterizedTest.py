import unittest
from sample.Pangram import *

class PangramParametrizedFile(unittest.TestCase):

    def test_from_file(self):
        f = open("../data/pangram_tests")
        pangramClass = IsPangram()
        for line in f:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                value, expected = (data[0], data[1].strip("\n"))
                self.assertEqual(pangramClass.game(value), expected)

    def test_from__file_exception(self):
        file = open("../data/pangram_tests_exception")
        pangramClass = IsPangram()
        for line in file:
            if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
                continue
            else:
                data = line.split(" ")
                value, expected = (data[0], data[1].strip("\n"))
                self.assertRaisesRegex(Exception, expected, pangramClass.game, int(value))


if __name__ == '__main__':
    unittest.main()

