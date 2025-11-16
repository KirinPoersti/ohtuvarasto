"""Pääohjelma"""
from varasto import Varasto


def tulosta_alkutilanne(mehua, olutta):
    """Tulostaa varastojen alkutilanne"""
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


def tulosta_getterit(olutta):
    """Tulostaa olutvaraston getterit"""
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def testaa_setterit(mehua):
    """Testaa mehuvaraston setterit"""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def testaa_virhetilanteet():
    """Testaa virhetilanteita"""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)
    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def testaa_ylivuoto(olutta, mehua):
    """Testaa ylivuototilanteet"""
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")


def testaa_olut_otto(olutta):
    """Testaa olutvaraston ottamista"""
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")


def testaa_mehu_otto(mehua):
    """Testaa mehuvaraston ottamista"""
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def suorita_testit(mehua, olutta):
    """Suorittaa kaikki testit"""
    tulosta_alkutilanne(mehua, olutta)
    tulosta_getterit(olutta)
    testaa_setterit(mehua)
    testaa_virhetilanteet()
    testaa_ylivuoto(olutta, mehua)
    testaa_olut_otto(olutta)
    testaa_mehu_otto(mehua)


def main():
    """Pääohjelma"""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    suorita_testit(mehua, olutta)


if __name__ == "__main__":
    main()
