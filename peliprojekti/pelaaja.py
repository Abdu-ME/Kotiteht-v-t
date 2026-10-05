class Pelaaja:
    def __init__(self, nimi, ikä,):
        self.nimi = nimi
        self.ikä = ikä
class Reppu:
    def __init__(self):
        self.esineet = []

    def lisää(self, esine):
        self.esineet.append(esine)

    def näytä(self):
        if len(self.esineet) == 0:
            print("Reppu on tyhjä")
        else:
            print("Repussa on:")
            for esine in self.esineet:
                print(f"-{esine}")