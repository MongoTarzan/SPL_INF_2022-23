import random

num1 = random.randint(1, 100)
num2 = random.randint(1, 100)

if num1 < num2 and num1 < 50:
    print("Zahl 1 ist kleiner als Zahl 2 und Mini")
if num1 or num2 < 30:
    print("Eine der beiden Zahlen ist kleiner als 30")
if num1 < 50 and num2 != 50:
    print("Erste Zahl klein, zweite kein 50iger")