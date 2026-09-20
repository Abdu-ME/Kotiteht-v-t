class Hissi:
    def __init__(self, alin, ylin):
        self.ylin = ylin
        self.alin = alin
        self.nykyinen_kerros = alin

    def kerros_ylos(self):
        if self.nykyinen_kerros < self.ylin:
            self.nykyinen_kerros += 1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin:
            self.nykyinen_kerros -=1
            print(f"Hissi on kerroksessa {self.nykyinen_kerros}")
    def siirry_kerrokseen(self,kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylos()

        while self.nykyinen_kerros > kerros:
            self.kerros_alas()

h = Hissi(1, 10)
h.siirry_kerrokseen(5)
h