import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie="Dariusz"
    nazwisko="Januszewski"
    pesel="12345678910"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "pesel nie zostal zapisany")
    # def test_za_krotki_pesel(self):
    #     krotki_pesel="123"
    #     konto=Konto(self.imie, self.nazwisko)
