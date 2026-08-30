sukupuoli = input("Oletko nainen tai mies?\n")
if sukupuoli == "nainen" :
    hemoglobiini_nainen = int(input("Mikä on hemoglobiiniarvosi?\n"))
    if hemoglobiini_nainen > 175 :
        print("Hemoglobiiniarvosi on korkea.")
    elif hemoglobiini_nainen < 117 :
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on normaali.")
elif sukupuoli == "mies":
    hemoglobiini_mies = int(input("Mikä on hemoglobiini arvosi?\n"))
    if hemoglobiini_mies > 195:
        print("Hemoglobiiniarvosi on korkea.")
    elif hemoglobiini_mies < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    else:
        print("Hemoglobiiniarvosi on alhainen.")