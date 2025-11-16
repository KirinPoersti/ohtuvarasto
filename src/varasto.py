"""Varasto-luokka"""


class Varasto:
    """Luokka varaston hallintaan"""

    def __init__(self, tilavuus, alku_saldo=0):
        """Alustaa varaston"""
        self.tilavuus = max(0.0, tilavuus)
        self.saldo = self._laske_alkusaldo(alku_saldo, self.tilavuus)

    def _laske_alkusaldo(self, alku_saldo, tilavuus):
        """Laskee oikean alkusaldon"""
        if alku_saldo < 0.0:
            return 0.0
        if alku_saldo <= tilavuus:
            return alku_saldo
        return tilavuus

    def paljonko_mahtuu(self):
        """Palauttaa vapaana olevan tilan määrän"""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """Lisää varastoon"""
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """Ottaa varastosta"""
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0
            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara
        return maara

    def __str__(self):
        """Merkkijonoesitys"""
        return (f"saldo = {self.saldo}, "
                f"vielä tilaa {self.paljonko_mahtuu()}")
