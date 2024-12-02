# import unittest
# import requests

# class TestCRUD(unittest.TestCase):
#     body={
#         "imie": "Dariusz",
#         "nazwisko": "Januszewski",
#         "pesel": "06211888888"
#     }

#     @classmethod
#     def setUpClass(cls):
#         cls.base_url = "http://127.0.0.1:5000/api/accounts"


#     def test_create_account(self):
#         response=requests.post(self.base_url, json=self.body)
#         self.assertEqual(response.status_code, 201, "Niepoprawny status")

#     def test_create_account_empty(self):
#         response = requests.post(self.base_url, json={})
#         self.assertEqual(response.status_code, 400, "Dane nie zostały podane")


#     def test_how_many_accounts(self):
#         response = requests.get(self.base_url+"/count")
#         self.assertEqual(response.status_code, 200)

#     def test_get_account_ok(self):
#         pesel = self.body["pesel"]
#         requests.post(self.base_url, json=self.body)
#         response = requests.get(f"{self.base_url}/{pesel}")
#         self.assertEqual(response.status_code, 200, "Niepoprawny status")
#         data = response.json()
#         self.assertEqual(data["imie"], self.body["imie"], "Niepoprawne imię")
#         self.assertEqual(data["nazwisko"], self.body["nazwisko"], "Niepoprawne nazwisko")
#         self.assertEqual(data["saldo"], 0, "Niepoprawne saldo początkowe")

#     def test_get_account_bad(self):
#         response = requests.get(f"{self.base_url}/28747547575")
#         self.assertEqual(response.status_code, 404, "Niepoprawny status")

#     def test_update_account_ok(self):
#         pesel = self.body["pesel"]
#         requests.post(self.base_url, json=self.body)
#         updated_body = {
#             "imie": "NoweImie",
#             "nazwisko": "NoweNazwisko",
#             "pesel": pesel,
#             "saldo": 500
#         }
#         response = requests.patch(f"{self.base_url}/{pesel}", json=updated_body)
#         self.assertEqual(response.status_code, 200, "Niepoprawny status aktualizacji")
#         get_response = requests.get(f"{self.base_url}/{pesel}")
#         data = get_response.json()
#         self.assertEqual(data["imie"], updated_body["imie"], "Imię nie zostało zaktualizowane")
#         self.assertEqual(data["nazwisko"], updated_body["nazwisko"], "Nazwisko nie zostało zaktualizowane")
#         self.assertEqual(data["saldo"], updated_body["saldo"], "Saldo nie zostało zaktualizowane")

#     def test_update_unreal_account(self):
#         updated_body = {
#             "imie": "NoweImie",
#             "nazwisko": "NoweNazwisko",
#             "pesel": "8888888888888",
#             "saldo": 500
#         }
#         response = requests.patch(f"{self.base_url}/74892000000", json=updated_body)
#         self.assertEqual(response.status_code, 404, "Niepoprawny status")

#     def test_delete_account_ok(self):
#         pesel = self.body["pesel"]
#         requests.post(self.base_url, json=self.body)
#         response = requests.delete(f"{self.base_url}/{pesel}")
#         self.assertEqual(response.status_code, 201, "Niepoprawny status usunięcia")
#         response2 = requests.get(f"{self.base_url}/{pesel}")
#         self.assertEqual(response2.status_code, 404, "Niepoprawny status usunięcia")

#     def test_delete_non_exiting_account(self):
#         response = requests.delete(f"{self.base_url}/74892000000")
#         self.assertEqual(response.status_code, 404, "Niepoprawny status usunięcia")


#     def test_get_account_after_update(self):
#         pesel = self.body["pesel"]
#         requests.post(self.base_url, json=self.body)
#         updated_body = {
#             "imie": "NoweImie",
#             "nazwisko": "NoweNazwisko",
#             "pesel": pesel,
#             "saldo": 500
#         }
#         requests.patch(f"{self.base_url}/{pesel}", json=updated_body)
#         response = requests.get(f"{self.base_url}/{pesel}")
#         data = response.json()
#         self.assertEqual(data["imie"], updated_body["imie"], "Imię nie zostało zaktualizowane")
#         self.assertEqual(data["nazwisko"], updated_body["nazwisko"], "Nazwisko nie zostało zaktualizowane")
#         self.assertEqual(data["saldo"], updated_body["saldo"], "Saldo nie zostało zaktualizowane")

    
#     def test_not_uniq_pesel(self):
#         response=requests.post(self.base_url, json=self.body)
#         self.assertEqual(response.status_code, 201, "Niepoprawny status")
#         response2=requests.post(self.base_url, json=self.body)
#         self.assertEqual(response2.status_code, 409, "Niepoprawny status")

#     def tearDown(self):
#         pesel = self.body.get("pesel")
#         if pesel:
#             requests.delete(f"{self.base_url}/{pesel}")

import unittest
import requests
from parameterized import parameterized


class TestCRUD(unittest.TestCase):
    body = {
        "imie": "Dariusz",
        "nazwisko": "Januszewski",
        "pesel": "06211888888"
    }

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://127.0.0.1:5000/api/accounts"

    @parameterized.expand([
        ("valid_account_creation", body, 201, "Niepoprawny status"),
        ("empty_account_creation", {}, 400, "Dane nie zostały podane")
    ])
    def test_create_account(self, name, input_body, expected_status, message):
        response = requests.post(self.base_url, json=input_body)
        self.assertEqual(response.status_code, expected_status, message)

    @parameterized.expand([
        ("valid_account_count", 200),
    ])
    def test_how_many_accounts(self, name, expected_status):
        response = requests.get(self.base_url + "/count")
        self.assertEqual(response.status_code, expected_status)

    @parameterized.expand([
        ("valid_account_get", body["pesel"], 200, "Niepoprawny status"),
        ("invalid_account_get", "28747547575", 404, "Niepoprawny status")
    ])
    def test_get_account(self, name, pesel, expected_status, message):
        if name == "valid_account_get":
            requests.post(self.base_url, json=self.body)
        response = requests.get(f"{self.base_url}/{pesel}")
        self.assertEqual(response.status_code, expected_status, message)

    @parameterized.expand([
        ("valid_account_update", 500, "NoweImie", "NoweNazwisko", "3333333333333", 200, "Niepoprawny status aktualizacji"),
        ("invalid_account_update", 300, "imie", "nazwisko", "8888888888888", 404, "Niepoprawny status")
    ])
    def test_update_account(self, name, saldo, imie, nazwisko, pesel, expected_status, message):
        pesel = self.body["pesel"]
        if name == "valid_account_update":
            requests.post(self.base_url, json=self.body)
            updated_body = {
                "imie": imie,
                "nazwisko": nazwisko,
                "pesel": pesel,
                "saldo": saldo
            }
            response = requests.patch(f"{self.base_url}/{pesel}", json=updated_body)
            self.assertEqual(response.status_code, expected_status, message)
            get_response = requests.get(f"{self.base_url}/{pesel}")
            data = get_response.json()
            self.assertEqual(data["imie"], updated_body["imie"], "Imię nie zostało zaktualizowane")
            self.assertEqual(data["nazwisko"], updated_body["nazwisko"], "Nazwisko nie zostało zaktualizowane")
            self.assertEqual(data["saldo"], updated_body["saldo"], "Saldo nie zostało zaktualizowane")
        else:
            updated_body = {
                "imie": "NoweImie",
                "nazwisko": "NoweNazwisko",
                "pesel": pesel,
                "saldo": saldo
            }
            response = requests.patch(f"{self.base_url}/74892000000", json=updated_body)
            self.assertEqual(response.status_code, expected_status, message)

    @parameterized.expand([
        ("valid_account_deletion", body["pesel"], 201, 404),
        ("invalid_account_deletion", "74892000000", 404, None)
    ])
    def test_delete_account(self, name, pesel, expected_delete_status, expected_get_status):
        if name == "valid_account_deletion":
            requests.post(self.base_url, json=self.body)
            response = requests.delete(f"{self.base_url}/{pesel}")
            self.assertEqual(response.status_code, expected_delete_status, "Niepoprawny status usunięcia")
            response2 = requests.get(f"{self.base_url}/{pesel}")
            self.assertEqual(response2.status_code, expected_get_status, "Niepoprawny status usunięcia")
        else:
            response = requests.delete(f"{self.base_url}/74892000000")
            self.assertEqual(response.status_code, expected_delete_status, "Niepoprawny status usunięcia")

    @parameterized.expand([
        ("valid_account_after_update", body["pesel"], "NoweImie", "NoweNazwisko", 500)
    ])
    def test_get_account_after_update(self, name, pesel, expected_imie, expected_nazwisko, expected_saldo):
        requests.post(self.base_url, json=self.body)
        updated_body = {
            "imie": expected_imie,
            "nazwisko": expected_nazwisko,
            "pesel": pesel,
            "saldo": expected_saldo
        }
        requests.patch(f"{self.base_url}/{pesel}", json=updated_body)
        response = requests.get(f"{self.base_url}/{pesel}")
        data = response.json()
        self.assertEqual(data["imie"], updated_body["imie"], "Imię nie zostało zaktualizowane")
        self.assertEqual(data["nazwisko"], updated_body["nazwisko"], "Nazwisko nie zostało zaktualizowane")
        self.assertEqual(data["saldo"], updated_body["saldo"], "Saldo nie zostało zaktualizowane")

    @parameterized.expand([
        ("duplicate_pesel", body, 201, 409)
    ])
    def test_not_uniq_pesel(self, name, input_body, expected_status, status):
        response = requests.post(self.base_url, json=input_body)
        self.assertEqual(response.status_code, expected_status)
        response2 = requests.post(self.base_url, json=input_body)
        self.assertEqual(response2.status_code, status)

    def tearDown(self):
        pesel = self.body.get("pesel")
        if pesel:
            requests.delete(f"{self.base_url}/{pesel}")


