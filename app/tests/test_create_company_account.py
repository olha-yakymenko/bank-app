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

    def test_przelew_wychodzacy_dobrze(self):
        konto = CompanyAccount(self.nazwa, self.nip)
        konto.saldo = 1000
        konto.przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 900, True)
    def test_przelew_wychodzacy_zle(self):
        konto = CompanyAccount(self.nazwa, self.nip)
        konto.saldo = 50
        konto.przelew_wychodzacy(100)
        self.assertEqual(konto.saldo, 50, False)
    def test_przelew_przychodzacy_dobrze(self):
        konto = CompanyAccount(self.nazwa, self.nip)
        konto.saldo = 1000
        konto.przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 1100)
    def test_przelew_przychodzacy_dobrze(self):
        konto = CompanyAccount(self.nazwa, self.nip)
        konto.saldo = 1000
        konto.przelew_przychodzacy(100)
        self.assertEqual(konto.saldo, 1100)

    # def test_outgoing_express_transfer_company(self):
    #     konto=CompanyAccount(self.name, self.nip)
    #     konto.saldo=110
    #     konto.outgoing_express_transfer(150)
    #     self.assertEqual(konto.saldo, 110, "nnonoi")
    #     def test