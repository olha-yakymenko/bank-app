import unittest

from ..CompanyAccount import CompanyAccount

class TestCreateCompanyAccount(unittest.TestCase):
    nazwa="FIRMA"
    nip="1111111111"

    def test_dlugosc_nip_krotki(self):
        krotki_nip="111"
        konto=CompanyAccount(self.nazwa,krotki_nip)
        self.assertEqual(konto.nip, None, "nip nie zostal zapisany")

    def test_dlugosc_nip_dlugi(self):
        krotki_nip="11111111111111111111111111111"
        konto=CompanyAccount(self.nazwa,krotki_nip)
        self.assertEqual(konto.nip, None, "nip nie zostal zapisany")

    def test_dlugosc_nip_dobry(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        self.assertEqual(konto.nip, self.nip, "nip zostal zapisany")

    def test_szybki_przelew_company_zle(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        konto.saldo=110
        konto.szybki_przelew(150)
        self.assertEqual(konto.saldo, 110, "Kwota jest powyzej dostepnej na saldzie")
    
    def test_szybki_przelew_company_dobrze(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        konto.saldo=160
        konto.szybki_przelew(150)
        self.assertEqual(konto.saldo, 5, "Przelew zostal wykonany")

    def test_szybki_przelew_company_ponizej_0(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        konto.saldo=160
        konto.szybki_przelew(160)
        self.assertEqual(konto.saldo, -5, "Przelew zostal wykonany")

    def test_kilka_przelewow_dobrze(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        konto.saldo=150
        konto.szybki_przelew(50)
        konto.przelew_przychodzacy(10)
        konto.przelew_wychodzacy(30)
        self.assertEqual(konto.saldo, 150-50-5+10-30, "Kwota jest ponizej dostepnej na saldzie")

    def test_kilka_przelewow_zle(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        konto.saldo=150
        konto.szybki_przelew(50)
        konto.przelew_przychodzacy(10)
        konto.przelew_wychodzacy(110)
        self.assertEqual(konto.saldo, 150-50-5+10, "Kwota jest ponizej dostepnej na saldzie")