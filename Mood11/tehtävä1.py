class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumäärä

    def tulosta_tiedot(self):
        print(f"Nimi on {self.nimi}")
        print(f"Kirjoittaja on {self.kirjoittaja}")
        print(f"sivumäärä on {self.sivumäärä}")

class Lehti:
    def __init__(self, nimi, päätoimittaja):
        super(nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f"nimi on {self.nimi}")
        print(f"päätoimittaja on {self.päätoimittaja}")
k1 = Kirja("Red rising", "Abdulmajid", 450)
l1 = Lehti("Lehti", "Wimme")
print(Kirja.tulosta_tiedot)