import unittest
from ..PersonalAccount import PersonalAccount
from ..AccountRegistry import AccountRegistry

class TestRegistry(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "06211888888"
    pesel_66 = "89394029495"
    pesel_77 = "893940739495"

    @classmethod
    def setUpClass(cls):
        cls.konto = PersonalAccount(cls.imie, cls.nazwisko, cls.pesel)
        cls.konto_66 = PersonalAccount(cls.imie, cls.nazwisko, cls.pesel_66)
        cls.konto_77 = PersonalAccount(cls.imie, cls.nazwisko, cls.pesel_77)

    def setUp(self):
        AccountRegistry.registry = []  # Resetowanie rejestru przed każdym testem

    def test_add_account(self):
        AccountRegistry.add_account(self.konto)
        self.assertEqual(AccountRegistry.get_accounts_count(), 1, "Niepoprawna liczba kont w rejestrze")

    def test_add_multiple_accounts(self):
        AccountRegistry.add_account(self.konto_66)
        AccountRegistry.add_account(self.konto_77)
        self.assertEqual(AccountRegistry.get_accounts_count(), 2, "Niepoprawna liczba kont w rejestrze")

    def test_search_by_pesel(self):
        AccountRegistry.add_account(self.konto)
        AccountRegistry.add_account(self.konto_66)
        AccountRegistry.add_account(self.konto_77)
        result = AccountRegistry.search_by_pesel(self.pesel)
        self.assertEqual(result, self.konto, "Niepoprawne konto znalezione po PESEL!")

    def test_search_by_invalid_pesel(self):
        AccountRegistry.add_account(self.konto)
        AccountRegistry.add_account(self.konto_66)
        result = AccountRegistry.search_by_pesel(self.konto_77)
        self.assertIsNone(result, "Pesel nie jest znaleziony")