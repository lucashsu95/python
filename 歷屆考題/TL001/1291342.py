#TL001 歸零的步驟數
num1 = int(input())
Lcount = 0
while num1 != 0:
    if num1 % 2 != 0:
        num1 -= 1
    else:
        num1 /= 2
    Lcount += 1
print(Lcount)