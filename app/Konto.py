class Konto:
    def __init__(self):
        self.saldo=0
    def przelew_wychodzacy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            return True
        return False

    def przelew_przychodzacy(self, kwota):
        self.saldo += kwota

    def szybki_przelew(self,kwota):
        if self.saldo>=kwota:
            self.saldo-=kwota+self.express_fee
        else:
            print("Przelew nie zostal wykonany")