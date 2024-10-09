class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie=imie
        self.nazwisko=nazwisko
        self.saldo=0
        if len(pesel)==11:
            self.pesel=pesel
        else:
            self.pesel="Niepoprawny pesel"
        if self.czy_kod_poprawny(kod):
            self.saldo=50
        if self.czy_po_roku_1960(pesel):
            self.saldo=50
        


    def czy_kod_poprawny(self, kod):
        if kod is None:
            return False
        if kod.startswith("PROM_") and len(kod)==8 :
            return True
        else :
            return False

    def czy_po_roku_1960(self, pesel):
        if int(str(pesel)[:2])>60:
            return True
        else:
            return False