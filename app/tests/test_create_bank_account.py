import unittest

from ..Konto import Konto

class TestCreateBankAccount2(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "06211888888"
    
    def test_przelew_wychodzacy_dobrze(self):
        konto =Konto()
        konto.saldo = 1000
        konto.przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 900, True)

    def test_przelew_wychodzacy_zle(self):
        konto =Konto()
        konto.saldo = 50
        konto.przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 50, False)

    def test_przelew_przychodzacy_dobrze(self):
        konto =Konto()
        konto.saldo = 1000
        konto.przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 1100)
