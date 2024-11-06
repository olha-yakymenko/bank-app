from .Konto import Konto
class CompanyAccount(Konto):
    express_fee=5
    def __init__(self, nazwa, nip):
        super().__init__()
        self.nazwa=nazwa
        
        if len(nip) == 10 and nip.isdigit():
            self.nip = nip
        else:
            self.nip = None

    