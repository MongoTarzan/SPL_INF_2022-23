import random

zahl = random.randint(1, 100)

print(zahl)

if zahl > 50:
    print("Large")

if 20 < zahl < 50:
    print("Medium")

if zahl < 20:
    print("mini")