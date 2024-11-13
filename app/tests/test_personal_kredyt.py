import unittest
from parameterized import parameterized
from ..PersonalAccount import PersonalAccount

class TestPersonalKredyt(unittest.TestCase):
    imie="Dariusz"
    nazwisko="Januszewski"
    pesel="06211888888"

    def setUp(self):
        self.konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        

    @parameterized.expand([
        ([-100, 200, -33, 10, 200, 50], 1000, 1000),
        ([-100, 200, -5000, 1, -2, -3], 1000, 0),
        ([-100, 200, 5000, 1, -2, -3], 1000, 1000),
        ([-100, 200, 500, 100, -1, 300], 10000, 0),
        ([200, 500], 10000, 0),
        ([-666, 200000, 500, -1, 200], 10000, 10000),
    ])
    
    def test_personal_kredyt(self, historia, kredyt, expected):
        self.konto.historia=historia
        self.konto.zaciagnij_kredyt(kredyt)
        self.assertEqual(self.konto.saldo, expected, "Saldo nie zostalo zwiekszone")