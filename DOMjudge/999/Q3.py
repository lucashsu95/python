#999Q3Max找最大(二維陣列)
Lary = []
Lary2 = []
Lmax = 0
import sys
for line in sys.stdin.read().splitlines():
    a = list(map(int,line.split(" ")))
    Lary.append(a)

for i in Lary:
    for j in i:
        if j > Lmax:
            Lmax = j
print(Lmax)
        
    