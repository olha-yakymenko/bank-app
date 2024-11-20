import unittest
import requests

class TestCRUD(unittest.TestCase):
    body={
        "imie": "Dariusz",
        "nazwisko": "Januszewski",
        "pesel": "06211888888"
    }


    def test_create_account(self):
        response=requests.post("http://127.0.0.1:5000/api/accounts", json=self.body)
        self.assertEqual(response.status_code, 201, "Niepoprawny status")

    def test_get_account_ok(self):
            pesel = self.body["pesel"]
            response = requests.get(f"http://127.0.0.1:5000/api/accounts/{pesel}")
            self.assertEqual(response.status_code, 200, "Niepoprawny status")
            data = response.json()
            self.assertEqual(data["imie"], self.body["imie"], "Niepoprawne imię")
            self.assertEqual(data["nazwisko"], self.body["nazwisko"], "Niepoprawne nazwisko")
            self.assertEqual(data["saldo"], 0, "Niepoprawne saldo początkowe")

    def test_get_account_bad(self):
        response = requests.get(f"http://127.0.0.1:5000/api/accounts/28747547575")
        self.assertEqual(response.status_code, 404, "Niepoprawny status")

    def test_update_account_ok(self):
        pesel = self.body["pesel"]
        requests.post("http://127.0.0.1:5000/api/accounts", json=self.body)
        updated_body = {
            "imie": "NoweImie",
            "nazwisko": "NoweNazwisko",
            "pesel": pesel,
            "saldo": 500
        }
        response = requests.patch(f"http://127.0.0.1:5000/api/accounts/{pesel}", json=updated_body)
        self.assertEqual(response.status_code, 200, "Niepoprawny status aktualizacji")
        get_response = requests.get(f"http://127.0.0.1:5000/api/accounts/{pesel}")
        data = get_response.json()
        self.assertEqual(data["imie"], updated_body["imie"], "Imię nie zostało zaktualizowane")
        self.assertEqual(data["nazwisko"], updated_body["nazwisko"], "Nazwisko nie zostało zaktualizowane")
        self.assertEqual(data["saldo"], updated_body["saldo"], "Saldo nie zostało zaktualizowane")

    def test_delete_account(self):
        pesel = self.body["pesel"]
        requests.post("http://127.0.0.1:5000/api/accounts", json=self.body)
        response = requests.delete(f"http://127.0.0.1:5000/api/accounts/{pesel}")
        self.assertEqual(response.status_code, 200, "Niepoprawny status usunięcia")
        # get_response = requests.get(f"http://127.0.0.1:5000/api/accounts/{pesel}")
        # self.assertEqual(get_response.status_code, 404, "Konto powinno być usunięte")


