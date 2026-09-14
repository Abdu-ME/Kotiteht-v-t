Lentoasema = {}

while True:
    print("1: Jos haluat syöttää uuden lentoaseman\n")
    print("2: Jos haluat Hakea lentoaseman\n")
    print("3: Jos haluat lopettaa\n")

    x = input("Valitse toiminto")

    if x == "1":
        icao = input("Anna koodi")
        nimi = input("Anna lentoaseman nimi")

        Lentoasema[icao] = nimi

    elif x == "2":
        icao = input("Anna lentoaseman ICAO koodi")

        if icao in Lentoasema:
            print(Lentoasema[icao])
        else:
            print("Lentoasemaa ei löydy")
    elif x == "3":
        print("Lopetus")
        break

    else:
        print("Virheellinen toiminto")