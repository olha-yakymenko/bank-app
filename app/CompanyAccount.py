from .Konto import Konto
class CompanyAccount(Konto):

    def __init__(self, nazwa, nip):
        self.nazwa=nazwa
        self.nip=nip
        self.saldo=0
        self.express_fee=5
        if len(nip) == 10 and nip.isdigit():
            self.nip = nip
        else:
            self.nip = "Niepoprawny NIP!"

    