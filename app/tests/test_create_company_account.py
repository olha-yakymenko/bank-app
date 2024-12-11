import unittest
from unittest.mock import patch
from ..CompanyAccount import CompanyAccount
from unittest.mock import patch, MagicMock 
from ..SMTPClient import SMTPClient
from datetime import datetime

class TestTworzenieKontaFirmowego(unittest.TestCase):
    nazwa = "Januszex sp. z o.o"
    nip = "8461627563"  

    @patch('app.CompanyAccount.CompanyAccount.is_nip_valid')
    def test_tworzenie_konta(self, mock_is_nip_valid):
        mock_is_nip_valid.return_value = True
        pierwsze_konto = CompanyAccount(self.nazwa, self.nip)
        
        self.assertEqual(pierwsze_konto.nazwa, self.nazwa, "Nazwa firmy nie została zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "NIP nie zostało zapisane!")

    def test_zbyt_dlugi_nip(self):
        konto = CompanyAccount(self.nazwa, "84616275639887")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "NIP jest za długi, powinno być 'Niepoprawny NIP!'")

    def test_zbyt_krotki_nip(self):
        konto = CompanyAccount(self.nazwa, "846162")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "NIP jest za krótki, powinno być 'Niepoprawny NIP!'")
    
    @patch('app.CompanyAccount.CompanyAccount.is_nip_valid')
    def test_incorrect_account(self, mock_is_nip_valid):
        mock_is_nip_valid.return_value = False
        incorrect_nip = "asdfghjklp"  
        with self.assertRaises(ValueError):
            konto = CompanyAccount(self.nazwa, incorrect_nip)

    @patch('app.CompanyAccount.CompanyAccount.is_nip_valid')
    def test_valid_nip_but_invalid_response(self, mock_is_nip_valid):
        mock_is_nip_valid.return_value = False
        
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 404 
            incorrect_nip = "8461627563"  
            with self.assertRaises(ValueError):
                konto = CompanyAccount(self.nazwa, incorrect_nip)
            
    @patch('app.CompanyAccount.CompanyAccount.is_nip_valid')
    def test_correct_nip_with_valid_api_response(self, mock_is_nip_valid):
        mock_is_nip_valid.return_value = True
        
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200  
            valid_nip = "8461627563"
            konto = CompanyAccount(self.nazwa, valid_nip)
            
            self.assertEqual(konto.nip, valid_nip)
            self.assertEqual(konto.nazwa, self.nazwa)

    @patch('app.CompanyAccount.CompanyAccount.is_nip_valid')
    def test_invalid_nip_with_404(self, mock_is_nip_valid):
        mock_is_nip_valid.return_value = False
    
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            incorrect_nip = "8461627563"  
            with self.assertRaises(ValueError):
                konto = CompanyAccount(self.nazwa, incorrect_nip)

    @patch('app.CompanyAccount.CompanyAccount.is_nip_valid')
    def test_invalid_nip_with_500(self, mock_is_nip_valid):
        mock_is_nip_valid.return_value = False
    
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            incorrect_nip = "8461627563"  
            with self.assertRaises(ValueError):
                konto = CompanyAccount(self.nazwa, incorrect_nip)

    def test_empty_nip(self):
        konto = CompanyAccount(self.nazwa, "")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "NIP nie może być pusty!")

    @patch('app.CompanyAccount.CompanyAccount.is_nip_valid')
    def test_valid_nip_with_unexpected_api_status(self, mock_is_nip_valid):
        mock_is_nip_valid.return_value = True
        
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 202 
            valid_nip = "8461627563"
            konto = CompanyAccount(self.nazwa, valid_nip)
            
            self.assertEqual(konto.nip, valid_nip)
            self.assertEqual(konto.nazwa, self.nazwa)

    @patch('requests.get')
    def test_api_response_400(self, mock_get):
        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {"error": "Bad Request"}
        
        with self.assertRaises(ValueError):
            konto = CompanyAccount(self.nazwa, self.nip)
            
    @patch('requests.get')
    def test_api_response_403(self, mock_get):
        mock_get.return_value.status_code = 403
        mock_get.return_value.json.return_value = {"error": "Forbidden"}
        
        with self.assertRaises(ValueError):
            konto = CompanyAccount(self.nazwa, self.nip)

    @patch('requests.get')
    def test_express_fee(self, mock_get):
        mock_get.return_value.status_code = 200  
        mock_get.return_value.json.return_value = {"valid": True}  
        konto = CompanyAccount(self.nazwa, self.nip)
        self.assertEqual(konto.express_fee, 5)  





# class TestSendHistoryToEmail(unittest.TestCase):
#     nazwa = "Januszex sp. z o.o"
#     nip = "8461627563" 
#     history=[334, 789]
#     date=datetime.now().strftime("%Y-%m-%d")
#     email="email@gmail.com"
#     @patch("app.")
#     def test_jedno_wywolanie(self):
#         smtp_client=SMTPClient()
#         smtp_client.send = MagicMock(return_value=True)
#         konto=CompanyAccount(self.nazwa, self.nip)
#         konto.historia=[334, 789]
#         result=konto.send_history_to_email(self.email, smtp_client)
#         smtp_client.send.assert_called_once()
#         smtp_client.send.assert_called_once_with(f'Wyciąg z dnia {datetime.now().strftime("%Y-%m-%d")}', f'Twoja historia konta to: {self.history}', self.email)


#     def test_send_history_to_email_personal_account(self):
#         konto=CompanyAccount(self.nazwa, self.nip)
#         konto.historia=[334, 789]
#         mock_smtp = MagicMock()
#         mock_smtp.send.return_value = True
        
#         result = konto.send_history_to_email(self.email, mock_smtp)
        
#         mock_smtp.send.assert_called_once_with(
#             f"Wyciąg z dnia {self.date}", 
#             f"Twoja historia konta to: {self.history}", 
#             self.email
#         )

#         self.assertTrue(result)

#     def test_send_history_to_email_company_account(self):
#         konto=CompanyAccount(self.nazwa, self.nip)
#         konto.historia=[334, 789]
#         mock_smtp = MagicMock()
#         mock_smtp.send.return_value = True
#         result = konto.send_history_to_email(self.email, mock_smtp)
        
#         # Sprawdzamy, czy metoda send została wywołana
#         mock_smtp.send.assert_called_once_with(
#             f"Wyciąg z dnia {self.date}", 
#             f"Twoja historia konta to: {konto.historia}",
#             self.email
#         )
        
#         # Sprawdzamy, czy wynik to True (sukces wysyłki)
#         self.assertTrue(result)

#     @patch('datetime.datetime')  # Mockowanie datetime
#     def test_send_history_to_email_fail(self, mock_datetime):
#         # Przygotowanie mocka dla datetime
#         mock_datetime.now.return_value = datetime(2024, 12, 10)  # Zmieniamy datę na konkretną
#         # Tworzymy obiekt PersonalAccount z przykładową historią
#         konto=CompanyAccount(self.nazwa, self.nip)
#         # Mockowanie klienta SMTP
#         mock_smtp = MagicMock()
#         # Ustawiamy, że metoda send zwróci False (symulujemy błąd)
#         mock_smtp.send.return_value = False
#         konto.historia=[334, 789]
        
#         # Wywołanie metody send_history_to_email
#         result = konto.send_history_to_email(self.email, mock_smtp)
        
#         # Sprawdzamy, czy metoda send została wywołana
#         mock_smtp.send.assert_called_once_with(
#             f"Wyciąg z dnia {self.date}", 
#             f"Twoja historia konta to: {konto.historia}",
#             self.email
#         )
        
#         # Sprawdzamy, czy wynik to False (błąd wysyłki)
#         self.assertFalse(result)

#     # @patch('datetime.datetime')  # Mockowanie datetime
#     # def test_send_history_to_email_called(self, mock_datetime):
#     #     # Przygotowanie mocka dla datetime
#     #     mock_datetime.now.return_value = datetime(2024, 12, 10)  # Zmieniamy datę na konkretną
#     #     # Tworzymy obiekt PersonalAccount z przykładową historią
#     #     konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
#     #     konto.historia=[334, 789]
#     #     # Mockowanie klienta SMTP
#     #     mock_smtp = MagicMock()
        
#     #     # Wywołanie metody send_history_to_email
#     #     konto.send_history_to_email('test@example.com', mock_smtp)
        
#     #     # Sprawdzamy, czy metoda send została wywołana
#     #     mock_smtp.send.assert_called_once()




# class TestSendHistoryToEmail(unittest.TestCase):
#     imie = "Dariusz"
#     nazwisko = "Januszewski"
#     pesel = "06211888888"
#     history=[334, 789]
#     date=datetime.now().strftime("%Y-%m-%d")
#     email="email@gmail.com"
#     @patch("app.PersonalAccount.SMTPClient.send")
#     def test_jedno_wywolanie(self):
#         smtp_client=SMTPClient()
#         smtp_client.send = MagicMock(return_value=True)
#         konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
#         konto.historia=[334, 789]
#         result=konto.send_history_to_email(self.email, smtp_client)
#         smtp_client.send.assert_called_once()
#         smtp_client.send.assert_called_once_with(f'Wyciąg z dnia {datetime.now().strftime("%Y-%m-%d")}', f'Twoja historia konta to: {self.history}', self.email)


#     def test_send_history_to_email_personal_account(self):
#         konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
#         konto.historia=[334, 789]
#         mock_smtp = MagicMock()
#         mock_smtp.send.return_value = True
        
#         result = konto.send_history_to_email(self.email, mock_smtp)
        
#         mock_smtp.send.assert_called_once_with(
#             f"Wyciąg z dnia {self.date}", 
#             f"Twoja historia konta to: {self.history}", 
#             self.email
#         )

#         self.assertTrue(result)

#     def test_send_history_to_email_company_account(self):
#         konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
#         konto.historia=[334, 789]
#         mock_smtp = MagicMock()
#         mock_smtp.send.return_value = True
#         result = konto.send_history_to_email(self.email, mock_smtp)
        
#         # Sprawdzamy, czy metoda send została wywołana
#         mock_smtp.send.assert_called_once_with(
#             f"Wyciąg z dnia {self.date}", 
#             f"Twoja historia konta to: {konto.historia}",
#             self.email
#         )
        
#         # Sprawdzamy, czy wynik to True (sukces wysyłki)
#         self.assertTrue(result)

#     @patch('datetime.datetime')  # Mockowanie datetime
#     def test_send_history_to_email_fail(self, mock_datetime):
#         # Przygotowanie mocka dla datetime
#         mock_datetime.now.return_value = datetime(2024, 12, 10)  # Zmieniamy datę na konkretną
#         # Tworzymy obiekt PersonalAccount z przykładową historią
#         konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
#         # Mockowanie klienta SMTP
#         mock_smtp = MagicMock()
#         # Ustawiamy, że metoda send zwróci False (symulujemy błąd)
#         mock_smtp.send.return_value = False
#         konto.historia=[334, 789]
        
#         # Wywołanie metody send_history_to_email
#         result = konto.send_history_to_email(self.email, mock_smtp)
        
#         # Sprawdzamy, czy metoda send została wywołana
#         mock_smtp.send.assert_called_once_with(
#             f"Wyciąg z dnia {self.date}", 
#             f"Twoja historia konta to: {konto.historia}",
#             self.email
#         )
        
#         # Sprawdzamy, czy wynik to False (błąd wysyłki)
#         self.assertFalse(result)

#     # @patch('datetime.datetime')  # Mockowanie datetime
#     # def test_send_history_to_email_called(self, mock_datetime):
#     #     # Przygotowanie mocka dla datetime
#     #     mock_datetime.now.return_value = datetime(2024, 12, 10)  # Zmieniamy datę na konkretną
#     #     # Tworzymy obiekt PersonalAccount z przykładową historią
#     #     konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
#     #     konto.historia=[334, 789]
#     #     # Mockowanie klienta SMTP
#     #     mock_smtp = MagicMock()
        
#     #     # Wywołanie metody send_history_to_email
#     #     konto.send_history_to_email('test@example.com', mock_smtp)
        
#     #     # Sprawdzamy, czy metoda send została wywołana
#     #     mock_smtp.send.assert_called_once()

