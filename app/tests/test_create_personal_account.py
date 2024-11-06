import unittest
from ..PersonalAccount import PersonalAccount
class TestCreateBankAccount(unittest.TestCase):
    imie="Dariusz"
    nazwisko="Januszewski"
    pesel="06211888888"

    def test_tworzenie_konta(self):
        pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(pierwsze_konto.imie, self.imie, "Imie zostało zapisane!")
        self.assertEqual(pierwsze_konto.nazwisko, self.nazwisko, "Nazwisko zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, self.pesel, "Saldo jest zerowe!")
        
    def test_za_krotki_pesel(self):
        krotki_pesel="123"
        konto=PersonalAccount(self.imie, self.nazwisko, krotki_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")

    def test_za_dlugi_pesel(self):
        dlugi_pesel="123878669696966969"
        konto=PersonalAccount(self.imie, self.nazwisko, dlugi_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")

    def test_zly_kod_dobry_rok(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel, "Prombkjjgkghgg")
        self.assertEqual(konto.saldo,0, "Kod promocyjny jest zly")

    def test_dobry_kod_dobry_rok(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel,  "PROM_123")
        self.assertEqual(konto.saldo, 50, "Kod promocyjny jest dobry")

    def test_zle_kod_dobry_rok(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel,  "PROM_876586")
        self.assertEqual(konto.saldo, 0, "Kod promocyjny jest zly")

    def test_rok_zle_kod_zle(self):
        konto = PersonalAccount(self.imie, self.nazwisko, "5905158888",  "PROM_876586")
        self.assertEqual(konto.saldo, 0, "Promocja jest niedostepna dla tego uzytkowanika")

    def test_rok_dobrze_kod_zle(self):
        konto = PersonalAccount(self.imie, self.nazwisko, "6105158888",  "Prgdgbk")
        self.assertEqual(konto.saldo, 0, "Promocja jest niedostepna dla tego uzytkowanika")
    
    def test_saldo_zero_gdy_brak_kodu(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(konto.saldo, 0, "Saldo powinno wynosić 0, gdy nie podano kodu promocyjnego")

    def test_szybki_przelew_personal_zle(self):
        konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.saldo=110
        konto.szybki_przelew(150)
        self.assertEqual(konto.saldo, 110, "Kwota jest powyzej dostepnej na saldzie")
    
    def test_szybki_przelew_personal_dobrze(self):
        konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.saldo=161
        konto.szybki_przelew(160)
        self.assertEqual(konto.saldo, 0, "Przelew zostal wykonany")

    def test_szybki_przelew_personal_ponizej_0(self):
        konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.saldo=160
        konto.szybki_przelew(160)
        self.assertEqual(konto.saldo, 160-160-1, "Przelew zostal wykonany")

    def test_kilka_przelewow_dobrze(self):
        konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.saldo=150
        konto.szybki_przelew(50)
        konto.przelew_przychodzacy(10)
        konto.przelew_wychodzacy(30)
        self.assertEqual(konto.saldo, 150-50-1+10-30)

    def test_historia_dobrze(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.przelew_wychodzacy(100)
        konto.przelew_przychodzacy(200)
        konto.szybki_przelew(100)
        self.assertEqual(konto.historia, [-100, 200, -100, -1])

    