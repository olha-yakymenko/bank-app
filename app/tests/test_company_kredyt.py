import unittest
from parameterized import parameterized
from ..CompanyAccount import CompanyAccount

class TestCompanyKredyt(unittest.TestCase):
    nazwa="Nazwa"
    nip="11111111111"

    def setUp(self):
        self.konto = CompanyAccount( self.nazwa, self.nip)

    @parameterized.expand([
        ([-100, 200, -33, 10, 200, 50], 777, 1000, 777),
        ([-100, 200, -33, 10, 200, 1775], 5000, 1000, 6000),
        ([-100, 200, -33, 10, 200], 5000, 1000, 5000), 
        ([-100, 200, 1775, -33, 10, 200], 2000, 1000, 3000),  
        ([-100, 200, -33, 10, 200, 1775], 5000, 10000, 5000),
        ([], 1000, 200, 1000),
        ([-100, 200, -33, 10, 200, 1775], 1000, 0, 1000),
        ])
    
    def test_personal_kredyt(self, historia, saldo, kredyt, expected):
        self.konto.historia=historia
        self.konto.saldo=saldo
        self.konto.zaciagnij_kredyt(kredyt)
        self.assertEqual(self.konto.saldo, expected, "Saldo nie zostalo zwiekszone")