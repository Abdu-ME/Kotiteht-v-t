import funktiot
import pelaaja

def nukahdit():
    print("")
    print("Oho! Vahingossa nukahdit 30 minuuttia pommiin!")
    print("Kello on nyt 8:30.")
    print("")

    print("Sinulla on kolme vaihtoehtoa:")
    print("1. Ostaa kaupasta syötävää.")
    print("2. Syödä kotona ja mennä kouluun myöhässä.")
    print("3. Lähteä kouluun syömättä.")

    komento = funktiot.kysy_valinta("Anna komento\n"["1", "2", "3"])

    if komento == "1":
        kauppa()

    elif komento == "2":
        syö_kotona()

    elif komento == "3":
        mene_kouluun_nälkäisenä()


def kauppa():
    print("")
    print("Ostit pientä purtavaa, jota syöt matkalla.")
    print("Nyt sinun pitäisi ehtiä kouluun hyvin.")
    print("")
    print("OHO!")
    print("Juna lähtee kahden minuutin päästä.")
    print("Sinun pitää juosta, jotta ehdit!")

    komento = funktiot.kysy_valinta(
        "Aiotko juosta? en/joo: ",
        ["en", "joo"]
    )

    if komento == "en":
        myöhästy_junasta()

    elif komento == "joo":
        ehdit_junaan()


def myöhästy_junasta():
    print("")
    print("Myöhästyit junasta ja tulit myöhässä oppitunnille.")
    print("Opettaja kysyy, miksi myöhästyit.")

    komento = funktiot.kysy_valinta("1. Kertoa totuus\n2. Huijata\n",["1", "2"])

    if komento == "1":
        print("Opettaja ymmärtää tilanteen.")
        print("Sait vain huomautuksen.")
        print("Peli päättyi.")

    elif komento == "2":
        print("Opettaja huomaa, että huijasit.")
        print("Opettaja antaa sinulle jälki-istuntoa.")
        print("Peli päättyi.")


def ehdit_junaan():
    print("")
    print("Ehdit junaan ja olet ajoissa tunnilla.")
    print("Opettaja on tyytyväinen!")
    print("Peli päättyi.")


def syö_kotona():
    print("")
    print("Olet nyt syönyt ruokasi.")
    print("Kello on 9:00.")
    print("")

    print("Sinulla on kaksi vaihtoehtoa:")
    print("1. Menet kouluun suoraan.")
    print("2. Tarkistat ennen lähtöä reppusi.")

    komento = funktiot.kysy_valinta("Anna komento\n",["1", "2"])

    if komento == "1":
        kouluun_ilman_esineitä()

    elif komento == "2":
        tarkista_reppu()


def tarkista_reppu():
    print("")
    print("Tarkistat reppusi.")

    funktiot.näytä_esineet()

    print("")
    print("Nyt lisää esineitä, jotka haluat ottaa kouluun mukaan.")

    funktiot.lisää_esineet()

    print("")
    print("Nyt olet ottanut kaikki mitä halusit.")
    print("Tarkistat repun vielä kerran.")

    funktiot.näytä_esineet()

    komento = funktiot.kysy_valinta("Oletko tyytyväinen? kyllä/ei\n",["kyllä", "ei"])

    if komento == "kyllä":
        kouluun()

    elif komento == "ei":
        print("Lisää vielä tarvittavat esineet.")
        funktiot.lisää_esineet()
        kouluun()


def kouluun():
    print("")
    print("Nyt olet tyytyväinen reppuusi.")
    print("Menet kouluun.")
    print("Saavut kouluun myöhässä.")
    print("Opettaja kysyy, miksi olet myöhässä.")
    print("Kerrot rehellisesti, että nukuit pommiin.")
    print("Opettaja ymmärtää tilanteen.")
    print("Peli loppui.")


def kouluun_ilman_esineitä():
    print("")
    print("Tulit kouluun myöhässä.")
    print("OHO! Huomaat, että reppu on tyhjä.")
    print("Opettaja on vihainen ja antaa jälki-istuntoa.")
    print("Peli loppui.")


def mene_kouluun_nälkäisenä():
    print("")
    print("Menet kouluun ilman, että syöt mitään.")
    print("Ehdit junaan helposti.")
    print("Tunnilla olet todella nälkäinen.")
    print("Et jaksa keskittyä tunnilla.")
    print("")

    print("Opettaja kysyy, mikä on hätänä.")

    komento = funktiot.kysy_valinta(
        "1. Kerrot totuuden\n2. Huijaat\n",
        ["1", "2"]
    )

    if komento == "1":
        print("Opettaja ymmärtää tilanteen.")
        print("Saat mennä ruokalaan ajoissa.")

    elif komento == "2":
        print("Opettaja huomaa, että huijasit.")

    print("Peli loppui.")


def heräät():
    print("")
    print("Nouset sängystä, peset hampaat ja syöt ruokaa hyvissä ajoin")
    print("Ennekuin lähdet aiot tarkistaa reppusi")
    print("")
    komento10 = funktiot.kysy_valinta("Vastaa kysymykseen en tai joo\n", ["en", "joo"])
    if komento10 == "en":
        print("Pääsit koululle ajoissa. mutta huomaat, että reppu on tyhjä")
        print("Opettaja on ärsyyntynyt ja kysyy mikä homman nimi on")
        print("1. kerro totuus")
        print("2. huijjaa")
        komento11 = funktiot.kysy_valinta("Anna komento.\n", ["1","2"])
        if komento11 == "1":
            print("Opettaja uskoo sinua, mutta silti antaa jälki istuntoa")
            print("Peli loppui")
        elif komento11 == "2":
            print("Opettaja ei usko sinua ja antaa jälki istuntoa ja varaa sinulle puhuttelun rehtorin kanssa")
            print("Peli loppui")
    elif komento10 == "joo":
        tarkista_reppu_ajoissa()
def tarkista_reppu_ajoissa():
    print("")
    print("Tarkistat reppusi.")
    
    funktiot.näytä_esineet()
    
    print("")
    print("Nyt lisää esineitä, jotka haluat ottaa kouluun mukaan.")
    
    funktiot.lisää_esineet()
    
    print("")
    print("Nyt olet ottanut kaikki mitä halusit.")
    print("Tarkistat repun vielä kerran.")
    
    funktiot.näytä_esineet()
    
    komento = funktiot.kysy_valinta("Oletko tyytyväinen? kyllä/ei\n",["kyllä", "ei"])

    print("")
    print("Nyt olet tyytyväinen reppuusi.")
    print("Menet kouluun.")
    print("Saavut kouluun ajoissa.")
    print("Opettaja on tyytyväinen")
    print("Pääsit koululle ajoissa ja hyvin aikaan.")
    print("\nPeli Loppui")