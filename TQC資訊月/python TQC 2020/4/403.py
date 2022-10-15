#403 位數總和計算
La = int(input())
Lb = int(input())
Lcount = 0
ary = []
for i in range(La,Lb+1):
    if i % 4 == 0 or i % 9 == 0:
        print(f'{i:<4d}',end='')
        ary.append(i)
        Lcount += 1
    if Lcount == 10:
        print()
        Lcount = 0
print()
print(len(ary))
print(sum(ary))