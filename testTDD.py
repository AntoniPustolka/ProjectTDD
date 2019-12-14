import unittest
import program

class TestProgram(unittest.TestCase):

    def test_zwroc_100(self):
        wynik = program.zwroc_100()
        self.assertEqual(wynik, 100)

    def test_zwroc_parametr(self):
        self.assertEqual(program.zwroc_parametr('Olek'),'Olek')

    def test_inna_metoda_2(self):
        pass

#if __name__ == '__main__':
    #unittest.main()
