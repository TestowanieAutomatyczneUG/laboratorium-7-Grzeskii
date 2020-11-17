import unittest
from sample.SolarAge import *
from parameterized import parameterized, parameterized_class

class SolarAgeParameterizedTest(unittest.TestCase):

    def setUp(self):
        self.temp = SolarAge()

    @parameterized.expand([
        (31557600, "Ziemia", 1),
        (5215621652, "Wenus", 268.65),
        (125161212, "jowisz", 0.33),
        (245152121, "Neptun", 0.47)
    ])
    def test_solar_age_positive(self, seconds, planet, expected):
        self.assertEqual(self.temp.game(seconds, planet), expected)

    @parameterized.expand([
        ("24112", "Ziemia", "Wrong arguments!"),
        (5215621652, 130, "Wrong arguments!"),
        (True, "jowisz", "Wrong arguments!"),
        (245152121, False, "Wrong arguments!")
    ])
    def test_solar_age_exceptions(self, seconds, planet, expected):
        self.assertRaisesRegex(Exception, expected, self.temp.game, seconds, planet)


@parameterized_class(("seconds", "planet", "expected"), [
    (521521521, "Merkury", 68.62),
    (598218952198, "saturn", 643.74),
    (1214211111211, "Uran", 4576.89),
    (421421412, "Mars", 7.1)
])
class SolarAgeParameterizedTestClass(unittest.TestCase):

    def setUp(self):
        self.temp = SolarAge()

    def test_solar_age_positive_class(self):
        self.assertEqual(self.temp.game(self.seconds, self.planet), self.expected)


if __name__ == '__main__':
     unittest.main()
