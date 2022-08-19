#104最大公約數計算
import math
for T in range(int(input())):
    val = list(map(int,input().split(',')))
    val_max = 0
    for i in range(1,len(val)):
        mt = math.gcd(val[i],val[i-1])
    print(mt)