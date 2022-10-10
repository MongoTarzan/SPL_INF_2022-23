import random

def add(num1, num2):
    print(num1 + " + ")
    print(num2)
    sum = num1 + num2

    return sum

def rand100():
    rand = random.randint(100, 200)

    return rand

def randomWord(array):
    return array[random.randrange(len(array))]

print(randomWord(["Schule", "Labor", "PC", "Soster"]))