import random
x = random.randint(1, 10)

while True: 
    arvaus = int(input("Arvaa luvulta 1-10\n"))
    if arvaus == x:
        print("Oikein!")
        break
    elif arvaus > x:
        print ("arvaus on liian suuri")
    else:
        print(" arvaus on liian pieni")
    