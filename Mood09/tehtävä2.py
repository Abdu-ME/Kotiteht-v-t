class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, tämänhetkinen_nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = tämänhetkinen_nopeus
        self.kuljettumatka = kuljettu_matka
    def kiihdytä(self, muutos):
        self.tämänhetkinen_nopeus += muutos
        if self.tämänhetkinen_nopeus > self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        if self.tämänhetkinen_nopeus < 0:
            self.tämänhetkinen_nopeus = 0


auto = Auto("ABC-123", 100)

auto.kiihdytä(30)

auto.kiihdytä(70)

auto.kiihdytä(50)

print(auto.tämänhetkinen_nopeus)

auto.kiihdytä(-100)

print(auto.tämänhetkinen_nopeus)