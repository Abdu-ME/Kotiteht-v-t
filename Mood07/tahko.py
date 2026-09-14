import random

def noppa(sivut):
   return random.randint(1, sivut)

sivut = int(input("Kuinka paljon sivua on nopassa\n"))

while True:
    heitto = noppa(sivut)
    if heitto == sivut:
        print(heitto)
        break
    else:
        print(heitto)
        print("kokeillaan uudestaan!")