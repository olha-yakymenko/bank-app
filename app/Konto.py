class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie=imie
        self.nazwisko=nazwisko

        if len(pesel)==11:
            self.pesel=pesel
        else:
            self.pesel="Niepoprawny pesel"
        if self.czy_kod_poprawny(kod):
            self.saldo=50
        else :
            self.saldo=0


    def czy_kod_poprawny(self, kod):
        if kod is None:
            return False
        if kod.startswith("PROM_") and len(kod)==8:
            return True
        else :
            return False
