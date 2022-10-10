import random

sum = 0
num = 0
i = False

while i == False:
    num = random.randint(10, 30)
    print(num)
    sum = sum + num
    if num == 15 or num == 25:
        i = True

print(sum)