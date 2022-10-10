import random

random = random.Random()
randomNumber = random.randint(1, 100)

if randomNumber < 20:
    print("Mini")
elif randomNumber < 50:
    print("Medium")
elif randomNumber < 100:
    print("Difficult")
