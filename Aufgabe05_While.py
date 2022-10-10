import random

sum = 0
randNumber = random.randint(10, 30)

while randNumber != 15 and randNumber != 25:
    sum += randNumber
    print(randNumber)
    randNumber = random.randint(10, 30)

print(randNumber)
