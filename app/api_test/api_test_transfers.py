import requests
import unittest

class TestAccountTransfers(unittest.TestCase):

    body={
        "imie": "Dariusz",
        "nazwisko": "Januszewski",
        "pesel": "06211888838"
    }

    def setUp(self):
        self.base_url = "http://127.0.0.1:5001/api/accounts"
        response=requests.post(self.base_url, json=self.body)
        self.assertEqual(response.status_code, 201)
    
    def tearDown(self) -> None:
        response=requests.delete(f"{self.base_url}/{self.body["pesel"]}")
        self.assertEqual(response.status_code, 201)


    def test_incoming_transfer_account_exists(self):
        response1 = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 500, "type": "incoming"})
        self.assertEqual(response1.status_code, 200)
        konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
        self.assertEqual(konto["saldo"], 500)
    
    def test_incoming_transfer_account_doesnt_exist(self):
        response = requests.post(self.base_url + "/02311801475/transfer", json={"amount": 500, "type": "incoming"})
        self.assertEqual(response.status_code, 404)
    
    def test_outgoing_transfer(self):
        requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 500, "type": "incoming"})
        requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 100, "type": "outgoing"})
        konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
        self.assertEqual(konto["saldo"], 400)


    def test_failed_outgoing_transfer(self):
        requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 600, "type": "incoming"})
        response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 700, "type": "outgoing"})
        self.assertEqual(response.status_code, 409)  
        konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
        self.assertEqual(konto["saldo"], 600)  

    def test_express_transfer_successful(self):
        requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 600, "type": "incoming"})
        response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 100, "type": "express"})
        self.assertEqual(response.status_code, 200)
        konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
        self.assertEqual(konto["saldo"], 499)  

    def test_failed_express_transfer(self):
        requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 600, "type": "incoming"})
        response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 700, "type": "express"})
        self.assertEqual(response.status_code, 409)  
        konto = requests.get(self.base_url + "/" + self.body["pesel"]).json()
        self.assertEqual(konto["saldo"], 600)  

    def test_missing_type(self):
        response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 500})
        self.assertEqual(response.status_code, 400)  

    def test_unknown_transfer_type(self):
        response = requests.post(self.base_url + "/" + self.body["pesel"] + "/transfer", json={"amount": 500, "type": "unknown"})
        self.assertEqual(response.status_code, 400)  

