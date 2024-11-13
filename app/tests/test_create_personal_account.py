import unittest
from ..PersonalAccount import PersonalAccount
from parameterized import parameterized
class TestCreateBankAccount(unittest.TestCase):
    imie="Dariusz"
    nazwisko="Januszewski"
    pesel="06211888888"

    def setUp(self):
        self.konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)

    # @parameterized.expand([
    #     ("imie", "imie", "Dariusz"),
    #     ("nazwisko", "nazwisko", "Januszewski"),
    #     ("saldo", "saldo", 0),
    #     ("pesel", "pesel", "06211888888"),
    #     ("historia", "historia", []),
    # ])
    # def test_tworzenie_konta(self, _, attribute, expected_value):
    #     self.assertEqual(getattr(self.konto, attribute), expected_value, f"{attribute} jest poprawnie ustawione")
    #
    # @parameterized.expand([
    #     ("za_krotki_pesel", "123", "Niepoprawny pesel"),
    #     ("za_dlugi_pesel", "123878669696966969", "Niepoprawny pesel"),
    # ])
    # def test_pesel_dlugosc(self, _, pesel, expected_value):
    #     konto = PersonalAccount(self.imie, self.nazwisko, pesel)
    #     self.assertEqual(konto.pesel, expected_value, "Pesel nie zostal zapisany")
    #
    # @parameterized.expand([
    #     ("zly_kod_dobry_rok", "06211888888", "Prombkjjgkghgg", 0),
    #     ("dobry_kod_dobry_rok", "06211888888", "PROM_123", 50),
    #     ("zly_kod_dobry_rok", "06211888888", "PROM_876586", 0),
    #     ("rok_zle_kod_zle", "5905158888", "PROM_876586", 0),
    #     ("rok_dobrze_kod_zle", "6105158888", "Prgdgbk", 0),
    #     ("brak_kodu", "06211888888", None, 0),
    # ])
    # def test_kod_promocyjny(self, _, pesel, kod, expected_saldo):
    #     konto = PersonalAccount(self.imie, self.nazwisko, pesel, kod)
    #     self.assertEqual(konto.saldo, expected_saldo, "Saldo niezgodne z oczekiwaniem")
    #
    # @parameterized.expand([
    #     ("ponizej_salda", 110, 150, 110),
    #     ("dokladne_saldo", 161, 160, 0),
    #     ("ponizej_z_oplata", 160, 160, 160 - 160 - 1),
    # ])
    # def test_szybki_przelew(self, _, saldo, kwota_przelewu, expected_saldo):
    #     self.konto.saldo = saldo
    #     self.konto.szybki_przelew(kwota_przelewu)
    #     self.assertEqual(self.konto.saldo, expected_saldo, "Saldo po przelewie niezgodne z oczekiwaniem")
    #
    # @parameterized.expand([
    #     ("kilka_przelewow", 150, [(50, -51), (10, +10), (30, -30)], 150 - 51 + 10 - 30),
    # ])
    # def test_kilka_przelewow(self, _, saldo, transactions, expected_saldo):
    #     self.konto.saldo = saldo
    #     for kwota, wynik in transactions:
    #         if wynik < 0:
    #             self.konto.przelew_wychodzacy(abs(kwota))
    #         else:
    #             self.konto.przelew_przychodzacy(kwota)
    #     self.assertEqual(self.konto.saldo, expected_saldo, "Saldo po kilku przelewach niezgodne z oczekiwaniem")
    #
    # @parameterized.expand([
    #     ("historia_przelewow", 1000, [(-100, -100), (200, 200), (-100, -100), (-1, -1)], [-100, 200, -100, -1]),
    # ])
    # def test_historia(self, _, saldo, transactions, expected_historia):
    #     self.konto.saldo = saldo
    #     for kwota, wynik in transactions:
    #         if wynik == -1:
    #             self.konto.szybki_przelew(abs(kwota))
    #         elif wynik < 0:
    #             self.konto.przelew_wychodzacy(abs(kwota))
    #         else:
    #             self.konto.przelew_przychodzacy(kwota)
    #     self.assertEqual(self.konto.historia, expected_historia, "Historia operacji niezgodna z oczekiwaniem")


    def test_tworzenie_konta(self):
        #pierwsze_konto = PersonalAccount(self.imie, self.nazwisko, self.pesel)
        self.assertEqual(self.konto.imie, self.imie, "Imie zostało zapisane!")
        self.assertEqual(self.konto.nazwisko, self.nazwisko, "Nazwisko zostało zapisane!")
        self.assertEqual(self.konto.saldo, 0, "Saldo jest zerowe!")
        self.assertEqual(self.konto.pesel, self.pesel)
        self.assertEqual(self.konto.historia, [])
        
    def test_za_krotki_pesel(self):
        krotki_pesel="123"
        konto=PersonalAccount(self.imie, self.nazwisko, krotki_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")

    def test_za_dlugi_pesel(self):
        dlugi_pesel="123878669696966969"
        konto=PersonalAccount(self.imie, self.nazwisko, dlugi_pesel)
        self.assertEqual(konto.pesel, "Niepoprawny pesel", "Pesel nie zostal zapisany")

    def test_zly_kod_dobry_rok(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel, "Prombkjjgkghgg")
        self.assertEqual(konto.saldo,0, "Kod promocyjny jest zly")

    def test_dobry_kod_dobry_rok(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel,  "PROM_123")
        self.assertEqual(konto.saldo, 50, "Kod promocyjny jest dobry")

    def test_zle_kod_dobry_rok(self):
        konto = PersonalAccount(self.imie, self.nazwisko, self.pesel,  "PROM_876586")
        self.assertEqual(konto.saldo, 0, "Kod promocyjny jest zly")

    def test_rok_zle_kod_zle(self):
        konto = PersonalAccount(self.imie, self.nazwisko, "5905158888",  "PROM_876586")
        self.assertEqual(konto.saldo, 0, "Promocja jest niedostepna dla tego uzytkowanika")

    def test_rok_dobrze_kod_zle(self):
        konto = PersonalAccount(self.imie, self.nazwisko, "6105158888",  "Prgdgbk")
        self.assertEqual(konto.saldo, 0, "Promocja jest niedostepna dla tego uzytkowanika")

    def test_saldo_zero_gdy_brak_kodu(self):
        self.assertEqual(self.konto.saldo, 0, "Saldo powinno wynosić 0, gdy nie podano kodu promocyjnego")

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


    def test_szybki_przelew_personal_zle(self):
        self.konto.saldo=110
        self.konto.szybki_przelew(150)
        self.assertEqual(self.konto.saldo, 110, "Kwota jest powyzej dostepnej na saldzie")

    def test_szybki_przelew_personal_dobrze(self):
        self.konto.saldo=161
        self.konto.szybki_przelew(160)
        self.assertEqual(self.konto.saldo, 0, "Przelew zostal wykonany")

    def test_szybki_przelew_personal_ponizej_0(self):
        self.konto.saldo=160
        self.konto.szybki_przelew(160)
        self.assertEqual(self.konto.saldo, 160-160-1, "Przelew zostal wykonany")

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

    