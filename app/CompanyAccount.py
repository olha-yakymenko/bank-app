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
    
    def zaciagnij_kredyt(self, kwota):
        if self.saldo >= 2 * kwota and 1775 in self.historia :
            self.saldo += kwota
        else:
            print(f"Warunki kredytu nie zostały spełnione. Saldo: {self.saldo}, Kwota kredytu: {kwota}")