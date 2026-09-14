nimilista = set()
nimi = input("Anna nimi, paina enter jotta lopetat\n")
while nimi != "":
    if nimi in nimilista:
        print("Nimi on aiemmin jo syötetty")
    else:
        print("Uusi nimi lisätty")
        nimilista.add(nimi)
    nimi = input("Anna nimi, paina enter jotta lopetat\n")
print("Nimilista")
for nimi in nimilista:
    print(nimi)