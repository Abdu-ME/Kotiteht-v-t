käyttäjätunnus = "python"
salasana = "rules"
x = -1

while x!=5:
    x +=1
    arvaus = input("Kerro käyttäjätunnus\n")
    salis = input("kerro salasana\n")
    if arvaus == käyttäjätunnus and salis == salasana:
        print("Tervetuloa")
        break
    else:
        ("Väärä salasana tai käyttäjätunnus kokeile uudestaan\n")
if x == 5:
    print("pääsy evätty")