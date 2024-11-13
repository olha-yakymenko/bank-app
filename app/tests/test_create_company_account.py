import unittest

from ..CompanyAccount import CompanyAccount

class TestCreateCompanyAccount(unittest.TestCase):
    nazwa="FIRMA"
    nip="1111111111"

    def setUp(self):
        self.konto=CompanyAccount(self.nazwa,self.nip)

    def test_nazwa(self):
        # konto=CompanyAccount(self.nazwa,self.nip)
        self.assertEqual(self.konto.nazwa, self.nazwa, "Nazwa zostala zapisana")

    def test_dlugosc_nip_krotki(self):
        krotki_nip="111"
        konto=CompanyAccount(self.nazwa,krotki_nip)
        self.assertEqual(konto.nip, None, "nip nie zostal zapisany")

    def test_dlugosc_nip_dlugi(self):
        krotki_nip="11111111111111111111111111111"
        konto=CompanyAccount(self.nazwa,krotki_nip)
        self.assertEqual(konto.nip, None, "nip nie zostal zapisany")

    def test_dlugosc_nip_dobry(self):
        self.assertEqual(self.konto.nip, self.nip, "nip zostal zapisany")

    def test_przelew_wychodzacy_dobrze(self):
        self.konto.saldo = 1000
        self.konto.przelew_wychodzacy(100)
        self.assertEqual(self.konto.saldo, 900, True)

    def test_przelew_wychodzacy_zle(self):
        self.konto.saldo = 50
        self.konto.przelew_wychodzacy(100)
        self.assertEqual(self.konto.saldo, 50, False)

    def test_przelew_przychodzacy_dobrze(self):
        self.konto.saldo = 1000
        self.konto.przelew_przychodzacy(100)
        self.assertEqual(self.konto.saldo, 1100)


    def test_szybki_przelew_company_zle(self):
        self.konto.saldo=110
        self.konto.szybki_przelew(150)
        self.assertEqual(self.konto.saldo, 110, "Kwota jest powyzej dostepnej na saldzie")
    
    def test_szybki_przelew_company_dobrze(self):
        self.konto.saldo=160
        self.konto.szybki_przelew(150)
        self.assertEqual(self.konto.saldo, 5, "Przelew zostal wykonany")

    def test_szybki_przelew_company_ponizej_0(self):
        self.konto.saldo=160
        self.konto.szybki_przelew(160)
        self.assertEqual(self.konto.saldo, -5, "Przelew zostal wykonany")

    def test_kilka_przelewow_dobrze(self):
        self.konto.saldo=150
        self.konto.szybki_przelew(50)
        self.konto.przelew_przychodzacy(10)
        self.konto.przelew_wychodzacy(30)
        self.assertEqual(self.konto.saldo, 150-50-5+10-30)


    def test_historia_dobrze(self):
        self.konto.saldo = 1000
        self.konto.przelew_wychodzacy(100)
        self.konto.przelew_przychodzacy(200)
        self.konto.szybki_przelew(100)
        self.assertEqual(self.konto.historia, [-100, 200, -100, -5])