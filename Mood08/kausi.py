kaudet = set("Talvi", "Talvi", "Kevät", "kevät", "kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

kuukausi = int(input("Anna kuukauden numero\n"))
if kuukausi >= 13:
    print("Kuukausi on 1-12,")
else:
    print(kaudet[kuukausi-1])