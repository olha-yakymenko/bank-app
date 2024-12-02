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

    def test_initial_balance(self):
        self.assertEqual(self.konto.saldo, 0, "Początkowe saldo wynosi 0")

