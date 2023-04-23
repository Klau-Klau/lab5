import unittest
import numpy as np

from main import odejmowanie, mnozenie, dzielenie, funkcja_numpy


class TestOdejmowanie(unittest.TestCase):
    def test_odejmowanie(self):
        self.assertEqual(odejmowanie(5, 2), 3)


class TestMnozenie(unittest.TestCase):
    def test_mnozenie(self):
        self.assertEqual(mnozenie(5, 2), 10)


class TestDzielenie(unittest.TestCase):
    def test_dzielenie(self):
        self.assertEqual(dzielenie(10, 2), 5)
        self.assertEqual(dzielenie(5, 0), "MIANOWNIK NIE MOŻE MIEĆ ZERA")
        self.assertEqual(dzielenie(0, 5), 0)
        self.assertEqual(dzielenie(-10, 2), -5)
        self.assertEqual(dzielenie(10, -2), -5)


class TestFunkcjaNumpy(unittest.TestCase):
    def test_funkcja_numpy(self):
        self.assertEqual(funkcja_numpy([1, 2, 3]), np.sum([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
