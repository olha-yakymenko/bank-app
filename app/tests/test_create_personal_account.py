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
        ("test zły kod(dlugi), dobry rok", "Prombkjjgkghgg", "6105158888", 0),
        ("test zły kod(krotki), dobry rok", "Pro", "6105158888", 0),
        ("test dobry kod, zły rok", "PROM_123", "5905158888", 0),
        ("test dobry kod, dobry rok", "PROM_123", "6105158888", 50),
        ("test zły kod i rok", "PROM_876", "5905158888", 0),
        ("test zły kod (niepoprawny) i dobry rok", "AAA_876", "6105158888", 0),
        ("test brak kodu promocyjnego", None, "6105158888", 0),
    ])
    def test_kod_promocyjny(self, name, kod, pesel, expected_saldo):
        konto = PersonalAccount(self.imie, self.nazwisko, pesel, kod)
        self.assertEqual(konto.saldo, expected_saldo, f"{name} - niepoprawne saldo")

    # def test_jedno_wywolanie(self):
    #     smtp_client=SMTPClient()
    #     smtp_client.send = MagicMock(return_value=True)
    #     self.email="email@gmail.com"
    #     konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.historia=[334, 789]
    #     result=konto.send_history_to_email(self.email, smtp_client)
    #     smtp_client.send.assert_called_once()
    #     smtp_client.send.assert_called_once_with(f'Wyciąg z dnia {datetime.now().strftime("%Y-%m-%d")}', f'Twoja historia konta to: {konto.historia}', self.email)


    # def test_send_history_to_email_personal_account(self):
    #     konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.historia=[334, 789]
    #     mock_smtp = MagicMock()
    #     mock_smtp.send.return_value = True
        
    #     result = konto.send_history_to_email(self.email, mock_smtp)
        
    #     mock_smtp.send.assert_called_once_with(
    #         f"Wyciąg z dnia {self.date}", 
    #         f"Twoja historia konta to: {self.history}", 
    #         self.email
    #     )

    #     self.assertTrue(result)

    # def test_send_history_to_email_company_account(self):
    #     konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     konto.historia=[334, 789]
    #     mock_smtp = MagicMock()
    #     mock_smtp.send.return_value = True
    #     result = konto.send_history_to_email(self.email, mock_smtp)
        
    #     # Sprawdzamy, czy metoda send została wywołana
    #     mock_smtp.send.assert_called_once_with(
    #         f"Wyciąg z dnia {self.date}", 
    #         f"Twoja historia konta to: {konto.historia}",
    #         self.email
    #     )
        
    #     # Sprawdzamy, czy wynik to True (sukces wysyłki)
    #     self.assertTrue(result)

    # @patch('datetime.datetime')  # Mockowanie datetime
    # def test_send_history_to_email_fail(self, mock_datetime):
    #     # Przygotowanie mocka dla datetime
    #     mock_datetime.now.return_value = datetime(2024, 12, 10)  # Zmieniamy datę na konkretną
    #     # Tworzymy obiekt PersonalAccount z przykładową historią
    #     konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
    #     # Mockowanie klienta SMTP
    #     mock_smtp = MagicMock()
    #     # Ustawiamy, że metoda send zwróci False (symulujemy błąd)
    #     mock_smtp.send.return_value = False
    #     konto.historia=[334, 789]
        
    #     # Wywołanie metody send_history_to_email
    #     result = konto.send_history_to_email(self.email, mock_smtp)
        
    #     # Sprawdzamy, czy metoda send została wywołana
    #     mock_smtp.send.assert_called_once_with(
    #         f"Wyciąg z dnia {self.date}", 
    #         f"Twoja historia konta to: {konto.historia}",
    #         self.email
    #     )
        
    #     # Sprawdzamy, czy wynik to False (błąd wysyłki)
    #     self.assertFalse(result)

    # # @patch('datetime.datetime')  # Mockowanie datetime
    # # def test_send_history_to_email_called(self, mock_datetime):
    # #     # Przygotowanie mocka dla datetime
    # #     mock_datetime.now.return_value = datetime(2024, 12, 10)  # Zmieniamy datę na konkretną
    # #     # Tworzymy obiekt PersonalAccount z przykładową historią
    # #     konto=PersonalAccount(self.imie, self.nazwisko, self.pesel)
    # #     konto.historia=[334, 789]
    # #     # Mockowanie klienta SMTP
    # #     mock_smtp = MagicMock()
        
    # #     # Wywołanie metody send_history_to_email
    # #     konto.send_history_to_email('test@example.com', mock_smtp)
        
    # #     # Sprawdzamy, czy metoda send została wywołana
    # #     mock_smtp.send.assert_called_once()

