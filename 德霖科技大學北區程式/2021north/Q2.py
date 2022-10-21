#試題二(16 分)：總流程時間
import sys
Lsum = 0
Lsum2 = []
Lsum3 = 0
for line in sys.stdin.read().splitlines():
    a = list(map(int,line.split(' ')))
    a.sort()
for i in range(len(a)):
    Lsum += a[i]
    Lsum2.append(Lsum)
for j in range(len(Lsum2)):
    Lsum3 += Lsum2[j]
print(Lsum3)
