n = int(input())
Lary = []
for i in range(n):
    Lary.append(int(input()))
Lary.sort()
#print(Lary)

ans = int(n * 0.25)
ans2 = int(n * 0.5)
ans3 = int(n * 0.75)
print(str(Lary[ans]) + ',' + str(Lary[ans2]) + ',' + str(Lary[ans3]))
