#105最大公約數計算
import math
for T in range(int(input())):
    value = list(map(int,input().split(',')))
    Lmax = []
    for i in range(len(value)):
        for j in range(len(value)):
            mt = math.gcd(value[i],value[j])
            if value[i] == value[j]:
                continue
            Lmax.append(mt)
    print(max(Lmax))
    #print(Lmax)
