tuuma = 2.54

while True:
    sentti = int(input("Kerro senttimetri"))
    if sentti < 0:
        break
    else:
        print(sentti/tuuma)