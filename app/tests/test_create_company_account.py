import unittest
from parameterized import parameterized
from ..CompanyAccount import CompanyAccount

class TestCreateCompanyAccount(unittest.TestCase):
    nazwa="FIRMA"
    nip="1111111111"

    def setUp(self):
        self.konto=CompanyAccount(self.nazwa,self.nip)

    def test_nazwa(self):
        self.assertEqual(self.konto.nazwa, self.nazwa, "Nazwa zostala zapisana")

    @parameterized.expand([
        ("krótki nip", "111", None),
        ("dłudi nip", "11111111111111111111111111111", None),
        ("poprawny nip", "1234567890", "1234567890"),  
    ])
    def test_dlugosc_nip(self, name, nip_input, expected_nip):
        konto = CompanyAccount(self.nazwa, nip_input)
        self.assertEqual(konto.nip, expected_nip, f"{name} - nip nie zostal zapisany")

    @parameterized.expand([
        ("przelew wychodzący - poprawnie", 1000, 100, 900),
        ("przelew wychodzący - za mało środków", 50, 100, 50),
    ])
    def test_przelew_wychodzacy(self, name, saldo_start, przelew_kwota, saldo_end):
        self.konto.saldo = saldo_start
        self.konto.przelew_wychodzacy(przelew_kwota)
        self.assertEqual(self.konto.saldo, saldo_end, f"{name} - saldo niepoprawne po przelewie wychodzącym")

    def test_przelew_przychodzacy_dobrze(self):
        self.konto.saldo = 1000
        self.konto.przelew_przychodzacy(100)
        self.assertEqual(self.konto.saldo, 1100)

    @parameterized.expand([
        ("szybki przelew - za mało środków", 110, 150, 110),
        ("szybki przelew - wystarczająca kwota", 160, 150, 5),
        ("szybki przelew - saldo poniżej 0", 160, 160, -5),
    ])
    def test_szybki_przelew(self, name, saldo_start, przelew_kwota, saldo_end):
        self.konto.saldo = saldo_start
        self.konto.szybki_przelew(przelew_kwota)
        self.assertEqual(self.konto.saldo, saldo_end, f"{name} - saldo niepoprawne po szybkim przelewie")

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