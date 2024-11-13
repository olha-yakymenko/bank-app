# import unittest
#
# from ..Konto import Konto
#
# class TestCreateBankAccount2(unittest.TestCase):
#     imie = "Dariusz"
#     nazwisko = "Januszewski"
#     pesel = "06211888888"
#
#     def setUp(self):
#         self.konto=Konto()
#
#     def test_przelew_wychodzacy_dobrze(self):
#         self.konto.saldo = 1000
#         self.konto.przelew_wychodzacy(100)
#         self.assertEqual(self.konto.saldo, 900, True)
#
#     def test_przelew_wychodzacy_zle(self):
#         self.konto.saldo = 50
#         self.konto.przelew_wychodzacy(100)
#         self.assertEqual(self.konto.saldo, 50, False)
#
#     def test_przelew_przychodzacy_dobrze(self):
#         self.konto.saldo = 1000
#         self.konto.przelew_przychodzacy(100)
#         self.assertEqual(self.konto.saldo, 1100)
