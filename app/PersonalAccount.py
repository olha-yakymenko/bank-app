from .Konto import Konto


class PersonalAccount(Konto):
    express_fee = 1

    def __init__(self, imie, nazwisko, pesel, kod=None):
        super().__init__()
        self.imie = imie
        self.nazwisko = nazwisko

        if len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "Niepoprawny pesel"
        if self.czy_po_roku_1960_i_poprawny_kod(pesel, kod):
            self.saldo = 50
        else:
            self.saldo = 0

    def czy_kod_poprawny(self, kod):
        if kod is None:
            return False
        if kod.startswith("PROM_") and len(kod) == 8:
            return True
        else:
            return False

    def czy_po_roku_1960_i_poprawny_kod(self, pesel, kod):
        rok_urodzenia = int(pesel[0:2])
        miesiac = int(pesel[2:4])

        if (rok_urodzenia >= 61 and (miesiac >= 1 and miesiac <= 32)) or (
                rok_urodzenia <= 24 and (miesiac >= 1 and miesiac <= 32)):
            if self.czy_kod_poprawny(kod):
                return True
            else:
                return False
        else:
            return False

    def zaciagnij_kredyt(self, kwota):
        if self.ostatnie_3_transakcje_wplaty() or self.suma_5_transakcji_wieksza_niz(kwota):
            self.saldo += kwota

    def ostatnie_3_transakcje_wplaty(self):
        if len(self.historia) < 3:
            return False

        ostatnie_3 = self.historia[-3:]
        for transakcja in ostatnie_3:
            if transakcja <= 0:
                return False
        return True

    def suma_5_transakcji_wieksza_niz(self, kwota):
        if len(self.historia) < 5:
            return False

        ostatnie_5 = self.historia[-5:]
        suma_ostatnich_5 = 0
        for transakcja in ostatnie_5:
            suma_ostatnich_5 += transakcja
        return suma_ostatnich_5 > kwota


        # def zaciagnij_kredyt(self, kwota):
    #     if self.ostatnie_3_transakcje_wplaty() or self.suma_5_transakcji_wieksza_niz(kwota):
    #         self.saldo += kwota
    #
    # def ostatnie_3_transakcje_wplaty(self):
    #     if len(self.historia)>3:
    #         return self.historia[-1] > 0 and self.historia[-2] > 0 and self.historia[-3] > 0
    #
    # def suma_5_transakcji_wieksza_niz(self, kwota):
    #     if len(self.historia) > 5:
    #         return sum(self.historia[-5:])>kwota
    #


