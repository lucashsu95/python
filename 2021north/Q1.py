#連分數轉換
import sys
import fractions

for line in sys.stdin.read().splitlines():
    a = list(map(int,line.split(",")))
    Lsum = a[-1]
    Lcount = 1
    for i in range(len(a)-2,-1,-1):
        Lsum = 1 / Lsum + a[i]
    Lsum = 1 / Lsum

    while Lsum // 10 != Lsum / 10:
        Lcount *= 10
        Lsum *= 10
    Lsum = int(Lsum)
    Lcount = int(Lcount)
    #print(Lsum)
    for num,decimal in [(Lsum,Lcount)]:
        fract = fractions.Fraction(num,decimal)
    fract = str(fract)
    print(fract[0])
    print(fract[-1])

        