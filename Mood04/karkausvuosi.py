vuosiluku = int(input("Anna joku vuosi luku\n"))
if vuosiluku % 400 == 0 :
    print("Vuosiluku on karkausvuosi")
elif vuosiluku % 100 == 0 :
    print("Vuosiluku ei ole karkausvuosi")
elif vuosiluku % 4 == 0 :
    print("Vuosiluku on karkausvuosi")
else:
    print("Vuosiluku ei ole karkausvuosi")