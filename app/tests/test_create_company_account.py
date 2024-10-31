import unittest

from ..CompanyAccount import CompanyAccount

class TestCreateCompanyAccount(unittest.TestCase):
    nazwa="FIRMA"
    nip="1111111111"

    def test_dlugosc_nip_krotki(self):
        krotki_nip="111"
        konto=CompanyAccount(self.nazwa,krotki_nip)
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "nip nie zostal zapisany")
        
    def test_dlugosc_nip_dlugi(self):
        krotki_nip="11111111111111111111111111111"
        konto=CompanyAccount(self.nazwa,krotki_nip)
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "nip nie zostal zapisany")

    def test_dlugosc_nip_dobry(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        self.assertEqual(konto.nip, self.nip, "nip zostal zapisany")

    def test_szybki_przelew_company_bad(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        konto.saldo=110
        konto.szybki_przelew(150)
        self.assertEqual(konto.saldo, 110, "Kwota jest powyzej dostepnej na saldzie")
    
    def test_szybki_przelew_company_good(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        konto.saldo=160
        konto.szybki_przelew(150)
        self.assertEqual(konto.saldo, 5, "Kwota jest powyzej dostepnej na saldzie")

    def test_szybki_przelew_company_good2(self):
        konto=CompanyAccount(self.nazwa, self.nip)
        konto.saldo=160
        konto.szybki_przelew(160)
        self.assertEqual(konto.saldo, -5, "Kwota jest powyzej dostepnej na saldzie")
