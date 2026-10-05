import pelaaja
import peli
import funktiot


pelaaja.nimi = input("Mikä on sinun nimi?\n")
pelaaja.ikä = int(input("Minkä ikäinen olet?\n"))

print("")
print(f"Pelaajan nimi: {pelaaja.nimi}")
print(f"Pelaajan ikä: {pelaaja.ikä}")

if pelaaja.ikä <= 12:
    print("Peli loppuu.")
    exit()

print("")
print(f"Terve {pelaaja.nimi}!")

while True:
    print("")
    print("1. Jos haluat peliohjeen")
    print("2. Pelaat peliä")
    print("Kirjoita lopeta, jos haluat lopettaa")

    komento = input("Anna komento\n")

    if komento == "1":
        with open ("peliprojekti/intro.txt", "r", encoding="utf-8") as intro:
            print(intro.read())

    elif komento == "2":
        print("Peli alkaa!")
        print("")
        print("Herätys kello soi!")
        print("Koulu alkaa 9:30. Heräsit kahdeksalta.")
        print("")
        
        print("Sinulla on kolme vaihtoehtoa:")
        print("1. Lepään vielä minuutin.")
        print("2. Herään ja pesen hampaani.")
        
        komento = funktiot.kysy_valinta("Valitse komento: ",["1", "2"])
        
        if komento == "1":
            peli.nukahdit()
        
        elif komento == "2":
            peli.heräät()
        

    elif komento == "lopeta":
        print("Lopetetaan")
        break

    else:
        print("Väärä komento, yritä uudestaan")