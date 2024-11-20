import unittest
import requests

class TestCRUD(unittest.TestCase):
    body={
        "imie": "Dariusz",
        "nazwisko": "Januszewski",
        "pesel": "06211888888"
    }

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://127.0.0.1:5001/api/accounts"


    def test_create_account(self):
        response=requests.post(self.base_url, json=self.body)
        self.assertEqual(response.status_code, 201, "Niepoprawny status")
        
    def test_how_many_accounts(self):
        response = requests.get(self.base_url+"/count")
        self.assertEqual(response.status_code, 200)

    def test_get_account_ok(self):
            pesel = self.body["pesel"]
            requests.post(self.base_url, json=self.body)
            response = requests.get(f"{self.base_url}/{pesel}")
            self.assertEqual(response.status_code, 200, "Niepoprawny status")
            data = response.json()
            self.assertEqual(data["imie"], self.body["imie"], "Niepoprawne imię")
            self.assertEqual(data["nazwisko"], self.body["nazwisko"], "Niepoprawne nazwisko")
            self.assertEqual(data["saldo"], 0, "Niepoprawne saldo początkowe")

    def test_get_account_bad(self):
        response = requests.get(f"{self.base_url}/28747547575")
        self.assertEqual(response.status_code, 404, "Niepoprawny status")

    def test_update_account_ok(self):
        pesel = self.body["pesel"]
        requests.post(self.base_url, json=self.body)
        updated_body = {
            "imie": "NoweImie",
            "nazwisko": "NoweNazwisko",
            "pesel": pesel,
            "saldo": 500
        }
        response = requests.patch(f"{self.base_url}/{pesel}", json=updated_body)
        self.assertEqual(response.status_code, 200, "Niepoprawny status aktualizacji")
        get_response = requests.get(f"{self.base_url}/{pesel}")
        data = get_response.json()
        self.assertEqual(data["imie"], updated_body["imie"], "Imię nie zostało zaktualizowane")
        self.assertEqual(data["nazwisko"], updated_body["nazwisko"], "Nazwisko nie zostało zaktualizowane")
        self.assertEqual(data["saldo"], updated_body["saldo"], "Saldo nie zostało zaktualizowane")

    def test_update_unreal_account(self):
        updated_body = {
            "imie": "NoweImie",
            "nazwisko": "NoweNazwisko",
            "pesel": 8888888888888,
            "saldo": 500
        }
        response = requests.patch(f"{self.base_url}/74892000000", json=updated_body)
        self.assertEqual(response.status_code, 404, "Niepoprawny status")

    def test_delete_account_ok(self):
        pesel = self.body["pesel"]
        requests.post(self.base_url, json=self.body)
        response = requests.delete(f"{self.base_url}/{pesel}")
        self.assertEqual(response.status_code, 200, "Niepoprawny status usunięcia")
        
    def test_delete_unreal_account(self):
        response = requests.delete(f"{self.base_url}/74892000000")
        self.assertEqual(response.status_code, 404, "Niepoprawny status usunięcia")


     
