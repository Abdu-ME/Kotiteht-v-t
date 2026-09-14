import random
def satunnainen():
    while True:
        noppa = random.randint(1, 6)
        if noppa == 6:
            print(noppa)
            break
        else:
            print(noppa)
            print("kokeillaan uudestaan")

x = satunnainen()
print(x)