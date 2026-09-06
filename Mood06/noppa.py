import random

noppa = input("Kuinka paljon noppia on")

luvut = 0

for i in range(noppa):
    luku = random.randint(1,6)
    luvut += luku

print(f"Silmälukujen yhteen laskettu on {luvut}")