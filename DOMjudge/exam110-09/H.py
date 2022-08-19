#樹的節點(找兒子)part1
m = int(input())
for i in range(m):
    n = int(input())
    Lary = []
    Lseta = set()
    Lsetb = set()
    for j in range(n-1):
        a,b = list(map(int,input().split(",")))
        Lseta.add(a)
        Lsetb.add(b)
    Lsetc = Lseta - Lsetb
    for k in Lsetc:
       Lary.append(str(k))
    Lans = ','
    Lans = Lans.join(Lary)
    print(Lans)
    if(i < m-1):
        n = input()