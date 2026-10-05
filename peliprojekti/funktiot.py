esineet = []

def lisää_esineet():
    while True:
        esine = input("Minkä esineen haluat mukaan (enter lopettaa)\n")
        if esine == "":
            break
        esineet.append(esine)
        print(f"{esine} lisätty")


def näytä_esineet():
        print("Kuinka paljon tavaraa repussasi on")

        if len(esineet) == 0:
            print("Reppu on tyhjä")
        else:
            for esine in esineet:
                print(f"-{esine}")
def kysy_valinta(kysymys, vastaukset):
      while True:
            vastaus = input(kysymys)
            if vastaus in vastaukset:
                return vastaus
            else:
                  print("Väärä komento.")

      