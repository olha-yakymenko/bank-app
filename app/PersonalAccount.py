from .Konto import Konto
class PersonalAccount(Konto):
    express_fee=1
    def __init__(self, imie, nazwisko, pesel, kod=None):
        super().__init__()
        self.imie=imie
        self.nazwisko=nazwisko

        if len(pesel)==11:
            self.pesel=pesel
        else:
            self.pesel="Niepoprawny pesel"
        if self.czy_po_roku_1960_i_poprawny_kod(pesel, kod):
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

    def czy_po_roku_1960_i_poprawny_kod(self, pesel, kod):
        rok_urodzenia = int(pesel[0:2])
        miesiac = int(pesel[2:4])

        if(rok_urodzenia >=61 and (miesiac >=1 and miesiac <=32 )) or (rok_urodzenia <=24 and (miesiac >=1 and miesiac <=32)):
            if self.czy_kod_poprawny(kod):
                return True
            else:
                return False
        else:
            return False



