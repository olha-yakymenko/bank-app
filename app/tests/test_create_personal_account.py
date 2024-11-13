import unittest
from parameterized import parameterized
from ..PersonalAccount import PersonalAccount

class TestCreateBankAccount(unittest.TestCase):
    imie = "Dariusz"
    nazwisko = "Januszewski"
    pesel = "06211888888"

    def setUp(self):
        self.konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)

    
    @parameterized.expand([
        ("test tworzenia konta", "Dariusz", "Januszewski", "06211888888", 0, []),
    ])
    def test_tworzenie_konta(self, name, imie, nazwisko, pesel, saldo, historia):
        konto = PersonalAccount(imie, nazwisko, pesel)  
        self.assertEqual(konto.imie, imie, f"{name} - imie nie zostało zapisane!")
        self.assertEqual(konto.nazwisko, nazwisko, f"{name} - nazwisko nie zostało zapisane!")
        self.assertEqual(konto.saldo, saldo, f"{name} - saldo nie zostało ustawione na 0!")
        self.assertEqual(konto.pesel, pesel, f"{name} - pesel nie został zapisany!")
        self.assertEqual(konto.historia, historia, f"{name} - historia transakcji nie jest pusta!")

    @parameterized.expand([
        ("test za krótki pesel", "123", "Niepoprawny pesel"),
        ("test za długi pesel", "123878669696966969", "Niepoprawny pesel"),
    ])
    def test_pesel(self, name, pesel, expected_result):
        konto = PersonalAccount(self.imie, self.nazwisko, pesel)
        self.assertEqual(konto.pesel, expected_result, f"{name} - pesel nie został zapisany")

    @parameterized.expand([
        ("test zły kod, dobry rok", "Prombkjjgkghgg", "6105158888", 0),
        ("test dobry kod, zły rok", "PROM_123", "5905158888", 0),
        ("test dobry kod, dobry rok", "PROM_123", "6105158888", 50),
        ("test zły kod i rok", "PROM_876586", "5905158888", 0),
        ("test brak kodu promocyjnego", None, "6105158888", 0),
    ])
    def test_kod_promocyjny(self, name, kod, pesel, expected_saldo):
        konto = PersonalAccount(self.imie, self.nazwisko, pesel, kod)
        self.assertEqual(konto.saldo, expected_saldo, f"{name} - niepoprawne saldo")

    @parameterized.expand([
        ("przelew wychodzący - poprawnie", 1000, 100, 900),
        ("przelew wychodzący - za mało środków", 50, 100, 50),
    ])
    def test_przelew_wychodzacy(self, name, saldo_start, przelew_kwota, saldo_end):
        self.konto.saldo = saldo_start
        self.konto.przelew_wychodzacy(przelew_kwota)
        self.assertEqual(self.konto.saldo, saldo_end, f"{name} - saldo niepoprawne po przelewie wychodzącym")

    def test_przelew_przychodzacy(self):
        self.konto.saldo = 1000
        self.konto.przelew_przychodzacy(100)
        self.assertEqual(self.konto.saldo, 1100)

    @parameterized.expand([
        ("szybki przelew - za mało środków", 110, 150, 110),
        ("szybki przelew - wystarczająca kwota", 161, 160, 0),
        ("szybki przelew - saldo poniżej 0", 160, 160, -1),
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
        self.assertEqual(self.konto.saldo, 150-50-1+10-30)

    def test_historia_dobrze(self):
        self.konto.saldo = 1000
        self.konto.przelew_wychodzacy(100)
        self.konto.przelew_przychodzacy(200)
        self.konto.szybki_przelew(100)
        self.assertEqual(self.konto.historia, [-100, 200, -100, -1])



