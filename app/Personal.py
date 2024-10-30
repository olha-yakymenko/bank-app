from .Konto import Konto
class CompanyAccount(Konto):
    express_fee=1
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie=imie
        self.nazwisko=nazwisko
        self.saldo=0