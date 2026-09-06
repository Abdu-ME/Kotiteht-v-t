numerot = []

while True:
    merkkijono = input("Anna lukusi\n")
    if merkkijono == "":
        break
    numerot.append(int(merkkijono))

print("pienin:", min(numerot))
print("Suurin:", max(numerot))