

import unittest
from parameterized import parameterized

from ..PersonalAccount import PersonalAccount
from ..AccountRegistry import AccountRegistry
imie = "Dariusz"
nazwisko = "Januszewski"
pesel = "06211888888"
pesel_66 = "89394029495"
pesel_77 = "893940739495"
konto = PersonalAccount(imie, nazwisko, pesel)


class TestRegistry(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "06211888888"
    pesel_1 = "89394029495"
    pesel_2 = "893940739495"
    konto = PersonalAccount(imie, nazwisko, pesel)
    konto1 = PersonalAccount(imie, nazwisko, pesel_1)
    konto2 = PersonalAccount(imie, nazwisko, pesel_2)

    def setUp(self):
        AccountRegistry.registry = []  

    @parameterized.expand([
        ("single_account", [konto], 1),
        ("multiple_accounts", [
            konto1,
            konto2
        ], 2),
    ])
    def test_add_accounts(self, name, accounts_to_add, expected_count):
        for account in accounts_to_add:
            AccountRegistry.add_account(account)
        self.assertEqual(AccountRegistry.get_accounts_count(), expected_count, f"Niepoprawna liczba kont: {name}")



    @parameterized.expand([
        ("single_account", [konto], "06211888888", konto),
        ("multiple_accounts", [
            konto1,
            konto2
        ], "89394029495", konto1),
        ("nonexistent_account", [
            konto1, konto2
        ], "43546478489", None),
    ])
    def test_search_by_pesel(self, name, accounts_to_add, searching_pesel, expected_account):
        for account in accounts_to_add:
            AccountRegistry.add_account(account)
        found_account = AccountRegistry.search_by_pesel(searching_pesel)
        if expected_account is None:
            self.assertEqual(found_account, None, f"Niepoprawny wynik wyszukiwania: {name}")
        else:
            self.assertEqual(found_account.imie, expected_account.imie, f"Niepoprawne imie: {name}")
            self.assertEqual(found_account.nazwisko, expected_account.nazwisko, f"Niepoprawne nazwisko: {name}")
            self.assertEqual(found_account.pesel, expected_account.pesel, f"Niepoprawny pesel: {name}")

    @parameterized.expand([
        ("delete_existing_account", [konto], "06211888888"),
       ("delete_nonexistent_account", [konto], "43546478489"),
    ])
    def test_delete_account(self, name, accounts_to_add, deleting_pesel):
        for account in accounts_to_add:
            AccountRegistry.add_account(account)
        result1 = AccountRegistry.delete_by_pesel(deleting_pesel)
        result2=AccountRegistry.search_by_pesel(deleting_pesel)
        self.assertEqual(result1, result2, f"Pesel nie jest znaleziony: {name}")
