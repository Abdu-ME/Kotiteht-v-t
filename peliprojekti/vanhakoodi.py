import pelaaja
import funktiot

pelaaja.nimi = input("Mikä on sinun nimi?\n")
pelaaja.ikä = int(input("Minkä ikäinen olet?\n"))
print("")
print(f"Pelaajan nimi: {pelaaja.nimi}")
print(f"Pelaajan ikä: {pelaaja.ikä}")

if pelaaja.ikä <= 12:
    print("Peli loppuu.")
    exit()
print(f"Terve {pelaaja.nimi}")
while True:
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
        print("Koulu alkaa 9:30 heräsit kahdeksalta.\n")
        print("Sinulla on kolmevaihtoehtoa, mitä aiot tehdä\n")
        print("1. Lepään vielä minuutin. \n2. Herään, pesen hampaani\n")
        komento1 = input("Valitse komento\n")
        if komento1 == "1":
             print("Oho! vahingossa nukahdit 30 minuuttia pommiin!")
             print("Sinun pitäisi vielä kerätä kouluun ja kello on 8:30.")
             print("Nyt heräät äkkiä sängystä ja huomaat, että sinulla on kolme vaihtoehtoa")
             print("1. Ostaa kaupasta syötävää.")
             print("2. Syödä kotona ja hyväksyä, että menet kouluun myöhässä.")
             print("3. Lähteä koulua päin syömättä mitään aamulla")
             komento2 = funktiot.kysy_valinta("Anna komento\n", ["1", "2", "3"])
             if komento2 == "1":
                print("Ostit pientä purtavaa, mitä syöt matkalla. ")
                print("Nytten pitäisi ehtiä kouluun hyvin")
                print("\nOHO!\nJuna on lähössä kahden minuutin päästä pois Sinun pitää juosta, jotta ehdit!")
                komento3 = funktiot.kysyvalinta("Aiotko juosta, vastaa en tai joo.\n", ["en", "joo"])
                if komento3 == "en":
                    print("Myöhätyit junasta ja tulit myöhässä oppitunnille")
                    print("\nOpettaja, kysyy miksi myöhästyit.")
                    print("")
                    print("Sinulla on kaksi vaihtoehtoa")
                    print("1. Kertoa totuus")
                    print("2. Huijjaat")
                    komento4 = funktiot.kysy_valinta("Anna komento\n", ["1", "2"])
                    if komento4 == "1":
                         print("Opettaja ymmärtää tilanteen")
                         print("Sait vain huomautuksen")
                         print("\n Peli päättyi.")
                         exit() 
                    elif komento4 == "2":
                         print("Opettajaa huomaa, että huijjasit")
                         print("Opettaja antaa sinulle jälki istuntoa")
                         print("")
                         print("Peli päättyi")
                         exit()
                elif komento3 == "joo":
                    print("Ehdit junaan ja olet ajoissa tunnille")
                    print("")
                    print("Opettaja on tyytyväinen!")
                    print("\nPeli päättyi")
             elif komento2 == "2":
                  print("Olet nyt syönyt ruokasi")
                  print("Kello on 9:00")
                  print("")
                  print("Nytten sinulla on kaksi vaihtoehtoa")
                  print("1. Menet kouluun suoraan kouluun")
                  print("2. Tarkistat ennen kuin lähdet reppusi")
                  komento5 = funktiot.kysy_valinta("Anna komento", ["1", "2"])
                  if komento5 == "1":
                       print("Tulit kouluun myöhässä")
                       print("Kerrot opelle, että tulit myöhässä, koska nukuit pommiin")
                       print("OHO! huomasit, että reppu on tyhjä.")
                       print("Opettaja on vihainen ja antaa sinulle jälki istuntoa")
                       print("\nPeli loppui")
                       exit()
                  elif komento5 == "2":
                       print("Tarkistat reppusi")
                       funktiot.näytä_esineet()
                       print("")
                       print("Huomaat, että reppu on tyhjä!")
                       print("Nyt lisää esineitä mitä haluat ottaa kouluun mukaan")
                       funktiot.lisää_esineet()
                       print("Nytten olet ottanut kaikki mitä halusit")
                       print("Tarkistat repun vielä kerran, ennen kuin lähdet ovesta")
                       funktiot.näytä_esineet()
                       komento6 = funktiot.kysy_valinta("Oletko tyytyväinen näihin esineisiin mitä otit mukaan kyllä/ei\n" 
                                ["ei","kyllä"])
                       if komento6 == "kyllä":
                            print("Olet nytten saapunut koululle myöhässä")
                            print("Opettaja kysyy miksi olet myöhässä ja aiot olla rehelinen ja vastaa miksi")
                            print("Opettaja ymmärtää tilanteen ja huomauttaa vain asiasta")
                            print("")
                            print("Pell loppui!")
                            exit()
                       elif komento6 == "ei":
                            print("Lisää tarvittavat esineet vielä")
                            funktiot.lisää_esineet()
                            print("Nytten olet tyytyväinen ja menet koululle päin")
                            print("Opettaja kysyy miksi olet myöhässä ja aiot olla rehelinen ja vastaa miksi")
                            print("Opettaja ymmärtää tilanteen ja huomauttaa vain asiasta")
                            print("")
                            print("Peli loppui!")
                            exit()
             elif komento2 == "3":
                  print("Menet kouluun ilman, että syöt mitään")
                  print("Ehdit junaan helposti")
                  print("Tunnilla olet todella nälkäinen ja et jaksa keskittyä tunnilla")
                  print("Opettaja kysyy mitä on hätänä, sinulla on kaksi vaihtoehtoa vastaa kysymykseen")
                  print("1. Kerrot totuuden")
                  print("2. Huijjaat opelle")
                  komento7 = funktiot.kysy_valinta("Anna komento\n", ["1", "2"])
                  if komento7 == "1":
                       print("Opettaja ymmärtää tilanteen ja antaa sinun mennä ruokalaan ajoissa.")
                       print("Kaikki on tyytyväinen lopputulokseen")
                       print("")
                       print("Peli loppui!")
                       exit()
                  elif komento7 == "2":
                       print("")                   
    elif komento == "lopeta":
        print("Lopetetaan")
        break
    else:
            print("Väärä komento yritä uudestaan")