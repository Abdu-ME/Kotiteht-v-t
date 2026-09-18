nimi = input("Mikä on sinun nimi?\n")
ikä = int(input("Minkä ikäinen olet?\n"))
print("")
print(f"Pelaajan nimi: {nimi}")
print(f"Pelaajan ikä: {ikä}")

if ikä < 12:
    print("Peli loppuu.")
else:
    print(f"Terve {nimi}")
    print("1. Jos haluat peliohjeen")
    print("2. Pelaat peliä")
    print("Kirjoita lopeta, jos haluat lopettaa")

    komento = input("Anna komento")

    if komento == 1:
          print("Peli ohjeet")
    elif komento == 2:
        print("Peli alkaa!")
    elif komento == "lopeta":
        print("Lopetetaan")
        break
    else:
        print("Väärä komento yritä uudestaan")

esineet = []

def lisaa_esine():
        esine = input("Minkä esineen haluat mukaan")
        esineet.append(esine)
        print("Esine lisätty")


def näytä_esineet():
        print("Kuinka paljon tavaraa repussasi on")

        if len(esineet) == 0:
            print("Reppu on tyhjä")
        else:
            for esine in esineet:
                print(f"-{esine}")
