from random import randrange
print("Willkommen zum Würfelspiel!")
computer = []
cSum = 0
while len(computer) < 6:
    computer.append(randrange(6) + 1)
    cSum += computer[-1]
print("[1] Ja\n[2] Nein")
start = int(input("Möchtest du starten?"))
if start == 1:
    wuerfe = 6
    pSum = 0
    while wuerfe > 0:
        wuerfe -= 1
        print("Schreibe x zum würfeln")
        play = input()
        if play == 'x':
            wurf = randrange(6) + 1
            pSum += wurf
            print("Du hast eine", wurf, "gewürfelt! Der Computer hat eine", computer[6 - wuerfe - 1], "gewürfelt.")
        else:
            print("Abgebrochen...")
            break
        if wuerfe == 0:
            if cSum > pSum:
                print("Du hast verloren :+(")
            elif pSum > cSum:
                print("Du hast gewonnen!")
            else:
                print("Du und der Computer sind gleich auf.")