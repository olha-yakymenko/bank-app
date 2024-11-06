class Konto:
    def __init__(self):
        self.saldo=0
        self.historia=[]
    def przelew_wychodzacy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            self.historia.append(-kwota)
            return True
        return False

    def przelew_przychodzacy(self, kwota):
        self.saldo += kwota
        self.historia.append(kwota)

    def szybki_przelew(self,kwota):
        if self.saldo>=kwota:
            self.saldo-=kwota+self.express_fee
            self.historia.append(-kwota)
            self.historia.append(-self.express_fee)
        else:
            print("Przelew nie zostal wykonany")