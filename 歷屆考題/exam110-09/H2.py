#樹的節點(找兒子)part2
m = int(input())
for i in range(m):
    n = int(input())
    Lary = []
    Larya = []
    Laryb = []
    for j in range(n-1):
        a,b = list(map(int,input().split(",")))
        Larya.append(a)
        Laryb.append(b)
    for k in range(len(Larya)):
        L = 0
        for q in range(len(Laryb)):
            if Larya[k] == Laryb[q]:
                L = 1
                break
        if L == 0:
            Lary.append(str(Larya[k]))
    print(Lary)
    Lans = ','
    Lans = Lans.join(Lary)
    print(Lans)
    if(i < m-1):
        n = input()