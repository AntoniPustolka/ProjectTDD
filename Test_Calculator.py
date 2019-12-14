import unittest
import Calculator

class test_calculator(unittest.TestCase):

    def test_dodawania(self):
        wynik = Calculator.dodaj(2,3)
        self.assertEqual(wynik, 5)
        self.assertNotEqual(wynik, 2)
        wynik = Calculator.dodaj(-1,3)
        self.assertEqual(wynik, 2)

    def test_odejmowania(self):
        wynik = Calculator.odejmowanie(2,3)
        self.assertEqual(wynik, -1)
        self.assertNotEqual(wynik, 2)

    def test_mnozenia(self):
        wynik = Calculator.mnozenie(2,3)
        self.assertEqual(wynik, 6)
        self.assertNotEqual(wynik, 2)

    def test_dzielenie(self):
        wynik = Calculator.dzielenie(2,3)
        self.assertEqual(round(wynik,2), 0.67)
        self.assertNotEqual(wynik, 2)

if __name__ == '__main__':
    unittest.main()
