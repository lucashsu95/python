Lary = []
Lstart = int(input())
Lend = int(input())
for i in range(Lstart,Lend):
    if i % 4 == 0 and i % 6 == 0:
        continue
    if i % 4 == 0:
        Lary.append(i)
    elif i % 6 == 0:
        Lary.append(i)
for i in range(1,len(Lary)+1):
    print(f'{Lary[i-1]:<4d}',end='')
    if i % 10 == 0:
        print()
if len(Lary) % 10 != 0:
    print()
# print(Lary)
print(len(Lary))
print(sum(Lary))
