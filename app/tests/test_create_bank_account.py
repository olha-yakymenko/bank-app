import unittest

from ..Konto import Konto

class TestCreateBankAccount(unittest.TestCase):
    imie="Dariusz"
    nazwisko="Januszewski"
    pesel="12345678910"

    def test_tworzenie_konta(self):
        pierwsze_konto = Konto(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        # self.assertEqual(pierwsze_konto.pesel, self.pesel, "pesel nie zostal zapisany")
    def test_za_krotki_pesel(self):
        krotki_pesel="123"
        konto=Konto(self.imie, self.nazwisko, krotki_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")
    def test_za_dlugi_pesel(self):
        dlugi_pesel="123878669696966969"
        konto=Konto(self.imie, self.nazwisko, dlugi_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")

    def test_zly_kod_sufix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "Prombkjjgkghgg")
        self.assertEqual(konto.saldo,0, "Kod promocyjny jest zly")

    def test_dobry_kod_sufix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_123")
        self.assertEqual(konto.saldo, 50, "Kod promocyjny jest dobry")

    def test_poczatek_kod_sufix(self):
        konto = Konto(self.imie, self.nazwisko, self.pesel, "PROM_876586")
        self.assertEqual(konto.saldo, 0, "Kod promocyjny jest zly")