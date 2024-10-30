class Konto:
    def __init__(self, imie, nazwisko, pesel, kod=None):
        self.imie=imie
        self.nazwisko=nazwisko
        self.saldo=0

        if len(pesel)==11:
            self.pesel=pesel
        else:
            self.pesel="Niepoprawny pesel"
        if self.czy_kod_poprawny(kod) and self.czy_po_roku_1960(pesel):
            self.saldo=50
        else:
            self.saldo=0




    def czy_kod_poprawny(self, kod):
        if kod is None:
            return False
        if kod.startswith("PROM_") and len(kod)==8 :
            return True
        else :
            return False

    def czy_po_roku_1960(self, pesel):
        year = int(pesel[0:2])
        month = int(pesel[2:4])

        if 1 <= month <= 12:
            year += 1900
        elif 21 <= month <= 32:
            year += 2000
        elif 81 <= month <= 92:
            year += 1800

        return year > 1960

    def przelew_wychodzacy(self, kwota):
        if self.saldo >= kwota:
            self.saldo -= kwota
            return True
        return False

    def przelew_przychodzacy(self, kwota):
        self.saldo += kwota



