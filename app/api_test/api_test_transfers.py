# import requests
# import unittest

# class TestAccountTransfers(unittest.TestCase):

#     body={
#         "imie": "Dariusz",
#         "nazwisko": "Januszewski",
#         "pesel": "06211888838"
#     }

#     def setUp(self):
#         self.base_url = "http://127.0.0.1:5000/api/accounts"
#         response=requests.post(self.base_url, json=self.body)
#         self.assertEqual(response.status_code, 201)
    
#     def tearDown(self) -> None:
#         response=requests.delete(f"{self.base_url}/{self.body["pesel"]}")
#         self.assertEqual(response.status_code, 201)


#     def test_incoming_transfer_account_exists(self):
#         response1 = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 500, "type": "incoming"})
#         self.assertEqual(response1.status_code, 200)
#         konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
#         self.assertEqual(konto["saldo"], 500)
    
#     def test_incoming_transfer_account_doesnt_exist(self):
#         response = requests.post(self.base_url + "/02311801475/transfer", json={"amount": 500, "type": "incoming"})
#         self.assertEqual(response.status_code, 404)
    
#     def test_outgoing_transfer(self):
#         requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 500, "type": "incoming"})
#         requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 100, "type": "outgoing"})
#         konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
#         self.assertEqual(konto["saldo"], 400)


#     def test_failed_outgoing_transfer(self):
#         requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 600, "type": "incoming"})
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 700, "type": "outgoing"})
#         self.assertEqual(response.status_code, 409)  
#         konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
#         self.assertEqual(konto["saldo"], 600)  

#     def test_express_transfer_successful(self):
#         requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 600, "type": "incoming"})
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 100, "type": "express"})
#         self.assertEqual(response.status_code, 200)
#         konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
#         self.assertEqual(konto["saldo"], 499)  

#     def test_failed_express_transfer(self):
#         requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 600, "type": "incoming"})
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 700, "type": "express"})
#         self.assertEqual(response.status_code, 409)  
#         konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
#         self.assertEqual(konto["saldo"], 600)  

#     def test_missing_type(self):
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 500})
#         self.assertEqual(response.status_code, 400)  

#     def test_unknown_transfer_type(self):
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 500, "type": "unknown"})
#         self.assertEqual(response.status_code, 400)  

#     def test_missing_amount(self):
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"type": "incoming"})
#         self.assertEqual(response.status_code, 400)

#     def test_negative_amount(self):
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": -500, "type": "incoming"})
#         self.assertEqual(response.status_code, 400)

#     def test_zero_amount(self):
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 0, "type": "incoming"})
#         self.assertEqual(response.status_code, 400)

#     def test_invalid_json(self):
#         response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={})
#         self.assertEqual(response.status_code, 400)
import requests
import unittest
from parameterized import parameterized

class TestAccountTransfers(unittest.TestCase):

    def setUp(self):
        self.body = {
            "imie": "Dariusz",
            "nazwisko": "Januszewski",
            "pesel": "06211888838"
        }
        self.base_url = "http://127.0.0.1:5000/api/accounts"
        
        response = requests.post(self.base_url, json=self.body)
        self.assertEqual(response.status_code, 201, f"Failed to create account: {response.text}")

        response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 1000, "type": "incoming"})
        self.assertEqual(response.status_code, 200, f"Failed to add initial balance: {response.text}")
    
    def tearDown(self):
        response = requests.delete(f"{self.base_url}/{self.body['pesel']}")
        self.assertEqual(response.status_code, 201, f"Failed to delete account: {response.text}")

    @parameterized.expand([
        ("test_incoming_transfer_account_exists", "06211888838", 500, "incoming", 200),
        ("test_incoming_transfer_account_doesnt_exist", "1111111111111", 500, "incoming", 404),
        ("test_outgoing_transfer", "06211888838", 100, "outgoing", 200),
        ("test_failed_outgoing_transfer", "06211888838", 1200, "outgoing", 409), 
        ("test_express_transfer_successful", "06211888838", 500, "express", 200),
        ("test_failed_express_transfer", "06211888838", 1200, "express", 409), 
        ("test_missing_type", "06211888838", None, None, 400),
        ("test_unknown_transfer_type", "06211888838", 500, "unknown", 400),
        ("test_missing_amount", "06211888838", None, "incoming", 400),
        ("test_negative_amount", "06211888838", -500, "incoming", 400),
        ("test_zero_amount", "06211888838", 0, "incoming", 400),
        ("test_invalid_json", "06211888838", None, None, 400)
    ])
    
    def test_transfers(self, name, pesel, amount, transfer_type, expected_result):
        if amount is None or transfer_type is None:
            response = requests.post(self.base_url + "/" + pesel + "/transfer", json={})
        else:
            response = requests.post(self.base_url + "/" + pesel + "/transfer", json={"amount": amount, "type": transfer_type})

        self.assertEqual(response.status_code, expected_result, f"Test {name} failed. Response: {response.text}")
