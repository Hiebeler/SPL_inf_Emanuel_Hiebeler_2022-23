import random

random = random.Random()
randomNumber1 = random.randint(1, 100)
randomNumber2 = random.randint(1, 100)

if randomNumber1 < randomNumber2 and randomNumber1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")
if randomNumber1 < 30 or randomNumber2 < 30:
    print("Eine der beiden ist kleiner als 30")
if randomNumber1 < 50 and randomNumber2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")
